# encoding: utf8


class Transition(object):
    def __init__(self, state, condition='', action=''):
        self.state = state
        self.condition = condition
        self.action = action

    def draw(self, painter, state):
        painter.save()

        painter.drawLine(state.transition_point, self.state.transition_point)

        painter.restore()


