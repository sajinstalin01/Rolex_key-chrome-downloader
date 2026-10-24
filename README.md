# Rolex_key Chrome Extension Downloader
Version 2.1.0 · Manifest V3 · Extension package and developer toolkit

## Phase 1 — Core upgrades
- Metadata dashboard: name, extension ID, version, publisher/author when exposed by the store page, and listing link.
- One-click ZIP export for a locally selected extension folder, with SHA-256 checksum.
- Searchable/filterable history, retry failed CRX downloads, copy extension IDs, and export metadata/history as JSON or CSV.

## Phase 2 — Security and verification
- SHA-256 for downloaded CRX packages, ZIP exports, and selected manifest files.
- Manifest inspector with permissions, host access, version, and manifest version.
- Permission-risk flags for broad host access and powerful/sensitive capabilities.
- Recorded integrity report compares saved hashes locally. A hash change is a difference signal, not publisher authentication or a malware verdict.

## Phase 3 — Productivity
- Batch queue with pause/resume/cancel and exponential backoff for temporary failures.
- Metadata snapshots and version comparison.
- Favorites and named collections for frequently used extensions.
- JSON/CSV reports and JSON backup/restore for the local library, tracked IDs, metadata, and history.

## Phase 4 — Advanced features
- GitHub release checker compares installed version 2.1.0 with the latest published release.
- AI Manifest Explainer: optionally use Google Gemini when a key is configured; otherwise use the local rule-based explainer.
- Developer diagnostics for network/endpoint failures and manifest compatibility.
- Custom accent color, compact mode, and standard/compact/wide dashboard layouts.

## Install
1. Download or clone this repository.
2. Open chrome://extensions in desktop Chrome.
3. Enable Developer mode, click Load unpacked, and select this folder.
4. Pin Rolex_key to the toolbar.

## Configure Gemini (optional)
1. Open the extension's Settings page.
2. Enter your Gemini API key and save appearance settings.
3. Use Analyzer → Explain manifest in simple language.

Only the selected manifest JSON is sent to Google's Gemini endpoint when the AI explainer is invoked. The key is stored in Chrome local storage in your profile; do not configure it on a shared device. Remove it from Settings when no longer needed. If the API is unavailable, the local rule-based explanation is used.

## CLI
Requires Python 3.9+ and no third-party packages.
```bash
python tools/extension_audit.py /path/to/unpacked-extension
python tools/extension_audit.py /path/to/unpacked-extension --json > audit-report.json
```

## Limitations
- Publisher and version metadata depend on public store HTML and may not be exposed consistently.
- Static security checks can produce false positives/negatives and cannot prove an extension safe.
- Recorded integrity compares local hashes only; it does not authenticate the original publisher.
- Scheduled update checks run while Chrome is running and depend on the store page structure.
- JSON backup/restore is local export/import, not hosted cloud sync.
- CRX download and endpoint behavior depend on Google's availability and policies.

## Automated validation
GitHub Actions checks JavaScript syntax, Python CLI syntax, Manifest V3 JSON, and required resources. Browser-based tests are still needed for real downloads, ZIP extraction, notifications, and endpoint behavior.

## Project files
manifest.json, popup.html/css/js, advanced.js, background.js, zip.js, options.html/css/js, tools/extension_audit.py, .github/workflows/validate.yml.

## License
MIT (see LICENSE).
