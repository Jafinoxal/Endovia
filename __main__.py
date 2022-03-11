#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Endovia (Endovia Main)
# Copyright (C) 2010-2021 Jeremy Aaron Flexer.

import tcod
import pickle
import random
import os.path

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

# Guide:
# 1. The player is stored at charts[0].entities[0], This is the host. The host
#    and the board's entities are stored with the host/player.
# 2. If a multiplayer online adaptation is made, store non-host players in a
#    variable named charts[0].foreign.
# 3. Games are saved with the pickle module (endovia.save).
# 4. A library called libtcod is used for /fov/ and /graphics/.

# Constants.
SCREEN_WIDTH = 125
SCREEN_HEIGHT = 82
RANDOM_CHART_ID = 0
CHART_WIDTH = 70
CHART_HEIGHT = 70
FRAMES_PER_SECOND = 60
WINDOW_NAME = "Endovia 1.211"
FONT_NAME = "ascii_8x8.png"
FILE_READ_MODE = "rb"
FILE_WRITE_MODE = "wb"
FONT_CHAR_MAP = tcod.tileset.CHARMAP_CP437
SAVE_FILE_NAME = "endovia.save"
PLAYER_GRID_ID = 2000
PLAYER_ENTITY_ID = 0
VSYNC = True
ORDER = 'F'

def load_game():
    return pickle.load(open(SAVE_FILE_NAME, FILE_READ_MODE))

def save_game(data):
    pickle.dump(data, open(SAVE_FILE_NAME, FILE_WRITE_MODE))

# All chart/map/dungeon generation and creation goes here.
def new_game():
    charts = {
    RANDOM_CHART_ID: Charts.charts["Dungeon"].Chart(RANDOM_CHART_ID, CHART_WIDTH, CHART_HEIGHT, True),
    }
    # Fill the object wall grid with walls, can be carved out later.
    charts[RANDOM_CHART_ID].create_filled_grid(0, CHART_WIDTH, CHART_HEIGHT, 0)
    # Fill all other object grids with None, they're empty.
    charts[RANDOM_CHART_ID].create_filled_grid(1, CHART_WIDTH, CHART_HEIGHT, 0)
    for category in range(2, OBJECT_CATEGORIES):
        charts[RANDOM_CHART_ID].create_empty_grid(category, CHART_WIDTH, CHART_HEIGHT)
    # Fill all item grids with None, they're empty.
    for category in range(1000, 1000 + ITEM_CATEGORIES):
        charts[RANDOM_CHART_ID].create_empty_grid(category, CHART_WIDTH, CHART_HEIGHT)
    # Fill all character grids with None, they're empty.
    for category in range(2000, 2000 + CHARACTER_CATEGORIES):
        charts[RANDOM_CHART_ID].create_empty_grid(category, CHART_WIDTH, CHART_HEIGHT)
    # Run the dungeon generator which returns the player position and the
    # enemy positions. NOTE: See Charts.Dungeon/Charts.Generators for more.
    # Enemy positions return as dictionary of very many sets of key/value
    # [(entity_category, entity_id)] = (x, y).
    player_position, enemy_positions = Charts.charts["Generators"].MainDungeonGenerator1(Objects.objects, Characters.characters, charts[0], charts[0].rooms, 0, 2001, range(0, RODENT_COUNT))
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
        charts[RANDOM_CHART_ID].entities = entities
    return charts

# Basic libtcod initialization (Python 3+).
TILESET = tcod.tileset.load_tilesheet(FONT_NAME, 16, 16, FONT_CHAR_MAP)
CONTEXT = tcod.context.new_terminal(SCREEN_WIDTH, SCREEN_HEIGHT, tileset=TILESET, title=WINDOW_NAME, vsync=VSYNC)
CONSOLE = tcod.Console(SCREEN_WIDTH, SCREEN_HEIGHT, order=ORDER)

