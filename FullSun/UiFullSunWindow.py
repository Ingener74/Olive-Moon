# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiFullSunWindow.ui'
#
# Created: Sat Jan 16 21:18:40 2016
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

        self.retranslateUi(FullSunWindow)
        QtCore.QMetaObject.connectSlotsByName(FullSunWindow)

    def retranslateUi(self, FullSunWindow):
        FullSunWindow.setWindowTitle(QtGui.QApplication.translate("FullSunWindow", "Full Sun - программа для редактирования машины состояния", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
