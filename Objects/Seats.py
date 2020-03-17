# -*- coding: utf-8 -*-
# Endovia (Seats)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 36,
    1: 36,
    2: 36,
    3: 36,
    4: 36,
    5: 36,
    6: 36,
    7: 36,
    8: 36,
    9: 36,
    10: 36,
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
    8: 8,
    9: 9,
    10: 10,
    }

def _name():
    return {
    0: "Wooden Chair",
    1: "Metal Chair",
    2: "Leather Chair",
    3: "Wooden Stool",
    4: "Metal Stool",
    5: "Wooden Bench",
    6: "Metal Bench",
    7: "Stone Bench",
    8: "Basic Couch",
    9: "Leather Couch",
    10: "Bean Bag Spread"
    }

def _kind():
    return {
    0: "Seat",
    1: "Seat",
    2: "Seat",
    3: "Seat",
    4: "Seat",
    5: "Seat",
    6: "Seat",
    7: "Seat",
    8: "Seat",
    9: "Seat",
    10: "Seat",
    }

def _description():
    return {
    0: "Somewhere normal to sit.",
    1: "Somewhere normal to sit.",
    2: "Somewhere comfy to sit.",
    3: "Somewhere normal to sit.",
    4: "Somewhere normal to sit.",
    5: "Somewhere normal to sit.",
    6: "Somewhere normal to sit.",
    7: "Somewhere normal to sit.",
    8: "Somewhere comfy to sit.",
    9: "Somewhere comfy to sit.",
    10: "Somewhere comfy to sit.",
    }

def _symbol(): # 15.
    return {
    0: "\x0f",
    1: "\x0f",
    2: "\x0f",
    3: "\x0f",
    4: "\x0f",
    5: "\x0f",
    6: "\x0f",
    7: "\x0f",
    8: "\x0f",
    9: "\x0f",
    10: "\x0f",
    }

def _color():
    return {
    0: ((255,165,165), (0,0,0)),
    1: ((255,165,165), (0,0,0)),
    2: ((255,165,165), (0,0,0)),
    3: ((255,165,165), (0,0,0)),
    4: ((255,165,165), (0,0,0)),
    5: ((255,165,165), (0,0,0)),
    6: ((255,165,165), (0,0,0)),
    7: ((255,165,165), (0,0,0)),
    8: ((255,165,165), (0,0,0)),
    9: ((255,165,165), (0,0,0)),
    10: ((255,165,165), (0,0,0)),
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
    8: True,
    9: True,
    10: True,
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
    8: True,
    9: True,
    10: True,
    }


def seats():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    5: (_category()[5], _identity()[5], _name()[5], _kind()[5], _description()[5], _symbol()[5], _color()[5], _clip()[5], _transparent()[5]),
    6: (_category()[6], _identity()[6], _name()[6], _kind()[6], _description()[6], _symbol()[6], _color()[6], _clip()[6], _transparent()[6]),
    7: (_category()[7], _identity()[7], _name()[7], _kind()[7], _description()[7], _symbol()[7], _color()[7], _clip()[7], _transparent()[7]),
    8: (_category()[8], _identity()[8], _name()[8], _kind()[8], _description()[8], _symbol()[8], _color()[8], _clip()[8], _transparent()[8]),
    9: (_category()[9], _identity()[9], _name()[9], _kind()[9], _description()[9], _symbol()[9], _color()[9], _clip()[9], _transparent()[9]),
    10: (_category()[10], _identity()[10], _name()[10], _kind()[10], _description()[10], _symbol()[10], _color()[10], _clip()[10], _transparent()[10]),
}

# Jafinoxal.
