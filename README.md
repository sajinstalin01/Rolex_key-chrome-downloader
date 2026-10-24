# Rolex_key Chrome Extension Downloader
Version 2.3.0 · Manifest V3 · Extension package and developer toolkit

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
- GitHub release checker compares installed version 2.1.1 with the latest published release.
- AI Manifest Explainer: optionally use Google Gemini when a key is configured; otherwise use the local rule-based explainer.
- Developer diagnostics for network/endpoint failures and manifest compatibility.
- Custom accent color, compact mode, and standard/compact/wide dashboard layouts.

## Version 2.3.0 — Premium UI, setup guide, and update alerts\n- Premium extension identity icons: use the Chrome Web Store image when exposed, with a generated branded fallback based on extension name/ID.\n- Added a graphical four-step install guide with screenshot-style diagrams and direct source ZIP link.\n- Added Midnight Neon, Deep Ocean, Emerald Matrix, Royal Purple, Sunset Ember, and Crystal Light theme presets plus custom accent color.\n- Added automatic daily GitHub manifest version checks, update notifications, an in-popup update banner, and source ZIP download action.\n- Important: unpacked extensions cannot silently self-replace or self-reload. Update alerts automate detection/download, but the user must replace files and reload; Chrome Web Store installations update through Chrome.\n\n## Version 2.2.0 — CRX extractor and ZIP converter
- Added a dedicated CRX Extractor tab for locally opening CRX2/CRX3 packages.
- Lists archive files and paths, filters filenames, previews text/config files, and downloads individual files.
- Converts all extracted archive contents into a ZIP and calculates its SHA-256.
- Archive parsing is local, rejects unsafe traversal paths and encrypted entries, and limits extraction to 5,000 files / 200 MB uncompressed. ZIP64 is not supported.

## Version 2.1.1 bug fixes
- Accepts IDs from both modern and legacy Chrome Web Store listing URL formats, including a direct ID path.
- Improves CRX request timeouts, error detection, and retry handling.
- If cross-origin package fetching is blocked by Chrome/Google, falls back to Chrome's native download manager instead of failing immediately. In fallback mode, a SHA-256 cannot be calculated in the extension.
- Adds Google redirect/download host permissions used by the native-download fallback.

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
