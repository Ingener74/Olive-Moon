# encoding: utf8
from random import random, randrange

from PySide.QtCore import (QRect, QSize, QPoint)
from PySide.QtGui import QColor


class Block(object):
    def __init__(self, columns=[], size=QSize(100, 100),
                 bg_color=QColor(randrange(0, 255), randrange(0, 255), randrange(0, 255), 50)):
        self.bg_color = bg_color
        self.columns = columns

        self.left_pins = []
        self.right_pins = []

        self.size = size

    def paint(self, painter, point):
        painter.save()

        size = QSize(self.width(), self.height())
        painter.setBrush(self.bg_color)
        painter.drawRoundedRect(QRect(point, size), 5, 5)

        p = QPoint(point) + QPoint(0, 5)
        for c in self.columns:
            p += QPoint(5, 0)
            c.paint(painter, p)
            p += QPoint(c.width(), 0)

        painter.restore()

    def width(self):
        nc = len(self.columns)
        return reduce(lambda res, c: res + c.width(), self.columns, 0) + (nc + 1) * 5 if nc else self.size.width()

    def height(self):
        return max(c.height() for c in self.columns) + 5 * 2 if len(self.columns) else self.size.height()
