# -*- coding: utf-8 -*-
# Endovia (DrawChart)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import time

def DrawFloorsWalls(library, objects, chart):
    for category in (1, 0):
        for y in  range(0, chart.chart_height):
            for x in range(0, chart.chart_width):
                if chart.grids[category][(x, y)] != None:
                    object_reference = objects[category][chart.grids[category][(x, y)][0]]
                    library.console_set_char_foreground(0, x+1, y+1, library.Color(object_reference[6][0][0],
                                                                                   object_reference[6][0][1],
                                                                                   object_reference[6][0][2]))
                    library.console_set_char_background(0, x+1, y+1, library.Color(object_reference[6][1][0],
                                                                                   object_reference[6][1][1],
                                                                                   object_reference[6][1][2]))
                    library.console_put_char(0, x+1, y+1, object_reference[5], library.BKGND_SET)

def DrawEntities(library, entities, chart):
    for category in (2000, 2000):
        for y in  range(0, chart.chart_height):
            for x in range(0, chart.chart_width):
                if chart.grids[category][(x, y)] != None:
                    entity_reference = entities[category][chart.grids[category][(x, y)][0]]
                    library.console_set_char_foreground(0, x+1, y+1, library.Color(entity_reference[6][0][0],
                                                                               entity_reference[6][0][1],
                                                                               entity_reference[6][0][2]))
                    library.console_set_char_background(0, x+1, y+1, library.Color(entity_reference[6][1][0],
                                                                               entity_reference[6][1][1],
                                                                               entity_reference[6][1][2]))
                    library.console_put_char(0, x+1, y+1, entity_reference[5], library.BKGND_SET)

# Jafinoxal.
