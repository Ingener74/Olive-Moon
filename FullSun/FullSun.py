# encoding: utf8
import sys
from PySide.QtGui import (QApplication, QWidget)
from FullSunWindow import (Ui_FullSunWindow)

# Icons from
# http://findicons.com/pack/475/solar_system


class Window(QWidget, Ui_FullSunWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec_()