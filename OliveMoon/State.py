# encoding: utf8


class State(object):
    def __init__(self, name='Root'):
        self.name = name
        self.states = []
        self.transitions = []
        self.initial = False

    def draw(self, painter):
        # painter.drawRoundedRect()
        pass


