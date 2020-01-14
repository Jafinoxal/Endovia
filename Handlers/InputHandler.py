# -*- coding: utf-8 -*-
# Endovia (InputHandler)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import Constant

def MainMenu(library):
    key = library.console_wait_for_keypress(True)
    key = library.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == library.KEY_ENTER and key.lalt:
        libtcod.console_set_fullscreen(not library.console_is_fullscreen())
        return Constant.SWITCH_FULLSCREEN
    # Exiting the game without saving.
    elif key.vk == library.KEY_ESCAPE:
        return Constant.EXIT_GAME_WITHOUT_SAVE
    # Moving selection up.
    elif key.vk == library.KEY_UP:
        return Constant.MOVE_MOVE_MENU_UP
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
    key = library.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == library.KEY_ENTER and key.lalt:
        libtcod.console_set_fullscreen(not library.console_is_fullscreen())
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
    key = library.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == library.KEY_ENTER and key.lalt:
        libtcod.console_set_fullscreen(not library.console_is_fullscreen())
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
    else:
        return Constant.NULL
