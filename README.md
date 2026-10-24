# Rolex_key Chrome Extension Downloader
Version 2.0.0 · Manifest V3 · Extension package and developer toolkit

## v2.0.0
- Local static security scanner: broad host access, sensitive permissions, dynamic-code and remote-network patterns, CSP hints, and obfuscation indicators. Heuristics only, not a malware verdict.
- Version diff engine: compares two extension folders by relative paths and SHA-256, identifying added, removed, and changed files.
- Extension library: save IDs/names, open listings, and track IDs for scheduled metadata checks.
- Scheduled update intelligence: configurable checks while Chrome is running and notifications when parsed version metadata changes.
- JSON backup/restore for library, tracked IDs, metadata snapshots, history, and theme preference.
- Developer diagnostics for manifest versions, common MV3 issues, and missing referenced resources.
- Existing CRX validation, SHA-256, batch queue/retries, ZIP export, history, and GitHub release checker.
- Offline Python CLI for repeatable local audits and JSON output.

## Install
1. Download or clone this repository.
2. Open chrome://extensions in desktop Chrome.
3. Enable Developer mode, click Load unpacked, and select this folder.
4. Pin Rolex_key to the toolbar.

## CLI
Requires Python 3.9+ and no third-party packages.
python tools/extension_audit.py /path/to/unpacked-extension
python tools/extension_audit.py /path/to/unpacked-extension --json > audit-report.json

## Test checklist
1. Load the extension and open each dashboard tab.
2. Scan a sample extension folder and review heuristic findings.
3. Compare two folders with added, removed, and changed files.
4. Add an extension to Library and enable scheduled checks in Settings.
5. Export a JSON backup and import it again.
6. Run Dev tools and the Python CLI against a sample extension.
7. Test CRX download where Google's endpoint makes the package available.
8. Test GitHub release checking after publishing a release.

## Limitations
- Static analysis can produce false positives and false negatives; it cannot prove an extension safe.
- Metadata parsing depends on public Chrome Web Store HTML and can break when the page changes.
- Scheduled checks run while Chrome is running; they are not server-side push notifications.
- Cloud sync is represented by portable JSON backup/restore, not hosted cloud synchronization. A secure hosted service needs a separate backend and explicit account/security design.
- Local storage remains on the browser profile; exported backups may include extension IDs and history.
- CRX availability is subject to Google's endpoints and policies. Only package folders you own or are authorized to process.

## Files
manifest.json, popup.html/css/js, advanced.js, background.js, zip.js, options.html/css/js, tools/extension_audit.py.

## License
MIT (see LICENSE).
