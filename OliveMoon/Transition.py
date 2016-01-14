# encoding: utf8


class Transition(object):
    def __init__(self, **kwargs):
        state = kwargs['state']
        if 'condition' in kwargs:
            condition = kwargs['condition']

        if 'action' in kwargs:
            action = kwargs['action']


