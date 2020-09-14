# -*- coding: utf-8 -*-
# Endovia (Handler Init)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

NULL = -1

EXIT_GAME_WITHOUT_SAVE = 0
EXIT_GAME_WITH_SAVE = 1
SWITCH_FULLSCREEN = 2

MOVE_MENU_UP = 3
MOVE_MENU_DOWN = 4
MOVE_MENU_LEFT = 5
MOVE_MENU_RIGHT = 6
SELECT_MENU_ENTER = 7

MOVE_PLAYER_NORTH = 8
MOVE_PLAYER_SOUTH = 9
MOVE_PLAYER_WEST = 10
MOVE_PLAYER_EAST = 11

MOVE_PLAYER_NORTHWEST = 12
MOVE_PLAYER_NORTHEAST = 13
MOVE_PLAYER_SOUTHWEST = 14
MOVE_PLAYER_SOUTHEAST = 15

EXIT_MENU = 16

ACCESS_INVENTORY = 17
INVENTORY_EQUIP_QUIVER = 18
INVENTORY_EQUIP_HEAD = 19
INVENTORY_EQUIP_SHOULDERS = 20
INVENTORY_EQUIP_HANDS = 21
INVENTORY_EQUIP_FEET = 22
INVENTORY_EQUIP_BODY = 23
INVENTORY_EQUIP_LEGS = 24
INVENTORY_EQUIP_LEFT_HAND = 25
INVENTORY_EQUIP_RIGHT_HAND = 26
INVENTORY_EQUIP_BACK = 27
INVENTORY_EQUIP_NECK = 28
INVENTORY_EQUIP_FINGER = 29

ACCESS_SPELLS = 30
SPELLS_SET_ACTIVE = 31

NORTH = (0, -1)
SOUTH = (0, +1)
WEST = (-1, 0)
EAST = (+1, 0)

# Spell indexes.
SPELLS_NAME = 0
SPELLS_LEVEL = 1
SPELLS_DAMAGE = 2
SPELLS_DAMAGE_TYPE = 3
SPELLS_EFFECT_TYPE = 4
SPELLS_MANA_NEEDED = 5

DESTRUCTION_SPELLS = { # Identitiy, name, level, damage, damage_type, effect_type, mana_needed.
None: (None, None, None, None, None, None),
0: ("air smack", 0, 4, "air", None, 5),
1: ("air blast", 10, 8, "air", None, 10),
2: ("air bolt", 20, 22, "air", None, 25),
3: ("air surge", 40, 70, "air", None, 60),
4: ("air rocket", 75, 230, "air", None, 150),
5: ("water smack", 2, 5, "water", None, 5),
6: ("water blast", 12, 10, "water", None, 10),
7: ("water bolt", 24, 25, "water", None, 25),
8: ("water surge", 44, 77, "water", None, 60),
9: ("water rocket", 80, 246, "water", None, 150),
10: ("earth smack", 4, 6, "earth", None, 5),
11: ("earth blast", 14, 12, "earth", None, 10),
12: ("earth bolt", 28, 28, "earth", None, 25),
13: ("earth surge", 48, 84, "earth", None, 60),
14: ("earth rocket", 85, 262, "earth", None, 150),
15: ("fire smack", 6, 7, "fire", None, 5),
16: ("fire blast", 16, 14, "fire", None, 10),
17: ("fire bolt", 32, 31, "fire", None, 25),
18: ("fire surge", 52, 91, "fire", None, 60),
19: ("fire rocket", 90, 278, "fire", None, 150),
20: ("shock smack", 8, 8, "shock", None, 5),
21: ("shock blast", 10, 9, "shock", None, 10),
22: ("shock bolt", 36, 34, "shock", None, 25),
23: ("shock surge", 56, 98, "shock", None, 60),
24: ("shock rocket", 95, 294, "shock", None, 150),
}

ATTACKS = { # Name, plural, damages.
"scratch": ("scratches", 1, 2),
"bite": ("bites", 1, 3),
"quill": ("quills", 2, 5),
"whack": ("whacks", 2, 4),
}

DROPS = { # Name, category, id, amounts.
"pettymoney": (1037, 1, (3, 7, 20, 32)),
"lessermoney": (1037, 1, (45, 71, 103)),
"okaymoney": (1037, 1, (178, 199, 223, 263)),
"goodmoney": (1037, 1, (271, 295, 312, 320, 340, 400)),
"greatmoney": (1037, 1, (420, 478, 512, 600, 712)),
"awesomemoney": (1037, 1, (850, 942, 1023, 1210)),
"powermoney": (1037, 1, (1500, 1673, 1782, 2000)),
}

# Jafinoxal.
