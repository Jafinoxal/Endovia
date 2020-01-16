# -*- coding: utf-8 -*-
# Endovia (Basic)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

class Chart(object):
    def __init__(self, chart_width, chart_height, active):
        self.width = chart_width
        self.height = chart_height
        self.active = active
        self.grids = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{},
                      9:{}, 10:{}, 11:{}, 12:{}, 13:{}, 14:{}, 15:{}, 2000:{}}
    def create_empty_grid(self, grid_number, grid_width, grid_height):
        for y in range(0, grid_height):
            for x in range(0, grid_width):
                self.grids[grid_number][(x, y)] = None
    def create_filled_grid(self, grid_number, grid_width, grid_height, object_id):
        for y in range(0, grid_height):
            for x in range(0, grid_width):
                self.grids[grid_number][(x, y)] = {}
                self.grids[grid_number][(x, y)][0] = object_id

# Jafinoxal.
