import sys

from PySide6.QtWidgets import QApplication, QWidget

from src.representation.ui_installer import UiInstaller


class Installer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UiInstaller()
        self.ui.setupUi(self)


def interface_version():
    app = QApplication(sys.argv)
    widget = Installer()
    widget.show()
    sys.exit(app.exec())
