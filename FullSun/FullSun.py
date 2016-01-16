# encoding: utf8
import sys

from PySide.QtCore import QPoint, Qt
from PySide.QtGui import (QApplication, QWidget, QPainter)

from OliveMoon import (Event, State, Transition)
from UiFullSunWindow import (Ui_FullSunWindow)

# Icons from
# http://findicons.com/pack/475/solar_system


class FullSunWindow(QWidget, Ui_FullSunWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.events = [
            Event('Keyboard'),
            Event('Mouse'),
            Event('Ui'),
            Event('Network')
        ]

        work_state =  State(name='Work', states=[
            State(name='Test'),
            State(name='Complex', states=[
                State(name='Step1'),
                State(name='Step2'),
                State(name='Step3')
            ])
        ])

        self.state = State(states=[
            State(name='Initial', transitions=[Transition(state=work_state)]),
            work_state,
            State(name='End')]
        )

    def paintEvent(self, event):
        painter = QPainter(self)

        ey = 10 # event y position
        emw = 0 # max event width
        for e in self.events:
            e.draw(painter=painter, point=QPoint(10, ey))
            ey += e.size.height() + 10
            emw = emw if e.size.width() < emw else e.size.width()

        self.state.draw(painter, QPoint(emw + 10*2, 10))
        self.state.draw_transitions(painter)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = FullSunWindow()
    window.show()

    sys.exit(app.exec_())
