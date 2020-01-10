# Endovia (Basic)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

class Chart(object):
    def __init__(self, chart_width, chart_height, active):
        self.chart_width = chart_width
        self.chart_height = chart_height
        self.active = active
        self.grid_count = 0
        self.grids = {}
    def create_empty_grid(self, grid_width, grid_height):
        self.grids[self.grid_count] = {}
        for y in range(0, grid_height):
            for x in range(0, grid_width):
                self.grids[self.grid_count][(x, y)] = None
        self.grid_count += 1
    def create_filled_grid(self, grid_width, grid_height, object_id):
        self.grids[self.grid_count] = {}
        for y in range(0, grid_height):
            for x in range(0, grid_width):
                self.grids[self.grid_count][(x, y)] = object_id
        self.grid_count += 1

# Jafinoxal
