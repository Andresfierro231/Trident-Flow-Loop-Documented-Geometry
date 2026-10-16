# Stop automatic Google Drive copying on this Mac

Checked against Google Drive Help on 2026-10-16. These instructions apply to Google Drive for desktop; the exact watched parent folder must be checked in its preferences.

## Pause copying now

1. Click the Google Drive triangle in the Mac menu bar. If needed, open Google Drive from Applications.
2. Click the gear and choose **Pause syncing**. This pauses Drive's background syncing generally.

## Stop syncing this folder permanently

1. Open the Drive menu, then the gear, then **Preferences**.
2. Open the section for folders from your computer (the label may be **My Mac** or **Folders from your computer**).
3. Find **Documents**, **Codex**, or the specific project folder. Select the actual watched parent that contains Documents/Codex.
4. Turn off **Sync with Google Drive** for that folder. Confirm **Stop syncing** and save if prompted. Turning it off for Documents affects the other folders beneath Documents too.
5. If you instead find this folder within **Folders from Drive / My Drive** mirroring, keep your project outside the mirrored My Drive location. Changing mirroring to streaming still keeps files in Google Drive and does not make the project local-only.
6. Resume your other Drive syncing after this folder is excluded.
7. Extract VCU_control_template.zip into the folder you have excluded, or another confirmed unsynced project directory. Verify that a newly created harmless local test file does not appear in Drive after it has had time to sync.

Pausing is temporary; folder exclusion is the lasting change. The project ZIP was preserved while the separate unpacked copies were removed. Do not delete the ZIP until the transferred/extracted package has been checked.

If this folder is absent from Drive's preferences, the copying service has not been identified. Do not change unrelated folder settings; inspect the app/workspace storage settings instead.

Official instructions:
- Pause syncing: https://support.google.com/drive/answer/13470231?hl=en
- Stop syncing a computer folder: https://support.google.com/drive/answer/2565956?hl=en
- Mirroring and streaming: https://support.google.com/drive/answer/13401938?hl=en
