# -*- coding: utf-8 -*-
# Endovia (Constant)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import time

def draw_floor_and_walls(self, objects, chart):
    # Set the color and then draw the character that represents this object at its position.
    # Data should be a dictionary of objects that use Object type classes.
    for category in (1, 0):
        for y in  range(0, chart.chart_height:
            for x in range(0, chart.chart_length:
                library.console_set_default_foreground(0, libtcod.Color(objects[category][chart.grid[category][x, y][0]][6][0]]))
                library.console_set_default_background(0, libtcod.Color(objects[category][chart.grid[category][x, y][0]][6][1]]))
                library.console_put_char(0, x, y,  objects[category][chart.grid[category][x, y][0]][5], libtcod.BKGND_SET)

def draw_entities(self, entities, chart):
    # Draw player entities which aren't held in the charts.
    for category in range(len(entities)):
        for y in  range(0, chart.chart_height:
            for x in range(0, chart.chart_length:
                library.console_set_default_foreground(0, libtcod.Color(objects[category][chart.grid[category][x, y][1]][6][0]]))
                library.console_set_default_background(0, libtcod.Color(objects[category][chart.grid[category][x, y][1]][6][1]]))
                library.console_put_char(0, x, y,  entities[category][chart.grid[category][x, y][0]][5], libtcod.BKGND_SET)

# Jafinoxal.