def Main():
    # Get the object set charts from start_game.
    # NOTE-DEFUNCT: player_position and enemy_positions are needed to place in the
    # object set characters. They can also be used in other places.
    # The Main Menu!
    #while not tcod.console_is_window_closed():
    while True:
        choice = 0
        while True:
            Graphics.graphics["DrawMenu"].DrawMainMenu(CONSOLE, choice)
            CONTEXT.present(CONSOLE)
            event = Handlers.handlers["InputHandler"].MainMenu(tcod)
            if event == SELECT_MENU_ENTER:
                # For unimplemented options.
                if choice not in (2, 3): # TODO: Construct & Credits.
                    break
            if choice == 0 and event == MOVE_MENU_UP:
                choice = 4
            elif choice == 4 and event == MOVE_MENU_DOWN:
                choice = 0
            elif choice > 0 and event == MOVE_MENU_UP:
                choice -= 1
            elif choice < 4 and event == MOVE_MENU_DOWN:
                choice += 1
        break
    if choice == 0:
        charts = new_game()
    elif choice == 1:
        if os.path.isfile(SAVE_FILE_NAME):
            charts = load_game()
        else:
            charts = new_game()
            print("NO SAVED GAME FOUND, STARTING NEW GAME.")
    elif choice == 4:
        exit()
    else:
        charts = new_game()
    # Messages will be displayed [-1:-10].
    messages = []
    # Initialize the enemy position for the DrawEnemyInfo function.
    enemy_x, enemy_y = None, None
    # Initialize main_level_up here so no error occurs.
    main_level_up = False
    while not tcod.console_is_window_closed():
        # To draw spell info to screen.
        destruction_spell_info = DESTRUCTION_SPELLS[charts[0].entities[0].active_destruction_spell[1]]
        restoration_spell_info = RESTORATION_SPELLS[charts[0].entities[0].active_restoration_spell[1]]
        # Don't skip input.
        skip_input = False
        # Reset turn_taken to False so enemies don't take a turn when player doesn't.
        turn_taken = False
        # Find the active chart, if so save the chart id in chart_id.
        for chart in charts.keys():
            if charts[chart].active:
                chart_id = charts[chart].id
                break
        player_id = 0
        # Chart related drawing.
        Graphics.graphics["DrawChart"].DrawFloorsWalls(tcod, CONSOLE, Objects.objects, charts[chart_id], charts[chart_id].entities[player_id])
        Graphics.graphics["DrawChart"].DrawObjects(tcod, CONSOLE, Objects.objects, charts[chart_id], charts[chart_id].entities[player_id])
        Graphics.graphics["DrawChart"].DrawEntities(tcod, CONSOLE, Objects.objects, Characters.characters, charts[chart_id], charts[chart_id].entities[player_id])
        Graphics.graphics["DrawChart"].DrawBorder(CONSOLE, charts[chart_id].width, charts[chart_id].height)
        # Info related drawing.
        Graphics.graphics["DrawInfo"].DrawStats(CONSOLE, charts[chart_id], charts[chart_id].entities[player_id])
        Graphics.graphics["DrawInfo"].DrawAttributes(CONSOLE, charts[chart_id], charts[chart_id].entities[player_id])
        Graphics.graphics["DrawInfo"].DrawSkills(CONSOLE, charts[chart_id], charts[chart_id].entities[player_id])
        Graphics.graphics["DrawInfo"].DrawLocation(CONSOLE, charts[chart_id], charts[chart_id].entities[player_id])
        Graphics.graphics["DrawInfo"].DrawMessages(CONSOLE, messages, charts[chart_id])
        Graphics.graphics["DrawInfo"].DrawEnemy(CONSOLE, charts[chart_id], charts[chart_id].entities, enemy_x, enemy_y)
        Graphics.graphics["DrawInfo"].DrawMagic(CONSOLE, charts[chart_id], charts[chart_id].entities[player_id], destruction_spell_info, restoration_spell_info)
        Graphics.graphics["DrawInfo"].DrawCombat(CONSOLE, charts[chart_id], charts[chart_id].entities[player_id], COMBAT_STYLES)
        # Reset the enemy position so enemy info doesn't draw out of fight.
        enemy_x, enemy_y = None, None
        # Flush the console.
        CONTEXT.present(CONSOLE)
        # The game is up, nice try though!
        if charts[chart_id].entities[player_id].stats["health"][0] <= 0:
            Graphics.graphics["DrawDeath"].DrawWindow(tcod, SCREEN_WIDTH, SCREEN_HEIGHT)
            Graphics.graphics["DrawDeath"].DrawMessage(tcod)
            CONTEXT.present(CONSOLE)
            tcod.console_wait_for_keypress(True)
            exit()
        if main_level_up:
            choice = 0
            stat_choices = ("health", "mana", "energy", "faith", "chakra")
            while True:
                # Stat menu drawing.
                Graphics.graphics["DrawMenu"].DrawBorderStatChoice(CONSOLE)
                Graphics.graphics["DrawMenu"].DrawFillerStatChoice(CONSOLE)
                Graphics.graphics["DrawMenu"].DrawStatChoice(CONSOLE, choice)
                CONTEXT.present(CONSOLE)
                # Choose a stat to advance and wait for the enter key.
                event = Handlers.handlers["InputHandler"].StatMenu(tcod)
                if event == SELECT_MENU_ENTER:
                    Handlers.handlers["LevelingHandler"].LevelStat(charts[chart_id].entities[player_id], stat_choices[choice])
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
            event = Handlers.handlers["InputHandler"].MainGame(tcod)
        else:
            event = None
        enemy_there = False
        # If event is the escape key exit game without saving.
        if event == EXIT_GAME_WITHOUT_SAVE:
            exit(0)
        # Check if the event is a move key; If so then try to move a player.
        # Returns True if an enemy is in the way, store that in enemy_there.
        # If event is the break wall key.
        elif event in (BREAK_WALL, MINE_VEIN):
            direction = Handlers.handlers["InputHandler"].SkillDirection(tcod)
            if direction == 3:
                direction = NORTH
            elif direction == 4:
                direction = SOUTH
            elif direction == 5:
                direction = WEST
            elif direction == 6:
                direction = EAST
            else:
                direction = (0, 0)
            if direction in (NORTH, SOUTH, WEST, EAST):
                if event == BREAK_WALL:
                    message = Handlers.handlers["SkillHandler"].BreakWall(charts[chart_id], charts[chart_id].entities[player_id], direction)
                elif event == MINE_VEIN:
                    message = Handlers.handlers["SkillHandler"].MineVein(charts[chart_id], charts[chart_id].entities[player_id], direction, Objects.objects[VEINS])
                messages.append(message)
                turn_taken = True
        elif event == MOVE_PLAYER_NORTH:
            enemy_there = Handlers.handlers["MovementHandler"].MoveCharacter(charts[chart_id].entities[player_id].x, charts[chart_id].entities[player_id].y, NORTH[0], NORTH[1], charts[chart_id].entities[player_id], charts[chart_id], Objects.objects, Characters.characters)
            if enemy_there:
                enemy_at = (charts[chart_id].entities[player_id].x + NORTH[0], charts[chart_id].entities[player_id].y + NORTH[1])
            turn_taken = True
        elif event == MOVE_PLAYER_SOUTH:
            enemy_there = Handlers.handlers["MovementHandler"].MoveCharacter(charts[chart_id].entities[player_id].x, charts[chart_id].entities[player_id].y, SOUTH[0], SOUTH[1], charts[chart_id].entities[player_id], charts[chart_id], Objects.objects, Characters.characters)
            if enemy_there:
                enemy_at = (charts[chart_id].entities[player_id].x + SOUTH[0], charts[chart_id].entities[player_id].y + SOUTH[1])
            turn_taken = True
        elif event == MOVE_PLAYER_WEST:
            enemy_there = Handlers.handlers["MovementHandler"].MoveCharacter(charts[chart_id].entities[player_id].x, charts[chart_id].entities[player_id].y, WEST[0], WEST[1], charts[chart_id].entities[player_id], charts[chart_id], Objects.objects, Characters.characters)
            if enemy_there:
                enemy_at = (charts[chart_id].entities[player_id].x + WEST[0], charts[chart_id].entities[player_id].y + WEST[1])
            turn_taken = True
        elif event == MOVE_PLAYER_EAST:
            enemy_there = Handlers.handlers["MovementHandler"].MoveCharacter(charts[chart_id].entities[player_id].x, charts[chart_id].entities[0].y, EAST[0], EAST[1], charts[chart_id].entities[player_id], charts[chart_id], Objects.objects, Characters.characters)
            if enemy_there:
                enemy_at = (charts[chart_id].entities[player_id].x + EAST[0], charts[chart_id].entities[player_id].y + EAST[1])
            turn_taken = True
        if event == ACCESS_COMBAT:
            choice = 0
            stat_choices = ("melee", "ranged", "magic", "jutsu", "arms")
            while True:
                # Stat menu drawing.
                Graphics.graphics["DrawMenu"].DrawBorderCombatChoice(CONSOLE)
                Graphics.graphics["DrawMenu"].DrawFillerCombatChoice(CONSOLE)
                Graphics.graphics["DrawMenu"].DrawCombatChoice(CONSOLE, choice)
                CONTEXT.present(CONSOLE)
                # Choose a stat to advance and wait for the enter key.
                event = Handlers.handlers["InputHandler"].CombatMenu(tcod)
                if event == SELECT_MENU_ENTER:
                    # Look in Handlers.Constant.
                    charts[0].entities[0].combat_style = choice
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
        # Inventory work.
        elif event == ACCESS_INVENTORY:
            # In practice all item categories start at 1000.
            inventory_category = 1000
            inventory_id = 0
            inventory_length = len(Items.items[inventory_category])
            while True:
                Graphics.graphics["DrawMenu"].DrawBorderInventoryChoice(CONSOLE)
                Graphics.graphics["DrawMenu"].DrawFillerInventoryChoice(CONSOLE)
                Graphics.graphics["DrawMenu"].DrawInventoryChoice(CONSOLE, (inventory_category, inventory_id), charts[0].entities[0].inventory, Items.items)
                CONTEXT.present(CONSOLE)
                event = Handlers.handlers["InputHandler"].InventoryMenu(tcod)
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
                event = Handlers.handlers["InputHandler"].MainGame(tcod)
        elif event == ACCESS_MAGIC:
            magic_category = "destruction"
            magic_id = 0
            magic_length = len(DESTRUCTION_SPELLS.values())
            magic_categories = ("destruction", "restoration")
            while True:
                Graphics.graphics["DrawMenu"].DrawBorderMagicChoice(CONSOLE)
                Graphics.graphics["DrawMenu"].DrawFillerMagicChoice(CONSOLE)
                Graphics.graphics["DrawMenu"].DrawMagicChoice(CONSOLE, (magic_category, magic_id), DESTRUCTION_SPELLS, RESTORATION_SPELLS, charts[0].entities[0])
                CONTEXT.present(CONSOLE)
                event = Handlers.handlers["InputHandler"].MagicMenu(tcod)
                if event == EXIT_MENU:
                    skip_input = True
                    break
                # These 4 conditionals move the inventory up and down.
                if magic_id == 0 and event == MOVE_MENU_UP:
                    magic_id = magic_length - 1
                elif magic_id == magic_length - 1 and event == MOVE_MENU_DOWN:
                    magic_id = 0
                elif magic_id > 0 and event == MOVE_MENU_UP:
                    magic_id -= 1
                elif magic_id < magic_length - 1 and event == MOVE_MENU_DOWN:
                    magic_id += 1
                elif magic_category == "destruction" and event in (MOVE_MENU_LEFT, MOVE_MENU_RIGHT):
                    magic_category = "restoration"
                    magic_id = 0
                    magic_length = len(RESTORATION_SPELLS.values())
                elif magic_category == "restoration" and event in (MOVE_MENU_LEFT, MOVE_MENU_RIGHT):
                    magic_category = "destruction"
                    magic_id = 0
                    magic_length = len(DESTRUCTION_SPELLS.values())
                elif event == MAGIC_SET_ACTIVE:
                    pass
            # Get the input event, event is a constant from Handlers.Constant.
            if not skip_input:
                event = Handlers.handlers["InputHandler"].MainGame(tcod)
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
    Main()

# Jafinoxal.
