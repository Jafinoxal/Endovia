# -*- coding: utf-8 -*-
# Endovia (Desks)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 16,
    1: 16,
    2: 16,
    3: 16,
    4: 16,
    5: 16,
    6: 16,
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
    0: "Desk",
    1: "Small School Desk",
    2: "Large School Desk",
    3: "Computer Desk",
    4: "Office Desk",
    5: "Work Desk",
    6: "Writing Desk",
    }

def _kind():
    return {
    0: "Desk",
    1: "Desk",
    2: "Desk",
    3: "Desk",
    4: "Desk",
    5: "Desk",
    6: "Desk",
    }

def _description():
    return {
    0: "A desk.",
    1: "A desk made for small people or kids.",
    2: "A desk made for adult people or teens.",
    3: "A desk with a computer, and other tech.",
    4: "A desk meant for office work.",
    5: "A desk made for studying, homework, and paperwork.",
    6: "A desk for writing, includes a typewriter."
    }

def _symbol(): # 28.
    return {
    0: "\x1c",
    1: "\x1c",
    2: "\x1c",
    3: "\x1c",
    4: "\x1c",
    5: "\x1c",
    6: "\x1c",
    }

def _color():
    return {
    0: ((255,255,255), (0,0,0)),
    1: ((31,31,31), (0,0,0)),
    2: ((63,63,63), (0,0,0)),
    3: ((95,95,95), (0,0,0)),
    4: ((127,127,127), (0,0,0)),
    5: ((191,191,191), (0,0,0)),
    6: ((223,223,223), (0,0,0)),
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
    1: True,
    2: True,
    3: False,
    4: False,
    5: False,
    6: False,
    }

def beds():
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
