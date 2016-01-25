# encoding: utf8
from random import randrange

from PySide.QtCore import (QRect, QSize, QPoint)
from PySide.QtGui import QColor

BLOCK_RADIUS = 5


class Block(object):
    def __init__(self, columns=[], size=QSize(100, 100),
                 bg_color=QColor(randrange(0, 255), randrange(0, 255), randrange(0, 255), 50), left_pins=[],
                 right_pins=[]):
        self.bg_color = bg_color
        self.columns = columns

        self.left_pins = left_pins
        self.right_pins = right_pins

        self.size = size

    def paint(self, painter, point):
        painter.save()

        size = QSize(self.width(), self.height())
        painter.setBrush(self.bg_color)
        painter.drawRoundedRect(QRect(point, size), BLOCK_RADIUS, BLOCK_RADIUS)

        # Рисуем столбцы
        p = QPoint(point) + QPoint(0, BLOCK_RADIUS)
        for c in self.columns:
            p += QPoint(BLOCK_RADIUS, 0)
            c.paint(painter, p)
            p += QPoint(c.width(), 0)

        # Рисуем левые порты
        if len(self.left_pins):
            p = QPoint(point)
            p += QPoint(0, size.height() / (len(self.left_pins) + 1))
            for lp in self.left_pins:
                lp.paint(painter, p)
                p += QPoint(0, size.height() / (len(self.left_pins) + 1))

        # Рисуем правые порты
        if len(self.right_pins):
            p = QPoint(point)
            p += QPoint(size.width(), size.height() / (len(self.right_pins) + 1))
            for rp in self.right_pins:
                rp.paint(painter, p)
                p += QPoint(0, size.height() / (len(self.right_pins) + 1))

        painter.restore()

    def width(self):
        nc = len(self.columns)
        return reduce(lambda res, c: res + c.width(), self.columns, 0) + (nc + 1) * 5 if nc else self.size.width()

    def height(self):
        return max(c.height() for c in self.columns) + 5 * 2 if len(self.columns) else self.size.height()
