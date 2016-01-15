# encoding: utf8
import sys

from PySide.QtCore import QPoint, Qt
from PySide.QtGui import (QApplication, QWidget, QPainter)

from OliveMoon.State import State
from UiFullSunWindow import (Ui_FullSunWindow)

# Icons from
# http://findicons.com/pack/475/solar_system


class FullSunWindow(QWidget, Ui_FullSunWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.state = State(states=[
            State(name='Initial'),
            State(name='Work', states=[
                State(name='Test'),
                State(name='Complex', states=[
                    State(name='Step1'),
                    State(name='Step2'),
                    State(name='Step3')
                ])
            ]),
            State(name='End')]
        )

    def paintEvent(self, event):
        painter = QPainter(self)
        self.state.draw(painter, QPoint(0, 0))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = FullSunWindow()
    window.show()

    sys.exit(app.exec_())
