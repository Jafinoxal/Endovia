# -*- coding: utf-8 -*-
# Endovia (Windows)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def category():
    return
    {
    0: 2,
    1: 2,
    2: 2,
    3: 2,
    4: 2,
    5: 2,
    6: 2,
    7: 2,
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
    7: 7,
    }

def name():
    return
    {
    0: "Window",
    1: "Thin Glass Window",
    2: "Thick Glass Window",
    3: "Reinforced Glass Window",
    4: "Pexi Glass Window",
    5: "Stained Glass Window",
    6: "Pane Glass Window",
    7: "Cracked Glass Window",
    }

def kind():
    return
    {
    0: "Window",
    1: "Window",
    2: "Window",
    3: "Window",
    4: "Window",
    5: "Window",
    6: "Window",
    7: "Window",
    }

def description():
    return
    {
    0: "A window.",
    1: "Easy to break.",
    2: "Hard to break.",
    3: "Pretty much bullet proof.",
    4: "A cheap glass window.",
    5: "A stained glass window.",
    6: "A pane glass window.",
    7: "A cracked glass window.",
    }

def symbol():
    return
    {
    0: "=",
    1: "=",
    2: "=",
    3: "=",
    4: "=",
    5: "=",
    6: "=",
    7: "=",
    }

def color():
    return
    {
    0: ((255,255,255), (191,239,255)),
    1: ((255,255,255), (191,239,255)),
    2: ((255,255,255), (191,239,255)),
    3: ((255,255,255), (191,239,255)),
    4: ((255,255,255), (191,239,255)),
    5: ((165,255,165), (191,239,255)),
    6: ((255,255,255), (191,239,255)),
    7: ((255,255,255), (191,239,255)),
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
    7: True,
    }

def transparent():
    return
    {
    0: True,
    1: True,
    3: True,
    4: True,
    5: True,
    6: True,
    7: True,
    }

def windows():
    return
    {
    0: (category()[0], identity()[0], name()[0], kind()[0], description()[0], symbol()[0], color()[0], clip()[0], transparent()[0]),
    1: (category()[1], identity()[1], name()[1], kind()[1], description()[1], symbol()[1], color()[1], clip()[1], transparent()[1]),
    2: (category()[2], identity()[2], name()[2], kind()[2], description()[2], symbol()[2], color()[2], clip()[2], transparent()[2]),
    3: (category()[3], identity()[3], name()[3], kind()[3], description()[3], symbol()[3], color()[3], clip()[3], transparent()[3]),
    4: (category()[4], identity()[4], name()[4], kind()[4], description()[4], symbol()[4], color()[4], clip()[4], transparent()[4]),
    5: (category()[5], identity()[5], name()[5], kind()[5], description()[5], symbol()[5], color()[5], clip()[5], transparent()[5]),
    6: (category()[6], identity()[6], name()[6], kind()[6], description()[6], symbol()[6], color()[6], clip()[6], transparent()[6]),
    7: (category()[7], identity()[7], name()[7], kind()[7], description()[7], symbol()[7], color()[7], clip()[7], transparent()[7]),
    }

# Jafinoxal.
