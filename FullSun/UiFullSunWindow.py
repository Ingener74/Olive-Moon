# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiFullSunWindow.ui'
#
# Created: Sat Jan 23 13:57:14 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FullSunWindow(object):
    def setupUi(self, FullSunWindow):
        FullSunWindow.setObjectName("FullSunWindow")
        FullSunWindow.resize(1184, 739)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/sun.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FullSunWindow.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(FullSunWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openPushButton = QtGui.QPushButton(FullSunWindow)
        self.openPushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/folder_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openPushButton.setIcon(icon1)
        self.openPushButton.setIconSize(QtCore.QSize(32, 32))
        self.openPushButton.setObjectName("openPushButton")
        self.horizontalLayout.addWidget(self.openPushButton)
        self.closePushButton = QtGui.QPushButton(FullSunWindow)
        self.closePushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/floppy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closePushButton.setIcon(icon2)
        self.closePushButton.setIconSize(QtCore.QSize(32, 32))
        self.closePushButton.setObjectName("closePushButton")
        self.horizontalLayout.addWidget(self.closePushButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter_2 = QtGui.QSplitter(FullSunWindow)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox_2 = QtGui.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.eventListWidget = QtGui.QListWidget(self.groupBox_2)
        self.eventListWidget.setObjectName("eventListWidget")
        self.verticalLayout_2.addWidget(self.eventListWidget)
        self.groupBox_3 = QtGui.QGroupBox(self.splitter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.statesTreeWidget = QtGui.QTreeWidget(self.groupBox_3)
        self.statesTreeWidget.setObjectName("statesTreeWidget")
        self.statesTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_3.addWidget(self.statesTreeWidget)
        self.viewGroupBox = QtGui.QGroupBox(self.splitter_2)
        self.viewGroupBox.setObjectName("viewGroupBox")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.viewGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.viewVerticalLayout = QtGui.QVBoxLayout()
        self.viewVerticalLayout.setObjectName("viewVerticalLayout")
        self.verticalLayout_5.addLayout(self.viewVerticalLayout)
        self.verticalLayout.addWidget(self.splitter_2)

        self.retranslateUi(FullSunWindow)
        QtCore.QMetaObject.connectSlotsByName(FullSunWindow)

    def retranslateUi(self, FullSunWindow):
        FullSunWindow.setWindowTitle(QtGui.QApplication.translate("FullSunWindow", "Full Sun - программа для редактирования машины состояния", None, QtGui.QApplication.UnicodeUTF8))
        self.openPushButton.setShortcut(QtGui.QApplication.translate("FullSunWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.closePushButton.setShortcut(QtGui.QApplication.translate("FullSunWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("FullSunWindow", "События", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("FullSunWindow", "Дерево состояний", None, QtGui.QApplication.UnicodeUTF8))
        self.viewGroupBox.setTitle(QtGui.QApplication.translate("FullSunWindow", "Вид", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
