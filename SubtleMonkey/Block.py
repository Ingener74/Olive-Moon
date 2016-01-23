# encoding: utf8


class Block(object):
    def __init__(self, columns=None):
        self.columns = columns

        self.left_pins = []
        self.right_pins = []

    def paint(self, painter):
        painter.save()

        painter.restore()
