# -*- coding: utf-8 -*-
# Endovia (InputHandler)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import Constant
for event in pygame.event.get():
    if event.type == pygame.QUIT: 
        mainloop = False # pygame window closed by user
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            mainloop = False # user pressed ESC

def MainMenu(library):
    event = library.event.get()
    # Switching fullscreen.
    # Exiting the game without saving..
    if event.type == pygame.QUIT:
        return Constant.EXIT_GAME_WITHOUT_SAVE
    # Moving up.
    elif key.vk == libtcod.KEY_UP:
        return Constant.MOVE_MOVE_MENU_UP
    # Moving down.
    elif key.vk == libtcod.KEY_DOWN:
        return Constant.MOVE_MENU_DOWN
    # Entering the selection.
    elif key.vk == libtcod.KEY_ENTER:
        return Constant.SELECT_MENU_ENTER
    else:
        return Constant.NULL


def CharacterSelectionMenu(library):
    key = libtcod.console_wait_for_keypress(True)
    key = libtcod.console_wait_for_keypress(True)
    # Switching fullscreen.
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        return Constant.SWITCH_FULLSCREEN
    # Exiting the game.
    elif key.vk == libtcod.KEY_ESCAPE:
        return Constant.EXIT_GAME_WITHOUT_SAVE
    # Moving north.
    elif key.vk == libtcod.KEY_UP:
        return Constant.MOVE_MENU_UP
    # Moving south.
    elif key.vk == libtcod.KEY_DOWN:
        return Constant.MOVE_MENU_DOWN
    else:
        return Constant.NULL
# Jafinoxal.
