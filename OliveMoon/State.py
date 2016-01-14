# encoding: utf8
from PySide.QtCore import QSize


class State(object):
    def __init__(self, name='Root', size=QSize(100, 80)):
        self.name = name
        self.states = []
        self.transitions = []
        self.initial = False

        self.size = size

    def draw(self, painter, point):

        m = .07

        x = point.x()
        y = point.y()

        if len(self.states) == 0:
            w = 100
        else:
            w = reduce(lambda res, s: res + s.size.width(), self.states, 0)
            w += (w * m) * (len(self.states) + 1)

        if len(self.states) == 0:
            h = w * 0.8
        else:
            h = reduce(lambda res, s: res + s.size.height(), self.states, 0)
            h += (w * m) * (len(self.states) + 1)

        r = w * m

        painter.drawRoundedRect(x, y, w, h, r, r)

        x += r
        y += r

        for i in self.states:
            painter.drawRoundedRect(x, y, i.size.width(), i.size.height(), r, r)

            # x += r + i.size.width()
            y += r + i.size.height()


