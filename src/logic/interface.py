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
        This method is used to set up the interface
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
        This method is used to set up the type installation buttons
        """

        # Connects the buttons to the methods
        # Every time the button is clicked, the connected function will be executed
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
        """
        Will increase the window index and changes the page.
        """

        # If there is a next page available increase the page
        if self.window_index + 1 < self.ui.stackedWidget.count():
            self.window_index += 1

            # If another installation method is checked then the advanced installation, increase the window index
            # one more time.
            if not self.ui.advancedBox.isChecked() and self.window_index == 2:
                self.window_index += 1

            # Change the page to the current index
            self.ui.stackedWidget.setCurrentIndex(self.window_index)

        # configure the buttons for the current window index
        self.configure_buttons()

    def click_back(self):
        """
        Will decrease the window index and changes the page.
        """

        # If we are not on the first page, decrease the index
        if self.window_index > 0:
            self.window_index -= 1

            # If we have not checked the advanced installation, we need to go back 2 pages of we are on the installation
            # page because we also skipped an extra one in this case.
            if not self.ui.advancedBox.isChecked() and self.window_index == 3:
                self.window_index -= 1

            # Change the page to the current index
            self.ui.stackedWidget.setCurrentIndex(self.window_index)

        # Configure the page to the window index
        self.configure_buttons()

    def click_cancel(self):
        """
        Closes the window of the installer
        """

        # If on the installation window, this button will be a next button instead of a cancel button.
        if self.window_index == 3:
            # Increase the window to go to the final window.
            self.window_index += 1
            self.ui.stackedWidget.setCurrentIndex(self.window_index)
            self.configure_buttons()
            return

        # Stop the program
        sys.exit(0)

    ############################## Configuration buttons ##############################

    def configure_buttons(self):
        """
        This method is used to enable or disable the buttons depending on the window index
        """

        # Retrieve the user his system language
        language = utils.get_dialog_language()

        # Set back button disabled and enable it if we are on page 2 or 3
        self.ui.BackButton.setDisabled(True)
        if self.window_index == 1:
            self.ui.BackButton.setEnabled(True)

        elif self.window_index == 2:
            self.ui.BackButton.setEnabled(True)

        # If we on the installation page, make the back en next button invisible and
        # make the cancel button a next button
        elif self.window_index == 3:
            self.ui.BackButton.setVisible(False)
            self.ui.NextButton.setVisible(False)
            self.ui.CancelButton.setText(utils.get_dialogs()["navigation"]["next"][language])
            self.ui.CancelButton.setDisabled(True)

        # If we are on the final page, make the button a finish button
        elif self.window_index == 4:
            self.ui.CancelButton.setText(utils.get_dialogs()["navigation"]["finish"][language])

    ############################## Type installation methods ##############################

    def select_default_installation(self):
        """
        Checks the default checkbox, disables all the others and show the default installation information.
        """

        # Retrieve the user his system language
        language = utils.get_dialog_language()

        # Unchecks all checkboxes if the default is checked
        if self.ui.defaultBox.isChecked():
            self.disable_type_installation_buttons()

        # Checks the default checkbox
        self.ui.defaultBox.setChecked(True)

        # Shows default installation information
        self.ui.set_text_installation_type_info('infoDefaultInstallation', language)

    def select_teacher_installation(self):
        """
        Checks the teacher checkbox, disables all the others and show the teacher installation information.
        """

        # Retrieve the user his system language
        language = utils.get_dialog_language()

        # Unchecks all checkboxes if the teacher is checked
        if self.ui.teacherBox.isChecked():
            self.disable_type_installation_buttons()

        # Checks the teacher checkbox
        self.ui.teacherBox.setChecked(True)

        # Shows teacher installation information
        self.ui.set_text_installation_type_info('infoTeacherInstallation', language)

    def select_advanced_installation(self):
        """
        Checks the advanced checkbox, disables all the others and show the advanced installation information.
        """
        language = utils.get_dialog_language()

        # Unchecks all checkboxes if the advanced is checked
        if self.ui.advancedBox.isChecked():
            self.disable_type_installation_buttons()

        # Checks the advanced checkbox
        self.ui.advancedBox.setChecked(True)

        # Shows advanced installation information
        self.ui.set_text_installation_type_info('infoAdvancedInstallation', language)

    def disable_type_installation_buttons(self):
        """
        This method is used to disable all the type installation buttons
        """
        self.ui.defaultBox.setChecked(False)
        self.ui.teacherBox.setChecked(False)
        self.ui.advancedBox.setChecked(False)

    ############################## Installation methods ##############################

    def install(self):
        """
        This method is used to install the selected components.
        """

        # If we are not on the installation page, return
        if self.window_index != 3:
            return

        # Check which installation type is selected
        install_type = self.check_installation_type()

        # If no installation type is selected, return
        if install_type is None:
            return

        # Check which components need to be installed
        components = self.get_installation_components(install_type)

        # If no components are selected, return
        if components is None:
            return

        try:
            # Install the components
            for step in self.install_function(
                    components["version"],
                    components["mods"],
                    components["maps"],
                    components["install_fabric"]
            ):
                # Update the progress bar and the label
                text, value = step
                self.ui.progressBar.setValue(value)
                self.ui.label_2.setText(text)
                self.ui.CancelButton.setEnabled(True)

        except Exception as error:
            # If there occurred an error, we go to the error page
            self.window_index = 4
            # We change the text of the last page so the user knows something went wrong and go to that page
            self.ui.setup_text_error_widget(utils.get_dialog_language())
            self.ui.stackedWidget.setCurrentIndex(self.window_index)
            # delete the temporary folder
            utils.delete_temporary_folder(utils.create_temporary_folder())

            self.ui.CancelButton.setEnabled(True)
            self.configure_buttons()

    def check_installation_type(self):
        """
        This method is used to check which installation type is selected
        """

        # If the default installation is selected, return default
        if self.ui.defaultBox.isChecked():
            return "default"

        # If the teacher installation is selected, return teacher
        elif self.ui.teacherBox.isChecked():
            return "teacher"

        # If the advanced installation is selected, return advanced
        elif self.ui.advancedBox.isChecked():
            return "advanced"

        return None

    def get_installation_components(self, install_type):
        """
        This method is used to get the components that need to be installed
        :param install_type: The type of installation
        :return:
        """

        # If the default installation is selected, return the default components
        if install_type == "default":
            return self.get_default_installation_components()

        # If the teacher installation is selected, return the teacher components
        elif install_type == "teacher":
            return self.get_teacher_installation_components()

        # If the advanced installation is selected, return the advanced components
        elif install_type == "advanced":
            return self.get_advanced_installation_components()

        return None

    @staticmethod
    def get_default_installation_components():
        """
        This method is used to get the default components
        """

        # Retrieve the default components from the config file
        config = utils.get_config()
        settings = config["installer-settings"]["interface_version"]['default']

        # Return the default components
        return {
            "version": settings["version"],
            "mods": settings["mods"],
            "maps": settings["maps"],
            "install_fabric": settings["fabric"]
        }

    @staticmethod
    def get_teacher_installation_components():
        """
        This method is used to get the teacher components
        """

        # Retrieve the teacher components from the config file
        config = utils.get_config()
        settings = config["installer-settings"]["interface_version"]['teacher']

        # Return the teacher components
        return {
            "version": settings["version"],
            "mods": settings["mods"],
            "maps": settings["maps"],
            "install_fabric": settings["fabric"]
        }

    def get_advanced_installation_components(self):
        """
        This method is used to get the advanced components
        """

        component_box = self.ui.componentBox

        components = {
            "version": "latest",
            "mods": [],
            "maps": [],
            "install_fabric": False
        }

        # Retrieve the components from the component box
        for i in range(component_box.topLevelItemCount()):
            # Retrieve the version
            item_version = component_box.topLevelItem(i)
            version = item_version.text(0)

            # If release is added to the version, remove it
            if '-release' in version:
                version = version.replace('-release', '')

            # Add the version to the components
            components["version"] = version

            # Retrieve the components
            for j in range(item_version.childCount()):

                # Retrieve the type (mods, maps, fabric-installer)
                item_type = item_version.child(j)
                type = item_type.text(0)

                # Retrieve the components
                for k in range(item_type.childCount()):

                    # Retrieve the component (which mod, which map)
                    item_component = item_type.child(k)
                    component = item_component.text(0)

                    # If the component is checked, add it to the components
                    if item_component.checkState(0) == Qt.Checked:
                        if type == "mods":
                            components["mods"].append(component)
                        elif type == "maps":
                            components["maps"].append(component)

                # If the fabric-installer is checked, add it to the components
                if type == "fabric-installer" and item_type.checkState(0) == Qt.Checked:
                    components["install_fabric"] = True

            # If there are mods, maps or the fabric-installer is checked, break
            # We can do this because we know from a point that there is something checked in the release (tree)
            # We now nothing else can be checked in another release (tree)
            if len(components["mods"]) > 0 or len(components["maps"]) > 0 or components["install_fabric"]:
                break

        # Return the components
        return components
