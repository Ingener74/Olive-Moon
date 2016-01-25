# encoding: utf8
from PySide.QtCore import QPoint
from PySide.QtGui import QColor

PIN_RADIUS = 2

PIN_OFFSET = 1


class Pin(object):
    def __init__(self, left_connections=[], right_connections=[]):
        self.left_side_connections = left_connections
        self.right_side_connections = right_connections

    def paint(self, painter, point):
        painter.save()

        painter.setBrush(QColor(0, 0, 0, 255))

        right_point = QPoint(point) + QPoint(PIN_OFFSET, 0)
        painter.drawEllipse(right_point, PIN_RADIUS, PIN_RADIUS)

        left_point = QPoint(point) + QPoint(-PIN_OFFSET, 0)
        painter.drawEllipse(left_point, PIN_RADIUS, PIN_RADIUS)

        for lc in self.left_side_connections:
            lc.paint(painter, QPoint(left_point))

        for rc in self.right_side_connections:
            rc.paint(painter, QPoint(right_point))

        painter.restore()
