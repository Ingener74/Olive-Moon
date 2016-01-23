# encoding: utf8
import json

from Templates import (STATE_CPP, STATE_H)
from jinja2 import Template


class FiniteStateMachine(object):
    def __init__(self, name='FiniteStateMachine', language='cpp', events=[], root_state=None):
        self.name = name
        self.__language = language
        self.__events = events
        self.__root_state = root_state

    def add_event(self, event):
        self.__events += event

    def paint(self, painter, point):
        pass

    def dict(self):
        return {
            'language': self.__language,
            'events': [e.dict() for e in self.__events],
            'root_state': self.__root_state.dict()
        }

    def save(self):
        with open(self.name + '.fsm', 'w') as fsm:
            json.dump(obj=self.dict(), fp=fsm, indent=4)

    def generate_code(self, output_directory):

        data = {
        }

        with open('State.h') as state_h:
            state_h.write(Template(STATE_H).render(data))

        with open('State.cpp') as state_cpp:
            state_cpp.write(Template(STATE_CPP).render(data))
