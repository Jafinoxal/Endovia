# -*- coding: utf-8 -*-
# Endovia (Anvils)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 25,
    1: 25,
    2: 25,
    3: 25,
    }

def _identity():
    return {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    }

def _name():
    return {
    0: "Anvil",
    1: "Lead Anvil",
    2: "Artisan Anvil",
    3: "Master Anvil",
    }

def _kind():
    return {
    0: "Anvil",
    1: "Anvil",
    2: "Anvil",
    3: "Anvil",
    }

def _description():
    return {
    0: "An anvil.",
    1: "An anvil good for working all types of metal.",
    2: "An anvil requiring somewhat less effort.",
    3: "An anvil that requires less effort.",
    }

def _symbol(): # 215.
    return {
    0: "@",
    1: "@",
    2: "@",
    3: "@",
    }

def _color():
    return {
    0: ((63,63,63), (0,0,0)),
    1: ((63,63,63), (0,0,0)),
    2: ((63,63,63), (0,0,0)),
    3: ((191,0,47), (0,0,0)),
    }

def _clip():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    }

def _transparent():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    }

def anvils():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    }

# Jafinoxal.
