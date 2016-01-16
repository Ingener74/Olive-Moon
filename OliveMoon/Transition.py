# encoding: utf8
from PySide.QtCore import QPoint


class Transition(object):
    def __init__(self, event=None, from_state=None, to_state=None, condition='', action=''):
        self.event = event
        self.from_state = from_state
        self.to_state = to_state
        self.condition = condition
        self.action = action

    def draw(self, painter):
        painter.save()

        painter.drawLine(self.from_state.transition_point, self.to_state.transition_point)

        x = (self.from_state.transition_point.x() + self.to_state.transition_point.x()) / 2
        y = (self.from_state.transition_point.y() + self.to_state.transition_point.y()) / 2

        painter.drawLine(self.event.output_point, QPoint(x, y))

        painter.restore()

    def dict(self):
        return {
            'on_event': self.event.name,
            'from': self.from_state.name,
            'to': self.to_state.name,
            'on_condition': self.condition,
            'do_action': self.action
        }
