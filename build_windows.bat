@echo off
REM Builds PDFForge-Setup-x.y.z.exe on Windows.
REM Needs: Python 3.11+ (64-bit) and Inno Setup 6 (https://jrsoftware.org/isdl.php).
setlocal
cd /d "%~dp0"

if not exist .venv (
    py -3 -m venv .venv || goto :fail
)
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip || goto :fail
pip install -r requirements.txt -r requirements-dev.txt || goto :fail

python assets\make_icon.py || goto :fail
python installer\make_wizard_images.py || goto :fail

echo Running engine tests...
python -m pytest tests -q || goto :fail

pyinstaller pdfforge.spec --noconfirm || goto :fail

set ISCC="%ProgramFiles(x86)%\Inno Setup 6\ISCC.exe"
if not exist %ISCC% set ISCC="%ProgramFiles%\Inno Setup 6\ISCC.exe"
if not exist %ISCC% (
    echo Inno Setup 6 not found. Install it, then run: iscc installer\pdfforge.iss
    goto :fail
)
%ISCC% installer\pdfforge.iss || goto :fail

echo.
echo Done. Installer is in dist_installer\
exit /b 0

:fail
echo.
echo Build failed. See the messages above.
exit /b 1
