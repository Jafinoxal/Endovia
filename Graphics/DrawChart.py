# -*- coding: utf-8 -*-
# Endovia (DrawChart)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def DrawFloorsWalls(library, console, objects, chart, player):
    fov_map = library.map_new(chart.width, chart.height)
    for category in (1, 0):
        for y in range(0, chart.height):
            for x in range(0, chart.width):
                if chart.grids[category][(x, y)] == None:
                    library.map_set_properties(fov_map, x, y, True, True)
                else:
                    library.map_set_properties(fov_map, x, y, objects[category][chart.grids[category][(x, y)][1]][8], not objects[category][chart.grids[category][(x, y)][1]][7])
    library.map_compute_fov(fov_map, player.x, player.y, 5, True, 2)
    for category in (1, 0):
        for y in  range(0, chart.height):
            for x in range(0, chart.width):
                if chart.grids[category][(x, y)] != None:
                    if library.map_is_in_fov(fov_map, x, y):
                        if (x, y) not in chart.seen:
                            chart.seen.append((x, y))
                        object_reference = objects[category][chart.grids[category][(x, y)][1]]
                        console.print(x=x+1, y=y+1, string=object_reference[5], fg=(object_reference[6][0][0],object_reference[6][0][1],object_reference[6][0][2]), bg=(object_reference[6][1][0],object_reference[6][1][1],object_reference[6][1][2]))
                    elif (x, y) in chart.seen:
                        console.print(x=x+1, y=y+1, string='?', fg=(35,35,35), bg=(0,0,0))
                    else:
                        console.print(x=x+1, y=y+1, string=' ', fg=(0,0,0), bg=(0,0,0))

def DrawObjects(library, console, objects, chart, player):
    fov_map = library.map_new(chart.width, chart.height)
    for category in range(0, 43):
        for y in range(0, chart.height):
            for x in range(0, chart.width):
                if chart.grids[category][(x, y)] == None:
                    library.map_set_properties(fov_map, x, y, True, True)
                else:
                    library.map_set_properties(fov_map, x, y, objects[category][chart.grids[category][(x, y)][1]][8], not objects[category][chart.grids[category][(x, y)][1]][7])
    library.map_compute_fov(fov_map, player.x, player.y, 5, True, 2)
    for category in range(2, 43):
        for y in  range(0, chart.height):
            for x in range(0, chart.width):
                if chart.grids[category][(x, y)] != None:
                    if library.map_is_in_fov(fov_map, x, y):
                        if (x, y) not in chart.seen:
                            chart.seen.append((x, y))
                        object_reference = objects[category][chart.grids[category][(x, y)][1]]
                        console.print(x=x+1, y=y+1, string=object_reference[5], fg=(object_reference[6][0][0],object_reference[6][0][1],object_reference[6][0][2]), bg=(object_reference[6][1][0],object_reference[6][1][1],object_reference[6][1][2]))
                    elif (x, y) in chart.seen:
                        console.print(x=x+1, y=y+1, string='?', fg=(35,35,35), bg=(0,0,0))
                    else:
                        console.print(x=x+1, y=y+1, string=' ', fg=(0,0,0), bg=(0,0,0))

def DrawEntities(library, console, objects, characters, chart, player):
    fov_map = library.map_new(chart.width, chart.height)
    grids = []
    for category in range(0, 43):
        for y in range(0, chart.height):
            for x in range(0, chart.width):
                if chart.grids[category][(x, y)] == None:
                    library.map_set_properties(fov_map, x, y, True, True)
                else:
                    if 2002 > category >= 2000:
                        library.map_set_properties(fov_map, x, y, characters[category][chart.grids[category][(x, y)][1]][8], not characters[category][chart.grids[category][(x, y)][1]][7])
                    else:
                        library.map_set_properties(fov_map, x, y, objects[category][chart.grids[category][(x, y)][1]][8], not objects[category][chart.grids[category][(x, y)][1]][7])
    library.map_compute_fov(fov_map, player.x, player.y, 5, True, 2)
    for category in range(2000, 2002):
        for y in  range(0, chart.height):
            for x in range(0, chart.width):
                if chart.grids[category][(x, y)] != None:
                    if library.map_is_in_fov(fov_map, x, y):
                        if (x, y) not in chart.seen:
                            chart.seen.append((x, y))
                        character_reference = characters[category][chart.grids[category][(x, y)][1]]
                        console.print(x=x+1, y=y+1, string=character_reference[5], fg=(character_reference[6][0][0],character_reference[6][0][1], character_reference[6][0][2]), bg = (character_reference[6][1][0], character_reference[6][1][1], character_reference[6][1][2]))

def DrawBorder(console, chart_width, chart_height):
    console.print(x=0, y=0, string='╔', fg=(255,255,255), bg=(0,0,0))
    console.print(x=chart_width+1, y=0, string='╗', fg=(255,255,255), bg=(0,0,0))
    console.print(x=0, y=chart_height+1, string='╚', fg=(255,255,255), bg=(0,0,0))
    console.print(x=chart_width+1, y=chart_height+1, string='╝', fg =(255,255,255), bg=(0,0,0))
    for y in range(1, chart_height + 1):
        console.print(x=0, y=y, string='║', fg=(255,255,255), bg=(0,0,0))
        console.print(x=chart_width+1, y=y, string='║', fg=(255,255,255), bg=(0,0,0))
    for x in range(1, chart_width + 1):
        console.print(x=x, y=0, string='═', fg=(255,255,255), bg=(0,0,0))
        console.print(x=x, y=chart_height+1, string='═', fg=(255,255,255), bg=(0,0,0))

# Jafinoxal.
