# -*- coding: utf-8 -*-
# Endovia (DrawDeath)
# Copyright (C) 2010-2022 Jeremy Aaron Flexer.

import random

def DrawWindow(console, screen_width, screen_height):
    for y in range(0, screen_height):
        for x in range(0, screen_width):
            console.print(x=x, y=y, string=random.choice(('?','!')), fg=(255,255,255), bg=(0,0,0))

def DrawMessage(console):
    death_message = "Oh dear, you have died!"
    for x in range(1, len(death_message) + 1):
        console.print(x=x, y=1, string=death_message[x-1], fg=(255,255,255), bg=(0,0,0))

# Jafinoxal.
