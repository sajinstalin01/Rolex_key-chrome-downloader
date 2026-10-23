# Rolex_key Chrome Extension Downloader

Manifest V3 extension focused **only on Chrome extension packages**. Universal website/file downloading has been removed.

## Features
- Inspect a Chrome Web Store listing URL or extension ID.
- Show listing name, ID, and version when the public page exposes them.
- Request a CRX package from Google's update endpoint when available.
- Package a locally selected extension folder containing `manifest.json` into ZIP.
- Local download history, dark/light theme, and GitHub release update checker.
- Files selected for ZIP export are processed locally and are not uploaded.

## Limitations
Google does not guarantee that every listing can be retrieved as CRX. Store metadata parsing can break if Google changes its page. This extension does not bypass authentication, paid access, DRM, or other access controls. ZIP export packages a local extension folder you own or are authorized to package; it does not extract protected extensions from another user's browser.

## Install
1. Download/clone this repository.
2. Open `chrome://extensions` in Chrome.
3. Enable **Developer mode**.
4. Select **Load unpacked** and choose this folder containing `manifest.json`.
5. Pin Rolex_key to the toolbar.

## Test checklist
1. Paste a Chrome Web Store listing URL or extension ID and click **Inspect**.
2. Confirm ID validation and metadata when publicly available.
3. Try **Download CRX package**; unavailable packages should show an error.
4. Choose a local extension folder containing `manifest.json`, then export it as ZIP.
5. Check history, clear it, and toggle theme.
6. Open Settings & updates and test the release checker after a GitHub Release exists.

## Project files
- `manifest.json` — Manifest V3 configuration
- `popup.html/css/js` — extension-only dashboard
- `background.js` — download status and local history
- `zip.js` — local ZIP packaging
- `options.html/css/js` — theme and release update settings

## License
MIT (see `LICENSE`).
