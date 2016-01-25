# encoding: utf8


class End(object):
    def __init__(self, connection=None):
        self.connection = connection
        self.__point = None

    def paint(self, painter, point):
        self.connection.paint(painter, self, point)

    def set_point(self, point):
        self.__point = point

    def get_point(self):
        return self.__point
