# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FullSun/UiFullSunWindow.ui'
#
# Created: Thu Jan 14 22:15:27 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FullSunWindow(object):
    def setupUi(self, FullSunWindow):
        FullSunWindow.setObjectName("FullSunWindow")
        FullSunWindow.resize(840, 593)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/sun.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FullSunWindow.setWindowIcon(icon)

        self.retranslateUi(FullSunWindow)
        QtCore.QMetaObject.connectSlotsByName(FullSunWindow)

    def retranslateUi(self, FullSunWindow):
        FullSunWindow.setWindowTitle(QtGui.QApplication.translate("FullSunWindow", "Полное Солнце", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
