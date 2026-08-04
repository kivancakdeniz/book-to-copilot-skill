# Licensing and reuse

This guide explains the repository's intended packaging boundaries. It is a
technical guide, not legal advice. Check the current source terms and obtain
qualified review for a specific reuse decision.

## Reuse matrix

| Material | Repository treatment | Reuse starting point | Required caution |
| --- | --- | --- | --- |
| Converter code, downstream modifications, and authored documentation | Tracked | MIT under the root `LICENSE.md` | Preserve notices and do not imply upstream or vendor endorsement. |
| Synthetic policies, cases, evaluation fixtures, and downstream articles | Tracked and identified as fictional or synthetic | MIT under the root `LICENSE.md` | Do not represent synthetic facts as real policy, evidence, customers, or legal conclusions. |
| Official law metadata and source links | Tracked without raw snapshots | Metadata and links may be reused with attribution | Verify the current official text, scope, effective date, and any applicable rights. |
| Official guidance pages | Metadata-only | Title, publisher, URL, date/version, and short independent method summary | Raw page snapshot is omitted; summary is unofficial and creates no endorsement. |
| HM Treasury Green Book | Link, metadata, and attributed method summary; raw PDF omitted | Open Government Licence v3.0 | Include the exact OGL attribution and check identified third-party material. |
| FTC and eCFR materials | Link, metadata, and independent method summary; raw snapshots omitted | U.S. federal-work rules may apply | 17 U.S.C. 105 has jurisdictional and third-party-material caveats. |
| Product UI screenshots | Selected evidence only | Repository MIT covers authored annotations and metadata | Third-party UI, logos, icons, fonts, and marks remain their owners' rights. |
| AI model outputs | Selected evaluation evidence | Provider terms and source rights may apply | Outputs may be wrong or non-unique and require human review before publication or reliance. |
| User-generated skill packages | Created from user-selected inputs | Depends on every input source and provider term | Generation does not transfer rights or automatically apply this repository's MIT licence. |

## Meaning of metadata-only

`Metadata-only` means the raw official snapshot is omitted, but the repository
may include the source title, publisher, URL, publication or effective date,
version or hash metadata, and a short independently written method summary. The
summary is included to explain an evaluation method; it is not a substitute for
the official source, an official interpretation, or permission to redistribute
the source.

## Generated packages

Before sharing a generated package, inventory its inputs, remove raw or
unnecessary source material, verify source freshness, preserve required
attribution, scan the archive for secrets and unsafe paths, and obtain human
publication approval. Generated skills based on copyrighted books or internal
documents should not be published unless the relevant rights and permissions
support that use.

The public site ZIP must contain the root `LICENSE.md` and
`THIRD_PARTY_NOTICES.md`; the release factory task includes them.

## Related documents

- [Repository notice](NOTICE.md)
- [Third-party notices](THIRD_PARTY_NOTICES.md)
- [Security policy](SECURITY.md)
- [Responsible use](RESPONSIBLE-USE.md)