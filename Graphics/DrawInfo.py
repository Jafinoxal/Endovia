# -*- coding: utf-8 -*-
# Endovia (DrawInfo)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def DrawStats(library, chart, player):
    title_to_draw = "+STATS+"
    name_to_draw = " Name: {0}".format(player.name)
    race_to_draw = " Race: {0}".format(player.race)
    level_to_draw = " Level: {0}".format(player.level)
    health_to_draw = " Health: {0}/{1}".format(player.stats["health"][0], player.stats["health"][1])
    mana_to_draw = " Mana: {0}/{1}".format(player.stats["mana"][0], player.stats["mana"][1])
    energy_to_draw = " Energy: {0}/{1}".format(player.stats["energy"][0], player.stats["energy"][1])
    to_draw_complete = (
    title_to_draw,
    name_to_draw,
    race_to_draw,
    level_to_draw,
    health_to_draw,
    mana_to_draw,
    energy_to_draw
    )
    for y in range(0, len(to_draw_complete)):
        for x in range(0, len(to_draw_complete[y])):
            library.console_set_char_foreground(0, x + chart.width + 2, y, library.Color(255, 255, 255))
            library.console_set_char_background(0, x + chart.width + 2, y, library.Color(0, 0, 0))
            library.console_set_char(0, x + chart.width + 2, y, to_draw_complete[y][x])

def DrawAttributes(library, chart, player):
    title_to_draw = "+ATTRIBUTES+"
    to_draw_complete = [title_to_draw,]
    for attribute_to_draw_name, attribute_to_draw_value in player.attributes.items():
        to_draw_complete.append(" {0}: {1}".format(attribute_to_draw_name, attribute_to_draw_value))
    for y in range(0, len(to_draw_complete)):
        for x in range(0, len(to_draw_complete[y])):
            library.console_set_char_foreground(0, x + chart.width + 2, y + 7, library.Color(255, 255, 255))
            library.console_set_char_background(0, x + chart.width + 2, y + 7, library.Color(0, 0, 0))
            library.console_set_char(0, x + chart.width + 2, y + 7, to_draw_complete[y][x])

def DrawSkills(library, chart, player):
    title_to_draw = "+SKILLS+"
    to_draw_complete = [title_to_draw,]
    for attribute_to_draw_name, attribute_to_draw_value in player.skills.items():
        to_draw_complete.append(" {0}: {1}".format(attribute_to_draw_name, attribute_to_draw_value[0]))
    for y in range(0, len(to_draw_complete)):
        for x in range(0, len(to_draw_complete[y])):
            library.console_set_char_foreground(0, x + chart.width + 2, y + 17, library.Color(255, 255, 255))
            library.console_set_char_background(0, x + chart.width + 2, y + 17, library.Color(0, 0, 0))
            library.console_set_char(0, x + chart.width + 2, y + 17, to_draw_complete[y][x])

# Jafinoxal.
