# encoding: utf8
from SubtleMonkey import End


class Connection(object):
    def __init__(self):
        self.start = End.End(connection=self)
        self.end = End.End(connection=self)

    def paint(self, painter, end, point):
        if end == self.start:
            self.start.set_point(point)
        elif end == self.end:
            self.end.set_point(point)
        else:
            return

        if self.start.get_point() is not None and self.end.get_point() is not None:
            painter.save()

            # Здесь будем рисовать
            painter.drawLine(self.end.get_point(), self.start.get_point())

            painter.restore()

            self.start.set_point(None)
            self.end.set_point(None)
