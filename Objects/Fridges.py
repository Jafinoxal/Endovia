# -*- coding: utf-8 -*-
# Endovia (Fridges)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 6,
    1: 6,
    2: 6,
    3: 6,
    4: 6,
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
    0: "Fridge",
    1: "Rusty Fridge",
    2: "Small Fridge",
    3: "Large Fridge",
    4: "Mini Fridge",
    }

def _kind():
    return {
    0: "Fridge",
    1: "Fridge",
    2: "Fridge",
    3: "Fridge",
    4: "Fridge",
    }

def _description():
    return {
    0: "A fridge.",
    1: "A rusty fridge.",
    2: "A small fridge.",
    3: "A large fridge.",
    4: "Perfect for beer and snacks.",
    }

def _symbol(): # 241.
    return {
    0: "\xf1",
    1: "\xf1",
    2: "\xf1",
    3: "\xf1",
    4: "\xf1",
    }

def _color():
    return {
    0: ((255,255,255), (0,0,0)),
    1: ((63,63,63), (0,0,0)),
    2: ((255,255,255), (0,0,0)),
    3: ((255,255,255), (0,0,0)),
    4: ((255,255,255), (0,0,0)),
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
    4: False,
    }

def fridges():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    }

# Jafinoxal.
