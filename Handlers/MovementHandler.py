# Endovia (MovementHandler)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def in_boundaries(self, x_from, y_from, x_add, y_add, chart):
    if x_from + x_add < 0:
        return False
    elif x_from + x_add >= chart.chart_width:
        return False
    elif y_from + y_add < 0:
        return False
    elif y_from + y_add >= chart.chart_height:
        return False
    else:
        return True

def no_obstruction(self, x_from, y_from, x_add, y_add, chart, objects, entities):
    for grid_number in chart.grids.keys():
        if grid_number < 1000: # Objects.
            if chart.grids[grid_number][0] == None:
                continue
            if not objects[grid_number][chart.grids[grid_number][0]][7]: # 7 is clip.
                continue
            else:
                return False
        if grid_number > 1999 and grid_number < 3000: # Entities.
            if chart.grids[grid_number][0] == None:
                continue
            if not entities[grid_number][chart.grids[grid_number][0]][7]: # 7 is clip.
                continue
            else:
                return False
    return True

def move_character(x_from, y_from, x_add, y_add, character_to_move, chart, objects, entities):
    if boundaries(x_from, y_from, x_add, y_add, chart) and self.obstruction(x, y, chart, objects, entities):
        character_to_move.x = x_from + x_add
        character_to_move.y = y_from + y_add
        chart.grids[character_to_move.grid_id][(x_from + x_add, y_from + y_add)] = chart.grids[character_to_move.grid_id][(x_from, y_from)]
        chart.grids[character_to_move.grid_id][(x_from, y_from)] = None

# Jafinoxal.
