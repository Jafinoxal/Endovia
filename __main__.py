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

from Characters.Constant import *
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
WINDOW_NAME = "Endovia 1.173"
FONT_NAME = "terminal8x8_gs_ro.png"
FILE_READ_MODE = "rb"
FILE_WRITE_MODE = "wb"
FONT_TYPE = libtcodpy.FONT_TYPE_GREYSCALE | libtcodpy.FONT_LAYOUT_ASCII_INROW
SAVE_FILE_NAME = "endovia.save"
PLAYER_GRID_ID = 2000
PLAYER_ENTITY_ID = 0

def load_game():
    return pickle.load(open(SAVE_FILE_NAME, FILE_READ_MODE))

def save_game(data):
    pickle.dump(data, open(SAVE_FILE_NAME, FILE_WRITE_MODE))

# All chart/map/dungeon generation and creation goes here.
def new_game():
    charts = {
    0: Charts.charts["Dungeon"].Chart(CHART_ID, CHART_WIDTH, CHART_HEIGHT, True),
    }
    # Fill the object wall grid with walls, can be carved out later.
    charts[0].create_filled_grid(0, CHART_WIDTH, CHART_HEIGHT, 0)
    # Fill all other object grids with None, they're empty.
    for category in range(1, OBJECT_CATEGORIES):
        charts[0].create_empty_grid(category, CHART_WIDTH, CHART_HEIGHT)
    # Fill all item grids with None, they're empty.
    for category in range(1000, 1000 + ITEM_CATEGORIES):
        charts[0].create_empty_grid(category, CHART_WIDTH, CHART_HEIGHT)
    # Fill all character grids with None, they're empty.
    for category in range(2000, 2000 + CHARACTER_CATEGORIES):
        charts[0].create_empty_grid(category, CHART_WIDTH, CHART_HEIGHT)
    # Run the dungeon generator which returns the player position and the
    # enemy positions. NOTE: See Charts.Dungeon/Charts.Generators for more.
    # Enemy positions return as dictionary of very many sets of key/value
    # [(entity_category, entity_id)] = (x, y).
    player_position, enemy_positions = Charts.charts["Generators"].MainDungeonGenerator(Objects.objects, Characters.characters, charts[0], charts[0].rooms, 0, 2001, range(0, RODENT_COUNT))
    # Find the active chart, if so save the chart id in chart_id.
    for chart in charts.keys():
        if charts[chart].active:
            chart_id = charts[chart].id
            break
    # Create a dictionary to hold the player's and enemy's characters.
    entities = {
    0: Entities.entities["Player"].Character(chart_id, PLAYER_GRID_ID, PLAYER_ENTITY_ID, 0, player_position[0], player_position[1], "Player", "Human"),
    }
    # Start at 1 because player is always unique_id 0.
    unique_id = 1
    # Iterate through each enemy and create an Enemy Character object.
    for enemy_category_and_id, enemy_position in enemy_positions.items():
        entities[unique_id] = Entities.entities["Enemy"].Character(chart_id, enemy_category_and_id[0],
        enemy_category_and_id[1], unique_id, enemy_position[0], enemy_position[1],
        Characters.characters[enemy_category_and_id[0]][enemy_category_and_id[1]][CHARACTER_HEALTH])
        # Each character gets a fresh id.
        unique_id += 1
        charts[0].entities = entities
    return charts

# Basic libtcod initialization.
libtcodpy.console_set_custom_font(FONT_NAME, FONT_TYPE, 0, 0)
libtcodpy.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_NAME, False)
libtcodpy.sys_set_fps(FRAMES_PER_SECOND)

