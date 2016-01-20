# encoding: utf8
from PySide.QtCore import QPoint


class FiniteStateMachine(object):
    def __init__(self, language='cpp', events=[], root_state=None):
        self.__language = language
        self.__events = events
        self.__root_state = root_state

    def add_event(self, event):
        self.__events += event

    def paint(self, painter, point):

        root_state_height = self.__root_state.height()
        events_height = reduce(lambda sum, e: sum + e.height(painter), self.__events, 0)

        max_height = max(root_state_height, events_height)

        for i, e in enumerate(self.__events):
            e.paint(painter=painter, point=point + QPoint(0, i * max_height / len(self.__events)))

        event_max_width = 0
        for e in self.__events:
            event_width = e.width(painter)
            event_max_width = event_max_width if event_width < event_max_width else event_width

    def generate_code(self, output_directory):
        pass
