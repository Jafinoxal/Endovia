# -*- coding: utf-8 -*-
# Endovia (Beds)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def category():
    return
    {
    0: 15,
    1: 15,
    2: 15,
    3: 15,
    4: 15,
    5: 15,
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
    }

def name():
    return
    {
    0: "Bed",
    1: "Sleeping Bag Bed",
    2: "Mattress Bed",
    3: "Coffin Bed",
    4: "Luxury Bed",
    5: "Feather Bed",
    }

def kind():
    return
    {
    0: "Pillar",
    1: "Pillar",
    2: "Pillar",
    3: "Pillar",
    4: "Pillar",
    5: "Pillar",
    6: "Pillar",
    }

def description():
    return
    {
    0: "A bed.",
    1: "A hard bed roll and pillow.",
    2: "A regular bed.",
    3: "A bed fit for vampires.",
    4: "The best bed money can buy.",
    5: "A soft bed roll and pillow filled with feathers.",
    }

def symbol():
    return
    {
    0: u"¥",
    1: u"¥",
    2: u"¥",
    3: u"¥",
    4: u"¥",
    5: u"¥",
    }

def color():
    return
    {
    0: ((255,255,255), (0,0,0)),
    1: ((63,62,15), (0,0,0)),
    2: ((159,244,159), (0,0,0)),
    3: ((127,127,127), (0,0,0)),
    4: ((191,191,191), (0,0,0)),
    5: ((223,223,223), (0,0,0)),
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
    }

def transparent():
    return
    {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    }

def beds():
    return
    {
    0: (category()[0], identity()[0], name()[0], kind()[0], description()[0], symbol()[0], color()[0], clip()[0], transparent()[0]),
    1: (category()[1], identity()[1], name()[1], kind()[1], description()[1], symbol()[1], color()[1], clip()[1], transparent()[1]),
    2: (category()[2], identity()[2], name()[2], kind()[2], description()[2], symbol()[2], color()[2], clip()[2], transparent()[2]),
    3: (category()[3], identity()[3], name()[3], kind()[3], description()[3], symbol()[3], color()[3], clip()[3], transparent()[3]),
    4: (category()[4], identity()[4], name()[4], kind()[4], description()[4], symbol()[4], color()[4], clip()[4], transparent()[4]),
    5: (category()[5], identity()[5], name()[5], kind()[5], description()[5], symbol()[5], color()[5], clip()[5], transparent()[5]),

# Jafinoxal.
