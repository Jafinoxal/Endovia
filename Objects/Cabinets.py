# -*- coding: utf-8 -*-
# Endovia (Cabinets)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 20,
    1: 20,
    2: 20,
    3: 20,
    4: 20,
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
    0: "Cabinet",
    1: "Kitchen Cabinet",
    2: "Medicine Cabinet",
    3: "Gun Cabinet",
    4: "Liquor Cabinet"
    }

def _kind():
    return {
    0: "Cabinet",
    1: "Cabinet",
    2: "Cabinet",
    3: "Cabinet",
    4: "Cabinet",
    }

def _description():
    return {
    0: "A cabinet.",
    1: "A cabinet holding dishes and food.",
    2: "A cabinet holding medicines and first aid.",
    3: "A cabinet holding guns and ammo.",
    4: "Just fill the bottles with water, the parents won't know!"
    }

def _symbol(): # 127.
    return {
    0: "\x7f",
    1: "\x7f",
    2: "\x7f",
    3: "\x7f",
    4: "\x7f",
    }

def _color():
    return {
    0: ((0,0,255), (0,0,0)),
    1: ((127,0,31), (0,0,0)),
    2: ((127,0,31), (0,0,0)),
    3: ((127,0,31), (0,0,0)),
    4: ((127,0,31), (0,0,0)),
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
    0: False,
    1: False,
    2: False,
    3: False,
    4: False,
    }

def cabinets():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    }

# Jafinoxal.
