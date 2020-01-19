# -*- coding: utf-8 -*-
# Endovia (Rodents)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 2001,
    1: 2001,
    2: 2001,
    3: 2001,
    4: 2001,
    5: 2001,
    6: 2001,
    7: 2001,
    8: 2001,
    9: 2001,
    10: 2001,
    11: 2001,
    12: 2001,
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
    11: 11,
    12: 12,
    }

def _name():
    return {
    0: "Rodent",
    1: "Mouse",
    2: "Rat",
    3: "Hamster",
    4: "Gerbil",
    5: "Squirrel",
    6: "Beaver",
    7: "Chinchilla",
    8: "Gopher",
    9: "Lemming",
    10: "Porcupine",
    11: "Guinea Pig",
    12: "Murid",
    }

def _kind():
    return {
    0: "Rodent",
    1: "Rodent",
    2: "Rodent",
    3: "Rodent",
    4: "Rodent",
    5: "Rodent",
    6: "Rodent",
    7: "Rodent",
    8: "Rodent",
    9: "Rodent",
    10: "Rodent",
    11: "Rodent",
    12: "Rodent",
    }

def _description():
    return {
    0: "A rodent.",
    1: "Small and sketchy, maybe it wants some cheese.",
    2: "Ew, disease ridden and always unwelcome.",
    3: "Just get a new one and don't tell the kids.",
    4: "A pet for the whole family.",
    5: "Tends to prefer the woods, often found up trees.",
    6: "God damn it.",
    7: "An energetic and kind rodent.",
    8: "Likes to hide beneath the ground.",
    9: "A small rodent with a coat of differing browns and beiges, they have short life spans and live about as long as my dreams.", # Skumbag.
    10: "Large for a rodent, equipped with quills for defence, Despite it's name, it does not copulate with pine trees", # Skumbag.
    11: "A small friendly rodent. Not related to the mythical land of Guinea, nor is it an actual pig.", # Slavfox.
    12: "It's a mouse. Or a rat. You don't care, and calling it a murid makes you feel smarter.",
    }

def _symbol():
    return {
    0: "r",
    1: "r",
    2: "r",
    3: "r",
    4: "r",
    5: "r",
    6: "r",
    7: "r",
    8: "r",
    9: "r",
    10: "r",
    11: "r",
    12: "r",
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
    7: ((127,0,255), (0,0,0)),
    8: ((191,0,255), (0,0,0)),
    9: ((255,0,255), (0,0,0)),
    10: ((255,0,191), (0,0,0)),
    11: ((255,0,63), (0,0,0)),
    12: ((0,255,255), (0,0,0)),
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
    11: True,
    12: True,
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
    11: True,
    12: True,
    }

def _aggressive():
    return {
    0: False,
    1: False,
    2: True,
    3: False,
    4: False,
    5: False,
    6: True,
    7: False,
    8: False,
    9: False,
    10: True,
    11: False,
    12: False,
    }

def _health():
    return {
    0: 3,
    1: 1,
    2: 3,
    3: 4,
    4: 4,
    5: 5,
    6: 6,
    7: 4,
    8: 3,
    9: 3,
    10: 8,
    11: 3,
    12: 4,
    }

def _attack():
    return {
    0: ("scratch", "bite"),
    1: ("scratch", "bite"),
    2: ("scratch", "bite"),
    3: ("scratch", "bite"),
    4: ("scratch", "bite"),
    5: ("scratch", "bite"),
    6: ("scratch", "bite"),
    7: ("scratch", "bite"),
    8: ("scratch", "bite"),
    9: ("scratch", "bite"),
    10: ("scratch", "bite"),
    11: ("scratch", "bite"),
    12: ("scratch", "bite"),
    }

def rodents():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0], _aggressive()[0], _health()[0], _attack()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1], _aggressive()[1], _health()[1], _attack()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2], _aggressive()[2], _health()[2], _attack()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3], _aggressive()[3], _health()[3], _attack()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4], _aggressive()[4], _health()[4], _attack()[4]),
    5: (_category()[5], _identity()[5], _name()[5], _kind()[5], _description()[5], _symbol()[5], _color()[5], _clip()[5], _transparent()[5], _aggressive()[5], _health()[5], _attack()[5]),
    6: (_category()[6], _identity()[6], _name()[6], _kind()[6], _description()[6], _symbol()[6], _color()[6], _clip()[6], _transparent()[6], _aggressive()[6], _health()[6], _attack()[6]),
    7: (_category()[7], _identity()[7], _name()[7], _kind()[7], _description()[7], _symbol()[7], _color()[7], _clip()[7], _transparent()[7], _aggressive()[7], _health()[7], _attack()[7]),
    8: (_category()[8], _identity()[8], _name()[8], _kind()[8], _description()[8], _symbol()[8], _color()[8], _clip()[8], _transparent()[8], _aggressive()[8], _health()[8], _attack()[8]),
    9: (_category()[9], _identity()[9], _name()[9], _kind()[9], _description()[9], _symbol()[9], _color()[9], _clip()[9], _transparent()[9], _aggressive()[9], _health()[9], _attack()[9]),
    10: (_category()[10], _identity()[10], _name()[10], _kind()[10], _description()[10], _symbol()[10], _color()[10], _clip()[10], _transparent()[10], _aggressive()[10], _health()[10], _attack()[10]),
    11: (_category()[11], _identity()[11], _name()[11], _kind()[11], _description()[11], _symbol()[11], _color()[11], _clip()[11], _transparent()[11], _aggressive()[11], _health()[11], _attack()[11]),
    12: (_category()[12], _identity()[12], _name()[12], _kind()[12], _description()[12], _symbol()[12], _color()[12], _clip()[12], _transparent()[12], _aggressive()[12], _health()[12], _attack()[12]),
    }

# Jafinoxal.
