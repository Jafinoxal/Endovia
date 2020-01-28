# -*- coding: utf-8 -*-
# Endovia (DrawChart)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def DrawFloorsWalls(library, objects, chart, player):
    fov_map = library.map_new(chart.width, chart.height)
    for category in (1, 0):
        for y in range(0, chart.height):
            for x in range(0, chart.width):
                if chart.grids[category][(x, y)] == None:
                    library.map_set_properties(fov_map, x, y, True, True)
                else:
                    library.map_set_properties(fov_map, x, y, objects[category][chart.grids[category][(x, y)][8]], not objects[category][chart.grids[category][(x, y)][7]])
    library.map_compute_fov(fov_map, player.x, player.y, 10, True, 0)
    for category in (1, 0):
        for y in  range(0, chart.height):
            for x in range(0, chart.width):
                if chart.grids[category][(x, y)] != None:
                    if library.map_is_in_fov(fov_map, x, y):
                        object_reference = objects[category][chart.grids[category][(x, y)][1]]
                        library.console_set_char_foreground(0, x+1, y+1, library.Color(object_reference[6][0][0],
                                                                                       object_reference[6][0][1],
                                                                                       object_reference[6][0][2]))
                        library.console_set_char_background(0, x+1, y+1, library.Color(object_reference[6][1][0],
                                                                                       object_reference[6][1][1],
                                                                                       object_reference[6][1][2]))
                        library.console_set_char(0, x+1, y+1, object_reference[5])
                    else:
                        library.console_set_char_foreground(0, x+1, y+1, library.Color(0, 0, 0))
                        library.console_set_char_background(0, x+1, y+1, library.Color(0, 0, 0))
                        library.console_set_char(0, x+1, y+1, " ")

def DrawEntities(library, entities, chart, player):
    fov_map = library.map_new(chart.width, chart.height)
    for category in (2000, 2001):
        for y in range(0, chart.height):
            for x in range(0, chart.width):
                if chart.grids[category][(x, y)] == None:
                    library.map_set_properties(fov_map, x, y, True, True)
                else:
                    library.map_set_properties(fov_map, x, y, entities[category][chart.grids[category][(x, y)][8]], not entities[category][chart.grids[category][(x, y)][7]])
    library.map_compute_fov(fov_map, player.x, player.y, 10, True, 0)
    for category in (2000, 2001):
        for y in  range(0, chart.height):
            for x in range(0, chart.width):
                if chart.grids[category][(x, y)] != None:
                    if library.map_is_in_fov(fov_map, x, y):
                        entity_reference = entities[category][chart.grids[category][(x, y)][1]]
                        library.console_set_char_foreground(0, x+1, y+1, library.Color(entity_reference[6][0][0],
                                                                                       entity_reference[6][0][1],
                                                                                       entity_reference[6][0][2]))
                        library.console_set_char_background(0, x+1, y+1, library.Color(entity_reference[6][1][0],
                                                                                       entity_reference[6][1][1],
                                                                                       entity_reference[6][1][2]))
                        library.console_set_char(0, x+1, y+1, entity_reference[5])
                    else:
                        library.console_set_char_foreground(0, x+1, y+1, library.Color(0, 0, 0))
                        library.console_set_char_background(0, x+1, y+1, library.Color(0, 0, 0))
                        library.console_set_char(0, x+1, y+1, " ")

def DrawBorder(library, chart_width, chart_height):
    library.console_set_char_foreground(0, 0, 0, library.Color(255, 255, 255))
    library.console_set_char_background(0, 0, 0, library.Color(0, 0, 0))
    library.console_set_char(0, 0, 0, '\xc9')
    library.console_set_char_foreground(0, chart_width + 1, 0, library.Color(255, 255, 255))
    library.console_set_char_background(0, chart_width + 1, 0, library.Color(0, 0, 0))
    library.console_set_char(0, chart_width + 1, 0, '\xbb')
    library.console_set_char_foreground(0, 0, chart_height + 1, library.Color(255, 255, 255))
    library.console_set_char_background(0, 0, chart_height + 1, library.Color(0, 0, 0))
    library.console_set_char(0, 0, chart_height + 1, '\xc8')
    library.console_set_char_foreground(0, chart_width + 1, chart_height + 1, library.Color(255, 255, 255))
    library.console_set_char_background(0, chart_width + 1, chart_height + 1, library.Color(0, 0, 0))
    library.console_set_char(0, chart_width + 1, chart_height + 1, '\xbc')
    for y in range(1, chart_height + 1):
        library.console_set_char_foreground(0, 0, y, library.Color(255, 255, 255))
        library.console_set_char_background(0, 0, y, library.Color(0, 0, 0))
        library.console_set_char(0, 0, y, '\xba')
        library.console_set_char_foreground(0, chart_width + 1, y, library.Color(255, 255, 255))
        library.console_set_char_background(0, chart_width + 1, y, library.Color(0, 0, 0))
        library.console_set_char(0, chart_width + 1, y, '\xba')
    for x in range(1, chart_width + 1):
        library.console_set_char_foreground(0, x, 0, library.Color(255, 255, 255))
        library.console_set_char_background(0, x, 0, library.Color(0, 0, 0))
        library.console_set_char(0, x, 0, '\xcd')
        library.console_set_char_foreground(0, x, chart_height + 1, library.Color(255, 255, 255))
        library.console_set_char_background(0, x, chart_height + 1, library.Color(0, 0, 0))
        library.console_set_char(0, x, chart_height + 1, '\xcd')

# Jafinoxal.
