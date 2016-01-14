# encoding: utf8
import sys

from PySide.QtCore import QPoint
from PySide.QtGui import (QApplication, QWidget, QPainter)

from OliveMoon.State import State
from UiFullSunWindow import (Ui_FullSunWindow)

# Icons from
# http://findicons.com/pack/475/solar_system


class FullSunWindow(QWidget, Ui_FullSunWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.state = State()

        self.state.states = [State(), State()]

    def paintEvent(self, event):
        painter = QPainter(self)
        self.state.draw(painter, QPoint(0, 0))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = FullSunWindow()
    window.show()

    sys.exit(app.exec_())
