# Organise_PC (Windows app)

Standalone packaging of Organise_PC: a background app that sorts, renames and
tidies your **Downloads**, **Pictures** and **Videos** folders.
Ships as a single `Organise_PC.exe` — no Python needed for end users.

## For users
1. Download `Organise_PC.exe` from the **Releases** page.
2. Run it. Windows may show "unknown publisher" — click **More info > Run anyway**.
3. It runs in the background with no window. To stop it, end `Organise_PC.exe` in Task Manager.

Settings and logs live in `%APPDATA%\Organise_PC` (type that into File Explorer's address bar):
- `.env` — optional `GEMINI_API_KEY` (AI renaming) and Telegram settings. The first run now shows a quick setup wizard, so you can paste a key without manually editing hidden files or restarting.
- `logs\activity.log` — everything the app did.

MOV → MP4 conversion needs [ffmpeg](https://ffmpeg.org) on PATH; otherwise that step is skipped.

## For the developer
**Release via GitHub:** push a tag and the workflow builds and publishes the exe.
```
git tag v1.0.0
git push origin v1.0.0
```
**Build locally:** run `build_exe.bat` → `dist\Organise_PC.exe`.
**Run from source:** `pip install -r requirements.txt` then `python main.py`
(data stays in the project folder when run this way).

Behaviour is configured in `config/settings.py` (e.g. `DRY_RUN`, `AI_RENAME_ENABLED`).
Never commit your real `.env`.
