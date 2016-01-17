# encoding: utf8

import random
from PySide.QtCore import (QSize, QPoint)
from PySide.QtGui import (QColor, QBrush, QPen)

STACK_OFFSET = 60

STATE_RADIUS = 5


class State(object):
    def __init__(self, name='Root', size=QSize(100, 80), states=[], transitions=[], on_enter='', on_exit=''):
        self.name = name
        self.__states = states
        self.__transitions = transitions
        self.background_color = QColor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255), 50)

        states_ = STATE_RADIUS * (len(states) + 1)
        self.size = size if len(states) == 0 else QSize(
                reduce(lambda res, s: res + s.size.width(), states, 0) + states_ + STACK_OFFSET,
                reduce(lambda res, s: res + s.size.height(), states, 0) + states_
        )

        self.on_enter = on_enter
        self.on_exit = on_exit

        self.input_point = QPoint(0, 0)
        self.transition_point = QPoint(0, 0)

        self.event_in_points = []
        self.trans_out_points = []
        self.trans_in_points = []

    def draw(self, painter, point=QPoint(0, 0)):
        painter.save()

        painter.setBrush(QBrush(self.background_color))
        painter.setPen(QPen(QColor(0, 0, 0, 255)))

        x = point.x()
        y = point.y()

        w = self.size.width()
        h = self.size.height()

        self.input_point = QPoint(x, y + h / 2)
        self.transition_point = QPoint(x + w, y + h / 2)

        fm = painter.fontMetrics()

        painter.drawRoundedRect(x, y, w, h, STATE_RADIUS, STATE_RADIUS)
        painter.drawText(x + w - fm.width(self.name) - STATE_RADIUS / 2, y + fm.height() + STATE_RADIUS / 2, self.name)

        x += STACK_OFFSET
        y += STATE_RADIUS

        for s in self.__states:
            s.draw(painter, QPoint(x, y))
            y += STATE_RADIUS + s.size.height()

        for t in self.__transitions:
            t.draw(painter, self)

        painter.restore()

    def dict(self):
        return {
            'name': self.name,
            'states': [s.dict() for s in self.__states],
            'transitions': [t.dict() for t in self.__transitions],
            'on_enter': self.on_enter,
            'on_exit': self.on_exit
        }
