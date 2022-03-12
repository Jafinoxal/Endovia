# Endovia (MovementHandler)
# Copyright (C) 2010-2022 Jeremy Aaron Flexer.

import random
import tcod

def _in_boundaries(x_from, y_from, x_add, y_add, chart):
    if x_from + x_add < 0:
        return False
    elif x_from + x_add >= chart.width:
        return False
    elif y_from + y_add < 0:
        return False
    elif y_from + y_add >= chart.height:
        return False
    else:
        return True

def _no_obstruction(x_from, y_from, x_add, y_add, chart, objects, entities):
    for grid_number in chart.grids.keys():
        if grid_number < 1000: # Objects.
            if chart.grids[grid_number][(x_from + x_add, y_from + y_add)] == None:
                continue
            if not objects[grid_number][chart.grids[grid_number][(x_from + x_add, y_from + y_add)][1]][7]: # 7 is clip.
                continue
            else:
                return False
        if grid_number > 1999 and grid_number < 3000: # Entities.
            if chart.grids[grid_number][(x_from + x_add, y_from + y_add)] == None:
                continue
            if not entities[grid_number][chart.grids[grid_number][(x_from + x_add, y_from + y_add)][1]][7]: # 7 is clip.
                continue
            else:
                return False
    return True

def _in_enemy(x_from, y_from, x_add, y_add, chart, entities):
    for grid_number in chart.grids.keys():
        if grid_number > 1999 and grid_number < 3000: # Entities.
            if chart.grids[grid_number][(x_from + x_add, y_from + y_add)] == None:
                continue
            #if not entities[grid_number][chart.grids[grid_number][(x_from + x_add, y_from + y_add)][1]][7]: # 7 is clip.
            #    continue
            else:
                return True
    return False

#def _path_finding(chart, entity, player, objects, characters):
     # http://www.roguebasin.com/index.php/Complete_Roguelike_Tutorial,_using_Python%2Blibtcod,_extras
#    fov_map = tcod.map_new(chart.width, chart.height)
#    for category in (1, 0):
#        for y in range(0, chart.height):
#            for x in range(0, chart.width):
#                if chart.grids[category][(x, y)] == None:
#                    tcod.map_set_properties(fov_map, x, y, True, True)
#                else:
#                    tcod.map_set_properties(fov_map, x, y, objects[category][chart.grids[category][(x, y)][1]][8], not objects[category][chart.grids[category][(x, y)][1]][7])
#    for category in range(0, 43):
#        for y in range(0, chart.height):
#            for x in range(0, chart.width):
#                if chart.grids[category][(x, y)] == None:
#                    tcod.map_set_properties(fov_map, x, y, True, True)
#                else:
#                    tcod.map_set_properties(fov_map, x, y, objects[category][chart.grids[category][(x, y)][1]][8], not objects[category][chart.grids[category][(x, y)][1]][7])
#    for category in range(0, 43):
#        for y in range(0, chart.height):
#            for x in range(0, chart.width):
#                if chart.grids[category][(x, y)] == None:
#                    tcod.map_set_properties(fov_map, x, y, True, True)
#                else:
#                    if 2002 > category >= 2000:
#                        tcod.map_set_properties(fov_map, x, y, characters[category][chart.grids[category][(x, y)][1]][8], not characters[category][chart.grids[category][(x, y)][1]][7])
#                    else:
#                        tcod.map_set_properties(fov_map, x, y, objects[category][chart.grids[category][(x, y)][1]][8], not objects[category][chart.grids[category][(x, y)][1]][7])
    # Allocate a A* path
    # The 1.41 is the normal diagonal cost of moving, it can be set as 0.0 if diagonal moves are prohibited
#    my_path = tcod.path_new_using_map(fov_map, 1.41)
    # Compute the path between self's coordinates and the target's coordinates
#    tcod.path_compute(my_path, entity.x, entity.y, player.x, player.y)
    # Check if the path exists, and in this case, also the path is shorter than 25 tiles
    # The path size matters if you want the monster to use alternative longer paths (for example through other rooms) if for example the player is in a corridor
    # It makes sense to keep path size relatively low to keep the monsters from running around the map if there's an alternative path really far away
#    if not tcod.path_is_empty(my_path) and tcod.path_size(my_path) < 25:
        # Find the next coordinates in the computed full path
#        x, y = tcod.path_walk(my_path, True)
#        if x or y:
            # Set self's coordinates to the next path
#            tcod.path_delete(my_path)
#            return fov_map, entity.x, entity.y, x, y
    # Delete the path to free memory
#    tcod.path_delete(my_path)
#    return False

def MoveEnemies(chart, entities, objects, characters, stay):
    for entity in entities.keys():
        if entity == 0:
            continue
        if entity == stay:
            continue
        if entities[entity].dead:
            continue
        x = random.choice((0, -1, 1))
        y = random.choice((0, -1, 1))
        if _in_boundaries(entities[entity].x, entities[entity].y, x, y, chart) and _no_obstruction(entities[entity].x, entities[entity].y, x, y, chart, objects, characters):
            x_from = entities[entity].x
            y_from = entities[entity].y
            entities[entity].x = entities[entity].x + x
            entities[entity].y = entities[entity].y + y
            chart.grids[entities[entity].grid_id][(entities[entity].x, entities[entity].y)] = chart.grids[entities[entity].grid_id][(x_from, y_from)]
            chart.grids[entities[entity].grid_id][(x_from, y_from)] = None
    return False

def MoveCharacter(x_from, y_from, x_add, y_add, character_to_move, chart, objects, characters):
    if _in_boundaries(x_from, y_from, x_add, y_add, chart) and _no_obstruction(x_from, y_from, x_add, y_add, chart, objects, characters):
        character_to_move.x = x_from + x_add
        character_to_move.y = y_from + y_add
        chart.grids[character_to_move.grid_id][(x_from + x_add, y_from + y_add)] = chart.grids[character_to_move.grid_id][(x_from, y_from)]
        chart.grids[character_to_move.grid_id][(x_from, y_from)] = None
        return False
    if _in_boundaries(x_from, y_from, x_add, y_add, chart):
        if _in_enemy(x_from, y_from, x_add, y_add, chart, characters):
            return True
    return False
# Jafinoxal.
