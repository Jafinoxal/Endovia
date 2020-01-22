# -*- coding: utf-8 -*-
# Endovia (Chests)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 7,
    1: 7,
    2: 7,
    3: 7,
    4: 7,
    5: 7,
    6: 7,
    7: 7,
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
    0: "Chest",
    1: "Wood Chest",
    2: "Small Chest",
    3: "Large Chest",
    4: "Armour Chest",
    5: "Weapon Chest",
    6: "Plastic Chest",
    7: "Metal Chest",
    }

def _kind():
    return {
    0: "Chest",
    1: "Chest",
    2: "Chest",
    3: "Chest",
    4: "Chest",
    5: "Chest",
    6: "Chest",
    7: "Chest",
    }

def _description():
    return {
    0: "A chest.",
    1: "A wood chest.",
    2: "A small chest.",
    3: "A large chest.",
    4: "A chest of armour.",
    5: "A chest of weapons.",
    6: "A plastic chest.",
    7: "A metal chest.",
    }

def _symbol(): # 184.
    return {
    0: "\xb8",
    1: "\xb8",
    2: "\xb8",
    3: "\xb8",
    4: "\xb8",
    5: "\xb8",
    6: "\xb8",
    7: "\xb8",
    }

def _color():
    return {
    0: ((255,255,255), (0,0,0)),
    1: ((63,0,15), (0,0,0)),
    2: ((255,255,255), (0,0,0)),
    3: ((255,255,255), (0,0,0)),
    4: ((255,255,255), (0,0,0)),
    5: ((255,255,255), (0,0,0)),
    6: ((95,95,95), (0,0,0)),
    7: ((191,191,191), (0,0,0)),
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

def chests():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    5: (_category()[5], _identity()[5], _name()[5], _kind()[5], _description()[5], _symbol()[5], _color()[5], _clip()[5], _transparent()[5]),
    6: (_category()[6], _identity()[6], _name()[6], _kind()[6], _description()[6], _symbol()[6], _color()[6], _clip()[6], _transparent()[6]),
    7: (_category()[7], _identity()[7], _name()[7], _kind()[7], _description()[7], _symbol()[7], _color()[7], _clip()[7], _transparent()[7]),
    }

# Jafinoxal.
