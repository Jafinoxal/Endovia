#!/usr/bin/env python2
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
from Items.Constant import *
from Objects.Constant import *

# Constants.
SCREEN_WIDTH = 125
SCREEN_HEIGHT = 82
CHART_ID = 0
CHART_WIDTH = 70
CHART_HEIGHT = 70
FRAMES_PER_SECOND = 60
WINDOW_NAME = "Endovia 1.147"
FONT_NAME = "terminal8x8_gs_ro.png"
FILE_READ_MODE = "rb"
FONT_TYPE = libtcodpy.FONT_TYPE_GREYSCALE | libtcodpy.FONT_LAYOUT_ASCII_INROW
CHARTS_SAVE_FILE_NAME = "Saves/Charts.save"
CHARACTERS_SAVE_FILE_NAME = "Saves/Characters.save"
PLAYER_GRID_ID = 2000
PLAYER_ENTITY_ID = 0
LOADING = False

# All chart/map/dungeon generation and creation goes here.
def start_charts(load=False):
    if load:
        return pickle.load(open(CHARTS_SAVE_FILE_NAME, FILE_READ_MODE))
    else:
        charts = {
        0: Charts.charts["Dungeon"].Chart(CHART_ID, CHART_WIDTH, CHART_HEIGHT, True),
        }
        # Fill the object wall grid with walls, can be carved out later.
        charts[0].create_filled_grid(0, CHART_WIDTH, CHART_HEIGHT, 0)
        # Fill all other object grids with None, they're empty.
        for category in range(1, OBJECT_CATEGORIES):
            charts[0].create_empty_grid(category, CHART_WIDTH, CHART_HEIGHT)
        # Fill all entity grids with None, they're empty.
        for category in range(2000, 2000 + ENTITY_CATEGORIES):
            charts[0].create_empty_grid(category, CHART_WIDTH, CHART_HEIGHT)
        # Run the dungeon generator which returns the player position and the
        # enemy positions. NOTE: See Charts.Dungeon/Charts.Generators for more.
        # Enemy positions return as dictionairy of very many sets of key/value
        # [(entity_category, entity_id)] = (x, y).
        player_position, enemy_positions = Charts.charts["Generators"].MainDungeonGenerator(Objects.objects, Entities.entities, charts[0], charts[0].rooms, 0, 0)
    return charts, player_position, enemy_positions

# All entity/character generation and creation goes here.
def start_characters(player_position, enemy_positions, charts, load=False):
    if load:
        return pickle.load(open(CHARACTERS_SAVE_FILE_NAME, FILE_READ_MODE))
    else:
        # Find the active chart, if so save the chart id in chart_id.
        for chart in charts.keys():
            if charts[chart].active:
                chart_id = charts[chart].id
                break
        # Create a dictionary to hold the player's and enemies's characters.
        characters = {
        0: Characters.characters["Player"].Character(chart_id, PLAYER_GRID_ID, PLAYER_ENTITY_ID, 0, player_position[0], player_position[1], "Player", "Human"),
        }
        # Start at 1 because player is always unique_id 0.
        unique_id = 1
        # Iterate through each enemy and create a Enemy Character object.
        for enemy_category_and_id, enemy_position in enemy_positions.items():
            characters[unique_id] = Characters.characters["Enemy"].Character(chart_id, enemy_category_and_id[0],
                                                                                enemy_category_and_id[1],
                                                                                unique_id,
                                                                                enemy_position[0],
                                                                                enemy_position[1],
                                                                                Entities.entities[enemy_category_and_id[0]][enemy_category_and_id[1]][ENTITY_HEALTH])

            # Each character gets a fresh id.
            unique_id += 1
    return characters

# Basic libtcod initialization.
libtcodpy.console_set_custom_font(FONT_NAME, FONT_TYPE, 0, 0)
libtcodpy.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_NAME, False)
libtcodpy.sys_set_fps(FRAMES_PER_SECOND)

