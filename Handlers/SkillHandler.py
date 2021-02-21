# Endovia (SkillHandler)
# Copyright (C) 2010-2021 Jeremy Aaron Flexer.

def BreakWall(chart, player, direction):
    if chart.grids[0][(player.x + direction[0], player.y + direction[1])] != None:
        chart.grids[0][(player.x + direction[0], player.y + direction[1])] = None
        player.skills["mining"] = (player.skills["mining"][0], player.skills["mining"][1] + 5)
        return "You break through the wall! You gain 5 mining experience."
    else:
        return "You should try breaking a wall instead of air."
