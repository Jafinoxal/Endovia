#!/usr/bin/env python
# Endovia (Main)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import libtcod
import pickle
import random

import Characters
import Charts
import Entities
import Graphics
import Handlers
import Items
import Objects


def start_charts(load=False):
    if load:
        return pickle.load(open("Saves/Charts.save", "rb"))
    else:
        charts = {
        0: Charts["Dungeon"].Chart(),
        }
        charts[0].create_filled_grid(1, 80, 50)
        import random
        for i in range(0, 200):
            x = random.randint(1, charts[0].chart_width - 11)
            x2 = random.randint(5, 10)
            y = random.randint(1, charts[0].chart_height - 11)
            y2 = random.randint(5, 10)
            charts[0].carve_rectangular_room(x, y, x2, y2, (0, 0))

def start_characters(load=False):
    if load:
        return pickle.load(open("Saves/Characters.save", "rb"))
    else:
        characters = {
        0: Characters["Player"].Character(),
        }

library.console_set_custom_font("consolas_unicode_12x12.png", libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(80, 50, name, False)
libtcod.sys_set_fps(60)

def main():
    charts = start_charts(False)
    while not libtcod.console_is_window_closed():
        draw_floor_and_walls(Objects, charts[0])
        draw_entities(Objects, charts[0])
    libtcod.console_flush()
    if exit:
        break
