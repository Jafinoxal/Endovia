# -*- coding: utf-8 -*-
# Endovia (InputHandler)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import Constant

def StatMenu(library):
    key = library.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == library.KEY_ENTER and key.lalt:
        library.console_set_fullscreen(not library.console_is_fullscreen())
        return Constant.SWITCH_FULLSCREENS
    # Moving selection up.
    elif key.vk == library.KEY_UP:
        return Constant.MOVE_MENU_UP
    # Moving selection down.
    elif key.vk == library.KEY_DOWN:
        return Constant.MOVE_MENU_DOWN
    # Entering the selection.
    elif key.vk == library.KEY_ENTER:
        return Constant.SELECT_MENU_ENTER
    else:
        return Constant.NULL

def InventoryMenu(library):
    key = library.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == library.KEY_ENTER and key.lalt:
        library.console_set_fullscreen(not library.console_is_fullscreen())
        return Constant.SWITCH_FULLSCREENS
    # Moving selection up.
    elif key.vk == library.KEY_UP:
        return Constant.MOVE_MENU_UP
    # Moving selection down.
    elif key.vk == library.KEY_DOWN:
        return Constant.MOVE_MENU_DOWN
    # Moving selection left.
    elif key.vk == library.KEY_LEFT:
        return Constant.MOVE_MENU_LEFT
    # Moving selection right.
    elif key.vk == library.KEY_RIGHT:
        return Constant.MOVE_MENU_RIGHT
    # Entering the selection.
    elif key.vk == library.KEY_ENTER:
        return Constant.SELECT_MENU_ENTER
    elif key.vk == library.KEY_ESCAPE:
        return Constant.EXIT_MENU
    else:
        return Constant.NULL

def MainMenu(library):
    key = library.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == library.KEY_ENTER and key.lalt:
        library.console_set_fullscreen(not library.console_is_fullscreen())
        return Constant.SWITCH_FULLSCREEN
    # Exiting the game without saving.
    elif key.vk == library.KEY_ESCAPE:
        return Constant.EXIT_GAME_WITHOUT_SAVE
    # Moving selection up.
    elif key.vk == library.KEY_UP:
        return Constant.MOVE_MENU_UP
    # Moving selection down.
    elif key.vk == library.KEY_DOWN:
        return Constant.MOVE_MENU_DOWN
    # Entering the selection.
    elif key.vk == library.KEY_ENTER:
        return Constant.SELECT_MENU_ENTER
    else:
        return Constant.NULL


def CharacterSelectionMenu(library):
    key = library.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == library.KEY_ENTER and key.lalt:
        library.console_set_fullscreen(not library.console_is_fullscreen())
        return Constant.SWITCH_FULLSCREEN
    # Exiting the game.
    elif key.vk == library.KEY_ESCAPE:
        return Constant.EXIT_GAME_WITHOUT_SAVE
    # Moving selection up.
    elif key.vk == library.KEY_UP:
        return Constant.MOVE_MENU_UP
    # Moving selection down.
    elif key.vk == library.KEY_DOWN:
        return Constant.MOVE_MENU_DOWN
    else:
        return Constant.NULL
# Jafinoxal.

def MainGame(library):
    key = library.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == library.KEY_ENTER and key.lalt:
        library.console_set_fullscreen(not library.console_is_fullscreen())
        return Constant.SWITCH_FULLSCREEN
    # Exiting the game without saving.
    elif key.vk == library.KEY_ESCAPE:
        return Constant.EXIT_GAME_WITHOUT_SAVE
    # Moving north.
    elif key.vk == library.KEY_UP:
        return Constant.MOVE_PLAYER_NORTH
    # Moving south.
    elif key.vk == library.KEY_DOWN:
        return Constant.MOVE_PLAYER_SOUTH
    # Moving west.
    elif key.vk == library.KEY_LEFT:
        return Constant.MOVE_PLAYER_WEST
    # Moving east.
    elif key.vk == library.KEY_RIGHT:
        return Constant.MOVE_PLAYER_EAST
    # Entering the selection.
    elif key.vk == library.KEY_ENTER:
        return Constant.SELECT_MENU_ENTER
    elif key.vk == library.KEY_CHAR:
            if chr(key.c) == 'i':
                return Constant.ACCESS_INVENTORY
    else:
        return Constant.NULL
