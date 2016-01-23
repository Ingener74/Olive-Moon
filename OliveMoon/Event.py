# encoding: utf8


class Event(object):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def paint(self, painter, point):
        painter.save()

        painter.restore()

    def dict(self):
        return {
            'name': self.name
        }