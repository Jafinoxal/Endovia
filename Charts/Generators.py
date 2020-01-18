# -*- coding: utf-8 -*-
# Endovia (Generators)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import random

def MainDungeonGenerator(objects, entities, chart, rooms, player_entity_id, enemy_entity_id):
    for i in range(0, 200):
        x = random.randint(1, chart.width - 11)
        x2 = random.randint(5, 10)
        y = random.randint(1, chart.height - 11)
        y2 = random.randint(5, 10)
        chart._carve_rectangular_room(x, y, x2, y2, 0)
    chart._carve_tunnels(0, 0, chart.width, chart.height, 0)
    player_position = chart._place_player_start(objects, entities, 2000, player_entity_id)
    entity_positions = chart._place_enemies_start(objects, entities, 2001, enemy_entity_id)
    return player_position, entity_positions

# Jafinoxal.
