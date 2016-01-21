# encoding: utf8
from PySide.QtCore import QPoint

from Templates import (STATE_CPP, STATE_H)
from jinja2 import Template


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
        between_events = max_height / len(self.__events)

        for i, e in enumerate(self.__events):
            e.paint(painter=painter, point=point + QPoint(0,
                                                          i * between_events +
                                                          between_events / 2 -
                                                          self.__events[0].height(painter) / 2))

        event_max_width = 0
        for e in self.__events:
            event_width = e.width(painter)
            event_max_width = event_max_width if event_width < event_max_width else event_width

        BETWEEN_EVENTS_AND_ROOT_STATE = 100

        self.__root_state.paint(painter, point + QPoint(event_max_width + BETWEEN_EVENTS_AND_ROOT_STATE, 0))

    def dict(self):
        return {
            'language': self.__language,
            'events': [e.dict() for e in self.__events],
            'root_state': self.__root_state
        }

    def generate_code(self, output_directory):

        data = {
        }

        with open('State.h') as state_h:
            state_h.write(Template(STATE_H).render(data))

        with open('State.cpp') as state_cpp:
            state_cpp.write(Template(STATE_CPP).render(data))
