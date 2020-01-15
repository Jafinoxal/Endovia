# -*- coding: utf-8 -*-
# Endovia (Fountains)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 13,
    1: 13,
    2: 13,
    3: 13,
    4: 13,
    5: 13,
    }

def _identity():
    return {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    }

def _name():
    return {
    0: "Fountain",
    1: "Broken Fountain",
    2: "Spouted Fountain",
    3: "Fresh Fountain",
    4: "Salty Fountain",
    5: "Dirty Fountain",
    }

def _kind():
    return {
    0: "Fountain",
    1: "Fountain",
    2: "Fountain",
    3: "Fountain",
    4: "Fountain",
    5: "Fountain",
    }

def _description():
    return {
    0: "A fountain.",
    1: "A broken fountain that doesn't function.",
    2: "A fountain with a water supply.",
    3: "A fresh water fountain.",
    4: "A salt water fountain.",
    5: "A nasty dirty fountain.",
    }

def _symbol():
    return {
    0: u"º",
    1: u"º",
    2: u"º",
    3: u"º",
    4: u"º",
    5: u"º",
    }

def _color():
    return {
    0: ((0,127,255), (0,0,0)),
    1: ((0,127,255), (0,0,0)),
    2: ((0,127,255), (0,0,0)),
    3: ((0,127,255), (0,0,0)),
    4: ((255,0,63), (0,0,0)),
    5: ((127,0,31), (0,0,0)),
    }

def _clip():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    }

def _transparent():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    }

def fountains():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    5: (_category()[5], _identity()[5], _name()[5], _kind()[5], _description()[5], _symbol()[5], _color()[5], _clip()[5], _transparent()[5]),
    }

# Jafinoxal.
