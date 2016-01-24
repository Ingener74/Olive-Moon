# encoding: utf8
from PySide.QtCore import (QRect, QSize, QPoint)


class Block(object):
    def __init__(self, columns=[], size=QSize(100, 100)):
        self.columns = columns

        self.left_pins = []
        self.right_pins = []

        self.size = size

    def paint(self, painter, point):
        painter.save()

        size = QSize(self.width(), self.height())
        painter.drawRoundedRect(QRect(point, size), 5, 5)

        for c in self.columns:
            c.paint(painter, QPoint(5, 5))

        painter.restore()

    def width(self):
        return reduce(lambda res, c: res + c.width(), self.columns, 0) + (len(self.columns) + 1) * 5 \
            if len(self.columns) else self.size.width()

    def height(self):
        return max(c.width() for c in self.columns) if len(self.columns) else self.size.height()
