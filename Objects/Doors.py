# -*- coding: utf-8 -*-
# Endovia (Doors)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def category():
    return
    {
    0: 3,
    1: 3,
    2: 3,
    3: 3,
    4: 3,
    5: 3,
    6: 3,
    }

def identity():
    return
    {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    }

def name():
    return
    {
    0: "Door",
    1: "Wood Door",
    2: "Metal Door",
    3: "Windowed Door",
    4: "Damaged Door",
    5: "Stuck Door",
    6: "Stone Door",
    }

def kind():
    return
    {
    0: "Door",
    1: "Door",
    2: "Door",
    3: "Door",
    4: "Door",
    5: "Door",
    6: "Door",
    7: "Door",
    }

def description():
    return
    {
    0: "A door.",
    1: "A wood door",
    2: "A metal door.",
    3: "A door with a window.",
    4: "A damaged door.",
    5: "A door that won't open.",
    6: "A stone door.",
    }

def symbol():
    return
    {
    0: "+",
    1: "+",
    2: "+",
    3: "+",
    4: "+",
    5: "+",
    6: "+",
    }

def color():
    return
    {
    0: ((255,255,255), (0,0,0)),
    1: ((191,143,0), (63,47,0)),
    2: ((127,127,127), (203,203,203)),
    3: ((191,239,255), (127,127,127)),
    4: ((95,95,95), (223,223,223)),
    5: ((95,95,95), (223,223,223)),
    6: ((31,31,31), (223,223,223)),
    }

def clip():
    return
    {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: True,
    }

def transparent():
    return
    {
    0: False,
    1: False,
    3: True,
    4: False,
    5: False,
    6: False,
    }

def doors():
    return
    {
    0: (category()[0], identity()[0], name()[0], kind()[0], description()[0], symbol()[0], color()[0], clip()[0], transparent()[0]),
    1: (category()[1], identity()[1], name()[1], kind()[1], description()[1], symbol()[1], color()[1], clip()[1], transparent()[1]),
    2: (category()[2], identity()[2], name()[2], kind()[2], description()[2], symbol()[2], color()[2], clip()[2], transparent()[2]),
    3: (category()[3], identity()[3], name()[3], kind()[3], description()[3], symbol()[3], color()[3], clip()[3], transparent()[3]),
    4: (category()[4], identity()[4], name()[4], kind()[4], description()[4], symbol()[4], color()[4], clip()[4], transparent()[4]),
    5: (category()[5], identity()[5], name()[5], kind()[5], description()[5], symbol()[5], color()[5], clip()[5], transparent()[5]),
    6: (category()[6], identity()[6], name()[6], kind()[6], description()[6], symbol()[6], color()[6], clip()[6], transparent()[6]),
    }

# Jafinoxal.
