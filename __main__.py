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


def start_charts(load=False):
    if load:
        return pickle.load(open("Saves/Charts.save", "rb"))
    else:
        charts = {
        0: Charts.charts["Dungeon"].Chart(80, 50, True),
        }
        charts[0].create_empty_grid(0, 80, 50)
        charts[0].create_filled_grid(1, 80, 50, 0)
        charts[0].create_empty_grid(2000, 80, 50)
        import random
        for i in range(0, 200):
            x = random.randint(1, charts[0].chart_width - 11)
            x2 = random.randint(5, 10)
            y = random.randint(1, charts[0].chart_height - 11)
            y2 = random.randint(5, 10)
            charts[0].carve_rectangular_room(x, y, x2, y2, (0, 0))
    return charts

def start_characters(load=False):
    if load:
        return pickle.load(open("Saves/Characters.save", "rb"))
    else:
        characters = {
        0: Characters.characters["Player"].Character(0, 0, 0, 2000, 10, 10),
        }
    return characters

libtcodpy.console_set_custom_font("consolas_unicode_16x16.png", libtcodpy.FONT_TYPE_GREYSCALE | libtcodpy.FONT_LAYOUT_ASCII_INROW, 0, 0)
libtcodpy.console_init_root(85, 55, "Endovia 1.025", False)
libtcodpy.sys_set_fps(60)

def main():
    charts = start_charts(False)
    characters = start_characters(False)
    while not libtcodpy.console_is_window_closed():
        Graphics.graphics["DrawCharts"].draw_floors_and_walls(libtcodpy, Objects.objects, charts[0])
        Graphics.graphics["DrawCharts"].draw_entities(libtcodpy, Entities.entities, charts[0])
        libtcodpy.console_flush()
main()
