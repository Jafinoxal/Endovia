#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Endovia (Main)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import libtcodpy
import pickle
import random

import Characters
import Charts
import Entities
import Graphics
import Handlers
import Items
import Objects

from Handlers.Constant import *
from Objects.Constant import *

def start_charts(load=False):
    if load:
        return pickle.load(open("Saves/Charts.save", "rb"))
    else:
        charts = {
        0: Charts.charts["Dungeon"].Chart(80, 50, True),
        }
        # Objects.
        charts[0].create_filled_grid(0, 80, 50, 0)
        for category in range(1, OBJECT_CATEGORIES):
            charts[0].create_empty_grid(category, 80, 50)
        # Entities.
        charts[0].create_empty_grid(2000, 80, 50)
        charts[0].grids[2000][(10, 10)] = {0:0, 1:0}
        # Dungeon.
        charts[0] = Charts.charts["MainDungeonGenerator"](charts[0], charts[0].rooms, 0)
    return charts

def start_characters(load=False):
    if load:
        return pickle.load(open("Saves/Characters.save", "rb"))
    else:
        characters = {
        0: Characters.characters["Player"].Character(0, 0, 0, 2000, 10, 10),
        }
    return characters

libtcodpy.console_set_custom_font("terminal8x8_gs_ro.png",libtcodpy.FONT_LAYOUT_ASCII_INROW, 0, 0)
libtcodpy.console_init_root(85, 55, "Endovia 1.036", False)
libtcodpy.sys_set_fps(20)

def main():
    charts = start_charts(False)
    characters = start_characters(False)
    while not libtcodpy.console_is_window_closed():
        Graphics.graphics["DrawChart"].DrawFloorsWalls(libtcodpy, Objects.objects, charts[0])
        Graphics.graphics["DrawChart"].DrawEntities(libtcodpy, Entities.entities, charts[0])
        #Graphics.graphics["DrawChart"].DrawChartBorders(charts[0])
        libtcodpy.console_flush()
        event = Handlers.handlers["InputHandler"].MainGame(libtcodpy)
        if event == EXIT_GAME_WITHOUT_SAVE:
            exit(0)
        elif event == MOVE_PLAYER_NORTH:
            Handlers.handlers["MovementHandler"].MoveCharacter(characters[0].x, characters[0].y, NORTH[0], NORTH[1], characters[0], charts[0], Objects.objects, Entities.entities)
        elif event == MOVE_PLAYER_SOUTH:
            Handlers.handlers["MovementHandler"].MoveCharacter(characters[0].x, characters[0].y, SOUTH[0], SOUTH[1], characters[0], charts[0], Objects.objects, Entities.entities)
        elif event == MOVE_PLAYER_WEST:
            Handlers.handlers["MovementHandler"].MoveCharacter(characters[0].x, characters[0].y, WEST[0], WEST[1], characters[0], charts[0], Objects.objects, Entities.entities)
        elif event == MOVE_PLAYER_EAST:
            Handlers.handlers["MovementHandler"].MoveCharacter(characters[0].x, characters[0].y, EAST[0], EAST[1], characters[0], charts[0], Objects.objects, Entities.entities)
if __name__ == '__main__':
    main()
