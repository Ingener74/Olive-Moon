# encoding: utf8

import sys
from jinja2 import Template

from OliveMoon import (STATE_CPP, STATE_H)

if __name__ == '__main__':
    print u'Brutal Mars - генератор кода машины состояния'

    data = {
        'events':
            [
                {
                    'name': 'Keyboard',
                    'argument': {
                        'type': 'const KeyboardEvent&',
                        'name': 'keyboardEvent'
                    }
                },
                {
                    'name': 'Mouse',
                    'argument': {
                        'type': 'const MouseEvent&',
                        'name': 'mouseEvent'
                    }
                },
                {
                    'name': 'Ui',
                    'argument': {
                        'type': 'const UiEvent&',
                        'name': 'uiEvent'
                    }
                }
            ]
    }

    with open('State.h', 'w') as h:
        h.write(Template(STATE_H).render(data))

    with open('State.cpp', 'w') as cpp:
        cpp.write(Template(STATE_CPP).render(data))
