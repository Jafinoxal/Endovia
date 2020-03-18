# -*- coding: utf-8 -*-
# Endovia (Looms)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 41,
    1: 41,
    2: 41,
    }

def _identity():
    return {
    0: 0,
    1: 1,
    2: 2,
    }

def _name():
    return {
    0: "Spinning Wheel",
    1: "Fabric Loom",
    2: "Clothier Loom",
    }

def _kind():
    return {
    0: "Loom",
    1: "Loom",
    2: "Loom",
    }

def _description():
    return {
    0: "Good for making thread and wool/cloth.",
    1: "Good for making fabrics out of wool/cloth.",
    2: "Good for making clothes.",
    }

def _symbol(): # +.
    return {
    0: "+",
    1: "+*",
    2: "+",
    }

def _color():
    return {
    0: ((255,255,165), (0,0,0)),
    1: ((255,255,165), (0,0,0)),
    2: ((255,255,165), (0,0,0)),
    }

def _clip():
    return {
    0: True,
    1: True,
    2: True,
    }

def _transparent():
    return {
    0: False,
    1: False,
    2: False,
    }


def looms():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
}

# Jafinoxal.
