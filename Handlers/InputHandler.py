# -*- coding: utf-8 -*-
# Endovia (InputHandler)
# Copyright (C) 2010-2022 Jeremy Aaron Flexer.

import tcod

from . import Constant

def StatMenu():
    #key = library.console_wait_for_keypress(True)
    key = tcod.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == tcod.KEY_ENTER and key.lalt:
        tcod.console_set_fullscreen(not library.console_is_fullscreen())
        return Constant.SWITCH_FULLSCREENS
    # Moving selection up.
    elif key.vk == tcod.KEY_UP:
        return Constant.MOVE_MENU_UP
    # Moving selection down.
    elif key.vk == tcod.KEY_DOWN:
        return Constant.MOVE_MENU_DOWN
    # Entering the selection.
    elif key.vk == tcod.KEY_ENTER:
        return Constant.SELECT_MENU_ENTER
    else:
        return Constant.NULL

def CombatMenu():
    key = tcod.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == tcod.KEY_ENTER and key.lalt:
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
        return Constant.SWITCH_FULLSCREENS
    # Moving selection up.
    elif key.vk == tcod.KEY_UP:
        return Constant.MOVE_MENU_UP
    # Moving selection down.
    elif key.vk == tcod.KEY_DOWN:
        return Constant.MOVE_MENU_DOWN
    # Entering the selection.
    elif key.vk == tcod.KEY_ENTER:
        return Constant.SELECT_MENU_ENTER
    else:
        return Constant.NULL

def InventoryMenu():
    key = tcod.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == tcod.KEY_ENTER and key.lalt:
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
        return Constant.SWITCH_FULLSCREENS
    # Moving selection up.
    elif key.vk == tcod.KEY_UP:
        return Constant.MOVE_MENU_UP
    # Moving selection down.
    elif key.vk == tcod.KEY_DOWN:
        return Constant.MOVE_MENU_DOWN
    # Moving selection left.
    elif key.vk == tcod.KEY_LEFT:
        return Constant.MOVE_MENU_LEFT
    # Moving selection right.
    elif key.vk == tcod.KEY_RIGHT:
        return Constant.MOVE_MENU_RIGHT
    # Entering the selection.
    elif key.vk == tcod.KEY_ENTER:
        return Constant.SELECT_MENU_ENTER
    elif key.vk == tcod.KEY_ESCAPE:
        return Constant.EXIT_MENU
    else:
        return Constant.NULL

def MagicMenu():
    key = tcod.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == tcod.KEY_ENTER and key.lalt:
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
        return Constant.SWITCH_FULLSCREENS
    # Moving selection up.
    elif key.vk == tcod.KEY_UP:
        return Constant.MOVE_MENU_UP
    # Moving selection down.
    elif key.vk == tcod.KEY_DOWN:
        return Constant.MOVE_MENU_DOWN
    # Moving selection left.
    elif key.vk == tcod.KEY_LEFT:
        return Constant.MOVE_MENU_LEFT
    # Moving selection right.
    elif key.vk == tcod.KEY_RIGHT:
        return Constant.MOVE_MENU_RIGHT
    # Entering the selection.
    elif key.vk == tcod.KEY_ENTER:
        return Constant.SELECT_MENU_ENTER
    elif key.vk == tcod.KEY_ESCAPE:
        return Constant.EXIT_MENU
    else:
        return Constant.NULL

def MainMenu():
    key = tcod.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == tcod.KEY_ENTER and key.lalt:
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
        return Constant.SWITCH_FULLSCREEN
    # Exiting the game without saving.
    elif key.vk == tcod.KEY_ESCAPE:
        return Constant.EXIT_GAME_WITHOUT_SAVE
    # Moving selection up.
    elif key.vk == tcod.KEY_UP:
        return Constant.MOVE_MENU_UP
    # Moving selection down.
    elif key.vk == tcod.KEY_DOWN:
        return Constant.MOVE_MENU_DOWN
    # Entering the selection.
    elif key.vk == tcod.KEY_ENTER:
        return Constant.SELECT_MENU_ENTER
    else:
        return Constant.NULL


def CharacterSelectionMenu(library):
    key = library.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == library.KEY_ENTER and key.lalt:
        library.console_set_fullscreen(not library.console_is_fullscreen())
        return Constant.SWITCH_FULLSCREEN
    # Moving selection up.
    elif key.vk == library.KEY_UP:
        return Constant.MOVE_MENU_UP
    # Moving selection down.
    elif key.vk == library.KEY_DOWN:
        return Constant.MOVE_MENU_DOWN
    else:
        return Constant.NULL

def MainGame():
    key = tcod.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == tcod.KEY_ENTER and key.lalt:
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
        return Constant.SWITCH_FULLSCREEN
    # Exiting the game without saving.
    #elif key.vk == library.KEY_ESCAPE:
    #    return Constant.EXIT_GAME_WITHOUT_SAVE
    if key.vk == tcod.KEY_ESCAPE:
        return Constant.EXIT_GAME_WITHOUT_SAVE
    # Moving north.
    elif key.vk == tcod.KEY_UP:
        return Constant.MOVE_PLAYER_NORTH
    # Moving south.
    elif key.vk == tcod.KEY_DOWN:
        return Constant.MOVE_PLAYER_SOUTH
    # Moving west.
    elif key.vk == tcod.KEY_LEFT:
        return Constant.MOVE_PLAYER_WEST
    # Moving east.
    elif key.vk == tcod.KEY_RIGHT:
        return Constant.MOVE_PLAYER_EAST
    # Entering the selection.
    elif key.vk == tcod.KEY_ENTER:
        return Constant.SELECT_MENU_ENTER
    elif key.vk == tcod.KEY_CHAR:
        if chr(key.c) == 'x':
            return Constant.ACCESS_COMBAT
        elif chr(key.c) == 'b':
            return Constant.BREAK_WALL
        elif chr(key.c) == 'n':
            return Constant.MINE_VEIN
        elif chr(key.c) == 'c':
            return Constant.CHOP_TREE
        elif chr(key.c) == 'i':
            return Constant.ACCESS_INVENTORY
        elif chr(key.c) == 'm':
            return Constant.ACCESS_MAGIC
        else:
            return Constant.NULL
    else:
        return Constant.NULL

def SkillDirection():
    key = tcod.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == tcod.KEY_ENTER and key.lalt:
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())
        return Constant.SWITCH_FULLSCREEN
    elif key.vk == tcod.KEY_UP:
        return Constant.MOVE_MENU_UP
    elif key.vk == tcod.KEY_DOWN:
        return Constant.MOVE_MENU_DOWN
    elif key.vk == tcod.KEY_LEFT:
        return Constant.MOVE_MENU_LEFT
    elif key.vk == tcod.KEY_RIGHT:
        return Constant.MOVE_MENU_RIGHT
    else:
        return Constant.NULL

# Jafinoxal.
