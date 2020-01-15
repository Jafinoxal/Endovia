# -*- coding: utf-8 -*-
# Endovia (Doors)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 3,
    1: 3,
    2: 3,
    3: 3,
    4: 3,
    5: 3,
    6: 3,
    }

def _identity():
    return {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    }

def _name():
    return {
    0: "Door",
    1: "Wood Door",
    2: "Metal Door",
    3: "Windowed Door",
    4: "Damaged Door",
    5: "Stuck Door",
    6: "Stone Door",
    }

def _kind():
    return {
    0: "Door",
    1: "Door",
    2: "Door",
    3: "Door",
    4: "Door",
    5: "Door",
    6: "Door",
    7: "Door",
    }

def _description():
    return {
    0: "A door.",
    1: "A wood door",
    2: "A metal door.",
    3: "A door with a window.",
    4: "A damaged door.",
    5: "A door that won't open.",
    6: "A stone door.",
    }

def _symbol():
    return {
    0: "+",
    1: "+",
    2: "+",
    3: "+",
    4: "+",
    5: "+",
    6: "+",
    }

def _color():
    return {
    0: ((255,255,255), (0,0,0)),
    1: ((191,143,0), (63,47,0)),
    2: ((127,127,127), (203,203,203)),
    3: ((191,239,255), (127,127,127)),
    4: ((95,95,95), (223,223,223)),
    5: ((95,95,95), (223,223,223)),
    6: ((31,31,31), (223,223,223)),
    }

def _clip():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: True,
    }

def _transparent():
    return {
    0: False,
    1: False,
    2: False,
    3: True,
    4: False,
    5: False,
    6: False,
    }

def doors():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    5: (_category()[5], _identity()[5], _name()[5], _kind()[5], _description()[5], _symbol()[5], _color()[5], _clip()[5], _transparent()[5]),
    6: (_category()[6], _identity()[6], _name()[6], _kind()[6], _description()[6], _symbol()[6], _color()[6], _clip()[6], _transparent()[6]),
    }

# Jafinoxal.
