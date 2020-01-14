# -*- coding: utf-8 -*-
# Endovia (Pillars)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def category():
    return {
    0: 14,
    1: 14,
    2: 14,
    3: 14,
    4: 14,
    5: 14,
    6: 14,
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
    0: "Pillar",
    1: "Wood Pillar",
    2: "Stone Pillar",
    3: "Metal Pillar",
    4: "Cement Pillar",
    5: "Concrete Pillar",
    6: "Sand Stone Pillar",
    }

def kind():
    return {
    0: "Pillar",
    1: "Pillar",
    2: "Pillar",
    3: "Pillar",
    4: "Pillar",
    5: "Pillar",
    6: "Pillar",
    }

def description():
    return {
    0: "A pillar.",
    1: "A basic wood pillar.",
    2: "A rock hard stone pillar.",
    3: "A strong metal pillar.",
    4: "A solid cement pillar.",
    5: "A truly tough concrete pillar.",
    6: "A somewhat strong pillar."
    }

def symbol():
    return {
    0: u"¦",
    1: u"¦",
    2: u"¦",
    3: u"¦",
    4: u"¦",
    5: u"¦",
    6: u"¦",
    }

def color():
    return {
    0: ((255,255,255), (0,0,0)),
    1: ((63,0,15), (0,0,0)),
    2: ((159,159,159), (0,0,0)),
    3: ((127,127,127), (0,0,0)),
    4: ((191,191,191), (0,0,0)),
    5: ((223,223,223), (0,0,0)),
    6: ((255,255,191), (0,0,0)),
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
    1: False,
    2: False,
    3: False,
    4: False,
    5: False,
    6: False,
    }

def pillars():
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
