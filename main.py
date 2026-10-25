"""PDFForge entry point.  Run:  python main.py   (add --smoke to open and close, for CI)."""
import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

import app_config as C
from ui.main_window import MainWindow
from ui.theme import apply_theme


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName(C.APP_NAME)
    app.setOrganizationName(C.APP_NAME)
    apply_theme(app)
    win = MainWindow()
    win.show()
    if "--smoke" in sys.argv:
        QTimer.singleShot(1500, app.quit)
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
