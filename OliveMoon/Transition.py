# encoding: utf8


class Transition(object):
    def __init__(self, state):
        self.state = state

    def paint(self, painter):
        painter.save()

        painter.restore()

    def dict(self):
        return {
        }
