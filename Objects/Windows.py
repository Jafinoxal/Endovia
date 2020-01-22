# -*- coding: utf-8 -*-
# Endovia (Windows)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 2,
    1: 2,
    2: 2,
    3: 2,
    4: 2,
    5: 2,
    6: 2,
    7: 2,
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
    7: 7,
    }

def _name():
    return {
    0: "Window",
    1: "Thin Glass Window",
    2: "Thick Glass Window",
    3: "Reinforced Glass Window",
    4: "Pexi Glass Window",
    5: "Stained Glass Window",
    6: "Pane Glass Window",
    7: "Cracked Glass Window",
    }

def _kind():
    return {
    0: "Window",
    1: "Window",
    2: "Window",
    3: "Window",
    4: "Window",
    5: "Window",
    6: "Window",
    7: "Window",
    }

def _description():
    return {
    0: "A window.",
    1: "Easy to break.",
    2: "Hard to break.",
    3: "Pretty much bullet proof.",
    4: "A cheap glass window.",
    5: "A stained glass window.",
    6: "A pane glass window.",
    7: "A cracked glass window.",
    }

def _symbol(): # 224.
    return {
    0: "\xe0",
    1: "\xe0",
    2: "\xe0",
    3: "\xe0",
    4: "\xe0",
    5: "\xe0",
    6: "\xe0",
    7: "\xe0",
    }

def _color():
    return {
    0: ((255,255,255), (191,239,255)),
    1: ((255,255,255), (191,239,255)),
    2: ((255,255,255), (191,239,255)),
    3: ((255,255,255), (191,239,255)),
    4: ((255,255,255), (191,239,255)),
    5: ((165,255,165), (191,239,255)),
    6: ((255,255,255), (191,239,255)),
    7: ((255,255,255), (191,239,255)),
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
    7: True,
    }

def _transparent():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: True,
    7: True,
    }

def windows():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    5: (_category()[5], _identity()[5], _name()[5], _kind()[5], _description()[5], _symbol()[5], _color()[5], _clip()[5], _transparent()[5]),
    6: (_category()[6], _identity()[6], _name()[6], _kind()[6], _description()[6], _symbol()[6], _color()[6], _clip()[6], _transparent()[6]),
    7: (_category()[7], _identity()[7], _name()[7], _kind()[7], _description()[7], _symbol()[7], _color()[7], _clip()[7], _transparent()[7]),
    }

# Jafinoxal.
