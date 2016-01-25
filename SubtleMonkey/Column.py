# encoding: utf8
from PySide.QtCore import QSize, QPoint

BORDER_SIZE = 5


class Column(object):
    def __init__(self, blocks=[], width=100):
        self.blocks = blocks
        self.__width = width

    def paint(self, painter, point):
        painter.save()

        p = QPoint(point)
        for b in self.blocks:
            b.paint(painter, p)
            p += QPoint(0, 5)
            p += QPoint(0, b.height())

        painter.restore()

    def width(self):
        return max(b.width() for b in self.blocks) if len(self.blocks) else self.__width

    def height(self):
        return reduce(lambda res, b: res + b.height(), self.blocks, 0) + (len(self.blocks) - 1) * 5 \
            if len(self.blocks) else 0
