# encoding: utf8


class Column(object):
    def __init__(self, blocks=None):
        self.blocks = blocks

    def paint(self, painter, point):
        painter.save()

        painter.restore()

    def width(self):
        return max(b.width() for b in self.blocks) if len(self.blocks) else 100

    def height(self):
        return reduce(lambda res, b: res + b.height()) if len(self.blocks) else 100
