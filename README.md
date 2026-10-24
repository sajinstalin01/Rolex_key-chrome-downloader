# Rolex_key Chrome Extension Downloader

**Version 1.2.0 · Manifest V3 · Extension packages only**

The universal website/file downloader is not part of this project.

## What's new in 1.2.0
- CRX4 magic-header and CRX3 header-length validation with explicit errors.
- SHA-256 integrity hashes for CRX packages, ZIP exports, and local manifest files.
- Local Manifest V3/manifest analyzer with permission and host-access risk hints.
- Sequential batch CRX queue with up to three attempts per extension.
- Local metadata snapshots, version comparison, and a toolbar badge when a changed version is detected.
- Redesigned dark-first dashboard with Downloader, Analyzer, Batch queue, and History tabs.

## Features
- Inspect a Chrome Web Store listing URL or extension ID.
- Request CRX packages from Google's update endpoint when available.
- Package an authorized local extension folder containing `manifest.json` into ZIP.
- Keep history, hashes, metadata snapshots, and theme preferences in Chrome local storage.
- Check the latest published GitHub release from Settings.

## Install
1. Clone/download this repository.
2. Open `chrome://extensions`.
3. Enable **Developer mode**.
4. Select **Load unpacked** and choose this folder containing `manifest.json`.
5. Pin Rolex_key to the toolbar.

## Testing checklist
1. Inspect a valid 32-character extension ID and a Chrome Web Store listing URL.
2. Try an invalid ID and verify a useful error is shown.
3. Request a CRX; the response must have the CRX magic header and a plausible CRX3 header length.
4. Select a local extension folder and run the manifest analyzer.
5. Confirm the analyzer displays permissions, host permissions, risk hints, and manifest SHA-256.
6. Create a ZIP and verify its SHA-256 is displayed and stored in history.
7. Enter several IDs in Batch queue and confirm sequential progress, retries, and per-item status.
8. Inspect the same listing twice; if the publicly parsed version changes, verify the toolbar badge and popup notice.
9. Open Settings and test the GitHub release checker after a release exists.

## Limitations
- CRX availability is controlled by Google's endpoint; not every listing will yield a downloadable package.
- Public store HTML can change, and version metadata may be absent or parsed incorrectly.
- Static permission analysis is a heuristic, not a malware scanner or a guarantee of safety.
- Metadata comparison works only when the listing exposes a version that can be parsed. The toolbar badge is a local, popup-triggered notice, not a server-side push notification.
- ZIP export handles the locally selected folder you own or are authorized to package; it does not extract protected extensions from other browsers.
- No authentication, paid access, DRM, or other access controls are bypassed.

## Files
- `manifest.json` — Manifest V3 permissions/configuration
- `popup.html/css/js` — redesigned dashboard and workflows
- `background.js` — download history tracking
- `zip.js` — dependency-free local ZIP writer
- `options.html/css/js` — settings and GitHub release checker

## License
MIT (see `LICENSE`).
