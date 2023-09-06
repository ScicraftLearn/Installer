import json
import sys

from PySide6.QtCore import (QCoreApplication)

from src.representation.ui_form import Ui_Installer


class UiInstaller(Ui_Installer):

    def __init__(self):
        super().__init__()
        self.window_index = 0

    def setupUi(self, installer):
        super().setupUi(installer)
        self.stackedWidget.setCurrentIndex(self.window_index)
        self.setup_buttons()
        self.setup_type_installation_buttons()

    def retranslateUi(self, Installer):
        dialogs = json.load(open('Resources/dialog.json', 'r', encoding='utf-8'))
        Installer.setWindowTitle(QCoreApplication.translate("Installer", f"{dialogs['window']['title']}", None))

        ### Page 1
        self.titelLabel.setText(
            QCoreApplication.translate("Installer", f"{dialogs['content']['mainWidget']['title']}", None))
        self.infoBox.setHtml(QCoreApplication.translate("Installer",
                                                        u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "hr { height: 1px; border-width: 0; }\n"
                                                        "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                        "li.checked::marker { content: \"\\2612\"; }\n"
                                                        "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                        f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{dialogs['content']['mainWidget']['info']}</p></body></html>",
                                                        None))
        self.imageBox.setText("")

        ### Page 2
        self.pageInfoBox.setHtml(QCoreApplication.translate("Installer",
                                                            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "hr { height: 1px; border-width: 0; }\n"
                                                            "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                            "li.checked::marker { content: \"\\2612\"; }\n"
                                                            "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                            f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">{dialogs['content']['typeInstallationWidget']['pageInfoBoxTitle']}</span></p>\n"
                                                            f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    {dialogs['content']['typeInstallationWidget']['extraInfoInstallation']}</p></body></html>",
                                                            None))
        self.change_installation_type_info('infoDefaultInstallation')
        self.defaultBox.setText(QCoreApplication.translate("Installer", u"Default", None))
        self.teacherBox.setText(QCoreApplication.translate("Installer", u"Teacher", None))
        self.advancedBox.setText(QCoreApplication.translate("Installer", u"Advanced", None))
        self.typeInstallationLabel.setText(QCoreApplication.translate("Installer", u"Type installation:", None))
        self.logo.setText("")

        ### Page 3
        self.logo_2.setText("")
        self.pageInfoBox_2.setHtml(QCoreApplication.translate("Installer",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "hr { height: 1px; border-width: 0; }\n"
                                                              "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                              "li.checked::marker { content: \"\\2612\"; }\n"
                                                              "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                              f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">{dialogs['content']['customInstallationWidget']['pageInfoBoxTitle']}</span></p>\n"
                                                              f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    {dialogs['content']['customInstallationWidget']['extraInfoInstallation']}</p></body></html>",
                                                              None))
        self.infoBox_2.setHtml(QCoreApplication.translate("Installer",
                                                          u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n"
                                                          "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n"
                                                          "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                          f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{dialogs['content']['customInstallationWidget']['instructions']}</p></body></html>",
                                                          None))

        __sortingEnabled = self.componentBox.isSortingEnabled()
        self.componentBox.setSortingEnabled(False)
        ___qtreewidgetitem = self.componentBox.topLevelItem(0)
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Installer", u"parent", None));
        ___qtreewidgetitem1 = ___qtreewidgetitem.child(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Installer", u"child", None));
        self.componentBox.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("Installer", u"Select components to install:", None))

        ### Page 4
        self.logo_3.setText("")
        self.pageInfoBox_3.setHtml(QCoreApplication.translate("Installer",
                                                              u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "hr { height: 1px; border-width: 0; }\n"
                                                              "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                              "li.checked::marker { content: \"\\2612\"; }\n"
                                                              "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                              f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">{dialogs['content']['installationWidget']['pageInfoBoxTitle']}</span></p>\n"
                                                              f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    {dialogs['content']['installationWidget']['extraInfoInstallation']}</p></body></html>",
                                                              None))
        self.label_2.setText(QCoreApplication.translate("Installer", u"", None))

        ### Page 5
        self.imageBox_2.setText("")
        self.infoBox_3.setHtml(QCoreApplication.translate("Installer",
                                                          u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "hr { height: 1px; border-width: 0; }\n"
                                                          "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                          "li.checked::marker { content: \"\\2612\"; }\n"
                                                          "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                          f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{dialogs['content']['finishWidget']['info_1']}</p>\n"
                                                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                          f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{dialogs['content']['finishWidget']['info_2']}</p></"
                                                          "body></html>", None))
        self.titelLabel_2.setText(
            QCoreApplication.translate("Installer", f"{dialogs['content']['finishWidget']['title']}", None))

        ### Buttons
        self.BackButton.setText(QCoreApplication.translate("Installer", u"< Back", None))
        self.NextButton.setText(QCoreApplication.translate("Installer", u"Next >", None))
        self.CancelButton.setText(QCoreApplication.translate("Installer", u"Cancel", None))

    def change_installation_type_info(self, installation_type):
        dialogs = json.load(open('Resources/dialog.json', 'r', encoding='utf-8'))

        self.installationInfoBox.setHtml(QCoreApplication.translate("Installer",
                                                                    u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                    "p, li { white-space: pre-wrap; }\n"
                                                                    "hr { height: 1px; border-width: 0; }\n"
                                                                    "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                                    "li.checked::marker { content: \"\\2612\"; }\n"
                                                                    "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                                    f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{dialogs['content']['typeInstallationWidget'][f'{installation_type}']}</p></body></html>",
                                                                    None))

    def setup_buttons(self):
        self.NextButton.clicked.connect(self.click_next)
        self.BackButton.clicked.connect(self.click_back)
        self.CancelButton.clicked.connect(self.click_cancel)
        self.NextButton.setShortcut("Ctrl+N")
        self.BackButton.setShortcut("Ctrl+B")
        self.CancelButton.setShortcut("Ctrl+Q")
        self.configure_buttons()

    def setup_type_installation_buttons(self):
        self.defaultBox.clicked.connect(self.select_default_installation)
        self.teacherBox.clicked.connect(self.select_teacher_installation)
        self.advancedBox.clicked.connect(self.select_advanced_installation)

    def select_default_installation(self):
        if self.defaultBox.isChecked():
            self.disable_type_installation_buttons()

        self.defaultBox.setChecked(True)
        self.change_installation_type_info('infoDefaultInstallation')

    def select_teacher_installation(self):
        if self.teacherBox.isChecked():
            self.disable_type_installation_buttons()

        self.teacherBox.setChecked(True)
        self.change_installation_type_info('infoTeacherInstallation')

    def select_advanced_installation(self):
        if self.advancedBox.isChecked():
            self.disable_type_installation_buttons()

        self.advancedBox.setChecked(True)
        self.change_installation_type_info('infoAdvancedInstallation')

    def disable_type_installation_buttons(self):
        self.defaultBox.setChecked(False)
        self.teacherBox.setChecked(False)
        self.advancedBox.setChecked(False)

    def click_next(self):
        if self.window_index + 1 < self.stackedWidget.count():
            self.window_index += 1
            if not self.advancedBox.isChecked() and self.window_index == 2:
                self.window_index += 1
            self.stackedWidget.setCurrentIndex(self.window_index)

        self.configure_buttons()

    def click_back(self):
        if self.window_index > 0:
            self.window_index -= 1
            if not self.advancedBox.isChecked() and self.window_index == 3:
                self.window_index -= 1
            self.stackedWidget.setCurrentIndex(self.window_index)

        self.configure_buttons()

    def configure_buttons(self):

        self.BackButton.setDisabled(True)
        if self.window_index == 1:
            self.BackButton.setEnabled(True)

        elif self.window_index == 2:
            self.BackButton.setEnabled(True)

        elif self.window_index == 3:
            self.BackButton.setVisible(False)
            self.NextButton.setVisible(False)
            self.CancelButton.setText("Next")
            self.CancelButton.setDisabled(True)

        elif self.window_index == 4:
            self.CancelButton.setText("Finish")

    @staticmethod
    def click_cancel():
        sys.exit(0)
