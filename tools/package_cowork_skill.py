#!/usr/bin/env python3
"""Build a deterministic Microsoft 365 Copilot Cowork custom-skill archive."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path


MAX_FILES = 100
MAX_FILE_BYTES = 5 * 1024 * 1024
MAX_UNCOMPRESSED_BYTES = 50 * 1024 * 1024
MAX_COMPRESSED_BYTES = 10 * 1024 * 1024
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


class PackageError(RuntimeError):
    """Raised when a skill cannot be safely packaged."""


def _frontmatter(text: str) -> str:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        raise PackageError("SKILL.md must start with valid YAML frontmatter")
    frontmatter = match.group(1)
    for field in ("name", "description"):
        if not re.search(rf"(?m)^{field}:\s*\S", frontmatter):
            raise PackageError(f"SKILL.md frontmatter is missing {field}")
    return frontmatter


def collect_skill_files(skill_dir: Path) -> list[Path]:
    requested = skill_dir.expanduser()
    if requested.is_symlink():
        raise PackageError("skill directory must not be a symbolic link")
    root = requested.resolve(strict=True)
    if not root.is_dir():
        raise PackageError("skill path must be a directory")

    master = root / "SKILL.md"
    if not master.is_file() or master.is_symlink():
        raise PackageError("SKILL.md is missing or is a symbolic link")
    _frontmatter(master.read_text(encoding="utf-8-sig"))

    files = []
    total_bytes = 0
    for path in sorted(root.rglob("*"), key=lambda item: item.relative_to(root).as_posix()):
        if path.is_symlink():
            raise PackageError(f"symbolic links are not allowed: {path.relative_to(root)}")
        if path.is_dir():
            continue
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            raise PackageError(f"hidden files are not allowed: {path.relative_to(root)}")
        size = path.stat().st_size
        if size > MAX_FILE_BYTES:
            raise PackageError(f"{path.relative_to(root)} exceeds the 5 MB file limit")
        total_bytes += size
        files.append(path)

    if len(files) > MAX_FILES:
        raise PackageError(f"skill has {len(files)} files; maximum is {MAX_FILES}")
    if total_bytes > MAX_UNCOMPRESSED_BYTES:
        raise PackageError("skill exceeds the 50 MB uncompressed archive limit")
    return files


def build_archive(skill_dir: Path, output_path: Path) -> Path:
    root = skill_dir.expanduser().resolve(strict=True)
    files = collect_skill_files(root)
    output = output_path.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            relative = path.relative_to(root).as_posix()
            info = zipfile.ZipInfo(relative, date_time=ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compresslevel=9)

    if output.stat().st_size > MAX_COMPRESSED_BYTES:
        output.unlink(missing_ok=True)
        raise PackageError("skill exceeds the 10 MB compressed archive limit")
    return output


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_dir", type=Path, help="Directory containing SKILL.md")
    parser.add_argument("output", type=Path, help="Output .skill or .zip archive")
    args = parser.parse_args(argv)

    try:
        output = build_archive(args.skill_dir, args.output)
    except (OSError, UnicodeError, PackageError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())