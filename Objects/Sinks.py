# -*- coding: utf-8 -*-
# Endovia (Sinks)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 18,
    1: 18,
    2: 18,
    3: 18,
    4: 18,
    }

def _identity():
    return {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    }

def _name():
    return {
    0: "Sink",
    1: "Bathroom Sink",
    2: "Kitchen Sink",
    3: "Marble Sink",
    4: "Metal Sink",
    }

def _kind():
    return {
    0: "Sink",
    1: "Sink",
    2: "Sink",
    3: "Sink",
    4: "Sink",
    }

def _description():
    return {
    0: "A sink.",
    1: "A sink used for washing hands and grooming.",
    2: "A sink meant for washing dishes and drinking water.",
    3: "A beautiful, sink, ah the asthetics!.",
    4: "A metal sink.",
    }

def _symbol(): # 10.
    return {
    0: "\x0a",
    1: "\x0a",
    2: "\x0a",
    3: "\x0a",
    4: "\x0a",
    }

def _color():
    return {
    0: ((0,0,255), (0,0,0)),
    1: ((0,0,255), (0,0,0)),
    2: ((0,0,255), (0,0,0)),
    3: ((0,0,255), (0,0,0)),
    4: ((0,0,255), (0,0,0)),
    }

def _clip():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    }

def _transparent():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    }

def sinks():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    }

# Jafinoxal.
