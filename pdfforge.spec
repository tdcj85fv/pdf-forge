# PyInstaller spec:  pyinstaller pdfforge.spec --noconfirm
from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = [("assets/icon.ico", "assets"), ("assets/icon.png", "assets")], [], []
for pkg in ("pypdfium2", "pypdfium2_raw", "pikepdf", "pdfplumber", "pdfminer", "docx", "pptx",
            "reportlab", "img2pdf", "pytesseract", "openpyxl"):
    try:
        d, b, h = collect_all(pkg)
        datas += d
        binaries += b
        hiddenimports += h
    except Exception:
        pass

a = Analysis(
    ["main.py"],
    pathex=["."],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports + ["core.tools_organize", "core.tools_optimize", "core.tools_convert",
                                   "core.tools_edit", "core.tools_security", "core.tools_ai"],
    excludes=["tkinter", "PySide6.QtWebEngineCore", "PySide6.QtQml", "PySide6.Qt3DCore", "PySide6.QtMultimedia"],
)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True, name="PDFForge", console=False,
          icon="assets/icon.ico", disable_windowed_traceback=False)
coll = COLLECT(exe, a.binaries, a.datas, name="PDFForge")
