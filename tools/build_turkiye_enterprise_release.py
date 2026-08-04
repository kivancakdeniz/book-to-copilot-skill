#!/usr/bin/env python3
"""Validate and build deterministic Türkiye enterprise demo releases."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import tempfile
import urllib.parse
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Optional, Sequence

from scan_generated_skill import _scan_text
from validate_skill import audit, get_scalar, parse_frontmatter, top_level_keys


SCHEMA_VERSION = 1
CATALOG_VERSION = "1.0.0"
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
ZIP_MODE = 0o100644 << 16
EXPECTED_SLUGS = (
    "kvkk-aydinlatma-kontrolu",
    "etk-iys-ileti-karari",
    "indirimli-fiyat-denetimi",
    "masak-musteri-kabul",
    "bddk-uzaktan-musteri-edinimi",
    "rekabet-birlesme-bildirimi",
    "isg-risk-degerlendirme",
    "titck-ilac-tanitimi",
    "kripto-odeme-kapisi",
    "btk-haberlesme-verisi",
)
COMPANION_NAMES = (
    "company-policy.md",
    "evidence-map.md",
    "output-schema.md",
    "public-method.md",
    "scenario-guide.md",
)
CATALOG_FIELDS = {
    "id",
    "title",
    "article",
    "status",
    "sector",
    "audience",
    "oneLineValue",
}
RAW_OFFICIAL_EXTENSIONS = {".pdf", ".xml", ".html", ".htm"}
EMBEDDED_OFFICIAL_FIELDS = {
    "body",
    "content",
    "contentPath",
    "excerpt",
    "file",
    "localPath",
    "quote",
    "raw",
    "snapshot",
    "text",
}
REAL_NAME_DENYLIST = (
    "Kuzey Finans",
    "PeraPazar",
    "PeraHome",
    "Novera Rx",
    "NovaTerra",
    "Telya",
    "Mercuria",
)
ANSWER_KEY_PHRASES = ("Beklenen sınıflandırma", "beklenen seçenek")
LEARN_SKILL_UPLOAD_URL = (
    "https://learn.microsoft.com/en-us/microsoft-copilot-studio/"
    "agents-experience/skills-add-existing"
)
DISCLAIMER = (
    "Bu paket eğitim ve yönetişim tasarımı içindir; hukuki, tıbbi, mühendislik "
    "veya mevzuata uygunluk görüşü değildir. Nihai kararlar ve bütün sistem "
    "eylemleri yetkili insanlarda kalır."
)
RELEASE_ROOT_MARKER = ".turkiye-enterprise-release-root"
RELEASE_ROOT_MARKER_BYTES = b"turkiye-enterprise-release-root-v1\n"
MAX_FILE_BYTES = 5 * 1024 * 1024
MAX_SKILL_TOTAL_BYTES = 10 * 1024 * 1024
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_ARTICLE_BYTES = 1 * 1024 * 1024
MAX_SITE_FILE_BYTES = 50 * 1024 * 1024
MAX_SITE_TOTAL_BYTES = 250 * 1024 * 1024
SOURCE_MANIFEST_FIELDS = {"schemaVersion", "demo", "demoId", "sources"}
EXTERNAL_SOURCE_FIELDS = {
    "id",
    "title",
    "type",
    "url",
    "officialUrl",
    "sha256",
    "publisher",
    "retrievedAt",
    "redistribution",
    "reuseBasis",
    "reuseCaveat",
    "reuse",
    "role",
    "tracked",
}
LOCAL_SOURCE_FIELDS = EXTERNAL_SOURCE_FIELDS | {"path", "license", "synthetic"}

_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
_CODE_TOKEN_RE = re.compile(r"`([a-z0-9][a-z0-9-]*)`")
_EMAIL_RE = re.compile(r"(?<![\w.+-])[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")
_UUID_RE = re.compile(
    r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-"
    r"[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\b"
)
_SECRET_RE = re.compile(
    r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----|"
    r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b|"
    r"\b(?:sk-[A-Za-z0-9_-]{16,}|gh[opusr]_[A-Za-z0-9]{20,}|"
    r"github_pat_[A-Za-z0-9_]{20,}|xox[A-Za-z0-9]-[A-Za-z0-9-]{10,}|"
    r"npm_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})\b|"
    r"(?i:\b(?:api[_-]?key|client[_-]?secret|accountkey|password)\s*[:=]\s*[^\s,;}]+)"
)
_UNSAFE_HTML_RE = re.compile(
    r"<\s*/?\s*(?:script|style|iframe|object|embed)\b|\bon[a-z]+\s*=|"
    r"\bjavascript\s*:|\bdata\s*:(?:[A-Za-z][A-Za-z0-9.+-]*/|[,;])",
    re.IGNORECASE,
)
_BIDI_CONTROL_RE = re.compile(r"[\u061c\u200e\u200f\u202a-\u202e\u2066-\u2069]")
_PROMPT_OVERRIDE_RE = re.compile(
    r"(?:önceki\s+talimatları\s+yok\s+say|"
    r"sistem\s+talimatlarını\s+göz\s+ardı\s+et|artık\s+sen)\b",
    re.IGNORECASE,
)
_WINDOWS_ABSOLUTE_RE = re.compile(r"\b[A-Za-z]:\\(?:[^\s\\]+\\)+[^\s\\]+")
_WINDOWS_DRIVE_PREFIX_RE = re.compile(r"^[A-Za-z]:")
_POSIX_ABSOLUTE_RE = re.compile(
    r"(?:^|[\s\"'`(=])((?:/[A-Za-z0-9._~-]+){2,})(?=$|[\s\"'`),.;])",
    re.MULTILINE,
)
_LOCAL_USER_PATH_RE = re.compile(
    r"(?:/Users/[^/\s]+|/home/[^/\s]+|/tmp/[^\s]+|"
    r"[A-Za-z]:\\Users\\[^\\\s]+)",
    re.IGNORECASE,
)


class ReleaseError(RuntimeError):
    """Raised when source validation or deterministic release building fails."""


@dataclass(frozen=True)
class SkillFile:
    source: Path
    relative: str
    data: bytes


@dataclass(frozen=True)
class ValidatedDemo:
    slug: str
    catalog_entry: Mapping[str, Any]
    demo_dir: Path
    skill_files: tuple[SkillFile, ...]
    source_manifest: Mapping[str, Any]
    official_sources: tuple[Mapping[str, Any], ...]
    source_tree_sha256: str


def _duplicate_safe_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ReleaseError(f"JSON contains duplicate key: {key}")
        result[key] = value
    return result


def _read_json(path: Path) -> Any:
    try:
        size = path.stat().st_size
    except OSError as exc:
        raise ReleaseError(f"invalid JSON: {path}: {exc}") from exc
    if size > MAX_JSON_BYTES:
        raise ReleaseError(f"JSON exceeds {MAX_JSON_BYTES} bytes: {path}")
    try:
        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_duplicate_safe_object,
        )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ReleaseError(f"invalid JSON: {path}: {exc}") from exc


def _json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode(
        "utf-8"
    )


def _write_text_lf(path: Path, text: str) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as output:
        output.write(text)


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _read_bounded_bytes(path: Path, limit: int, label: str) -> bytes:
    if path.is_symlink() or not path.is_file():
        raise ReleaseError(f"{label} must be a real file: {path}")
    size = path.stat().st_size
    if size > limit:
        raise ReleaseError(f"{label} exceeds {limit} bytes: {path}")
    return path.read_bytes()


def _safe_relative_path(base: Path, value: str, label: str) -> Path:
    candidate = Path(value)
    if candidate.is_absolute() or _WINDOWS_ABSOLUTE_RE.search(value):
        raise ReleaseError(f"{label} must be relative: {value}")
    resolved = (base / candidate).resolve()
    if not _inside(resolved, base.resolve()):
        raise ReleaseError(f"{label} escapes its root: {value}")
    return resolved


def _validate_tree(demo_dir: Path) -> None:
    for path in sorted(demo_dir.rglob("*")):
        relative = path.relative_to(demo_dir)
        if path.is_symlink():
            raise ReleaseError(f"symlinks are not allowed: {relative.as_posix()}")
        if any(part.startswith(".") for part in relative.parts):
            raise ReleaseError(f"hidden paths are not allowed: {relative.as_posix()}")
        if path.is_file() and path.stat().st_size > MAX_FILE_BYTES:
            raise ReleaseError(
                f"demo file exceeds {MAX_FILE_BYTES} bytes: {relative.as_posix()}"
            )
        if path.is_file() and path.suffix.lower() in RAW_OFFICIAL_EXTENSIONS:
            raise ReleaseError(
                f"official PDF/XML/HTML snapshots must not be tracked: {relative.as_posix()}"
            )


def _validate_sensitive_text(path: Path, text: str) -> None:
    relative = path.as_posix()
    checks = (
        (_EMAIL_RE, "email address"),
        (_UUID_RE, "UUID"),
        (_SECRET_RE, "secret-shaped value"),
        (_WINDOWS_ABSOLUTE_RE, "absolute Windows path"),
        (_LOCAL_USER_PATH_RE, "local user path"),
        (_POSIX_ABSOLUTE_RE, "absolute POSIX path"),
    )
    for pattern, label in checks:
        if pattern.search(text):
            raise ReleaseError(f"{relative} contains a prohibited {label}")
    if _UNSAFE_HTML_RE.search(text):
        raise ReleaseError(f"{relative} contains prohibited active HTML or URL content")
    if _BIDI_CONTROL_RE.search(text):
        raise ReleaseError(f"{relative} contains a prohibited Unicode bidi control")
    if _PROMPT_OVERRIDE_RE.search(text):
        raise ReleaseError(f"{relative} contains a prohibited prompt override pattern")
    for denied in REAL_NAME_DENYLIST:
        if denied in text:
            raise ReleaseError(f"{relative} contains denied real-name string: {denied}")


def _validate_public_method_length(path: Path, text: str) -> None:
    for block in re.split(r"\n\s*\n", text):
        if block.lstrip().startswith("```"):
            continue
        word_count = len(re.findall(r"\b[^\W_]+(?:[-’'][^\W_]+)*\b", block, re.UNICODE))
        stripped = block.lstrip()
        authored_list = bool(re.match(r"^(?:[-*+]\s+|\d+\.\s+)", stripped))
        quote_looking = stripped.startswith(">") or not authored_list
        if word_count > 80 and quote_looking:
            raise ReleaseError(
                f"{path.as_posix()} contains a public-method block longer than 80 words"
            )


def _validate_all_json(demo_dir: Path) -> None:
    for path in sorted(demo_dir.rglob("*.json")):
        _read_json(path)


def _collect_skill_files(skill_dir: Path, slug: str) -> tuple[SkillFile, ...]:
    markdown_paths = sorted(
        skill_dir.rglob("*.md"), key=lambda item: item.relative_to(skill_dir).as_posix()
    )
    if len(markdown_paths) != 6:
        raise ReleaseError(f"{slug}: skill must contain exactly 6 Markdown files")
    names = [path.name for path in markdown_paths]
    expected_names = {"SKILL.md", *COMPANION_NAMES}
    if set(names) != expected_names or len(names) != len(set(names)):
        raise ReleaseError(f"{slug}: skill Markdown names must be SKILL.md plus five companions")

    total_size = 0
    for path in markdown_paths:
        if path.is_symlink():
            raise ReleaseError(f"{slug}: skill Markdown must not be a symlink: {path.name}")
        size = path.stat().st_size
        if size > MAX_FILE_BYTES:
            raise ReleaseError(
                f"{slug}: skill Markdown exceeds {MAX_FILE_BYTES} bytes: {path.name}"
            )
        total_size += size
    if total_size > MAX_SKILL_TOTAL_BYTES:
        raise ReleaseError(
            f"{slug}: canonical skill exceeds {MAX_SKILL_TOTAL_BYTES} bytes"
        )

    files: list[SkillFile] = []
    for path in markdown_paths:
        relative = path.relative_to(skill_dir).as_posix()
        data = path.read_bytes()
        try:
            text = data.decode("utf-8-sig")
        except UnicodeDecodeError as exc:
            raise ReleaseError(f"{slug}: skill Markdown is not UTF-8: {relative}") from exc
        findings = _scan_text(relative, text)
        if findings:
            finding = findings[0]
            raise ReleaseError(
                f"{slug}: unsafe skill Markdown {finding.path}:{finding.line} "
                f"[{finding.rule_id}] {finding.message}"
            )
        files.append(SkillFile(path, relative, data))
    return tuple(files)


def _validate_frontmatter(skill_path: Path, slug: str) -> str:
    text = skill_path.read_text(encoding="utf-8-sig")
    frontmatter, body = parse_frontmatter(text)
    if frontmatter is None or body is None:
        raise ReleaseError(f"{slug}: SKILL.md must have valid frontmatter")
    keys = top_level_keys(frontmatter)
    if len(keys) != len(set(keys)):
        raise ReleaseError(f"{slug}: duplicate top-level SKILL.md frontmatter key")
    if not set(keys).issubset({"name", "description", "license"}):
        raise ReleaseError(f"{slug}: only name, description, and license are allowed")
    if "allowed-tools" in keys:
        raise ReleaseError(f"{slug}: allowed-tools is prohibited")
    if get_scalar(frontmatter, "name") != slug:
        raise ReleaseError(f"{slug}: SKILL.md frontmatter name must match the slug")
    if not get_scalar(frontmatter, "description"):
        raise ReleaseError(f"{slug}: SKILL.md frontmatter description is required")
    for lens in ("copilot", "claude", "amp"):
        errors, _warns = audit(skill_path, lens=lens)
        if errors:
            raise ReleaseError(f"{slug}: validate_skill {lens} audit failed: {errors[0]}")
    return body.lstrip("\n")


def _validate_markdown_links(skill_dir: Path, files: Iterable[SkillFile], slug: str) -> None:
    root = skill_dir.resolve()
    for skill_file in files:
        text = skill_file.data.decode("utf-8-sig")
        for match in _MARKDOWN_LINK_RE.finditer(text):
            raw_target = match.group(1).strip()
            if raw_target.startswith("<") and ">" in raw_target:
                raw_target = raw_target[1 : raw_target.index(">")]
            else:
                raw_target = raw_target.split(maxsplit=1)[0]
            parsed = urllib.parse.urlsplit(raw_target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target_path = urllib.parse.unquote(parsed.path)
            if not target_path.lower().endswith(".md"):
                continue
            if target_path.startswith("/"):
                raise ReleaseError(f"{slug}: absolute Markdown link is not allowed: {raw_target}")
            resolved = (skill_file.source.parent / target_path).resolve()
            if not _inside(resolved, root) or not resolved.is_file():
                raise ReleaseError(
                    f"{slug}: local Markdown link does not resolve inside skill root: "
                    f"{skill_file.relative} -> {raw_target}"
                )


def _external_url(source: Mapping[str, Any]) -> Optional[str]:
    value = source.get("officialUrl", source.get("url"))
    return value if isinstance(value, str) else None


def _official_metadata(source: Mapping[str, Any]) -> Mapping[str, Any]:
    return {key: source[key] for key in sorted(EXTERNAL_SOURCE_FIELDS) if key in source}


def _validate_source_manifest(
    demo_dir: Path, slug: str
) -> tuple[Mapping[str, Any], tuple[Mapping[str, Any], ...]]:
    path = demo_dir / "sources" / "source-manifest.json"
    manifest = _read_json(path)
    if not isinstance(manifest, dict):
        raise ReleaseError(f"{slug}: source manifest must be an object")
    unknown_manifest_fields = set(manifest) - SOURCE_MANIFEST_FIELDS
    if unknown_manifest_fields:
        raise ReleaseError(
            f"{slug}: source manifest has unknown fields: "
            f"{sorted(unknown_manifest_fields)}"
        )
    if manifest.get("schemaVersion") != SCHEMA_VERSION:
        raise ReleaseError(f"{slug}: source manifest schemaVersion must be 1")
    if manifest.get("demoId", manifest.get("demo")) != slug:
        raise ReleaseError(f"{slug}: source manifest demo id does not match")
    sources = manifest.get("sources")
    if not isinstance(sources, list) or not sources:
        raise ReleaseError(f"{slug}: source manifest must contain sources")

    official: list[Mapping[str, Any]] = []
    source_root = path.parent.resolve()
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            raise ReleaseError(f"{slug}: source {index} must be an object")
        if "path" not in source:
            embedded_fields = EMBEDDED_OFFICIAL_FIELDS.intersection(source)
            if embedded_fields:
                field_list = ", ".join(sorted(embedded_fields))
                raise ReleaseError(
                    f"{slug}: external source {index} embeds official content: {field_list}"
                )
        allowed_fields = LOCAL_SOURCE_FIELDS if "path" in source else EXTERNAL_SOURCE_FIELDS
        unknown_fields = set(source) - allowed_fields
        if unknown_fields:
            raise ReleaseError(
                f"{slug}: source {index} has unknown fields: {sorted(unknown_fields)}"
            )
        source_hash = source.get("sha256")
        if not isinstance(source_hash, str) or not _SHA256_RE.fullmatch(source_hash):
            raise ReleaseError(f"{slug}: source {index} has an invalid SHA-256")
        if not isinstance(source.get("title"), str) or not source["title"].strip():
            raise ReleaseError(f"{slug}: source {index} is missing title")
        if "path" not in source:
            url = _external_url(source)
            if not url or urllib.parse.urlsplit(url).scheme not in {"http", "https"}:
                raise ReleaseError(f"{slug}: external source {index} is missing an official URL")
            if source.get("synthetic") is True:
                raise ReleaseError(f"{slug}: external source {index} cannot be synthetic")
            if not isinstance(source.get("publisher"), str) or not source["publisher"].strip():
                raise ReleaseError(f"{slug}: external source {index} is missing publisher")
            if not isinstance(source.get("retrievedAt"), str) or not source["retrievedAt"].strip():
                raise ReleaseError(f"{slug}: external source {index} is missing retrievedAt")
            caveat = source.get("reuseCaveat", source.get("reuse"))
            if not isinstance(caveat, str) or not caveat.strip():
                raise ReleaseError(f"{slug}: external source {index} is missing reuse caveat")
            if source.get("redistribution") != "metadata-only":
                raise ReleaseError(f"{slug}: external source {index} must be metadata-only")
            official.append(_official_metadata(source))
            continue

        if str(source.get("type", "")).startswith("external"):
            raise ReleaseError(f"{slug}: external source {index} must not declare a path")
        if source.get("synthetic") is not True:
            raise ReleaseError(f"{slug}: local source {index} must be marked synthetic")
        source_value = source.get("path")
        if not isinstance(source_value, str) or not source_value:
            raise ReleaseError(f"{slug}: local source {index} has an invalid path")
        source_path = _safe_relative_path(source_root, source_value, "synthetic source path")
        if not source_path.is_file() or source_path.is_symlink():
            raise ReleaseError(f"{slug}: synthetic source does not exist: {source_value}")
        if _sha256_file(source_path) != source_hash:
            raise ReleaseError(f"{slug}: synthetic source hash mismatch: {source_value}")
    if not official:
        raise ReleaseError(f"{slug}: at least one external official source is required")
    return manifest, tuple(official)


def _code_tokens(demo_dir: Path) -> set[str]:
    paths = (
        demo_dir / "sources" / "company-policy.md",
        demo_dir / "skill" / "SKILL.md",
    )
    return {
        token
        for path in paths
        for token in _CODE_TOKEN_RE.findall(path.read_text(encoding="utf-8-sig"))
    }


def _string_list(value: Any) -> Optional[list[str]]:
    if not isinstance(value, list) or not value or not all(isinstance(item, str) for item in value):
        return None
    return value


def _validate_scenarios(demo_dir: Path, slug: str) -> None:
    data = _read_json(demo_dir / "evaluation" / "scenarios.json")
    if not isinstance(data, dict):
        raise ReleaseError(f"{slug}: scenario root must be an object")
    if data.get("demoId", data.get("demo")) != slug:
        raise ReleaseError(f"{slug}: scenario demo id does not match")
    cases = data.get("scenarios", data.get("cases"))
    if not isinstance(cases, list) or len(cases) != 12:
        raise ReleaseError(f"{slug}: scenarios/cases must contain exactly 12 cases")
    ids = [case.get("id") for case in cases if isinstance(case, dict)]
    if len(ids) != 12 or any(not isinstance(case_id, str) or not case_id for case_id in ids):
        raise ReleaseError(f"{slug}: every scenario must have an id")
    if len(set(ids)) != 12:
        raise ReleaseError(f"{slug}: scenario ids must be unique")

    decisions = _string_list(data.get("allowedDecisionClasses")) or _string_list(
        data.get("decisionClasses")
    )
    options = _string_list(data.get("allowedOptions")) or _string_list(data.get("options"))
    tokens = _code_tokens(demo_dir)
    permitted_decisions = set(decisions) if decisions else tokens
    permitted_options = set(options) if options else tokens
    for case in cases:
        case_demo = case.get("demoId", case.get("demo"))
        if case_demo is not None and case_demo != slug:
            raise ReleaseError(f"{slug}: scenario {case.get('id')} demo id does not match")
        decision = case.get("expectedDecision")
        option = case.get("expectedOption")
        if not isinstance(decision, str) or decision not in permitted_decisions:
            raise ReleaseError(
                f"{slug}: scenario {case.get('id')} decision is not permitted: {decision}"
            )
        if not isinstance(option, str) or option not in permitted_options:
            raise ReleaseError(
                f"{slug}: scenario {case.get('id')} option is not permitted: {option}"
            )


def _validate_rubric(demo_dir: Path, slug: str) -> None:
    rubric = _read_json(demo_dir / "evaluation" / "rubric.json")
    if not isinstance(rubric, dict):
        raise ReleaseError(f"{slug}: rubric root must be an object")
    dimensions = rubric.get("dimensions")
    if not isinstance(dimensions, list) or not dimensions:
        raise ReleaseError(f"{slug}: rubric must contain dimensions")
    maximums: list[int] = []
    for dimension in dimensions:
        if not isinstance(dimension, dict) or not isinstance(dimension.get("max"), int):
            raise ReleaseError(f"{slug}: every rubric dimension needs an integer max")
        maximum = dimension["max"]
        if maximum < 0:
            raise ReleaseError(f"{slug}: rubric dimension max must be nonnegative")
        anchors = dimension.get("anchors")
        if not isinstance(anchors, dict) or set(anchors) != {str(value) for value in range(maximum + 1)}:
            raise ReleaseError(
                f"{slug}: rubric anchors must cover 0..{maximum} for {dimension.get('id')}"
            )
        maximums.append(maximum)
    if sum(maximums) != 14 or rubric.get("maximumPositiveScore") != 14:
        raise ReleaseError(f"{slug}: rubric positive maximum must sum to 14")
    penalties = rubric.get("penalties")
    if not isinstance(penalties, list):
        raise ReleaseError(f"{slug}: rubric penalties must be a list")
    for penalty in penalties:
        if not isinstance(penalty, dict):
            raise ReleaseError(f"{slug}: rubric penalty must be an object")
        score = penalty.get("score")
        if not isinstance(score, (int, float)) or isinstance(score, bool) or score > 0:
            raise ReleaseError(f"{slug}: rubric penalties must be nonpositive")
        if not isinstance(penalty.get("repeatable"), bool):
            raise ReleaseError(f"{slug}: rubric penalties must declare repeatable")


def _tree_sha256(files: Iterable[SkillFile]) -> str:
    digest = hashlib.sha256()
    for skill_file in sorted(files, key=lambda item: item.relative):
        relative = skill_file.relative.encode("utf-8")
        digest.update(len(relative).to_bytes(4, "big"))
        digest.update(relative)
        digest.update(len(skill_file.data).to_bytes(8, "big"))
        digest.update(skill_file.data)
    return digest.hexdigest()


def _validate_catalog(root: Path) -> list[Mapping[str, Any]]:
    path = root / "demos" / "turkiye-enterprise" / "catalog.json"
    catalog = _read_json(path)
    if not isinstance(catalog, dict):
        raise ReleaseError("catalog root must be an object")
    if catalog.get("schemaVersion") != SCHEMA_VERSION:
        raise ReleaseError("catalog schemaVersion must be 1")
    if catalog.get("catalogVersion") != CATALOG_VERSION:
        raise ReleaseError("catalog catalogVersion must be 1.0.0")
    entries = catalog.get("entries")
    if not isinstance(entries, list) or len(entries) != 10:
        raise ReleaseError("catalog must contain exactly 10 entries")
    ids = [entry.get("id") for entry in entries if isinstance(entry, dict)]
    if tuple(ids) != EXPECTED_SLUGS or len(set(ids)) != 10:
        raise ReleaseError("catalog entries must use the canonical unique order")
    for entry in entries:
        if set(entry) != CATALOG_FIELDS:
            raise ReleaseError(f"catalog entry {entry.get('id')} has incorrect fields")
        if entry.get("status") != "release":
            raise ReleaseError(f"catalog entry {entry.get('id')} status must be release")
        for field in CATALOG_FIELDS - {"status"}:
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                raise ReleaseError(f"catalog entry {entry.get('id')} has empty {field}")
        expected_article = f"docs/skills/{entry['id']}.md"
        if entry["article"] != expected_article:
            raise ReleaseError(f"catalog entry {entry['id']} article path is not canonical")
        article = _safe_relative_path(root, entry["article"], "catalog article")
        if not article.is_file() or article.is_symlink():
            raise ReleaseError(f"catalog article is missing: {entry['article']}")
        if article.stat().st_size > MAX_ARTICLE_BYTES:
            raise ReleaseError(
                f"catalog article exceeds {MAX_ARTICLE_BYTES} bytes: {entry['article']}"
            )
    return entries


def validate_release(root: Path) -> tuple[ValidatedDemo, ...]:
    root = root.expanduser().resolve(strict=True)
    entries = _validate_catalog(root)
    demos: list[ValidatedDemo] = []
    for entry in entries:
        slug = entry["id"]
        demo_dir = root / "demos" / "turkiye-enterprise" / slug
        if not demo_dir.is_dir() or demo_dir.is_symlink():
            raise ReleaseError(f"demo path is missing or invalid: {slug}")
        _validate_tree(demo_dir)
        _validate_all_json(demo_dir)
        for path in sorted(demo_dir.rglob("*")):
            if path.is_file() and path.suffix.lower() in {".md", ".json"}:
                text = path.read_text(encoding="utf-8-sig")
                _validate_sensitive_text(path.relative_to(root), text)
                if path.name == "public-method.md":
                    _validate_public_method_length(path.relative_to(root), text)
        case_brief = (demo_dir / "sources" / "case-brief.md").read_text(
            encoding="utf-8-sig"
        )
        for phrase in ANSWER_KEY_PHRASES:
            if phrase in case_brief:
                raise ReleaseError(f"{slug}: case brief contains answer-key phrase: {phrase}")

        skill_dir = demo_dir / "skill"
        skill_files = _collect_skill_files(skill_dir, slug)
        _validate_frontmatter(skill_dir / "SKILL.md", slug)
        _validate_markdown_links(skill_dir, skill_files, slug)
        source_manifest, official_sources = _validate_source_manifest(demo_dir, slug)
        _validate_scenarios(demo_dir, slug)
        _validate_rubric(demo_dir, slug)
        demos.append(
            ValidatedDemo(
                slug=slug,
                catalog_entry=entry,
                demo_dir=demo_dir,
                skill_files=skill_files,
                source_manifest=source_manifest,
                official_sources=official_sources,
                source_tree_sha256=_tree_sha256(skill_files),
            )
        )
    return tuple(demos)


def _validate_archive_path(name: str) -> None:
    if not name or "\\" in name or _WINDOWS_DRIVE_PREFIX_RE.match(name):
        raise ReleaseError(f"unsafe archive path: {name!r}")
    if name.startswith("/") or name.startswith("//"):
        raise ReleaseError(f"unsafe archive path: {name!r}")
    if any(ord(character) < 32 or ord(character) == 127 for character in name):
        raise ReleaseError(f"unsafe archive path: {name!r}")
    parts = name.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        raise ReleaseError(f"unsafe archive path: {name!r}")


def _write_deterministic_zip(path: Path, entries: Mapping[str, bytes]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for name in sorted(entries):
            _validate_archive_path(name)
            info = zipfile.ZipInfo(name, date_time=ZIP_TIMESTAMP)
            info.create_system = 3
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = ZIP_MODE
            archive.writestr(info, entries[name], compresslevel=9)


def _skill_entries(demo: ValidatedDemo, prefix: str = "") -> dict[str, bytes]:
    return {f"{prefix}{item.relative}": item.data for item in demo.skill_files}


def _vscode_install(slug: str) -> bytes:
    return (
        f"# GitHub Copilot for VS Code kurulumu\n\n"
        f"Bu ZIP'i depo kökünde açın. Skill `.github/skills/{slug}/` altına "
        "yerleşir. Dosyaları inceleyin, depoyu güvenilir bir çalışma alanında açın "
        "ve Copilot Agent ile uygun bir istek üzerinden çağırın. Nihai kararlar ve "
        "bütün eylemler yetkili insanlarda kalır.\n"
    ).encode("utf-8")


def _scout_install(slug: str) -> bytes:
    return (
        f"# Scout kurulumu\n\n"
        f"Bu ZIP'i depo kökünde açın. Skill `.copilot/skills/{slug}/` altına "
        "yerleşir. Yüklemeden önce içeriği inceleyin. Bu paket araç veya MCP "
        "bağlantısı kurmaz; nihai kararlar ve bütün eylemler yetkili insanlarda kalır.\n"
    ).encode("utf-8")


def _harness_install(slug: str) -> bytes:
    return (
        "# Copilot Studio GitHub Copilot harness kurulumu\n\n"
        f"Bu dosya, `{slug}` için doğrudan yüklenebilir mevcut-skill ZIP paketidir. "
        "Copilot Studio'da GitHub Copilot harness preview ile oluşturulmuş ajanın "
        "Build > Skills alanında mevcut skill yükleme akışını kullanın. ZIP kökünde "
        "`SKILL.md` ve beş destek dosyası bulunur.\n\n"
        f"Resmî yönerge: {LEARN_SKILL_UPLOAD_URL}\n\n"
        "Skill insan yetkisini devralmaz. MCP sunucuları, araçlar, bağlantılar, "
        "kimlik ve izinler bu ZIP'ten ayrı yapılandırılmalı ve doğrulanmalıdır.\n"
    ).encode("utf-8")


def _classic_readme(slug: str) -> bytes:
    return (
        "# Copilot Studio classic kurulum malzemesi\n\n"
        f"Bu `{slug}` paketi doğrudan ajan veya solution içe aktarma paketi değildir. "
        "Classic ortamında bir maker tarafından uygulanacak yönerge, bilgi ve kaynak "
        "metadatası sağlar. This is not a direct agent or solution import package.\n\n"
        "## Kurulum\n\n"
        "1. `instructions.md` içeriğini ajanın talimat alanına insan incelemesiyle "
        "uyarlayın.\n"
        "2. `knowledge/` altındaki beş Markdown dosyasını ayrı bilgi kaynakları "
        "olarak ekleyin ve erişimi test edin.\n"
        "3. `source-manifest.json` ile resmî kaynak metadatasını ve sentetik kaynak "
        "sınırını doğrulayın.\n\n"
        "Nihai karar ve bütün operasyonel eylemler yetkili insanlarda kalır. MCP "
        "sunucuları, araçlar, bağlantılar, kimlik, izin ve yayımlama ayarları bu "
        "paketten ayrı yapılandırılmalıdır.\n"
    ).encode("utf-8")


def _archive_record(path: Path, output_dir: Path, file_count: int, host: str) -> dict[str, Any]:
    return {
        "host": host,
        "path": path.relative_to(output_dir).as_posix(),
        "sha256": _sha256_file(path),
        "size": path.stat().st_size,
        "fileCount": file_count,
    }


def _build_demo(
    demo: ValidatedDemo, output_dir: Path, license_bytes: bytes
) -> Mapping[str, Any]:
    slug = demo.slug
    slug_dir = output_dir / slug
    slug_dir.mkdir(parents=True, exist_ok=True)
    for existing in slug_dir.iterdir():
        if existing.is_dir():
            shutil.rmtree(existing)
        else:
            existing.unlink()

    notices_bytes = _demo_third_party_notices(demo)
    package_extras = {
        "LICENSE.md": license_bytes,
        "THIRD_PARTY_NOTICES.md": notices_bytes,
    }
    archive_specs: list[tuple[str, str, Mapping[str, bytes]]] = []
    cowork_entries = _skill_entries(demo)
    cowork_entries.update(package_extras)
    archive_specs.append(("cowork", f"{slug}-cowork.skill", cowork_entries))

    vscode_entries = _skill_entries(demo, f".github/skills/{slug}/")
    vscode_entries["INSTALL.md"] = _vscode_install(slug)
    vscode_entries.update(package_extras)
    archive_specs.append(
        ("github-copilot-vscode", f"{slug}-copilot-vscode.zip", vscode_entries)
    )

    scout_entries = _skill_entries(demo, f".copilot/skills/{slug}/")
    scout_entries["INSTALL.md"] = _scout_install(slug)
    scout_entries.update(package_extras)
    archive_specs.append(("scout", f"{slug}-scout.zip", scout_entries))

    harness_entries = _skill_entries(demo)
    harness_entries["INSTALL.md"] = _harness_install(slug)
    harness_entries.update(package_extras)
    archive_specs.append(
        (
            "copilot-studio-github-harness",
            f"{slug}-copilot-studio-github-harness.zip",
            harness_entries,
        )
    )

    skill_text = (demo.demo_dir / "skill" / "SKILL.md").read_text(encoding="utf-8-sig")
    _frontmatter, skill_body = parse_frontmatter(skill_text)
    if skill_body is None:
        raise ReleaseError(f"{slug}: SKILL.md body could not be extracted")
    companion_by_name = {item.source.name: item.data for item in demo.skill_files if item.source.name != "SKILL.md"}
    classic_entries: dict[str, bytes] = {
        "LICENSE.md": license_bytes,
        "README.md": _classic_readme(slug),
        "THIRD_PARTY_NOTICES.md": notices_bytes,
        "instructions.md": skill_body.lstrip("\n").encode("utf-8"),
        "source-manifest.json": _json_bytes(demo.source_manifest),
    }
    for name in COMPANION_NAMES:
        classic_entries[f"knowledge/{name}"] = companion_by_name[name]
    archive_specs.append(
        (
            "copilot-studio-classic",
            f"{slug}-copilot-studio-classic-setup.zip",
            classic_entries,
        )
    )

    archive_records: list[Mapping[str, Any]] = []
    for host, filename, entries in archive_specs:
        archive_path = slug_dir / filename
        _write_deterministic_zip(archive_path, entries)
        archive_records.append(
            _archive_record(archive_path, output_dir, len(entries), host)
        )

    manifest = {
        "schemaVersion": SCHEMA_VERSION,
        "catalogVersion": CATALOG_VERSION,
        "id": slug,
        "title": demo.catalog_entry["title"],
        "sourceSkillTreeSha256": demo.source_tree_sha256,
        "archives": archive_records,
        "officialSources": list(demo.official_sources),
        "disclaimer": DISCLAIMER,
    }
    (slug_dir / "release-manifest.json").write_bytes(_json_bytes(manifest))
    return manifest


def _notice_lines(demo: ValidatedDemo, heading: str) -> list[str]:
    lines = [f"{heading} {demo.catalog_entry['title']}", ""]
    for source in demo.official_sources:
        lines.extend(
            (
                f"- **{source['title']}**",
                f"  - Kimlik: {source.get('id', 'Belirtilmedi')}",
                f"  - Yayıncı: {source['publisher']}",
                f"  - URL: {_external_url(source)}",
                f"  - Erişim tarihi: {source['retrievedAt']}",
                f"  - SHA-256: {source['sha256']}",
                f"  - Dağıtım: {source['redistribution']}",
                "  - Yeniden kullanım sınırı: "
                f"{source.get('reuseCaveat', source.get('reuse', 'Resmî kaynaktan doğrulayın.'))}",
            )
        )
        if source.get("reuseBasis"):
            lines.append(f"  - Yeniden kullanım dayanağı: {source['reuseBasis']}")
        if source.get("role"):
            lines.append(f"  - Rol: {source['role']}")
    lines.append("")
    return lines


def _demo_third_party_notices(demo: ValidatedDemo) -> bytes:
    lines = [
        "# Third-party notices",
        "",
        "Bu paket resmî kaynakların tam içeriğini içermez. Kayıtlar yalnız kaynak "
        "metadatası ve yeniden kullanım uyarılarıdır.",
        "",
        *_notice_lines(demo, "##"),
        "## Disclaimer",
        "",
        DISCLAIMER,
        "",
    ]
    return "\n".join(lines).encode("utf-8")


def _third_party_notices(demos: Iterable[ValidatedDemo]) -> bytes:
    lines = [
        "# Third-party notices",
        "",
        "Paketler resmî kaynakların tam içeriğini içermez. Aşağıdaki kayıtlar yalnız "
        "kaynak metadatası ve yeniden kullanım uyarılarıdır.",
        "",
    ]
    for demo in demos:
        lines.extend(_notice_lines(demo, "##"))
    lines.extend(("## Disclaimer", "", DISCLAIMER, ""))
    return ("\n".join(lines).rstrip() + "\n").encode("utf-8")


def _prepare_output_directory(root: Path, output_dir: Path) -> Path:
    source_root = root.expanduser().resolve(strict=True)
    requested_output = output_dir.expanduser()
    if requested_output.is_symlink():
        raise ReleaseError("release output directory must not be a symlink")
    resolved_output = requested_output.resolve()
    protected_roots = tuple(
        (source_root / name).resolve()
        for name in ("demos", "docs", "tools", "tests", ".git")
    )
    if (
        resolved_output.parent == resolved_output
        or resolved_output == Path.home().resolve()
        or _inside(source_root, resolved_output)
        or any(_inside(resolved_output, protected) for protected in protected_roots)
    ):
        raise ReleaseError("release output directory is in a protected location")

    if resolved_output.exists():
        if not resolved_output.is_dir():
            raise ReleaseError("release output path must be a directory")
        contents = list(resolved_output.iterdir())
        if contents:
            marker = resolved_output / RELEASE_ROOT_MARKER
            if (
                not marker.is_file()
                or marker.is_symlink()
                or marker.read_bytes() != RELEASE_ROOT_MARKER_BYTES
            ):
                raise ReleaseError(
                    "nonempty release output directory lacks the exact factory marker"
                )
            shutil.rmtree(resolved_output)
    resolved_output.mkdir(parents=True, exist_ok=True)
    (resolved_output / RELEASE_ROOT_MARKER).write_bytes(RELEASE_ROOT_MARKER_BYTES)
    return resolved_output


def build_release(root: Path, output_dir: Path) -> tuple[ValidatedDemo, ...]:
    demos = validate_release(root)
    source_root = root.expanduser().resolve(strict=True)
    license_bytes = _read_bounded_bytes(
        source_root / "LICENSE.md", MAX_FILE_BYTES, "root LICENSE.md"
    )
    output_dir = _prepare_output_directory(root, output_dir)
    manifests = [_build_demo(demo, output_dir, license_bytes) for demo in demos]
    top_manifest = {
        "schemaVersion": SCHEMA_VERSION,
        "catalogVersion": CATALOG_VERSION,
        "demoCount": len(demos),
        "archiveCount": sum(len(manifest["archives"]) for manifest in manifests),
        "demos": [
            {
                "id": manifest["id"],
                "manifest": f"{manifest['id']}/release-manifest.json",
                "sourceSkillTreeSha256": manifest["sourceSkillTreeSha256"],
                "archives": manifest["archives"],
            }
            for manifest in manifests
        ],
        "disclaimer": DISCLAIMER,
    }
    (output_dir / "release-manifest.json").write_bytes(_json_bytes(top_manifest))
    (output_dir / "LICENSE.md").write_bytes(license_bytes)
    (output_dir / "THIRD_PARTY_NOTICES.md").write_bytes(_third_party_notices(demos))

    checksum_paths = sorted(
        path
        for path in output_dir.rglob("*")
        if path.is_file()
        and path.name not in {"SHA256SUMS", RELEASE_ROOT_MARKER}
    )
    checksum_text = "".join(
        f"{_sha256_file(path)}  {path.relative_to(output_dir).as_posix()}\n"
        for path in checksum_paths
    )
    _write_text_lf(output_dir / "SHA256SUMS", checksum_text)
    return demos


def stage_docs(root: Path, output_dir: Path, docs_dir: Path) -> Path:
    demos = build_release(root, output_dir)
    target = docs_dir.expanduser().resolve() / "downloads" / "turkiye-enterprise"
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True)
    for demo in demos:
        source_dir = output_dir.expanduser().resolve() / demo.slug
        target_dir = target / demo.slug
        target_dir.mkdir()
        for path in sorted(source_dir.iterdir()):
            if path.name == "release-manifest.json" or path.suffix in {".zip", ".skill"}:
                shutil.copy2(path, target_dir / path.name)
    for name in (
        "LICENSE.md",
        "release-manifest.json",
        "SHA256SUMS",
        "THIRD_PARTY_NOTICES.md",
    ):
        shutil.copy2(output_dir.expanduser().resolve() / name, target / name)
    return target


def build_site_zip(
    site_dir: Path, output: Path, license_path: Path, notices_path: Path
) -> Path:
    site_root = site_dir.expanduser().resolve(strict=True)
    if not site_root.is_dir() or site_root.is_symlink():
        raise ReleaseError("site directory must be a real directory")
    output = output.expanduser().resolve()
    if _inside(output, site_root):
        raise ReleaseError("site ZIP output must be outside the site directory")
    entries: dict[str, bytes] = {}
    total_size = 0
    for path in sorted(site_root.rglob("*"), key=lambda item: item.relative_to(site_root).as_posix()):
        if path.is_symlink():
            raise ReleaseError(f"site contains a symlink: {path.relative_to(site_root)}")
        if path.is_file():
            relative = path.relative_to(site_root).as_posix()
            size = path.stat().st_size
            if size > MAX_SITE_FILE_BYTES:
                raise ReleaseError(f"site file exceeds {MAX_SITE_FILE_BYTES} bytes: {relative}")
            total_size += size
            if total_size > MAX_SITE_TOTAL_BYTES:
                raise ReleaseError(f"site exceeds {MAX_SITE_TOTAL_BYTES} bytes")
            entries[relative] = path.read_bytes()
    if "index.html" not in entries:
        raise ReleaseError("site ZIP requires index.html at the ZIP root")
    injected = {
        "LICENSE.md": license_path,
        "THIRD_PARTY_NOTICES.md": notices_path,
    }
    for name, source in injected.items():
        if name in entries:
            raise ReleaseError(f"site ZIP root collision: {name}")
        data = _read_bounded_bytes(source.expanduser().resolve(), MAX_SITE_FILE_BYTES, name)
        total_size += len(data)
        if total_size > MAX_SITE_TOTAL_BYTES:
            raise ReleaseError(f"site exceeds {MAX_SITE_TOTAL_BYTES} bytes")
        entries[name] = data
    _write_deterministic_zip(output, entries)
    checksum_path = output.with_name(output.name + ".sha256")
    _write_text_lf(checksum_path, f"{_sha256_file(output)}  {output.name}\n")
    return output


def _file_map(root: Path) -> dict[str, bytes]:
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def verify_release(root: Path, output_dir: Path) -> None:
    expected_root = output_dir.expanduser().resolve(strict=True)
    expected = _file_map(expected_root)
    with tempfile.TemporaryDirectory(prefix="turkiye-enterprise-verify-") as temp_dir:
        rebuilt_root = Path(temp_dir) / "release"
        build_release(root, rebuilt_root)
        rebuilt = _file_map(rebuilt_root)
    if set(expected) != set(rebuilt):
        missing = sorted(set(rebuilt) - set(expected))
        extra = sorted(set(expected) - set(rebuilt))
        raise ReleaseError(f"release file set differs; missing={missing}, extra={extra}")
    changed = [name for name in sorted(expected) if expected[name] != rebuilt[name]]
    if changed:
        raise ReleaseError(f"release is not byte-identical: {changed}")


def _default_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)

    validate_parser = commands.add_parser("validate", help="Validate all release sources")
    validate_parser.add_argument("--root", type=Path, default=_default_root())

    build_parser = commands.add_parser("build", help="Build deterministic host archives")
    build_parser.add_argument("--output-dir", type=Path, required=True)
    build_parser.add_argument("--root", type=Path, default=_default_root())

    stage_parser = commands.add_parser("stage-docs", help="Build and stage documentation downloads")
    stage_parser.add_argument("--output-dir", type=Path, required=True)
    stage_parser.add_argument("--docs-dir", type=Path, required=True)
    stage_parser.add_argument("--root", type=Path, default=_default_root())

    site_parser = commands.add_parser("site-zip", help="Build a deterministic MkDocs site ZIP")
    site_parser.add_argument("--site-dir", type=Path, required=True)
    site_parser.add_argument("--output", type=Path, required=True)
    site_parser.add_argument("--license", type=Path, required=True)
    site_parser.add_argument("--notices", type=Path, required=True)

    verify_parser = commands.add_parser("verify-release", help="Rebuild and byte-compare a release")
    verify_parser.add_argument("--output-dir", type=Path, required=True)
    verify_parser.add_argument("--root", type=Path, default=_default_root())
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "validate":
            demos = validate_release(args.root)
            print(f"Validated {len(demos)} Türkiye enterprise demos.")
        elif args.command == "build":
            demos = build_release(args.root, args.output_dir)
            print(f"Built {len(demos) * 5} host archives in {args.output_dir}.")
        elif args.command == "stage-docs":
            target = stage_docs(args.root, args.output_dir, args.docs_dir)
            print(target)
        elif args.command == "site-zip":
            print(
                build_site_zip(
                    args.site_dir, args.output, args.license, args.notices
                )
            )
        elif args.command == "verify-release":
            verify_release(args.root, args.output_dir)
            print("Release is byte-identical to a clean rebuild.")
    except (OSError, UnicodeError, ReleaseError, zipfile.BadZipFile) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())