def main(load = False):
    # Get the object set charts from start_game.
    # NOTE-DEFUNCT: player_position and enemy_positions are needed to place in the
    # object set characters. They can also be used in other places.
    if load:
        pass
    else:
        charts = new_game()
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
        Graphics.graphics["DrawChart"].DrawFloorsWalls(libtcodpy, Objects.objects, charts[0], charts[0].entities[0])
        Graphics.graphics["DrawChart"].DrawEntities(libtcodpy, Objects.objects, Characters.characters, charts[0], charts[0].entities[0])
        Graphics.graphics["DrawChart"].DrawBorder(libtcodpy, charts[chart_id].width, charts[0].height)
        # Info related drawing.
        Graphics.graphics["DrawInfo"].DrawStats(libtcodpy, charts[chart_id], charts[0].entities[0])
        Graphics.graphics["DrawInfo"].DrawAttributes(libtcodpy, charts[chart_id], charts[0].entities[0])
        Graphics.graphics["DrawInfo"].DrawSkills(libtcodpy, charts[chart_id], charts[0].entities[0])
        Graphics.graphics["DrawInfo"].DrawLocation(libtcodpy, charts[chart_id], charts[0].entities[0])
        Graphics.graphics["DrawInfo"].DrawMessages(libtcodpy, messages, charts[chart_id])
        Graphics.graphics["DrawInfo"].DrawEnemyInfo(libtcodpy, charts[chart_id], charts[0].entities, enemy_x, enemy_y)
        # Reset the enemy position so enemy info doesn't draw out of fight.
        enemy_x, enemy_y = None, None
        # Flush the console.
        libtcodpy.console_flush()
        if main_level_up:
            choice = 0
            stat_choices = ("health", "mana", "energy", "faith", "chakra")
            while True:
                # Stat menu drawing.
                Graphics.graphics["DrawMenu"].DrawBorderStatChoice(libtcodpy)
                Graphics.graphics["DrawMenu"].DrawFillerStatChoice(libtcodpy)
                Graphics.graphics["DrawMenu"].DrawStatChoice(libtcodpy, choice)
                libtcodpy.console_flush()
                # Choose a stat to advance and wait for the enter key.
                event = Handlers.handlers["InputHandler"].StatMenu(libtcodpy)
                if event == SELECT_MENU_ENTER:
                    Handlers.handlers["LevelingHandler"].LevelStat(charts[0].entities[0], stat_choices[choice])
                    skip_input = True
                    break
                if choice == 0 and event == MOVE_MENU_UP:
                    choice = 4
                elif choice == 4 and event == MOVE_MENU_DOWN:
                    choice = 0
                elif choice > 0 and event == MOVE_MENU_UP:
                    choice -= 1
                elif choice < 4 and event == MOVE_MENU_DOWN:
                    choice += 1
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
            enemy_there = Handlers.handlers["MovementHandler"].MoveCharacter(charts[0].entities[0].x, charts[0].entities[0].y, NORTH[0], NORTH[1], charts[0].entities[0], charts[chart_id], Objects.objects, Characters.characters)
            if enemy_there:
                enemy_at = (charts[0].entities[0].x + NORTH[0], charts[0].entities[0].y + NORTH[1])
            turn_taken = True
        elif event == MOVE_PLAYER_SOUTH:
            enemy_there = Handlers.handlers["MovementHandler"].MoveCharacter(charts[0].entities[0].x, charts[0].entities[0].y, SOUTH[0], SOUTH[1], charts[0].entities[0], charts[chart_id], Objects.objects, Characters.characters)
            if enemy_there:
                enemy_at = (charts[0].entities[0].x + SOUTH[0], charts[0].entities[0].y + SOUTH[1])
            turn_taken = True
        elif event == MOVE_PLAYER_WEST:
            enemy_there = Handlers.handlers["MovementHandler"].MoveCharacter(charts[0].entities[0].x, charts[0].entities[0].y, WEST[0], WEST[1], charts[0].entities[0], charts[chart_id], Objects.objects, Characters.characters)
            if enemy_there:
                enemy_at = (charts[0].entities[0].x + WEST[0], charts[0].entities[0].y + WEST[1])
            turn_taken = True
        elif event == MOVE_PLAYER_EAST:
            enemy_there = Handlers.handlers["MovementHandler"].MoveCharacter(charts[0].entities[0].x, charts[0].entities[0].y, EAST[0], EAST[1], charts[0].entities[0], charts[chart_id], Objects.objects, Characters.characters)
            if enemy_there:
                enemy_at = (charts[0].entities[0].x + EAST[0], charts[0].entities[0].y + EAST[1])
            turn_taken = True
        elif event == ACCESS_INVENTORY:
            inventory_category = 1000
            inventory_id = 0
            inventory_length = len(Items.items[inventory_category])
            while True:
                Graphics.graphics["DrawMenu"].DrawBorderInventoryChoice(libtcodpy)
                Graphics.graphics["DrawMenu"].DrawFillerInventoryChoice(libtcodpy)
                Graphics.graphics["DrawMenu"].DrawInventoryChoice(libtcodpy, (inventory_category, inventory_id), charts[0].entities[0].inventory, Items.items)
                libtcodpy.console_flush()
                event = Handlers.handlers["InputHandler"].InventoryMenu(libtcodpy)
                if event == EXIT_MENU:
                    skip_input = True
                    break
                # These 4 conditionals move the inventory up and down.
                if inventory_id == 0 and event == MOVE_MENU_UP:
                    inventory_id = inventory_length - 1
                elif inventory_id == inventory_length - 1 and event == MOVE_MENU_DOWN:
                    inventory_id = 0
                elif inventory_id > 0 and event == MOVE_MENU_UP:
                    inventory_id -= 1
                elif inventory_id < inventory_length - 1 and event == MOVE_MENU_DOWN:
                    inventory_id += 1
                # These 4 conditionals move the category type.
                elif inventory_category == 1000 and event == MOVE_MENU_LEFT:
                    inventory_category = 1000 + ITEM_CATEGORIES - 1
                    inventory_id = 0
                elif inventory_category < 1000 + ITEM_CATEGORIES - 1 and event == MOVE_MENU_RIGHT:
                    inventory_category += 1
                    inventory_id = 0
                elif inventory_category > 1000 and event == MOVE_MENU_LEFT:
                    inventory_category -= 1
                    inventory_id = 0
                elif inventory_category == 1000 + ITEM_CATEGORIES - 1 and event == MOVE_MENU_RIGHT:
                    inventory_category = 1000
                    inventory_id = 0
                inventory_length = len(Items.items[inventory_category])
            # Get the input event, event is a constant from Handlers.Constant.
            if not skip_input:
                event = Handlers.handlers["InputHandler"].MainGame(libtcodpy)
        else:
            event = None
        if enemy_there:
            for message in Handlers.handlers["CombatHandler"].FightCharacter(charts[chart_id], charts[0].entities[0], charts[0].entities, enemy_at[0], enemy_at[1], Characters.characters):
                messages.append(message)
            enemy_x, enemy_y = enemy_at[0], enemy_at[1]
            # main_level_up is used to see if we should pick a stat to increase.
        main_level_up, messages_new = Handlers.handlers["LevelingHandler"].LevelCharacter(charts[0].entities[0])
        for message in messages_new:
            messages.append(message)

# If running this file, call the main function.
if __name__ == '__main__':
    main()

# Jafinoxal.
