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

def start_charts(load=False):
    if load:
        return pickle.load(open("Saves/Charts.save", "rb"))
    else:
        charts = {
        0: Charts.charts["Dungeon"].Chart(80, 50, True),
        }
        charts[0].create_filled_grid(0, 80, 50, 0)
        charts[0].create_empty_grid(1, 80, 50)
        charts[0].create_empty_grid(2, 80, 50)
        charts[0].create_empty_grid(3, 80, 50)
        charts[0].create_empty_grid(4, 80, 50)
        charts[0].create_empty_grid(5, 80, 50)
        charts[0].create_empty_grid(6, 80, 50)
        charts[0].create_empty_grid(7, 80, 50)
        charts[0].create_empty_grid(8, 80, 50)
        charts[0].create_empty_grid(9, 80, 50)
        charts[0].create_empty_grid(10, 80, 50)
        charts[0].create_empty_grid(11, 80, 50)
        charts[0].create_empty_grid(12, 80, 50)
        charts[0].create_empty_grid(13, 80, 50)
        charts[0].create_empty_grid(14, 80, 50)
        charts[0].create_empty_grid(15, 80, 50)
        charts[0].create_empty_grid(2000, 80, 50)
        charts[0].grids[2000][(10, 10)] = {0:0, 1:0}
        import random
        for i in range(0, 200):
            x = random.randint(1, charts[0].chart_width - 11)
            x2 = random.randint(5, 10)
            y = random.randint(1, charts[0].chart_height - 11)
            y2 = random.randint(5, 10)
            charts[0].carve_rectangular_room(x, y, x2, y2, 0)
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

main()
