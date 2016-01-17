# encoding: utf8
import json
import sys

from PySide.QtCore import QPoint, Qt
from PySide.QtGui import (QApplication, QWidget, QPainter)

from OliveMoon import (Event, State, Transition)
from UiFullSunWindow import (Ui_FullSunWindow)


# Icons from
# http://findicons.com/pack/475/solar_system

class DrawWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

    def paintEvent(self, e):
        painter = QPainter(self)


class FullSunWindow(QWidget, Ui_FullSunWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)



        keyboard = Event('Keyboard')
        ui = Event('Ui')
        network = Event('Network')
        self.events = [
            keyboard,
            Event('Mouse'),
            ui,
            network
        ]

        initial = State(name='Initial')
        test = State(name='Test')
        step1 = State(name='Step1')
        step2 = State(name='Step2')
        step3 = State(name='Step3')
        complex = State(name='Complex', states=[
            step1, step2, step3
        ], transitions=[
            Transition(event=network, from_state=step1, to_state=step2),
            Transition(event=network, from_state=step2, to_state=step3),
            # Transition(event=network, from_state=step3, to_state=step1)
        ])
        work_state = State(name='Work', states=[
            test,
            complex
        ], transitions=[
            Transition(event=ui, from_state=test, to_state=complex, condition='e.m_type == ToComplexButton',
                       action='complexView->doComplex();')
        ])
        end = State(name='End')
        self.state = State(states=[
            initial,
            work_state,
            end
        ], transitions=[
            Transition(event=ui, from_state=initial, to_state=initial),
            Transition(event=keyboard, from_state=initial, to_state=work_state, condition='e.getKey() == 27',
                       action='workView->setCaption("Test");'),
            Transition(event=network, from_state=work_state, to_state=end, condition='e.getType() == QuitSignal',
                       action='application->quit();'),
            Transition(event=ui, from_state=initial, to_state=end)
        ])

        with open('StateMachine.json', 'w') as js:
            fsm = self.state.dict()
            json.dump(obj=fsm, fp=js, separators=(',', ':'), indent=4, sort_keys=True)

    def paintEvent(self, event):
        painter = QPainter(self)

        ey = 10  # event y position
        emw = 0  # max event width
        for e in self.events:
            e.draw(painter=painter, point=QPoint(10, ey))
            ey += e.size.height() + 10
            emw = emw if e.size.width() < emw else e.size.width()

        self.state.draw(painter, QPoint(emw + 10 * 2, 10))
        # self.state.draw_transitions(painter)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = FullSunWindow()
    window.show()

    sys.exit(app.exec_())
