# -*- coding: utf-8 -*-
# Endovia (Constant)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import time

def draw_floors_and_walls(library, objects, chart):
    for category in (1, 0):
        for y in  range(0, chart.chart_height):
            for x in range(0, chart.chart_width):
                if chart.grids[category][(x, y)] != None:
                    library.console_set_default_foreground(0, library.Color(objects[category][chart.grids[category][(x, y)][0]][6][0][0],
                                                                            objects[category][chart.grids[category][(x, y)][0]][6][0][1],
                                                                            objects[category][chart.grids[category][(x, y)][0]][6][0][2]))
                    library.console_set_default_background(0, library.Color(objects[category][chart.grids[category][(x, y)][0]][6][1][0],
                                                                            objects[category][chart.grids[category][(x, y)][0]][6][1][1],
                                                                            objects[category][chart.grids[category][(x, y)][0]][6][1][2]))
                    library.console_put_char(0, x, y,  objects[category][chart.grids[category][(x, y)][0]][5], library.BKGND_SET)
                else:
                    library.console_set_default_foreground(0, library.Color(0,0,0))
                    library.console_set_default_background(0, library.Color(0,0,0))
                    library.console_put_char(0, x, y,  " ", library.BKGND_SET)

def draw_entities(library, entities, chart):
    for category in range(2000, 2000 + len(entities)):
        for y in  range(0, chart.chart_height):
            for x in range(0, chart.chart_width):
                if chart.grids[category][(x, y)] != None:
                    library.console_set_default_foreground(0, library.Color(entities[category][chart.grids[category][(x, y)][0]][6][0][0],
                                                                            entities[category][chart.grids[category][(x, y)][0]][6][0][1],
                                                                            entities[category][chart.grids[category][(x, y)][0]][6][0][2]))
                    library.console_set_default_background(0, library.Color(entities[category][chart.grids[category][(x, y)][0]][6][1][0],
                                                                            entities[category][chart.grids[category][(x, y)][0]][6][1][1],
                                                                            entities[category][chart.grids[category][(x, y)][0]][6][1][2]))
                    library.console_put_char(0, x, y,  entities[category][chart.grids[category][(x, y)][0]][5], library.BKGND_SET)
                else:
                    library.console_set_default_foreground(0, library.Color(0,0,0))
                    library.console_set_default_background(0, library.Color(0,0,0))
                    library.console_put_char(0, x, y,  " ", library.BKGND_SET)

# Jafinoxal.