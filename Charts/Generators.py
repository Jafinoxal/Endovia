# -*- coding: utf-8 -*-
# Endovia (Generators)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import random

def MainDungeonGenerator(objects, chart, rooms, entity_id):
    for i in range(0, 200):
        x = random.randint(1, chart.width - 11)
        x2 = random.randint(5, 10)
        y = random.randint(1, chart.height - 11)
        y2 = random.randint(5, 10)
        chart._carve_rectangular_room(x, y, x2, y2, 0)
    chart._carve_tunnels(0, 0, chart.width, chart.height, 0)
    player_position = chart._place_character_start(objects, 2000, entity_id)
    return player_position

# Jafinoxal.
