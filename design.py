# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject,
                            QSize, Qt)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(420, 628)
        MainWindow.setMinimumSize(QSize(420, 520))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.generate_tab = QWidget()
        self.generate_tab.setObjectName(u"generate_tab")
        self.gridLayout = QGridLayout(self.generate_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.qr_content = QLabel(self.generate_tab)
        self.qr_content.setObjectName(u"qr_content")
        self.qr_content.setMinimumSize(QSize(295, 295))
        self.qr_content.setMaximumSize(QSize(295, 295))
        self.qr_content.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.qr_content)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)

        self.correction_level = QComboBox(self.generate_tab)
        self.correction_level.addItem("")
        self.correction_level.addItem("")
        self.correction_level.addItem("")
        self.correction_level.addItem("")
        self.correction_level.setObjectName(u"correction_level")

        self.gridLayout.addWidget(self.correction_level, 2, 0, 1, 1)

        self.version_label = QLabel(self.generate_tab)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setMinimumSize(QSize(90, 0))
        self.version_label.setMaximumSize(QSize(90, 16777215))

        self.gridLayout.addWidget(self.version_label, 2, 1, 1, 1)

        self.version = QSpinBox(self.generate_tab)
        self.version.setObjectName(u"version")
        self.version.setMaximumSize(QSize(80, 16777215))
        self.version.setMinimum(1)
        self.version.setMaximum(40)

        self.gridLayout.addWidget(self.version, 2, 2, 1, 1)

        self.generate = QPushButton(self.generate_tab)
        self.generate.setObjectName(u"generate")

        self.gridLayout.addWidget(self.generate, 3, 0, 1, 3)

        self.text = QPlainTextEdit(self.generate_tab)
        self.text.setObjectName(u"text")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.text, 1, 0, 1, 3)

        self.tabWidget.addTab(self.generate_tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.decoded_qr_content = QLabel(self.tab_2)
        self.decoded_qr_content.setObjectName(u"decoded_qr_content")
        self.decoded_qr_content.setMinimumSize(QSize(295, 295))
        self.decoded_qr_content.setMaximumSize(QSize(295, 295))
        self.decoded_qr_content.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.decoded_qr_content)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)

        self.decoded_text = QPlainTextEdit(self.tab_2)
        self.decoded_text.setObjectName(u"decoded_text")
        self.decoded_text.setReadOnly(True)

        self.gridLayout_3.addWidget(self.decoded_text, 4, 0, 1, 2)

        self.open_file = QPushButton(self.tab_2)
        self.open_file.setObjectName(u"open_file")

        self.gridLayout_3.addWidget(self.open_file, 5, 0, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QR-code generator", None))
        self.qr_content.setText(QCoreApplication.translate("MainWindow", u"No image", None))
        self.correction_level.setItemText(0,
                                          QCoreApplication.translate("MainWindow", u"Correction level H (30%)", None))
        self.correction_level.setItemText(1,
                                          QCoreApplication.translate("MainWindow", u"Correction level Q (25%)", None))
        self.correction_level.setItemText(2,
                                          QCoreApplication.translate("MainWindow", u"Correction level M (15%)", None))
        self.correction_level.setItemText(3, QCoreApplication.translate("MainWindow", u"Correction level L (7%)", None))

        # if QT_CONFIG(tooltip)
        self.correction_level.setToolTip(QCoreApplication.translate("MainWindow",
                                                                    u"Correction level: the higher this level, the higher the acceptable level of image damage and the less information with an equal size",
                                                                    None))
        # endif // QT_CONFIG(tooltip)
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"Version:", None))
        # if QT_CONFIG(tooltip)
        self.version.setToolTip(QCoreApplication.translate("MainWindow",
                                                           u"Version affects the amount of encrypted data. The larger the version, the more data.",
                                                           None))
        # endif // QT_CONFIG(tooltip)
        self.generate.setText(QCoreApplication.translate("MainWindow", u"Generate QR-code", None))
        # if QT_CONFIG(tooltip)
        self.text.setToolTip(QCoreApplication.translate("MainWindow", u"Enter your text here.", None))
        # endif // QT_CONFIG(tooltip)
        self.text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter text", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generate_tab),
                                  QCoreApplication.translate("MainWindow", u"Generate", None))
        self.decoded_qr_content.setText(QCoreApplication.translate("MainWindow", u"No image", None))
        self.decoded_text.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Decoded text will be here", None))
        self.open_file.setText(QCoreApplication.translate("MainWindow", u"Open and decode file", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("MainWindow", u"Decode", None))
    # retranslateUi
