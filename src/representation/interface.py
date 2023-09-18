from PySide6.QtCore import (QCoreApplication, Qt)
from PySide6.QtGui import (QPixmap, QIcon)
from PySide6.QtWidgets import QTreeWidgetItem

import src.logic.utils as utils
from src.representation.ui_form import Ui_Installer


# ####################################################################################################### #
# To generate the ui_form.py file run the following command in the terminal in the representation folder: #
# pyside6-uic form.ui -o ui_form.py                                                                       #
#                                                                                                         #
# This class is a subclass of the Ui_Installer class, this class is used to set up the interface          #
# In this way, if changed made in gui we don't lose them when we generate the ui_form.py file             #
# NOTE: if text style changes are made, you need te copy the html content from the ui_form.py file        #
# and replace it with the content in this file. (No solution found for just changing the text in the html #
# content)                                                                                                #
# ####################################################################################################### #


class Interface(Ui_Installer):

    def __init__(self):
        super().__init__()
        self.dialogs = utils.get_dialogs()

    def setupUi(self, installer):
        super().setupUi(installer)

    def retranslateUi(self, installer):
        """
        This method sets the text of the widgets from the interface for each page & buttons
        :param installer: the installer
        """
        super().retranslateUi(installer)
        # Sets the title & icon of de window the installer
        installer.setWindowTitle(QCoreApplication.translate("Installer", f"{self.dialogs['window']['title']}", None))
        installer.setWindowIcon(QIcon(utils.get_logo('ico')))

        language = utils.get_dialog_language()

        # Sets the text of the widgets from the interface for each page
        self.setup_text_main_widget(language)
        self.setup_text_type_installation_widget(language)
        self.setup_text_custom_installation_widget(language)
        self.setup_text_installation_widget(language)
        self.setup_text_finish_widget(language)

        # Sets the text of the buttons
        self.setup_text_buttons(language)

        # Sets the logos
        self.set_all_logos()

        # Sets the tree widget items
        self.setup_tree_widget_items()

    def set_all_logos(self):
        """
        This method is used to set the logos
        """
        self.imageBox.setPixmap(QPixmap(utils.get_logo('png')))
        self.logo.setPixmap(QPixmap(utils.get_logo('png')))
        self.logo_2.setPixmap(QPixmap(utils.get_logo('png')))
        self.logo_3.setPixmap(QPixmap(utils.get_logo('png')))
        self.imageBox_2.setPixmap(QPixmap(utils.get_logo('png')))

    ############################## Main widget ##############################

    def setup_text_main_widget(self, language):
        self.titelLabel.setText(self.dialogs['content']['mainWidget']['title'])
        self.infoBox.setText(self.dialogs['content']['mainWidget']['info'][language])

    ############################## type Installation Widget ##############################

    def setup_text_type_installation_widget(self, language):
        self.set_text_info_box(language)
        self.set_text_installation_type_info('infoDefaultInstallation', language)
        self.set_text_type_installation_boxes(language)
        self.set_text_type_installation_label(language)

    def set_text_info_box(self, language):
        self.pageInfoBox.setHtml(QCoreApplication.translate("Installer",
                                                            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "hr { height: 1px; border-width: 0; }\n"
                                                            "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                            "li.checked::marker { content: \"\\2612\"; }\n"
                                                            "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                            f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">"
                                                            f"{self.dialogs['content']['typeInstallationWidget']['pageInfoBoxTitle'][language]}</span></p>\n"
                                                            f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    "
                                                            f"{self.dialogs['content']['typeInstallationWidget']['extraInfoInstallation'][language]}</p></body></html>",
                                                            None))

    def set_text_installation_type_info(self, installation_type, language):
        self.installationInfoBox.setHtml(QCoreApplication.translate("Installer",
                                                                    u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                    "p, li { white-space: pre-wrap; }\n"
                                                                    "hr { height: 1px; border-width: 0; }\n"
                                                                    "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                                    "li.checked::marker { content: \"\\2612\"; }\n"
                                                                    "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                                    f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                                                                    f"{self.dialogs['content']['typeInstallationWidget'][f'{installation_type}'][language]}</p></body></html>",
                                                                    None))

    def set_text_type_installation_label(self, language):
        self.typeInstallationLabel.setText(QCoreApplication.translate("Installer",
                                                                      f"{self.dialogs['content']['typeInstallationWidget']['typeInstallationLabel'][language]}",
                                                                      None))

    def set_text_type_installation_boxes(self, language):
        self.defaultBox.setText(QCoreApplication.translate("Installer",
                                                           f"{self.dialogs['content']['typeInstallationWidget']['typeInstallations']['default'][language]}",
                                                           None))
        self.teacherBox.setText(QCoreApplication.translate("Installer",
                                                           f"{self.dialogs['content']['typeInstallationWidget']['typeInstallations']['teacher'][language]}",
                                                           None))
        self.advancedBox.setText(QCoreApplication.translate("Installer",
                                                            f"{self.dialogs['content']['typeInstallationWidget']['typeInstallations']['advanced'][language]}",
                                                            None))

    ############################## custom Installation Widget ##############################

    def setup_text_custom_installation_widget(self, language):
        self.set_text_info_box2(language)
        self.set_text_instructions(language)
        self.set_text_select_components_label(language)

    def set_text_info_box2(self, language):
        self.pageInfoBox_2.setHtml(QCoreApplication.translate("Installer",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "hr { height: 1px; border-width: 0; }\n"
                                                              "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                              "li.checked::marker { content: \"\\2612\"; }\n"
                                                              "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                              f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">"
                                                              f"{self.dialogs['content']['customInstallationWidget']['pageInfoBoxTitle'][language]}</span></p>\n"
                                                              f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    "
                                                              f"{self.dialogs['content']['customInstallationWidget']['extraInfoInstallation'][language]}</p></body></html>",
                                                              None))

    def set_text_instructions(self, language):
        self.infoBox_2.setHtml(QCoreApplication.translate("Installer",
                                                          u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n"
                                                          "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n"
                                                          "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                          f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                                                          f"{self.dialogs['content']['customInstallationWidget']['instructions'][language]}</p></body></html>",
                                                          None))

    def set_text_select_components_label(self, language):
        self.label.setText(QCoreApplication.translate("Installer",
                                                      f"{self.dialogs['content']['customInstallationWidget']['selectComponentsLabel'][language]}",
                                                      None))

    ############################## installation Widget ##############################

    def setup_text_installation_widget(self, language):
        self.pageInfoBox_3.setHtml(QCoreApplication.translate("Installer",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "hr { height: 1px; border-width: 0; }\n"
                                                              "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                              "li.checked::marker { content: \"\\2612\"; }\n"
                                                              "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                              f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">"
                                                              f"{self.dialogs['content']['installationWidget']['pageInfoBoxTitle'][language]}</span></p>\n"
                                                              f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    "
                                                              f"{self.dialogs['content']['installationWidget']['extraInfoInstallation'][language]}</p></body></html>",
                                                              None))

    def setup_tree_widget_items(self):
        """
        Creates the items of the tree widget based on the content of the config file
        """
        structure = utils.get_tree_structure_config()
        self.componentBox.clear()
        for version in structure:
            # Create the version item
            version_item = QTreeWidgetItem(self.componentBox)
            version_item.setText(0, QCoreApplication.translate("Installer", f"{version}-release", None))
            version_item.setFlags(version_item.flags() | Qt.ItemIsUserCheckable)
            version_item.setCheckState(0, Qt.Unchecked)

            # Creates the sub items
            # sub item mods
            mods_item = QTreeWidgetItem(version_item)
            mods_item.setText(0, QCoreApplication.translate("Installer", "mods", None))
            mods_item.setFlags(mods_item.flags() | Qt.ItemIsUserCheckable)
            mods_item.setCheckState(0, Qt.Unchecked)

            # sub item maps
            maps_item = QTreeWidgetItem(version_item)
            maps_item.setText(0, QCoreApplication.translate("Installer", "maps", None))
            maps_item.setFlags(mods_item.flags() | Qt.ItemIsUserCheckable)
            maps_item.setCheckState(0, Qt.Unchecked)

            # sub item fabric
            fabric = QTreeWidgetItem(version_item)
            fabric.setText(0, QCoreApplication.translate("Installer", "fabric-installer", None))
            fabric.setFlags(mods_item.flags() | Qt.ItemIsUserCheckable)
            fabric.setCheckState(0, Qt.Unchecked)

            # Adds mods to the mods item
            for i, mod in enumerate(structure[version]["mods"]):
                mod_item = QTreeWidgetItem(mods_item)
                mod_item.setText(0, QCoreApplication.translate("Installer", f"{mod}", None))
                mod_item.setFlags(mod_item.flags() | Qt.ItemIsUserCheckable)
                mod_item.setCheckState(0, Qt.Unchecked)

            # Adds maps to the maps item
            for i, map in enumerate(structure[version]["maps"]):
                map_item = QTreeWidgetItem(maps_item)
                map_item.setText(0, QCoreApplication.translate("Installer", f"{map}", None))
                map_item.setFlags(map_item.flags() | Qt.ItemIsUserCheckable)
                map_item.setCheckState(0, Qt.Unchecked)

        # A checkbox that can be checked or unchecked for deleting already installed mods
        delete_mods_item = QTreeWidgetItem(self.componentBox)
        # If changing the "Delete ... " text, also change the text in the remove_other_version_checkboxes method
        # because there is and check with "Delete" in it.
        delete_mods_item.setText(0, QCoreApplication.translate("Installer", f"Delete all previous installed mods", None))
        delete_mods_item.setFlags(delete_mods_item.flags() | Qt.ItemIsUserCheckable)
        delete_mods_item.setCheckState(0, Qt.Checked)

        # Connects the itemChanged signal to the methods, for handling the checkboxes
        # Function are mostly structured so every change will be done from the lowest child to the top
        # because if using different orders, the changes will be overwritten
        self.componentBox.itemChanged.connect(self.select_tree_structure)
        self.componentBox.itemChanged.connect(self.remove_parent_check_if_no_checked_children)
        self.componentBox.itemChanged.connect(self.check_parent_if_all_children_checked)
        self.componentBox.itemChanged.connect(self.remove_other_version_checkboxes)

    @staticmethod
    def select_tree_structure(item):
        """
        Check or uncheck all child items when a parent item is checked or unchecked
        """
        state = item.checkState(0)

        for i in range(item.childCount()):
            item.child(i).setCheckState(0, state)

    @staticmethod
    def remove_parent_check_if_no_checked_children(item):
        """
        This method is used to remove the check of the parent if no children are checked, if so the parent will be unchecked
        """
        if item.parent() is None:
            return

        parent = item.parent()
        if parent.checkState(0) == Qt.Checked:
            for i in range(parent.childCount()):
                if parent.child(i).checkState(0) == Qt.Checked:
                    return
            parent.setCheckState(0, Qt.Unchecked)

    @staticmethod
    def check_parent_if_all_children_checked(item):
        """
        This method is used to check the parent if all the children are checked, if so the parent will be checked
        """
        if item.parent() is None:
            return

        parent = item.parent()
        if parent.checkState(0) == Qt.Unchecked:
            for i in range(parent.childCount()):
                if parent.child(i).checkState(0) == Qt.Unchecked:
                    return
            parent.setCheckState(0, Qt.Checked)

    def remove_other_version_checkboxes(self, item):
        """
        This method is used to remove the checkboxes of the other versions
        :param item: The item that was checked
        """

        # If the delete checkbox is checked, the other checkboxes will not be removed
        if "Delete" in item.text(0):
            return

        # search parent of item
        parent = item
        while parent is not None:
            if parent.parent() is None:
                break
            parent = parent.parent()

        self.componentBox.blockSignals(True)
        for i in range(self.componentBox.topLevelItemCount()):
            other_version = self.componentBox.topLevelItem(i)

            # Don't uncheck the Delete checkbox
            if other_version is not parent and "Delete" not in other_version.text(0):
                for j in range(other_version.childCount()):
                    child = other_version.child(j)
                    for k in range(child.childCount()):
                        child.child(k).setCheckState(0, Qt.Unchecked)
                    child.setCheckState(0, Qt.Unchecked)
                other_version.setCheckState(0, Qt.Unchecked)
        self.componentBox.blockSignals(False)

    ############################## finish Widget ##############################

    def setup_text_finish_widget(self, language):
        self.titelLabel_2.setText(
            QCoreApplication.translate("Installer", f"{self.dialogs['content']['finishWidget']['title'][language]}",
                                       None))
        self.infoBox_3.setHtml(QCoreApplication.translate("Installer",
                                                          u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n"
                                                          "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n"
                                                          "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                          f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                                                          f"{self.dialogs['content']['finishWidget']['info_1'][language]}</p>\n"
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                          f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                                                          f"{self.dialogs['content']['finishWidget']['info_2'][language]}</p></"
                                                          "body></html>", None))

    def setup_text_error_widget(self, language):
        self.titelLabel_2.setText(
            QCoreApplication.translate("Installer", f"{self.dialogs['content']['errorWidget']['title'][language]}",
                                       None))
        self.infoBox_3.setHtml(QCoreApplication.translate("Installer",
                                                          u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n"
                                                          "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n"
                                                          "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                          f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                                                          f"{self.dialogs['content']['errorWidget']['info_1'][language]}</p>\n"
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                          f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                                                          f"{self.dialogs['content']['errorWidget']['info_2'][language]}</p></"
                                                          "body></html>", None))

    ############################## Buttons ##############################

    def setup_text_buttons(self, language):
        """
        This method is used to configure the buttons
        """

        self.BackButton.setText(
            QCoreApplication.translate("Installer", f"< {self.dialogs['navigation']['back'][language]}", None))
        self.NextButton.setText(
            QCoreApplication.translate("Installer", f"{self.dialogs['navigation']['next'][language]} >", None))
        self.CancelButton.setText(
            QCoreApplication.translate("Installer", f"{self.dialogs['navigation']['cancel'][language]}", None))
