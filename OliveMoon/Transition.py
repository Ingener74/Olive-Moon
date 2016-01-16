# encoding: utf8
from PySide.QtCore import QPoint
from PySide.QtGui import QPainterPath, QColor, QBrush, QPolygon


class Transition(object):
    def __init__(self, event=None, from_state=None, to_state=None, condition='', action=''):
        self.event = event
        self.from_state = from_state
        self.to_state = to_state
        self.condition = condition
        self.action = action

    def draw(self, painter, parent_state):
        painter.save()

        x = (parent_state.transition_point.x() + max(self.from_state.transition_point.x(),
                                                     self.to_state.transition_point.x())) / 2

        painter.setBrush(QBrush(QColor(0, 0, 0, 0)))
        p1 = self.from_state.transition_point
        p2 = QPoint(x, self.from_state.transition_point.y())
        p3 = QPoint(x, self.to_state.transition_point.y())
        p4 = QPoint(self.to_state.transition_point.x(), self.to_state.transition_point.y())
        path = QPainterPath()
        path.moveTo(p1)
        path.cubicTo(p2, p3, p4)
        painter.drawPath(path)

        painter.setBrush(QBrush(QColor(0, 0, 0, 255)))
        polygon = QPolygon()
        polygon << p4 << p4 + QPoint(12, -4) << p4 + QPoint(12, 4)
        painter.drawConvexPolygon(polygon)

        painter.drawLine(self.event.output_point, self.from_state.input_point)

        painter.restore()

    def dict(self):
        return {
            'on_event': self.event.name,
            'from': self.from_state.name,
            'to': self.to_state.name,
            'on_condition': self.condition,
            'do_action': self.action
        }
