# encoding: utf8

import sys
from jinja2 import Template

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
                }
            ]
    }

    with open('State.h', 'w') as h:
        h.write(Template(open('../OliveMoon/templates/State.h.template').read()).render(data))

    with open('State.cpp', 'w') as cpp:
        cpp.write(Template(open('../OliveMoon/templates/State.cpp.template').read()).render(data))
