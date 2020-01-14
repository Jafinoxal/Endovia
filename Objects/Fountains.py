# -*- coding: utf-8 -*-
# Endovia (Fountains)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def category():
    return {
    0: 13,
    1: 13,
    2: 13,
    3: 13,
    4: 13,
    5: 13,
    }

def identity():
    return {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    }

def name():
    return {
    0: "Fountain",
    1: "Broken Fountain",
    2: "Spouted Fountain",
    3: "Fresh Fountain",
    4: "Salty Fountain",
    5: "Dirty Fountain",
    }

def kind():
    return {
    0: "Fountain",
    1: "Fountain",
    2: "Fountain",
    3: "Fountain",
    4: "Fountain",
    5: "Fountain",
    }

def description():
    return {
    0: "A fountain.",
    1: "A broken fountain that doesn't function.",
    2: "A fountain with a water supply.",
    3: "A fresh water fountain.",
    4: "A salt water fountain.",
    5: "A nasty dirty fountain.",
    }

def symbol():
    return {
    0: u"º",
    1: u"º",
    2: u"º",
    3: u"º",
    4: u"º",
    5: u"º",
    }

def color():
    return {
    0: ((0,127,255), (0,0,0)),
    1: ((0,127,255), (0,0,0)),
    2: ((0,127,255), (0,0,0)),
    3: ((0,127,255), (0,0,0)),
    4: ((255,0,63), (0,0,0)),
    5: ((127,0,31), (0,0,0)),
    }

def clip():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    }

def transparent():
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
    0: (category()[0], identity()[0], name()[0], kind()[0], description()[0], symbol()[0], color()[0], clip()[0], transparent()[0]),
    1: (category()[1], identity()[1], name()[1], kind()[1], description()[1], symbol()[1], color()[1], clip()[1], transparent()[1]),
    2: (category()[2], identity()[2], name()[2], kind()[2], description()[2], symbol()[2], color()[2], clip()[2], transparent()[2]),
    3: (category()[3], identity()[3], name()[3], kind()[3], description()[3], symbol()[3], color()[3], clip()[3], transparent()[3]),
    4: (category()[4], identity()[4], name()[4], kind()[4], description()[4], symbol()[4], color()[4], clip()[4], transparent()[4]),
    5: (category()[5], identity()[5], name()[5], kind()[5], description()[5], symbol()[5], color()[5], clip()[5], transparent()[5]),
    }
# Jafinoxal.
