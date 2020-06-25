# -*- coding: utf-8 -*-
# Endovia (Generators)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import random

def MainDungeonGenerator(objects, characters, chart, rooms, player_character_id, enemy_grid_id, enemy_character_ids):
    for i in range(0, 500):
        x = random.randint(1, chart.width - 11)
        x2 = random.randint(5, 10)
        y = random.randint(1, chart.height - 11)
        y2 = random.randint(5, 10)
        chart._carve_rectangular_room(x, y, x2, y2, 0)
    chart._carve_tunnels(objects, characters, 0, 0, chart.width, chart.height, 0)
    player_position = chart._place_player_start(objects, characters, 2000, player_character_id)
    character_positions = chart._place_enemies_start(objects, characters, enemy_grid_id, enemy_character_ids)
    return player_position, character_positions

# Jafinoxal.
