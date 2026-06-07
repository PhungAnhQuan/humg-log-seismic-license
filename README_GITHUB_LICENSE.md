# GitHub Pages license files

Upload these files to a public GitHub repository and enable GitHub Pages from the main branch/root folder.

Files:
- config.json: global remote switches for the app and Petrel export.
- licenses.json: license records indexed by salted SHA256 hash.
- make_license_hash.py: helper script to generate hashes for new license keys.

Demo license key included in licenses.json:
HUMG-DEMO-2026-001

After GitHub Pages is enabled, update LICENSE_BASE_URL in app.py, for example:
LICENSE_BASE_URL = "https://yourgithubname.github.io/humg-log-seismic-license"
