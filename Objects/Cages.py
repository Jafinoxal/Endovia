# -*- coding: utf-8 -*-
# Endovia (Cages)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 23,
    1: 23,
    2: 23,
    3: 23,
    4: 23,
    }

def _identity():
    return {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    }

def _name():
    return {
    0: "Cage",
    1: "Empty Cage",
    2: "Jail Cage",
    3: "Skeleton Cage",
    4: "Dog Cage",
    }

def _kind():
    return {
    0: "Cage",
    1: "Cage",
    2: "Cage",
    3: "Cage",
    4: "Cage",
    }

def _description():
    return {
    0: "A cage.",
    1: "An uninhabited cage.",
    2: "A cage for holding a prisoner.",
    3: "A cage, it's inhabitent has long since died.",
    4: "A cage for holding dogs."
    }

def _symbol(): # 215.
    return {
    0: "#",
    1: "#",
    2: "#",
    3: "#",
    4: "#",
    }

def _color():
    return {
    0: ((159,159,159), (0,0,0)),
    1: ((159,159,159), (0,0,0)),
    2: ((159,159,159), (0,0,0)),
    3: ((159,159,159), (0,0,0)),
    4: ((159,159,159), (0,0,0)),
    }

def _clip():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    }

def _transparent():
    return {
    0: False,
    1: False,
    2: False,
    3: False,
    4: False
    }

def cages():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    }

# Jafinoxal.
