# -*- coding: utf-8 -*-
# Endovia (Handler Init)
# Copyright (C) 2010-2021 Jeremy Aaron Flexer.

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

ACCESS_MAGIC = 30
MAGIC_SET_ACTIVE = 31

ACCESS_COMBAT = 32

ACCESS_QUICK_INVENTORY = 33

BREAK_WALL = 34
MINE_VEIN = 35

ATTACK_MELEE = 0
ATTACK_RANGED = 1
ATTACK_MAGIC = 2
ATTACK_JUTSU = 3
ATTACK_ARMS = 4

COMBAT_STYLES = {0:"Melee",
1:"Ranged",
2:"Magic",
3:"Jutsu",
4:"Arms",
}

NORTH = (0, -1)
SOUTH = (0, +1)
WEST = (-1, 0)
EAST = (+1, 0)

# Spell indexes.
SPELLS_NAME = 0
SPELLS_LEVEL = 1
SPELLS_DAMAGE = 2
SPELLS_EFFECT_AMOUNT = 2
SPELLS_DAMAGE_TYPE = 3
SPELLS_EFFECT_TYPE = 3
SPELLS_EFFECT_TYPE = 4
SPELLS_DES_MANA_NEEDED = 5
SPELLS_RES_MANA_NEEDED = 4

DESTRUCTION_SPELLS = { # Identitiy, name, level, damage, damage_type, effect_type, mana_needed.
0: ("Air Smack", 0, 4, "air", None, 5),
1: ("Air Blast", 10, 8, "air", None, 10),
2: ("Air Bolt", 20, 22, "air", None, 25),
3: ("Air Surge", 40, 70, "air", None, 60),
4: ("Air Rocket", 75, 230, "air", None, 150),
5: ("Water Smack", 2, 5, "water", None, 5),
6: ("Water Blast", 12, 10, "water", None, 10),
7: ("Water Bolt", 24, 25, "water", None, 25),
8: ("Water Surge", 44, 77, "water", None, 60),
9: ("Water Rocket", 80, 246, "water", None, 150),
10: ("Earth Smack", 4, 6, "earth", None, 5),
11: ("Earth Blast", 14, 12, "earth", None, 10),
12: ("Earth Bolt", 28, 28, "earth", None, 25),
13: ("Earth Surge", 48, 84, "earth", None, 60),
14: ("Earth Rocket", 85, 262, "earth", None, 150),
15: ("Fire Smack", 6, 7, "fire", None, 5),
16: ("Fire Blast", 16, 14, "fire", None, 10),
17: ("Fire Bolt", 32, 31, "fire", None, 25),
18: ("Fire Surge", 52, 91, "fire", None, 60),
19: ("Fire Rocket", 90, 278, "fire", None, 150),
20: ("Shock Smack", 8, 8, "shock", None, 5),
21: ("Shock Blast", 10, 9, "shock", None, 10),
22: ("Shock Bolt", 36, 34, "shock", None, 25),
23: ("Shock Surge", 56, 98, "shock", None, 60),
24: ("Shock Rocket", 95, 294, "shock", None, 150),
}

RESTORATION_SPELLS = { # Identitiy, name, level, effect_amount, effect_type, mana_needed.
0: ("Crude Heal", 0, 40, "heal", 20),
1: ("Fair Heal", 7, 100, "heal", 50),
2: ("Strong Heal", 17, 300, "heal", 150),
3: ("Mighty Heal", 29, 680, "heal", 340),
4: ("Vigor Heal", 48, 1600, "heal", 800),
5: ("Massive Heal", 75, 3500, "heal", 1750),
6: ("Godly Heal", 100, 10000, "heal", 5000),
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
