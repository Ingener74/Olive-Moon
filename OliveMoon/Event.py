# encoding: utf8
import random

from PySide.QtCore import (QPoint, QSize)
from PySide.QtGui import (QColor, QBrush, QPen)

EVENT_RADIUS = 5


class Event(object):
    def __init__(self, name):
        self.name = name
        self.size = QSize(80, 40)
        self.background_color = QColor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255), 50)

        self.output_point = QPoint(0, 0)

    def draw(self, painter, point=QPoint(0, 0)):
        painter.save()

        painter.setBrush(QBrush(self.background_color))
        painter.setPen(QPen(QColor(0, 0, 0, 255)))

        fm = painter.fontMetrics()

        self.size = QSize(fm.width(self.name) + 40, fm.height() + 40)

        self.output_point = QPoint(point.x() + self.size.width(), point.y() + self.size.height() / 2)

        painter.drawRoundedRect(point.x(), point.y(), self.size.width(), self.size.height(), EVENT_RADIUS, EVENT_RADIUS)
        painter.drawText(point.x() + EVENT_RADIUS, point.y() + fm.height() + EVENT_RADIUS, self.name)

        painter.restore()
