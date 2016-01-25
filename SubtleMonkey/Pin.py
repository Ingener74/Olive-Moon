# encoding: utf8
from PySide.QtCore import QPoint
from PySide.QtGui import QColor

PIN_RADIUS = 2

PIN_OFFSET = 1


class Pin(object):
    def __init__(self):
        self.left_side_connections = []
        self.right_side_connections = []

    def paint(self, painter, point):
        painter.save()

        painter.setBrush(QColor(0, 0, 0, 255))
        painter.drawEllipse(QPoint(point) + QPoint(PIN_OFFSET, 0), PIN_RADIUS, PIN_RADIUS)
        painter.drawEllipse(QPoint(point) + QPoint(-PIN_OFFSET, 0), PIN_RADIUS, PIN_RADIUS)

        painter.restore()
