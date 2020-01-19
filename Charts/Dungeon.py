# -*- coding: utf-8 -*-
# Endovia (Dungeon)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import random

import Basic

# NOTE: This will be Dungeon.Chart, or just Chart if used here.
class Chart(Basic.Chart):
    def __init__(self, chart_width, chart_height, active):
        super(Chart, self).__init__(chart_width, chart_height, active)
        # rooms contains (start_x, start_y, end_x, end_y
        self.rooms = []

    def _intersect(self, proposed_room):
        # Keep something to mark if an non-intersection occurs.
        pass_count = 0
        # See if the room intersects with any other rooms, if it doesn't, increase the pass count.
        for room in self.rooms:
            if (room[0] > proposed_room[2]) or (room[2] < proposed_room[0]) or (room[1] > proposed_room[3]) or (room[3] < proposed_room[1]):
                pass_count += 1
        if pass_count == len(self.rooms):
            return False
        return True

    def _carve_rectangular_room(self, start_x, start_y, width, height, object_id):
        end_x = start_x + width
        end_y = start_y + height
        # Go through each coordinate in the room and erase the walls, add floor if needed.
        if not self._intersect((start_x, start_y, end_x, end_y)):
            for x in range(start_x + 1, end_x):
                for y in range(start_y + 1, end_y):
                    self.grids[0][(x, y)] = None
                    if self.grids[1][(x, y)] == None:
                        self.grids[1][(x, y)] = {0: object_id}
            self.rooms.append((start_x, start_y, end_x, end_y))
            return True
        else:
            return False

    def _carve_tunnels(self, start_x, start_y, width, height, object_id):
        for y in range(start_y, height):
            horizontal_tunnels_dug = 0
            vertical_tunnels_dug = 0
            for x in range(start_x, width):
                if random.randint(0, 25) == 0 and horizontal_tunnels_dug < 3:
                    tunnel_length = random.randint(4, 12)
                    for x in range(x, x + tunnel_length):
                        self.grids[0][(x, y)] = None
                        self.grids[1][(x, y)] = {0: object_id}
                    horizontal_tunnels_dug += 1
                if random.randint(0, 25) == 0 and vertical_tunnels_dug < 3:
                    tunnel_length = random.randint(4, 12)
                    for y in range(y, y + tunnel_length):
                        self.grids[0][(x, y)] = None
                        self.grids[1][(x, y)] = {0: object_id}
                    vertical_tunnels_dug += 1

    def _is_free(self, objects, entities, x, y):
        for category in objects.keys():
            if category == 1:
                continue
            if self.grids[category][(x, y)]:
                return False
        for category in entities:
            if self.grids[category][(x, y)]:
                return False
        return True

    def _place_player_start(self, objects, entities, entity_category, entity_id):
        for y in range(self.height):
            for x in range(self.width):
                if not self._is_free(objects, entities, x, y):
                    continue
                self.grids[entity_category][(x, y)] = (entity_category, entity_id)
                return (x, y)

    def _place_enemies_start(self, objects, entities, entity_category, entity_id):
        entity_positions = dict()
        for i in range (0, 100):
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if not self._is_free(objects, entities, x, y):
                continue
            if random.randint(0, 1):
                self.grids[entity_category][(x, y)] = (entity_category, entity_id)
                entity_positions[(entity_category, entity_id)] = (x, y)
        return entity_positions

# Jafinoxal.
