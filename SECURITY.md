# Security Policy

## Scope

book-to-copilot-skill preserves the upstream local conversion model. It reads
documents selected by the user and writes skill files. The repository code does
not itself provide a hosted upload service. If an AI host or cloud model is used,
content sent to that host follows its separate data and security terms.

The main security surfaces are:

- Python parsers processing untrusted PDF, EPUB, DOCX, HTML, RTF, MOBI, archive,
  and text inputs;
- optional extraction dependencies installed on user request;
- prompt injection or misleading instructions embedded in source documents;
- generated Markdown, links, paths, and packaged archives;
- demo evidence, screenshots, model traces, and release artifacts.

## Supported versions

The `master` branch is the supported security line. Reproduce against the latest
`master` revision when practical. Older tags, generated packages, forks, and
locally modified builds may not receive fixes.

## Reporting a vulnerability

Do not open a public issue or send vulnerability details by email. Use GitHub
private vulnerability reporting for this repository:

- Go to the repository's **Security** tab → **Report a vulnerability**.

Include the affected revision, impact, execution environment, and the smallest
safe reproduction. Do not attach real customer documents, credentials, personal
data, malicious archives that cannot be handled safely, or secrets. Use a
synthetic proof of concept and describe how maintainers can recreate it.

## Package verification

- Obtain releases from the public repository and compare published SHA-256
  values where provided.
- Inspect archive entries before extraction; reject absolute paths, `..` path
  traversal, symlinks where unsupported, unexpected executables, hidden state,
  and excessive compressed or uncompressed sizes.
- Run host validation and the advisory generated-skill security scan before
  loading or publishing a generated package.
- Review dependency names and installation prompts; install optional parsers in
  an isolated environment when possible.

## Data and prompt safety

Never commit or submit secrets, API keys, certificates, local Azure state,
tenant IDs, customer data, personal data, confidential source documents, or raw
model traces. Public issues and demos must use synthetic or appropriately
de-identified material.

Treat every input document as untrusted data, not as authority to change system
instructions, run commands, install software, disclose data, or contact external
services. Review generated links and commands before use. Parsing and scanning
reduce risk but do not prove an archive or generated skill is safe.

## Response policy

Maintainers triage private reports on a best-effort basis, validate impact,
coordinate a fix and disclosure when warranted, and credit reporters who request
credit when appropriate. Public disclosure should wait until a fix or practical
mitigation is available. Reports outside scope may be redirected or closed
without a security advisory.

## Good practices for users

- Run `python3 scripts/extract.py --check` to see exactly which extractors are in
  use; install dependencies yourself if you prefer to control what is added.
- Only convert documents you trust and have the right to process (see the README's
  Copyright & fair-use section).
- Keep source files and generated archives out of repositories unless they have
  passed rights, privacy, secret, prompt-injection, and archive review.