def main():
    # Get the object set charts from start_charts.
    # NOTE: player_position and enemy_positions are needed to place in the
    # object set characters. They can also be used in other places.
    if not LOADING:
        charts, player_position, enemy_positions = start_charts(LOADING)
    else:
        charts = start_charts(LOADING)
    if not LOADING:
        characters = start_characters(player_position, enemy_positions, charts,  LOADING)
    else:
        characters = start_characters(None, None, None,  LOADING)
    # Messages will be displayed [-1:-10].
    messages = []
    # Initialize the enemy position for the DrawEnemyInfo function.
    enemy_x, enemy_y = None, None
    # Initialize main_level_up here so no error occurs.
    main_level_up = False
    while not libtcodpy.console_is_window_closed():
        skip_input = False
        # Reset turn_taken to False so enemies don't take a turn when player doesn't.
        turn_taken = False
        # Find the active chart, if so save the chart id in chart_id.
        for chart in charts.keys():
            if charts[chart].active:
                chart_id = charts[chart].id
                break
        # Chart related drawing.
        Graphics.graphics["DrawChart"].DrawFloorsWalls(libtcodpy, Objects.objects, charts[0], characters[0])
        Graphics.graphics["DrawChart"].DrawEntities(libtcodpy, Objects.objects, Entities.entities, charts[0], characters[0])
        Graphics.graphics["DrawChart"].DrawBorder(libtcodpy, charts[chart_id].width, charts[0].height)
        # Info related drawing.
        Graphics.graphics["DrawInfo"].DrawStats(libtcodpy, charts[chart_id], characters[0])
        Graphics.graphics["DrawInfo"].DrawAttributes(libtcodpy, charts[chart_id], characters[0])
        Graphics.graphics["DrawInfo"].DrawSkills(libtcodpy, charts[chart_id], characters[0])
        Graphics.graphics["DrawInfo"].DrawLocation(libtcodpy, charts[chart_id], characters[0])
        Graphics.graphics["DrawInfo"].DrawMessages(libtcodpy, messages, charts[chart_id])
        Graphics.graphics["DrawInfo"].DrawEnemyInfo(libtcodpy, charts[chart_id], characters, enemy_x, enemy_y, Entities.entities)
        # Reset the enemy position so enemy info doesn't draw out of fight.
        enemy_x, enemy_y = None, None
        # Flush the console.
        libtcodpy.console_flush()
        if main_level_up:
            choice = 0
            stat_choices = ("health", "mana", "energy")
            while True:
                # Stat menu drawing.
                Graphics.graphics["DrawMenu"].DrawBorder(libtcodpy, charts[chart_id].width, charts[0].height)
                Graphics.graphics["DrawMenu"].DrawFiller(libtcodpy)
                Graphics.graphics["DrawMenu"].DrawStatChoice(libtcodpy, choice)
                libtcodpy.console_flush()
                # Choose a stat to advance and wait for the enter key.
                event = Handlers.handlers["InputHandler"].StatMenu(libtcodpy)
                if event == SELECT_MENU_ENTER:
                    Handlers.handlers["LevelingHandler"].LevelStat(characters[0], stat_choices[choice])
                    skip_input = True
                    break
                if choice == 0 and event == MOVE_MENU_UP:
                    choice = 2
                elif choice == 0 and event == MOVE_MENU_DOWN:
                    choice = 1
                elif choice == 2 and event == MOVE_MENU_DOWN:
                    choice = 0
                elif choice == 2 and event == MOVE_MENU_UP:
                    choice = 1
                elif choice == 1 and event == MOVE_MENU_UP:
                    choice = 0
                elif choice == 1 and event == MOVE_MENU_DOWN:
                    choice = 2
        # Get the input event, event is a constant from Handlers.Constant.
        if not skip_input:
            event = Handlers.handlers["InputHandler"].MainGame(libtcodpy)
        else:
            event = None
        enemy_there = False
        # If event is the escape key exit game without saving.
        if event == EXIT_GAME_WITHOUT_SAVE:
            exit(0)
            # Check if the event is a move key; If so then try to move a player.
            # Returns True if an enemy is in the way, store that in enemy_there.
        elif event == MOVE_PLAYER_NORTH:
            enemy_there = Handlers.handlers["MovementHandler"].MoveCharacter(characters[0].x, characters[0].y, NORTH[0], NORTH[1], characters[0], charts[chart_id], Objects.objects, Entities.entities)
            if enemy_there:
                enemy_at = (characters[0].x + NORTH[0], characters[0].y + NORTH[1])
            turn_taken = True
        elif event == MOVE_PLAYER_SOUTH:
            enemy_there = Handlers.handlers["MovementHandler"].MoveCharacter(characters[0].x, characters[0].y, SOUTH[0], SOUTH[1], characters[0], charts[chart_id], Objects.objects, Entities.entities)
            if enemy_there:
                enemy_at = (characters[0].x + SOUTH[0], characters[0].y + SOUTH[1])
            turn_taken = True
        elif event == MOVE_PLAYER_WEST:
            enemy_there = Handlers.handlers["MovementHandler"].MoveCharacter(characters[0].x, characters[0].y, WEST[0], WEST[1], characters[0], charts[chart_id], Objects.objects, Entities.entities)
            if enemy_there:
                enemy_at = (characters[0].x + WEST[0], characters[0].y + WEST[1])
            turn_taken = True
        elif event == MOVE_PLAYER_EAST:
            enemy_there = Handlers.handlers["MovementHandler"].MoveCharacter(characters[0].x, characters[0].y, EAST[0], EAST[1], characters[0], charts[chart_id], Objects.objects, Entities.entities)
            if enemy_there:
                enemy_at = (characters[0].x + EAST[0], characters[0].y + EAST[1])
            turn_taken = True
        if enemy_there:
            for message in Handlers.handlers["CombatHandler"].FightCharacter(charts[chart_id], characters[0], characters, enemy_at[0], enemy_at[1], Entities.entities):
                messages.append(message)
            enemy_x, enemy_y = enemy_at[0], enemy_at[1]
            # main_level_up is used to see if we should pick a stat to increase.
        main_level_up, messages_new = Handlers.handlers["LevelingHandler"].LevelCharacter(characters[0])
        for message in messages_new:
            messages.append(message)

# If running this file, call the main function.
if __name__ == '__main__':
    main()

# Jafinoxal.
