"""Branding and links. Change these in one place."""
import sys
from pathlib import Path

APP_NAME = "PDFForge"
APP_TAGLINE = "Every PDF tool, offline on your PC"
VERSION = "0.1.0"
PUBLISHER = "PDFForge"

# Where the Donate buttons (in the app and at the end of the installer) send people.
# Replace with your own link: Ko-fi, Buy Me a Coffee, PayPal.me, a UPI page, GitHub Sponsors...
DONATE_URL = "https://example.com/donate"
DONATE_MESSAGE = (
    "PDFForge is free and works completely offline, with no uploads, no ads and no limits.\n\n"
    "If it saved you time, a small donation helps keep it free and growing."
)

# Colour theme: pinkish red on black
BG = "#0B0B0D"
PANEL = "#141417"
CARD = "#1B1B20"
CARD_HOVER = "#24242B"
BORDER = "#2C2C34"
TEXT = "#F4F4F6"
MUTED = "#9B9BA7"
ACCENT = "#FF2D55"
ACCENT_HOVER = "#FF5C7C"
ACCENT_PRESSED = "#D91F45"
ACCENT_SOFT = "#3A1220"
ERROR = "#FF6B6B"
OK = "#5BE3A0"


def resource_path(rel: str) -> Path:
    """Works both from source and from a PyInstaller bundle."""
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return base / rel
