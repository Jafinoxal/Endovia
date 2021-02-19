# -*- coding: utf-8 -*-
# Endovia (DrawChart)
# Copyright (C) 2010-2021 Jeremy Aaron Flexer.

import random

def DrawWindow(library, screen_width, screen_height):
    for y in range(0, screen_height):
        for x in range(0, screen_width):
            library.console_set_char_foreground(0, x, y, library.Color(255, 255, 255))
            library.console_set_char_background(0, x, y, library.Color(0, 0, 0))
            library.console_set_char(0, x, y, random.choice(('?', '!')))

def DrawMessage(library):
    death_message = "Oh dear, you have died!"
    for x in range(1, len(death_message) + 1):
            library.console_set_char_foreground(0, x, 1, library.Color(255, 255, 255))
            library.console_set_char_background(0, x, 1, library.Color(0, 0, 0))
            library.console_set_char(0, x, 1, death_message[x -1])
