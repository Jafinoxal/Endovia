# Endovia (Player)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

from . import Basic

class Character(Basic.Character):
    def __init__(self, chart_id, grid_id, entity_id, unique_id, x, y, health):
        super(Character, self).__init__(chart_id, grid_id, entity_id, unique_id, x, y)
        self.dead = False
        self.health = health

# Jafinoxal
