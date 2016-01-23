# encoding: utf8
import json
import sys

from PySide.QtCore import QPoint, Qt, QSettings
from PySide.QtGui import (QApplication, QWidget, QPainter)

from OliveMoon import (Event, State, Transition, FiniteStateMachine)
from UiFullSunWindow import (Ui_FullSunWindow)

# Icons from
# http://findicons.com/pack/475/solar_system
SPLITTER_2 = 'splitter2'
SPLITTER = 'splitter'

COMPANY = 'Venus.Games'
APPNAME = 'FullSun'


class DrawWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        keyboard = Event('Keyboard')
        ui = Event('Ui')
        network = Event('Network')
        mouse = Event('Mouse')

        step3 = State(name='Step3')
        step2 = State(name='Step2', event_transitions={keyboard: [Transition(step3)]})
        step1 = State(name='Step1', event_transitions={ui: [step2]})

        self.fsm = FiniteStateMachine(root_state=State(states=[step1, step2, step3]), events=[keyboard, ui])

        # with open('StateMachine.json', 'w') as js:
        #     fsm = self.state.dict()
        #     json.dump(obj=fsm, fp=js, separators=(',', ':'), indent=4, sort_keys=True)

        self.fsm.save()

    def paintEvent(self, e):
        self.fsm.paint(QPainter(self), QPoint(5, 5))


class FullSunWindow(QWidget, Ui_FullSunWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.widget = DrawWidget()
        self.viewVerticalLayout.addWidget(self.widget)

        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, COMPANY, APPNAME)
        self.restoreGeometry(self.settings.value(self.__class__.__name__))
        self.splitter.restoreState(self.settings.value(SPLITTER))
        self.splitter_2.restoreState(self.settings.value(SPLITTER_2))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        self.settings.setValue(self.__class__.__name__, self.saveGeometry())
        self.settings.setValue(SPLITTER, self.splitter.saveState())
        self.settings.setValue(SPLITTER_2, self.splitter_2.saveState())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = FullSunWindow()
    window.show()

    sys.exit(app.exec_())
