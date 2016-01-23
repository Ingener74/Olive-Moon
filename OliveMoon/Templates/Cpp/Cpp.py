# encoding: utf8

STATE_CPP = """
/*
Generated file.
Do not edit.
*/
#include "State.h"

State::State(): _state(0){
}

State::~State(){
    if(_state)
        delete _state;
}

void State::onEnter(){
}

void State::onExit(){
}
{% for event in events %}
void State::handle{{ event.name }} ( {{event.argument.type}} {{event.argument.name}} ){
    if (_state)
        _state->handle{{event.name}}({{event.argument.name}});
}
{% endfor %}
void State::switchState(State* state){
    if(_state) {
        _state->onExit();
        delete _state;
    }
    _state = state;
    _state->onEnter();
}
"""

STATE_H = """
/*
Generated file.
Do not edit.
*/

#pragma once

class State{
public:
    State();
    virtual ~State();

    virtual void onEnter();
    virtual void onExit();

    // events
    {% for event in events %}
    virtual void handle{{ event.name }} ( {{ event.argument.type }} );
    {% endfor %}
    // end events

private:
    void switchState(State*);
    State* _state;
};
"""

DERIVATIVE_STATE_CPP = """
/*
Generated file.
Do not edit.
*/

#include "{{state.name}}State.h"

{{state.name}}State::{{state.name}}State() {
    switchState(new {{state.initial.name}}({{state.initial.parameters}}));
}

{{state.name}}State::~{{state.name}}State(){
}

{% if %}
void {{state.name}}State::onEnter(){
}
{% endif %}
{% if %}
void {{state.name}}State::onExit(){
}
{% endif %}

{% for event in events %}
void {{state.name}}State::handle{{ event.name }} ( {{event.argument.type}} {{event.argument.name}} ){
    if (_state)
        _state->handle{{event.name}}({{event.argument.name}});
}
{% endfor %}

"""

DERIVATIVE_STATE_H = """
/*
Generated file.
Do not edit.
*/

#pragma once

#include "State.h"

class {{state.name}}State: public State {
public:
    {{state.name}}State();
    virtual ~{{state.name}}State();

    {% if %}
    virtual void onEnter();
    {% endif %}
    {% if %}
    virtual void onExit();
    {% endif %}

    {% for event in events %}
    virtual void handle{{ event.name }} ( {{ event.argument.type }} );
    {% endfor %}
};
"""
