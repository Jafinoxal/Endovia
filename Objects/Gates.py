# -*- coding: utf-8 -*-
# Endovia (Gates)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def category():
    return {
    0: 5,
    1: 5,
    2: 5,
    3: 5,
    4: 5,
    5: 5,
    6: 5,
    }

def identity():
    return {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    }

def name():
    return {
    0: "Gate",
    1: "Short Wood Gate",
    2: "Tall Wood Gate",
    3: "Picket Gate",
    4: "Chain Link Gate",
    5: "Barb Wire Gate",
    6: "ELectric Gate",
    }

def kind():
    return {
    0: "Gate",
    1: "Gate",
    2: "Gate",
    3: "Gate",
    4: "Gate",
    5: "Gate",
    6: "Gate",
    }

def description():
    return {
    0: "A gate",
    1: "A short wood gate",
    2: "A tall wood gate.",
    3: "A picket gate, how friendly.",
    4: "A chain link gate.",
    5: "Go through, not over.",
    6: "Safe when turned off.",
    }

def symbol():
    return {
    0: "+",
    1: "+",
    2: "+",
    3: "+",
    4: "+",
    5: "+",
    6: "+",
    }

def color():
    return {
    0: ((255,255,255), (0,0,0)),
    1: ((191,0,47), (63,47,0)),
    2: ((191,0,47), (63,47,0)),
    3: ((159,159,159), (223,223,223)),
    4: ((63,63,63), (203,203,203)),
    5: ((63,63,63), (203,203,203)),
    6: ((63,63,63), (203,203,203)),
    }

def clip():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: True,
    }

def transparent():
    return {
    0: False,
    1: True,
    2: False,
    3: True,
    4: True,
    5: True,
    6: True,
    }

def gates():
    return {
    0: (category()[0], identity()[0], name()[0], kind()[0], description()[0], symbol()[0], color()[0], clip()[0], transparent()[0]),
    1: (category()[1], identity()[1], name()[1], kind()[1], description()[1], symbol()[1], color()[1], clip()[1], transparent()[1]),
    2: (category()[2], identity()[2], name()[2], kind()[2], description()[2], symbol()[2], color()[2], clip()[2], transparent()[2]),
    3: (category()[3], identity()[3], name()[3], kind()[3], description()[3], symbol()[3], color()[3], clip()[3], transparent()[3]),
    4: (category()[4], identity()[4], name()[4], kind()[4], description()[4], symbol()[4], color()[4], clip()[4], transparent()[4]),
    5: (category()[5], identity()[5], name()[5], kind()[5], description()[5], symbol()[5], color()[5], clip()[5], transparent()[5]),
    6: (category()[6], identity()[6], name()[6], kind()[6], description()[6], symbol()[6], color()[6], clip()[6], transparent()[6]),
    }

# Jafinoxal.
