# -*- coding: utf-8 -*-
# Endovia (DrawMenu)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def DrawBorder(library, chart_width, chart_height):
    library.console_set_char_foreground(0, 2, 2, library.Color(255, 255, 255))
    library.console_set_char_background(0, 2, 2, library.Color(0, 0, 0))
    library.console_set_char(0, 2, 0, '\xc9')
    library.console_set_char_foreground(0, 25, 2, library.Color(255, 255, 255))
    library.console_set_char_background(0, 25, 2, library.Color(0, 0, 0))
    library.console_set_char(0, 25, 0, '\xbb')
    library.console_set_char_foreground(0, 2, 10, library.Color(255, 255, 255))
    library.console_set_char_background(0, 2, 10, library.Color(0, 0, 0))
    library.console_set_char(0, 0, chart_height + 1, '\xc8')
    library.console_set_char_foreground(0, 25, 10, library.Color(255, 255, 255))
    library.console_set_char_background(0, 25, 10, library.Color(0, 0, 0))
    library.console_set_char(0, chart_width + 1, chart_height + 1, '\xbc')
    for y in range(3, 10):
        library.console_set_char_foreground(0, 2, y, library.Color(255, 255, 255))
        library.console_set_char_background(0, 2, y, library.Color(0, 0, 0))
        library.console_set_char(0, 0, y, '\xba')
        library.console_set_char_foreground(0, chart_width + 1, y, library.Color(255, 255, 255))
        library.console_set_char_background(0, chart_width + 1, y, library.Color(0, 0, 0))
        library.console_set_char(0, chart_width + 1, y, '\xba')
    for x in range(3, 25):
        library.console_set_char_foreground(0, x, 0, library.Color(255, 255, 255))
        library.console_set_char_background(0, x, 0, library.Color(0, 0, 0))
        library.console_set_char(0, x, 0, '\xcd')
        library.console_set_char_foreground(0, x, chart_height + 1, library.Color(255, 255, 255))
        library.console_set_char_background(0, x, chart_height + 1, library.Color(0, 0, 0))
        library.console_set_char(0, x, chart_height + 1, '\xcd')

# Jafinoxal.
