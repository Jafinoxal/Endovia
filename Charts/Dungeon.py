# -*- coding: utf-8 -*-
# Endovia (Dungeon)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import Basic

# NOTE: This will be Dungeon.Chart, or just Chart if used here.
class Chart(Basic.Chart):
    def __init__(self, chart_width, chart_height, active):
        super(Chart, self).__init__(chart_width, chart_height, active)
        # rooms contains (start_x, start_y, end_x, end_y
        self.rooms = []
    def intersect(self, proposed_room):
        # Keep something to mark if an non-intersection occurs.
        pass_count = 0
        # See if the room intersects with any other rooms, if it doesn't, increase the pass count.
        for room in self.rooms:
            if (room[0] > proposed_room[2]) or (room[2] < proposed_room[0]) or (room[1] > proposed_room[3]) or (room[3] < proposed_room[1]):
                pass_count += 1
        if pass_count == len(self.rooms):
            return False
        return True
    def carve_rectangular_room(self, start_x, start_y, width, height, object_id):
        end_x = start_x + width
        end_y = start_y + height
        # Go through each coordinate in the room and erase the walls, add floor if needed.
        if not self.intersect((start_x, start_y, end_x, end_y)):
            for x in range(start_x + 1, end_x):
                for y in range(start_y + 1, end_y):
                    self.grids[0][(x, y)] = None
                    if self.grids[1][(x, y)] == None:
                        self.grids[1][(x, y)] = {}
                        self.grids[1][(x, y)][0] = object_id
            self.rooms.append((start_x, start_y, end_x, end_y))
            return True
        else:
            return False
    def carve_horizontal_tunnel(self, start_x, end_x, current_y, object_id):
        # Erase the walls to make a tunnel between two things.
        for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
            self.grids[0][(x, current_y)] = None
            if self.grids[1][(x, current_y)] == None:
                self.grids[1][(x, y)] = {}
                self.grids[1][(x, current_y)][0] = object_id
    def carve_vertical_tunnel(self, start_y, end_y, current_x, object_id):
        # Erase the walls to make a tunnel between two things.
        for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
            self.grids[1][(current_x, y)] = None
            if self.grids[0][(current_x, y)] == None:
                self.grids[1][(x, y)] = {}
                self.grids[0][(current_x, y)][0] = object_id

# Jafinoxal.
