# -*- coding: utf-8 -*-
# Endovia (Players)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 2000,
    1: 2000,
    2: 2000,
    3: 2000,
    4: 2000,
    5: 2000,
    6: 2000,
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
    0: "Human",
    1: "Half Elf",
    2: "Snow Elf",
    3: "Wood Elf",
    4: "Deep Elf",
    5: "High Elf",
    6: "Dark Elf",
    }

def _kind():
    return {
    0: "Player",
    1: "Player",
    2: "Player",
    3: "Player",
    4: "Player",
    5: "Player",
    6: "Player",
    }

def _description():
    return {
    0: "A human, hails from various lands, good at most things.",
    1: "A human elf hybrid, harder to produce, affinity for magic.",
    2: "A snow elf, from the north, secretive and can take the cold.",
    3: "A wood elf, from the forests, uses nature as a weapon and tool.",
    4: "A deep elf, from the mountains and caves, stealthy and cunning.",
    5: "A high elf, from the plains, great affinity for magic and dominant.",
    6: "A dark elf, from the volcanic ash lands, pride and high cultured.",
    }

def _symbol():
    return {
    0: "☺",
    1: "☺",
    2: "☺",
    3: "☺",
    4: "☺",
    5: "☺",
    6: "☺",
    }

def _color():
    return {
    0: ((255,0,0), (0,0,0)),
    1: ((255,127,0), (0,0,0)),
    2: ((255,255,0), (0,0,0)),
    3: ((191,255,0), (0,0,0)),
    4: ((0,255,0), (0,0,0)),
    5: ((0,255,191), (0,0,0)),
    6: ((0,0,255), (0,0,0)),
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
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: True,
    }

def players():
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
