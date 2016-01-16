# encoding: utf8
from PySide.QtCore import (QPoint, QSize)

EVENT_RADIUS = 5


class Event(object):
    def __init__(self, name):
        self.name = name
        self.size = QSize(80, 40)

    def draw(self, painter, point=QPoint(0, 0)):
        painter.save()

        fm = painter.fontMetrics()

        self.size = QSize(fm.width(self.name) + 40, fm.height() + 40)

        painter.drawRoundedRect(point.x(), point.y(), self.size.width(), self.size.height(), EVENT_RADIUS, EVENT_RADIUS)
        painter.drawText(point.x() + EVENT_RADIUS, point.y() + fm.height() + EVENT_RADIUS, self.name)

        painter.restore()
