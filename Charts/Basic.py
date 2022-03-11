# -*- coding: utf-8 -*-
# Endovia (Basic)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

class Chart(object):
    def __init__(self, id, chart_width, chart_height, active):
        self.id = id
        self.width = chart_width
        self.height = chart_height
        self.active = active
        # Initialize all grids as empty.
        self.grids = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{},
                      9:{}, 10:{}, 11:{}, 12:{}, 13:{}, 14:{}, 15:{}, 16:{},
                      17:{}, 18:{}, 19:{}, 20:{}, 21:{}, 22:{}, 23:{}, 24:{},
                      25:{}, 26:{}, 27:{}, 28:{}, 29:{}, 30:{}, 31:{}, 32:{},
                      33:{}, 34:{}, 35:{}, 36:{}, 37:{}, 38:{}, 39:{}, 40:{},
                      41:{}, 42:{}, 1000:{}, 1001:{}, 1002:{}, 1003:{}, 1004:{},
                      1005:{}, 1006:{}, 1007:{}, 1008:{}, 1009:{}, 1010:{},
                      1011:{}, 1012:{}, 1013:{}, 1014:{}, 1015:{}, 1016:{},
                      1017:{}, 1018:{}, 1019:{}, 1020:{}, 1021:{}, 1022:{},
                      1023:{}, 1024:{}, 1025:{}, 1026:{}, 2000:{}, 2001:{},
                     }
        # Positions seen.
        self.seen = list()
        entities = {}
    def create_empty_grid(self, grid_id, grid_width, grid_height):
        # Loop through the entire grid and fill it with None.
        for y in range(0, grid_height):
            for x in range(0, grid_width):
                self.grids[grid_id][(x, y)] = None
    def create_filled_grid(self, grid_id, grid_width, grid_height, thing_id):
        # Loop through the entire grid and fill it with thing_id.
        for y in range(0, grid_height):
            for x in range(0, grid_width):
                self.grids[grid_id][(x, y)] = {}
                self.grids[grid_id][(x, y)] = (grid_id, thing_id)
    def is_obstruction_single(self, grid_id, grid_x, grid_y):
        if self.grids[grid_id][(grid_x, grid_y)] != None:
            return True
        else:
            return False
    def is_obstruction_all(self, grid_x, grid_y, ignore_floor = True):
        for grid_id in self.grids.keys():
            # Ignore the floor possibly because objects go over floors.
            if ignore_floor:
                if grid_id == 1:
                    continue
            if self.grids[grid_id][(grid_x, grid_y)] != None:
                return True

# Jafinoxal.
