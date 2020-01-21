# -*- coding: utf-8 -*-
# Endovia (Dungeon)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import random

import Basic

# NOTE: This will be Dungeon.Chart, or just Chart if used here.
class Chart(Basic.Chart):
    def __init__(self, id, chart_width, chart_height, active):
        super(Chart, self).__init__(id, chart_width, chart_height, active)
        # rooms contains (start_x, start_y, end_x, end_y
        self.rooms = []

    def _intersect(self, proposed_room):
        # Keep something to mark if an non-intersection occurs.
        pass_count = 0
        # See if the room intersects with any other rooms, if it doesn't, increase the pass count.
        for room in self.rooms:
            # Check if room is within another room.
            if (room[0] > proposed_room[2]) or (room[2] < proposed_room[0]) or (room[1] > proposed_room[3]) or (room[3] < proposed_room[1]):
                pass_count += 1
        # Continue if all rooms have been checked and none intersect.
        if pass_count == len(self.rooms):
            # Return False because no rooms intersect.
            return False
        # Return True because a room intersects.
        return True

    def _carve_rectangular_room(self, start_x, start_y, width, height, object_id):
        end_x = start_x + width
        end_y = start_y + height
        # Go through each coordinate in the room and erase the walls, add floor if needed.
        # Continue if this room is not inside of another room.
        if not self._intersect((start_x, start_y, end_x, end_y)):
            # Start looping through the rooms coordinates.
            for x in range(start_x + 1, end_x):
                for y in range(start_y + 1, end_y):
                    # Replace wall with None.
                    self.grids[0][(x, y)] = None
                    # If floor is None; Replace with object_id (floor).
                    if self.grids[1][(x, y)] == None:
                        self.grids[1][(x, y)] = {0: 1, 1: object_id, 2: None}
            # Add this room to rooms list so other rooms don't intersect.
            self.rooms.append((start_x, start_y, end_x, end_y))
            # Return True because room carving was successful.
            return True
        else:
            # Return False because room carving was a failure.
            return False

    def _carve_tunnels(self, start_x, start_y, width, height, object_id):
        for y in range(start_y, height):
            # The max horizontal or vertical tunnels that can be dug is 3.
            horizontal_tunnels_dug = 0
            vertical_tunnels_dug = 0
            # Iterate the start of the the grid.
            for x in range(start_x, width):
                # If by random chance start carving a horizontal tunnel.
                if random.randint(0, 25) == 0 and horizontal_tunnels_dug < 3:
                    # Decide tunnel length.
                    tunnel_length = random.randint(4, 12)
                    for x in range(x, x + tunnel_length):
                        # Check if tunnel position is within bounds.
                        if width > x > start_x and height > y > start_y:
                            # Carve out tunnel position.
                            self.grids[0][(x, y)] = None
                            self.grids[1][(x, y)] = {0: 1, 1: object_id, 2: None}
                    horizontal_tunnels_dug += 1
                # If by random chance start digging a vertical tunnel.
                elif random.randint(0, 25) == 0 and vertical_tunnels_dug < 3:
                    # Decide tunnel length.
                    tunnel_length = random.randint(4, 12)
                    for y in range(y, y + tunnel_length):
                        # Check if tunnel position is within bounds.
                        if width > x > start_x and height > y > start_y:
                            # Carve out tunnel position.
                            self.grids[0][(x, y)] = None
                            self.grids[1][(x, y)] = {0: 1, 1: object_id, 2: None}
                    vertical_tunnels_dug += 1

    def _is_free(self, objects, entities, x, y): # HexDecimal
        for category in objects.keys():
            # Skip category 1 because objects and entities can be placed on most floors.
            if category == 1:
                continue
            # If True, something is there. Return False because something is there.
            if self.grids[category][(x, y)]:
                return False
        for category in entities:
            # Like above, returns False if something is there.
            if self.grids[category][(x, y)]:
                return False
        # Returns True if nothing has been detected at the position.
        return True

    def _place_player_start(self, objects, entities, entity_category, entity_id):
        # Iterate through entire grid to start.
        for y in range(self.height):
            for x in range(self.width):
                # If true, the position holds something other than None or a floor.
                if not self._is_free(objects, entities, x, y):
                    continue
                # Place the player at the position in the grid and return the position.
                self.grids[entity_category][(x, y)] = {0: entity_category, 1: entity_id, 2: None}
                return (x, y)

    def _place_enemies_start(self, objects, entities, entity_category, entity_id):
        entity_positions = dict()
        # Try to place an enemy at max 100 times.
        for i in range (0, 100):
            # Select random position for the enemy.
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            # If there is something there other than floor, continue to next iteration.
            if not self._is_free(objects, entities, x, y):
                continue
            # There is a 50% chance to spawn a monster.
            if random.randint(0, 1):
                # Place the enemy at the position in the grid.
                self.grids[entity_category][(x, y)] = {0: entity_category, 1: entity_id, 2: None}
                entity_positions[(entity_category, entity_id, i)] = (x, y)
        # Return {(0, 0): (x, y), ...}
        return entity_positions

# Jafinoxal.
