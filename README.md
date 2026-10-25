# PDFForge

Offline PDF toolkit for Windows (an iLovePDF-style app where nothing leaves your PC).
Pink-red and black theme, a search bar (Ctrl+K), and a donation screen as the last page of the installer.

## Run from source
    pip install -r requirements.txt
    python main.py

## Build the Windows installer
Either double-click `build_windows.bat` (needs Python 3.11+ and Inno Setup 6),
or push this folder to GitHub and run the **Build Windows installer** workflow; the `.exe` appears as a download.

## Make it yours (one place: `app_config.py`, plus one line in `installer/pdfforge.iss`)
- `APP_NAME`, colours, `DONATE_URL` / `DONATE_MESSAGE`
- In `installer/pdfforge.iss` change `#define DonateUrl` (the installer's donation page)

## What works today
| Group | Tools |
|---|---|
| Organize | Merge, Split, Remove pages, Extract pages, Organize (reorder) |
| Optimize | Compress, Repair, OCR* |
| To PDF | JPG to PDF, Word / PowerPoint / Excel / HTML to PDF** |
| From PDF | PDF to JPG, Word, PowerPoint, Excel, Markdown, PDF/A*** |
| Edit | Rotate, Page numbers, Watermark, Crop, Edit (add text/image), PDF Forms |
| Security | Protect (AES-256), Unlock, Sign (visible), Redact (true removal), Compare |
| Intelligence | Summarizer (offline, extractive) |

Planned (already listed and searchable, marked SOON): Scan to PDF, Translate PDF, Workflows.

\* needs Tesseract OCR (put a portable copy in `third_party/` before building, or install it)
\** needs LibreOffice installed on the PC (detected automatically)
\*** needs Ghostscript (AGPL licensed; not bundled by default)

## Adding a tool
Write one function in `core/tools_*.py` and decorate it with `@register(...)` and its `Field`s.
The UI page, search entry and file validation are generated automatically.

## Tests
    pip install -r requirements-dev.txt
    python -m pytest tests -q
