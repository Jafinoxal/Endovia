# -*- coding: utf-8 -*-
# Endovia (Constant)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import time

def draw_floors_and_walls(library, objects, chart):
    # Set the color and then draw the character that represents this object at its position.
    # Data should be a dictionary of objects that use Object type classes.
    for category in (1, 0):
        for y in  range(0, chart.chart_height):
            for x in range(0, chart.chart_width):
                if chart.grids[category][(x, y)] != None:
                    library.console_set_default_foreground(0, library.Color(objects[category][chart.grids[category][(x, y)][0]][6][0]))
                    library.console_set_default_background(0, library.Color(objects[category][chart.grids[category][(x, y)][0]][6][1]))
                    library.console_put_char(0, x, y,  objects[category][chart.grid[category][(x, y)][0]][5], library.BKGND_SET)
                else:
                    library.console_set_default_foreground(0, library.Color((0,0,0)))
                    library.console_set_default_background(0, library.Color((0,0,0)))
                    library.console_put_char(0, x, y,  " ", library.BKGND_SET)
def draw_entities(library, entities, chart):
    # Draw player entities which aren't held in the charts.
    for category in range(len(entities)):
        for y in  range(0, chart.chart_height):
            for x in range(0, chart.chart_width):
                if chart.grids[category][(x, y)] != None:
                    library.console_set_default_foreground(0, library.Color(objects[category][chart.grids[category][(x, y)][1]][6][0]))
                    library.console_set_default_background(0, library.Color(objects[category][chart.grids[category][(x, y)][1]][6][1]))
                    library.console_put_char(0, x, y,  entities[category][chart.grid[category][(x, y)][0]][5], library.BKGND_SET)
                else:
                    library.console_set_default_foreground(0, library.Color((0,0,0)))
                    library.console_set_default_background(0, library.Color((0,0,0)))
                    library.console_put_char(0, x, y,  " ", library.BKGND_SET)

# Jafinoxal.
