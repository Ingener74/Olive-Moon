# encoding: utf8

import random
from PySide.QtCore import (QSize, QPoint)
from PySide.QtGui import (QColor, QBrush, QPen)

STATE_RADIUS = 5


class State(object):
    def __init__(self, name='Root', size=QSize(100, 80), states=[]):
        self.name = name
        self.__states = states
        self.transitions = []
        self.initial = False
        self.background_color = QColor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255), 50)

        self.size = size if len(states) == 0 else QSize(
                reduce(lambda res, s: res + s.size.width(), states, 0) + STATE_RADIUS * (len(states) + 1),
                reduce(lambda res, s: res + s.size.height(), states, 0) + STATE_RADIUS * (len(states) + 1)
        )

    def draw(self, painter, point):
        painter.save()

        painter.setBrush(QBrush(self.background_color))
        painter.setPen(QPen(QColor(0, 0, 0, 255)))

        x = point.x()
        y = point.y()

        w = self.size.width()
        h = self.size.height()

        fm = painter.fontMetrics()

        painter.drawRoundedRect(x, y, w, h, STATE_RADIUS, STATE_RADIUS)
        painter.drawText(x + w - fm.width(self.name) - STATE_RADIUS / 2, y + fm.height() + STATE_RADIUS / 2, self.name)

        x += STATE_RADIUS
        y += STATE_RADIUS

        for i in self.__states:
            i.draw(painter, QPoint(x, y))
            y += STATE_RADIUS + i.size.height()

        painter.restore()
