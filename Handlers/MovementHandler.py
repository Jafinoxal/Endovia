# Endovia (MovementHandler)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def in_boundaries(self, x_from, y_from, x_to, y_to, chart):
    if x_from + x_to < 0:
        return False
    elif x_from + x_to >= chart.chart_width:
        return False
    elif y_from + y_to < 0:
        return False
    elif y_from + y_to >= chart.chart_height:
        return False
    else:
        return True

def no_obstruction(self, x_from, y_from, x_to, y+to, chart, objects, entities):
    for grid_number in chart.grids.keys():
        if grid_number < 1000: # Objects.
            if chart.grids[grid_number][0] == None:
                continue
            if not objects[grid_number][chart.grids[grid_number][0]][7]: # 7 is clip.
                continue
            else:
                return False
        if grid_number > 999 and grid_number < 2000: # Entities
            if chart.grids[grid_number][0] == None:
                continue
            if not entities[grid_number][chart.grids[grid_number][0]][7]: # 7 is clip.
                continue
            else:
                return False
    return True

    def move(self, x, y, objects, charts):
        # Move by the given amount. Check if it's within boundaries of the area
        # and check if there is an obstruction.
        if self.boundaries(x, y, charts) and self.obstruction(x, y, objects, charts):
            self.x += x
            self.y += y

# Jafinoxal.
