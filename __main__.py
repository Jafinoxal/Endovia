#!/usr/bin/env python
# Endovia (Test)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.


import Objects

import pygame

pygame.init()
screen = pygame.display.set_mode((800,640))
background = pygame.Surface(screen.get_size())
background.fill((0,0,0))
background = background.convert()

dungeons = {
0: cha.ChartDungeon(80, 50, True),
}

# Dungeon generation.
dungeons[0].create_filled_grid(80, 50, (0, 0))
dungeons[0].create_filled_grid(80, 50, (1, 0))

import random
for i in range(0, 200):
    x = random.randint(1, dungeons[0].chart_width - 11)
    x2 = random.randint(5, 10)
    y = random.randint(1, dungeons[0].chart_height - 11)
    y2 = random.randint(5, 10)
    dungeons[0].carve_rectangular_room(x, y, x2, y2, (0, 0))
#dungeons[0].carve_rectangular_room(20, 15, 10, 10, (0, 0))
#dungeons[0].carve_rectangular_room(50, 15, 10, 10, (0, 0))
#dungeons[0].carve_horizontal_tunnel(25, 55, 20, (0, 0))

charts = {
0: dungeons,
}

while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(0, libtcod.white)
    graphics[0][0].draw_charts(objects, charts)
    graphics[0][0].draw_players(objects, entities[0])
    libtcod.console_flush()
    exit = handle_keys(objects, graphics, charts, entities[0][0])
    if exit:
        break
