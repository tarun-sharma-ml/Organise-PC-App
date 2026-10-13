@echo off
REM Builds dist\Organise_PC.exe locally (Windows, Python 3.10+ required).
setlocal
cd /d "%~dp0"
python -m venv .venv || goto :fail
call .venv\Scripts\activate || goto :fail
pip install -r requirements.txt pyinstaller || goto :fail
pyinstaller --noconfirm --onefile --noconsole --name Organise_PC --collect-all pypdfium2 --collect-all pillow_heif --collect-all google.genai --collect-submodules telegram main.py || goto :fail
echo.
echo Done: dist\Organise_PC.exe
pause
exit /b 0
:fail
echo Build failed.
pause
exit /b 1
