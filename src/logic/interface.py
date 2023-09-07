import sys

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget

import src.logic.utils as utils
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
        self.ui.stackedWidget.currentChanged.connect(self.page_changed)
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

    def page_changed(self):
        """
        This function is called when a page is changed.
        It calls the installation method, but makes sure the widget is first switched to the installation page
        """
        if self.window_index == 3:
            QTimer.singleShot(100, self.install)

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

    def click_cancel(self):
        if self.window_index == 3:
            self.window_index += 1
            self.ui.stackedWidget.setCurrentIndex(self.window_index)
            self.configure_buttons()
            return
        sys.exit(0)

    ############################## Configuration buttons ##############################

    def configure_buttons(self):
        """
        This method is used to enable or disable the buttons depending on the window index
        """

        language = utils.get_dialog_language()

        self.ui.BackButton.setDisabled(True)
        if self.window_index == 1:
            self.ui.BackButton.setEnabled(True)

        elif self.window_index == 2:
            self.ui.BackButton.setEnabled(True)

        elif self.window_index == 3:
            self.ui.BackButton.setVisible(False)
            self.ui.NextButton.setVisible(False)
            self.ui.CancelButton.setText(utils.get_dialogs()["navigation"]["next"][language])
            self.ui.CancelButton.setDisabled(True)

        elif self.window_index == 4:
            self.ui.CancelButton.setText(utils.get_dialogs()["navigation"]["finish"][language])

    ############################## Type installation methods ##############################

    def select_default_installation(self):

        language = utils.get_dialog_language()

        if self.ui.defaultBox.isChecked():
            self.disable_type_installation_buttons()

        self.ui.defaultBox.setChecked(True)
        self.ui.set_text_installation_type_info('infoDefaultInstallation', language)

    def select_teacher_installation(self):

        language = utils.get_dialog_language()

        if self.ui.teacherBox.isChecked():
            self.disable_type_installation_buttons()

        self.ui.teacherBox.setChecked(True)
        self.ui.set_text_installation_type_info('infoTeacherInstallation', language)

    def select_advanced_installation(self):

        language = utils.get_dialog_language()

        if self.ui.advancedBox.isChecked():
            self.disable_type_installation_buttons()

        self.ui.advancedBox.setChecked(True)
        self.ui.set_text_installation_type_info('infoAdvancedInstallation', language)

    def disable_type_installation_buttons(self):
        self.ui.defaultBox.setChecked(False)
        self.ui.teacherBox.setChecked(False)
        self.ui.advancedBox.setChecked(False)

    ############################## Installation methods ##############################

    def install(self):
        if self.window_index != 3:
            return
        install_type = self.check_installation_type()

        if install_type is None:
            return

        components = self.get_installation_components(install_type)

        if components is None:
            return

        for step in self.install_function(
                components["version"],
                components["mods"],
                components["maps"],
                components["install_fabric"]
        ):
            text, value = step
            self.ui.progressBar.setValue(value)
            self.ui.label_2.setText(text)

        self.ui.CancelButton.setEnabled(True)

    def check_installation_type(self):
        if self.ui.defaultBox.isChecked():
            return "default"

        elif self.ui.teacherBox.isChecked():
            return "teacher"

        elif self.ui.advancedBox.isChecked():
            return "advanced"

        return None

    def get_installation_components(self, install_type):
        if install_type == "default":
            return self.get_default_installation_components()

        elif install_type == "teacher":
            return self.get_teacher_installation_components()

        elif install_type == "advanced":
            return self.get_advanced_installation_components()

        return None

    def get_default_installation_components(self):
        return {
            "version": "latest",
            "mods": ["minelabs", "dashboard-link"],
            "maps": ["demo-world"],
            "install_fabric": True
        }

    def get_teacher_installation_components(self):
        return {
            "version": "latest",
            "mods": ["minelabs"],
            "maps": ["demo-world"],
            "install_fabric": True
        }

    def get_advanced_installation_components(self):
        component_box = self.ui.componentBox

        components = {
            "version": "latest",
            "mods": [],
            "maps": [],
            "install_fabric": False
        }

        for i in range(component_box.topLevelItemCount()):
            item_version = component_box.topLevelItem(i)
            version = item_version.text(0)
            if '-release' in version:
                version = version.replace('-release', '')

            components["version"] = version
            for j in range(item_version.childCount()):
                item_type = item_version.child(j)
                type = item_type.text(0)
                for k in range(item_type.childCount()):
                    item_component = item_type.child(k)
                    component = item_component.text(0)
                    if item_component.checkState(0) == Qt.Checked:
                        if type == "mods":
                            components["mods"].append(component)
                        elif type == "maps":
                            components["maps"].append(component)
                if type == "fabric-installer" and item_type.checkState(0) == Qt.Checked:
                    components["install_fabric"] = True

            if len(components["mods"]) > 0 or len(components["maps"]) > 0 or components["install_fabric"]:
                break

        return components
