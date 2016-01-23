# encoding: utf8


class State(object):
    def __init__(self, name='Root', states=None, event_transitions=None):
        self.name = name
        self.states = states
        self.event_transitions = event_transitions

    def paint(self, painter):
        painter.save()

        painter.restore()

    def dict(self):
        return {
        }

    def code(self):
        return ''
