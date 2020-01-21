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

NORTH = (0, -1)
SOUTH = (0, +1)
WEST = (-1, 0)
EAST = (+1, 0)

ATTACKS = { # Name, plural, damages, specials.
"scratch": ("scratches", 1, 2),
"bite": ("bites", 1, 3),
}

# Jafinoxal.
