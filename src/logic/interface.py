import sys

from PySide6.QtWidgets import QWidget

from src.representation.interface import Interface


class LogicInterface(QWidget):
    def __init__(self, install_function, parent=None):
        super().__init__(parent)
        self.ui = Interface()

        # Creates the interface layout
        self.ui.setupUi(self)

        self.install_function = install_function

        # Variable to store the window index
        self.window_index = 0

        # Variables to store the information of the installation
        self.mods_to_install = []
        self.maps_to_install = []
        self.install_fabric = True
        self.version = "latest"

        # Set up the interface
        self.setup_interface()

    ############################## Setup Methods ##############################

    def setup_interface(self):
        """
        This method is used to setup the interface
        """
        self.ui.stackedWidget.setCurrentIndex(self.window_index)
        self.setup_buttons()
        self.setup_type_installation_buttons()

    def setup_buttons(self):
        """
        This method is used to setup the buttons
        :return:
        """

        # Connects the buttons to the methods
        self.ui.NextButton.clicked.connect(self.click_next)
        self.ui.BackButton.clicked.connect(self.click_back)
        self.ui.CancelButton.clicked.connect(self.click_cancel)

        # Sets the shortcuts for the buttons
        self.ui.NextButton.setShortcut("Ctrl+N")
        self.ui.BackButton.setShortcut("Ctrl+B")
        self.ui.CancelButton.setShortcut("Ctrl+Q")

        # Sets the default button
        self.configure_buttons()

    def setup_type_installation_buttons(self):
        """
        This method is used to setup the type installation buttons
        """

        # Connects the buttons to the methods
        self.ui.defaultBox.clicked.connect(self.select_default_installation)
        self.ui.teacherBox.clicked.connect(self.select_teacher_installation)
        self.ui.advancedBox.clicked.connect(self.select_advanced_installation)

    ############################## Click Methods ##############################

    def click_next(self):
        if self.window_index + 1 < self.ui.stackedWidget.count():
            self.window_index += 1
            if not self.ui.advancedBox.isChecked() and self.window_index == 2:
                self.window_index += 1
            self.ui.stackedWidget.setCurrentIndex(self.window_index)

        self.configure_buttons()

    def click_back(self):
        if self.window_index > 0:
            self.window_index -= 1
            if not self.ui.advancedBox.isChecked() and self.window_index == 3:
                self.window_index -= 1
            self.ui.stackedWidget.setCurrentIndex(self.window_index)

        self.configure_buttons()

    @staticmethod
    def click_cancel():
        sys.exit(0)

    ############################## Configuration buttons ##############################

    def configure_buttons(self):
        """
        This method is used to enable or disable the buttons depending on the window index
        """

        self.ui.BackButton.setDisabled(True)
        if self.window_index == 1:
            self.ui.BackButton.setEnabled(True)

        elif self.window_index == 2:
            self.ui.BackButton.setEnabled(True)

        elif self.window_index == 3:
            self.ui.BackButton.setVisible(False)
            self.ui.NextButton.setVisible(False)
            self.ui.CancelButton.setText("Next")
            self.ui.CancelButton.setDisabled(True)

        elif self.window_index == 4:
            self.ui.CancelButton.setText("Finish")

    ############################## Type installation methods ##############################

    def select_default_installation(self):
        if self.ui.defaultBox.isChecked():
            self.disable_type_installation_buttons()

        self.ui.defaultBox.setChecked(True)
        self.ui.set_text_installation_type_info('infoDefaultInstallation')

    def select_teacher_installation(self):
        if self.ui.teacherBox.isChecked():
            self.disable_type_installation_buttons()

        self.ui.teacherBox.setChecked(True)
        self.ui.set_text_installation_type_info('infoTeacherInstallation')

    def select_advanced_installation(self):
        if self.ui.advancedBox.isChecked():
            self.disable_type_installation_buttons()

        self.ui.advancedBox.setChecked(True)
        self.ui.set_text_installation_type_info('infoAdvancedInstallation')

    def disable_type_installation_buttons(self):
        self.ui.defaultBox.setChecked(False)
        self.ui.teacherBox.setChecked(False)
        self.ui.advancedBox.setChecked(False)

