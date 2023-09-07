# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHeaderView,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QStackedWidget, QTextBrowser, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_Installer(object):
    def setupUi(self, Installer):
        if not Installer.objectName():
            Installer.setObjectName(u"Installer")
        Installer.resize(500, 400)
        Installer.setMinimumSize(QSize(500, 400))
        Installer.setMaximumSize(QSize(500, 400))
        Installer.setStyleSheet(u"background: rgb(62,62,62);")
        self.content = QFrame(Installer)
        self.content.setObjectName(u"content")
        self.content.setGeometry(QRect(0, 0, 500, 350))
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 500, 400))
        self.stackedWidget.setMinimumSize(QSize(500, 400))
        self.stackedWidget.setMaximumSize(QSize(500, 400))
        self.stackedWidget.setStyleSheet(u"background: rgb(240,240,240);")
        self.mainWidget = QWidget()
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setMinimumSize(QSize(500, 350))
        self.mainWidget.setMaximumSize(QSize(500, 350))
        self.mainWidget.setStyleSheet(u"background: rgb(240,240,240);")
        self.titelLabel = QLabel(self.mainWidget)
        self.titelLabel.setObjectName(u"titelLabel")
        self.titelLabel.setGeometry(QRect(185, 0, 315, 50))
        self.titelLabel.setMinimumSize(QSize(315, 50))
        self.titelLabel.setMaximumSize(QSize(315, 50))
        self.titelLabel.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.titelLabel.setFont(font)
        self.titelLabel.setStyleSheet(u"background: rgb(240,240,240);")
        self.infoBox = QTextBrowser(self.mainWidget)
        self.infoBox.setObjectName(u"infoBox")
        self.infoBox.setGeometry(QRect(185, 100, 315, 250))
        self.infoBox.setMinimumSize(QSize(315, 250))
        self.infoBox.setMaximumSize(QSize(315, 250))
        self.infoBox.setStyleSheet(u"background: rgb(240,240,240);")
        self.infoBox.setFrameShape(QFrame.NoFrame)
        self.imageBox = QLabel(self.mainWidget)
        self.imageBox.setObjectName(u"imageBox")
        self.imageBox.setGeometry(QRect(0, 10, 170, 170))
        self.imageBox.setMinimumSize(QSize(170, 0))
        self.imageBox.setMaximumSize(QSize(170, 350))
        self.imageBox.setStyleSheet(u"background: rgb(255,255,255);")
        self.imageBox.setPixmap(QPixmap(u"Resources/Logo.png"))
        self.imageBox.setScaledContents(True)
        self.imageBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.imageBox.setWordWrap(False)
        self.frame = QFrame(self.mainWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 178, 355))
        self.frame.setStyleSheet(u"background: rgb(255,255,255);")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.stackedWidget.addWidget(self.mainWidget)
        self.frame.raise_()
        self.titelLabel.raise_()
        self.infoBox.raise_()
        self.imageBox.raise_()
        self.typeInstallationWidget = QWidget()
        self.typeInstallationWidget.setObjectName(u"typeInstallationWidget")
        self.typeInstallationWidget.setMinimumSize(QSize(500, 350))
        self.typeInstallationWidget.setMaximumSize(QSize(500, 350))
        self.typeInstallationWidget.setStyleSheet(u"background: rgb(240, 240, 240);")
        self.pageInfoBox = QTextBrowser(self.typeInstallationWidget)
        self.pageInfoBox.setObjectName(u"pageInfoBox")
        self.pageInfoBox.setGeometry(QRect(-1, -1, 502, 65))
        self.pageInfoBox.setMinimumSize(QSize(502, 65))
        self.pageInfoBox.setMaximumSize(QSize(502, 65))
        self.pageInfoBox.setStyleSheet(u"background: rgb(255,255,255);")
        self.pageInfoBox.setFrameShape(QFrame.Box)
        self.pageInfoBox.setFrameShadow(QFrame.Sunken)
        self.installationInfoBox = QTextBrowser(self.typeInstallationWidget)
        self.installationInfoBox.setObjectName(u"installationInfoBox")
        self.installationInfoBox.setGeometry(QRect(240, 95, 250, 245))
        self.installationInfoBox.setStyleSheet(u"background: rgb(255,255,255);")
        self.installationInfoBox.setFrameShape(QFrame.Box)
        self.installationInfoBox.setFrameShadow(QFrame.Sunken)
        self.defaultBox = QCheckBox(self.typeInstallationWidget)
        self.defaultBox.setObjectName(u"defaultBox")
        self.defaultBox.setGeometry(QRect(50, 120, 181, 22))
        self.defaultBox.setAutoFillBackground(False)
        self.defaultBox.setStyleSheet(u"")
        self.defaultBox.setChecked(True)
        self.teacherBox = QCheckBox(self.typeInstallationWidget)
        self.teacherBox.setObjectName(u"teacherBox")
        self.teacherBox.setGeometry(QRect(50, 150, 181, 22))
        self.advancedBox = QCheckBox(self.typeInstallationWidget)
        self.advancedBox.setObjectName(u"advancedBox")
        self.advancedBox.setGeometry(QRect(50, 180, 181, 22))
        self.typeInstallationLabel = QLabel(self.typeInstallationWidget)
        self.typeInstallationLabel.setObjectName(u"typeInstallationLabel")
        self.typeInstallationLabel.setGeometry(QRect(15, 95, 220, 16))
        self.logo = QLabel(self.typeInstallationWidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(445, 5, 50, 50))
        self.logo.setStyleSheet(u"background: rgb(255,255,255);")
        self.logo.setPixmap(QPixmap(u"Resources/Logo.png"))
        self.logo.setScaledContents(True)
        self.stackedWidget.addWidget(self.typeInstallationWidget)
        self.customInstallationWidget = QWidget()
        self.customInstallationWidget.setObjectName(u"customInstallationWidget")
        self.customInstallationWidget.setMinimumSize(QSize(500, 350))
        self.customInstallationWidget.setMaximumSize(QSize(500, 350))
        self.customInstallationWidget.setStyleSheet(u"background: rgb(240, 240, 240);")
        self.logo_2 = QLabel(self.customInstallationWidget)
        self.logo_2.setObjectName(u"logo_2")
        self.logo_2.setGeometry(QRect(445, 5, 50, 50))
        self.logo_2.setStyleSheet(u"background: rgb(255,255,255);")
        self.logo_2.setPixmap(QPixmap(u"Resources/Logo.png"))
        self.logo_2.setScaledContents(True)
        self.pageInfoBox_2 = QTextBrowser(self.customInstallationWidget)
        self.pageInfoBox_2.setObjectName(u"pageInfoBox_2")
        self.pageInfoBox_2.setGeometry(QRect(-1, -1, 502, 65))
        self.pageInfoBox_2.setMinimumSize(QSize(502, 65))
        self.pageInfoBox_2.setMaximumSize(QSize(502, 65))
        self.pageInfoBox_2.setStyleSheet(u"background: rgb(255,255,255);")
        self.pageInfoBox_2.setFrameShape(QFrame.Box)
        self.pageInfoBox_2.setFrameShadow(QFrame.Sunken)
        self.infoBox_2 = QTextBrowser(self.customInstallationWidget)
        self.infoBox_2.setObjectName(u"infoBox_2")
        self.infoBox_2.setGeometry(QRect(10, 75, 480, 50))
        self.infoBox_2.setFrameShape(QFrame.NoFrame)
        self.infoBox_2.setFrameShadow(QFrame.Plain)
        self.componentBox = QTreeWidget(self.customInstallationWidget)
        font1 = QFont()
        font1.setKerning(False)
        self.componentBox.headerItem().setText(0, "")
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font1);
        self.componentBox.setHeaderItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.componentBox)
        __qtreewidgetitem1.setCheckState(0, Qt.Unchecked);
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2.setCheckState(0, Qt.Unchecked);
        self.componentBox.setObjectName(u"componentBox")
        self.componentBox.setGeometry(QRect(180, 140, 311, 200))
        self.componentBox.setStyleSheet(u"background: rgb(255,255,255);")
        self.componentBox.setFrameShape(QFrame.Box)
        self.componentBox.setProperty("showDropIndicator", True)
        self.componentBox.setAnimated(False)
        self.componentBox.setAllColumnsShowFocus(False)
        self.componentBox.setWordWrap(False)
        self.componentBox.setHeaderHidden(True)
        self.label = QLabel(self.customInstallationWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(15, 140, 151, 16))
        self.stackedWidget.addWidget(self.customInstallationWidget)
        self.pageInfoBox_2.raise_()
        self.logo_2.raise_()
        self.infoBox_2.raise_()
        self.componentBox.raise_()
        self.label.raise_()
        self.installationWidget = QWidget()
        self.installationWidget.setObjectName(u"installationWidget")
        self.installationWidget.setMinimumSize(QSize(500, 350))
        self.installationWidget.setMaximumSize(QSize(500, 350))
        self.installationWidget.setStyleSheet(u"background: rgb(240,240,240);")
        self.logo_3 = QLabel(self.installationWidget)
        self.logo_3.setObjectName(u"logo_3")
        self.logo_3.setGeometry(QRect(445, 5, 50, 50))
        self.logo_3.setStyleSheet(u"background: rgb(255,255,255);")
        self.logo_3.setPixmap(QPixmap(u"Resources/Logo.png"))
        self.logo_3.setScaledContents(True)
        self.pageInfoBox_3 = QTextBrowser(self.installationWidget)
        self.pageInfoBox_3.setObjectName(u"pageInfoBox_3")
        self.pageInfoBox_3.setGeometry(QRect(-1, -1, 502, 65))
        self.pageInfoBox_3.setMinimumSize(QSize(502, 65))
        self.pageInfoBox_3.setMaximumSize(QSize(502, 65))
        self.pageInfoBox_3.setStyleSheet(u"background: rgb(255,255,255);")
        self.pageInfoBox_3.setFrameShape(QFrame.Box)
        self.pageInfoBox_3.setFrameShadow(QFrame.Sunken)
        self.progressBar = QProgressBar(self.installationWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 110, 461, 23))
        self.progressBar.setValue(0)
        self.label_2 = QLabel(self.installationWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 150, 461, 20))
        self.stackedWidget.addWidget(self.installationWidget)
        self.pageInfoBox_3.raise_()
        self.logo_3.raise_()
        self.progressBar.raise_()
        self.label_2.raise_()
        self.finalWidget = QWidget()
        self.finalWidget.setObjectName(u"finalWidget")
        self.finalWidget.setMinimumSize(QSize(500, 350))
        self.finalWidget.setMaximumSize(QSize(500, 350))
        self.finalWidget.setStyleSheet(u"background: rgb(240,240,240);")
        self.imageBox_2 = QLabel(self.finalWidget)
        self.imageBox_2.setObjectName(u"imageBox_2")
        self.imageBox_2.setGeometry(QRect(0, 10, 170, 170))
        self.imageBox_2.setMinimumSize(QSize(170, 0))
        self.imageBox_2.setMaximumSize(QSize(170, 350))
        self.imageBox_2.setStyleSheet(u"background: rgb(255,255,255);")
        self.imageBox_2.setPixmap(QPixmap(u"Resources/Logo.png"))
        self.imageBox_2.setScaledContents(True)
        self.imageBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.imageBox_2.setWordWrap(False)
        self.frame_2 = QFrame(self.finalWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-1, -1, 178, 355))
        self.frame_2.setStyleSheet(u"background: rgb(255,255,255);")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.infoBox_3 = QTextBrowser(self.finalWidget)
        self.infoBox_3.setObjectName(u"infoBox_3")
        self.infoBox_3.setGeometry(QRect(185, 100, 315, 250))
        self.infoBox_3.setMinimumSize(QSize(315, 250))
        self.infoBox_3.setMaximumSize(QSize(315, 250))
        self.infoBox_3.setStyleSheet(u"background: rgb(240,240,240);")
        self.infoBox_3.setFrameShape(QFrame.NoFrame)
        self.titelLabel_2 = QLabel(self.finalWidget)
        self.titelLabel_2.setObjectName(u"titelLabel_2")
        self.titelLabel_2.setGeometry(QRect(185, 0, 315, 50))
        self.titelLabel_2.setMinimumSize(QSize(315, 50))
        self.titelLabel_2.setMaximumSize(QSize(315, 50))
        self.titelLabel_2.setBaseSize(QSize(0, 0))
        self.titelLabel_2.setFont(font)
        self.titelLabel_2.setStyleSheet(u"background: rgb(240,240,240);")
        self.stackedWidget.addWidget(self.finalWidget)
        self.frame_2.raise_()
        self.imageBox_2.raise_()
        self.infoBox_3.raise_()
        self.titelLabel_2.raise_()
        self.navigationBar = QFrame(Installer)
        self.navigationBar.setObjectName(u"navigationBar")
        self.navigationBar.setGeometry(QRect(0, 351, 500, 49))
        self.navigationBar.setMinimumSize(QSize(500, 49))
        self.navigationBar.setMaximumSize(QSize(500, 49))
        self.navigationBar.setStyleSheet(u"background: rgb(210, 210, 210);")
        self.navigationBar.setFrameShape(QFrame.StyledPanel)
        self.navigationBar.setFrameShadow(QFrame.Raised)
        self.BackButton = QPushButton(self.navigationBar)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setGeometry(QRect(230, 14, 75, 21))
        self.BackButton.setMinimumSize(QSize(75, 21))
        self.BackButton.setMaximumSize(QSize(75, 21))
        self.BackButton.setStyleSheet(u"QPushButton {\n"
"    border-style: solid;\n"
"    border-color: rgb(173,173,173);\n"
"    border-width: 1px;\n"
"    background-color: rgb(240,240,240); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-width: 2px;\n"
"	border-color: rgb(0,120,215);\n"
"	background-color: rgb(230, 230, 230); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    border-width: 1px;\n"
"    background-color: rgb(225, 225, 225); \n"
"}")
        self.NextButton = QPushButton(self.navigationBar)
        self.NextButton.setObjectName(u"NextButton")
        self.NextButton.setGeometry(QRect(310, 14, 75, 21))
        self.NextButton.setMinimumSize(QSize(75, 21))
        self.NextButton.setMaximumSize(QSize(75, 21))
        self.NextButton.setStyleSheet(u"QPushButton {\n"
"    border-style: solid;\n"
"    border-color: rgb(173,173,173);\n"
"    border-width: 1px;\n"
"    background-color: rgb(240,240,240); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-width: 2px;\n"
"	border-color: rgb(0,120,215);\n"
"	background-color: rgb(230, 230, 230); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    border-width: 1px;\n"
"    background-color: rgb(225, 225, 225); \n"
"}")
        self.CancelButton = QPushButton(self.navigationBar)
        self.CancelButton.setObjectName(u"CancelButton")
        self.CancelButton.setGeometry(QRect(410, 14, 75, 21))
        self.CancelButton.setMinimumSize(QSize(75, 21))
        self.CancelButton.setMaximumSize(QSize(75, 21))
        self.CancelButton.setStyleSheet(u"QPushButton {\n"
"    border-style: solid;\n"
"    border-color: rgb(173,173,173);\n"
"    border-width: 1px;\n"
"    background-color: rgb(240,240,240); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-width: 2px;\n"
"	border-color: rgb(0,120,215);\n"
"	background-color: rgb(230, 230, 230); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    border-width: 1px;\n"
"    background-color: rgb(225, 225, 225); \n"
"}")

        self.retranslateUi(Installer)

        self.stackedWidget.setCurrentIndex(1)
        self.BackButton.setDefault(False)


        QMetaObject.connectSlotsByName(Installer)
    # setupUi

    def retranslateUi(self, Installer):
        Installer.setWindowTitle(QCoreApplication.translate("Installer", u"Installer", None))
        self.titelLabel.setText(QCoreApplication.translate("Installer", u"Title Installer", None))
        self.infoBox.setHtml(QCoreApplication.translate("Installer", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hier kan wat extra uitleg komen over de installer.</p></body></html>", None))
        self.imageBox.setText("")
        self.pageInfoBox.setHtml(QCoreApplication.translate("Installer", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Type of installation:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    hier kan nog extra informatie komen</p></body></html>", None))
        self.installationInfoBox.setHtml(QCoreApplication.translate("Installer", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hier kan info over de geselecteerde installatie inkomen</p></body></html>", None))
        self.defaultBox.setText(QCoreApplication.translate("Installer", u"Default", None))
        self.teacherBox.setText(QCoreApplication.translate("Installer", u"Teacher", None))
        self.advancedBox.setText(QCoreApplication.translate("Installer", u"Advanced", None))
        self.typeInstallationLabel.setText(QCoreApplication.translate("Installer", u"Type installation:", None))
        self.logo.setText("")
        self.logo_2.setText("")
        self.pageInfoBox_2.setHtml(QCoreApplication.translate("Installer", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Choose components:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    hier kan nog extra informatie komen</p></body></html>", None))
        self.infoBox_2.setHtml(QCoreApplication.translate("Installer", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Check the components you want to install and uncheck the components you don't want to install. Click Next to continue.</p></body></html>", None))

        __sortingEnabled = self.componentBox.isSortingEnabled()
        self.componentBox.setSortingEnabled(False)
        ___qtreewidgetitem = self.componentBox.topLevelItem(0)
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Installer", u"parent", None));
        ___qtreewidgetitem1 = ___qtreewidgetitem.child(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Installer", u"child", None));
        self.componentBox.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("Installer", u"Select components to install:", None))
        self.logo_3.setText("")
        self.pageInfoBox_3.setHtml(QCoreApplication.translate("Installer", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Installing components:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    hier kan nog extra informatie komen</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Installer", u"Installing ...", None))
        self.imageBox_2.setText("")
        self.infoBox_3.setHtml(QCoreApplication.translate("Installer", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Setup has finished installing the required Minelabs components on your computer.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click Finish to exit Setup.</p></"
                        "body></html>", None))
        self.titelLabel_2.setText(QCoreApplication.translate("Installer", u"Completing the Minelabs installation.", None))
        self.BackButton.setText(QCoreApplication.translate("Installer", u"< Back", None))
        self.NextButton.setText(QCoreApplication.translate("Installer", u"Next >", None))
        self.CancelButton.setText(QCoreApplication.translate("Installer", u"Cancel", None))
#if QT_CONFIG(shortcut)
        self.CancelButton.setShortcut("")
#endif // QT_CONFIG(shortcut)
    # retranslateUi

