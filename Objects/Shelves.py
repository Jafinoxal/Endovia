# -*- coding: utf-8 -*-
# Endovia (Shelves)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def category():
    return {
    0: 8,
    1: 8,
    2: 8,
    3: 8,
    4: 8,
    5: 8,
    6: 8,
    }

def identity():
    return {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    }

def name():
    return {
    0: "Shelf",
    1: "Wood Shelf",
    2: "Book Shelf",
    3: "Empty Shelf",
    4: "Damaged Shelf",
    5: "Plastic Shelf",
    6: "Metal Shelf",
    }

def kind():
    return {
    0: "Shelf",
    1: "Shelf",
    2: "Shelf",
    3: "Shelf",
    4: "Shelf",
    5: "Shelf",
    6: "Shelf",
    }

def description():
    return {
    0: "A shelf.",
    1: "A wood shelf.",
    2: "A shelf of books.",
    3: "An empty shelf.",
    4: "A damaged shelf.",
    5: "A plastic shelf",
    6: "A metal shelf.",
    }

def symbol():
    return {
    0: u"®",
    1: u"®",
    2: u"®",
    3: u"®",
    4: u"®",
    4: u"®",
    6: u"®",
    }

def color():
    return {
    0: ((255,255,255), (0,0,0)),
    1: ((63,0,15), (0,0,0)),
    2: ((255,255,255), (0,0,0)),
    3: ((255,255,255), (0,0,0)),
    4: ((255,255,255), (0,0,0)),
    5: ((95,95,95), (0,0,0)),
    6: ((191,191,191), (0,0,0)),
    }

def clip():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: True,
    }

def transparent():
    return {
    0: False,
    1: False,
    2: False,
    3: False,
    4: False,
    5: False,
    6: False,
    }

def shelves():
    return {
    0: (category()[0], identity()[0], name()[0], kind()[0], description()[0], symbol()[0], color()[0], clip()[0], transparent()[0]),
    1: (category()[1], identity()[1], name()[1], kind()[1], description()[1], symbol()[1], color()[1], clip()[1], transparent()[1]),
    2: (category()[2], identity()[2], name()[2], kind()[2], description()[2], symbol()[2], color()[2], clip()[2], transparent()[2]),
    3: (category()[3], identity()[3], name()[3], kind()[3], description()[3], symbol()[3], color()[3], clip()[3], transparent()[3]),
    4: (category()[4], identity()[4], name()[4], kind()[4], description()[4], symbol()[4], color()[4], clip()[4], transparent()[4]),
    5: (category()[5], identity()[5], name()[5], kind()[5], description()[5], symbol()[5], color()[5], clip()[5], transparent()[5]),
    6: (category()[6], identity()[6], name()[6], kind()[6], description()[6], symbol()[6], color()[6], clip()[6], transparent()[6]),
    }

# Jafinoxal.
