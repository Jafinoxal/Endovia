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

from Entities.Constant import *
from Handlers.Constant import *
from Objects.Constant import *

SCREEN_WIDTH = 125
SCREEN_HEIGHT = 85
CHART_WIDTH = 70
CHART_HEIGHT = 70
WINDOW_NAME = "Endovia 1.051"
FONT_NAME = "terminal8x8_gs_ro.png"
FONT_TYPE = libtcodpy.FONT_TYPE_GREYSCALE | libtcodpy.FONT_LAYOUT_ASCII_INROW
CHARTS_SAVE_FILE_NAME = "Saves/Charts.save"
CHARACTERS_SAVE_FILE_NAME = "Saves/Characters.save"
PLAYER_GRID_ID = 0
PLAYER_ENTITY_ID = 0

def start_charts(load=False):
    if load:
        return pickle.load(open(CHARTS_SAVE_FILE_NAME, "rb"))
    else:
        charts = {
        0: Charts.charts["Dungeon"].Chart(CHART_WIDTH, CHART_HEIGHT, True),
        }
        # Objects.
        charts[0].create_filled_grid(0, CHART_WIDTH, CHART_HEIGHT, 0)
        for category in range(1, OBJECT_CATEGORIES):
            charts[0].create_empty_grid(category, CHART_WIDTH, CHART_HEIGHT)
        # Entities.
        for category in range(2000, 2000 + ENTITY_CATEGORIES):
            charts[0].create_empty_grid(category, CHART_WIDTH, CHART_HEIGHT)
        # Dungeon.
        player_position, enemy_positions = Charts.charts["Generators"].MainDungeonGenerator(Objects.objects, Entities.entities, charts[0], charts[0].rooms, 0, 0)
    return charts, player_position, enemy_positions

def start_characters(player_position, enemy_positions, load=False):
    if load:
        return pickle.load(open(CHARACTERS_SAVE_FILE_NAME, "rb"))
    else:
        characters = {
        0: Characters.characters["Player"].Character(0, PLAYER_GRID_ID, PLAYER_ENTITY_ID, 0, player_position[0], player_position[1], "Player", "Human"),
        }
        unique_id = 1
        for enemy_category_and_id, enemy_position in enemy_positions.items():
            characters[(enemy_category_and_id[0], enemy_category_and_id[1], unique_id)] = Characters.characters["Enemy"].Character(0, enemy_category_and_id[0],
                                                                                                                                      enemy_category_and_id[1],
                                                                                                                                      unique_id,
                                                                                                                                      enemy_position[0],
                                                                                                                                      enemy_position[1],
                                                                                                                                      Entities.entities[enemy_category_and_id[0]][enemy_category_and_id[1]][ENTITY_HEALTH])
            unique_id += 1
    return characters

libtcodpy.console_set_custom_font(FONT_NAME, FONT_TYPE, 0, 0)
libtcodpy.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_NAME, False)
libtcodpy.sys_set_fps(20)

def main():
    charts, player_position, enemy_positions = start_charts(False)
    characters = start_characters(player_position, enemy_positions, False)
    while not libtcodpy.console_is_window_closed():
        Graphics.graphics["DrawChart"].DrawFloorsWalls(libtcodpy, Objects.objects, charts[0])
        Graphics.graphics["DrawChart"].DrawEntities(libtcodpy, Entities.entities, charts[0])
        Graphics.graphics["DrawChart"].DrawBorder(libtcodpy, charts[0].width, charts[0].height)
        Graphics.graphics["DrawInfo"].DrawStats(libtcodpy, charts[0], characters[0])
        Graphics.graphics["DrawInfo"].DrawAttributes(libtcodpy, charts[0], characters[0])
        Graphics.graphics["DrawInfo"].DrawSkills(libtcodpy, charts[0], characters[0])
        #Graphics.graphics["DrawChart"].DrawChartBorders(charts[0])
        libtcodpy.console_flush()
        event = Handlers.handlers["InputHandler"].MainGame(libtcodpy)
        if event == EXIT_GAME_WITHOUT_SAVE:
            exit(0)
        elif event == MOVE_PLAYER_NORTH:
            enemy_there = Handlers.handlers["MovementHandler"].MoveCharacter(characters[0].x, characters[0].y, NORTH[0], NORTH[1], characters[0], charts[0], Objects.objects, Entities.entities)
            if enemy_there:
                enemy_at = (characters[0].x + NORTH[0], characters[0].y + NORTH[1])
        elif event == MOVE_PLAYER_SOUTH:
            enemy_there = Handlers.handlers["MovementHandler"].MoveCharacter(characters[0].x, characters[0].y, SOUTH[0], SOUTH[1], characters[0], charts[0], Objects.objects, Entities.entities)
            if enemy_there:
                enemy_at = (characters[0].x + SOUTH[0], characters[0].y + SOUTH[1])
        elif event == MOVE_PLAYER_WEST:
            enemy_there = Handlers.handlers["MovementHandler"].MoveCharacter(characters[0].x, characters[0].y, WEST[0], WEST[1], characters[0], charts[0], Objects.objects, Entities.entities)
            if enemy_there:
                enemy_at = (characters[0].x + WEST[0], characters[0].y + WEST[1])
        elif event == MOVE_PLAYER_EAST:
            enemy_there = Handlers.handlers["MovementHandler"].MoveCharacter(characters[0].x, characters[0].y, EAST[0], EAST[1], characters[0], charts[0], Objects.objects, Entities.entities)
            if enemy_there:
                enemy_at = (characters[0].x + EAST[0], characters[0].y + EAST[1])
        #if enemy_there:
        #    Handlers.handlers["CombatHandler"].FightCharacter()
if __name__ == '__main__':
    main()

# Jafinoxal.
