# encoding: utf8
from PySide.QtCore import QSize, QPoint

BORDER_SIZE = 5


class Column(object):
    def __init__(self, blocks=[], size=QSize(100, 100)):
        self.blocks = blocks
        self.__size = size

    def paint(self, painter, point):
        painter.save()

        # for b in self.blocks:
        #     b.paint(painter, QPoint(0, 0))

        painter.restore()

    def width(self):
        return max(b.width() for b in self.blocks) + self.all_border_size() if len(self.blocks) else self.__size.width()

    def height(self):
        return reduce(lambda res, b: res + b.height()) + self.all_border_size() if \
            len(self.blocks) else self.__size.height()

    def all_border_size(self):
        return (len(self.blocks) + 1) * BORDER_SIZE
