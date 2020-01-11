# -*- coding: utf-8 -*-
# Endovia (Basic)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

class Chart(object):
    def __init__(self, chart_width, chart_height, active):
        self.chart_width = chart_width
        self.chart_height = chart_height
        self.active = active
        self.grids = {}
    def create_empty_grid(self, grid_number, grid_width, grid_height):
        for y in range(0, grid_height):
            for x in range(0, grid_width):
                self.grids[grid_number][(x, y)][0] = None
    def create_filled_grid(self, grid_number, grid_width, grid_height, object_id):
        for y in range(0, grid_height):
            for x in range(0, grid_width):
                self.grids[grid_number][(x, y)][0] = object_id

# Jafinoxal.
