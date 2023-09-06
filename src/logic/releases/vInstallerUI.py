import sys

from PySide6.QtWidgets import QApplication

from src.logic.installation import *
from src.logic.interface import LogicInterface


def interface_version():
    app = QApplication(sys.argv)
    minelabs_installer = LogicInterface(run_installer)
    minelabs_installer.show()
    sys.exit(app.exec())
