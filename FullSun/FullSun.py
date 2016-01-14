# encoding: utf8
import sys
from PySide.QtGui import QApplication, QWidget

# Icons from
# http://findicons.com/pack/475/solar_system
from FullSunWindow import Ui_FullSunWindow


class Window(QWidget, Ui_FullSunWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Window()
    w.show()

    app.exec_()