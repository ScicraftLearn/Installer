import sys

from PySide6.QtWidgets import QApplication

from src.logic.interface import LogicInterface


def interface_version():
    app = QApplication(sys.argv)
    installer = LogicInterface()
    installer.show()
    sys.exit(app.exec())
