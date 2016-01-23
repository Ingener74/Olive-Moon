# encoding: utf8


class Block(object):
    def __init__(self, columns=None):
        self.columns = columns

        self.left_pins = []
        self.right_pins = []

    def paint(self, painter):
        painter.save()

        painter.restore()

    def width(self):
        return reduce(lambda res, c: res + c.width(), self.columns) if len(self.columns) else 100

    def height(self):
        return max(c.width() for c in self.columns) if len(self.columns) else 100
