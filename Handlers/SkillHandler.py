# Endovia (SkillHandler)
# Copyright (C) 2010-2021 Jeremy Aaron Flexer.

def BreakWall(chart, player, direction):
    if chart.grids[0][(player.x + direction[0], player.y + direction[1])] != None:
        if player.inventory[1000][0]:
            chart.grids[0][(player.x + direction[0], player.y + direction[1])] = None
            player.skills["mining"] = (player.skills["mining"][0], player.skills["mining"][1] + 4)
            return "You break through the wall! You gain 4 mining experience.            "
        else:
            return "You need a pick to break the wall.               "
    else:
        return "You should try breaking a wall instead of air.            "

def MineVein(chart, player, direction, veins):
    if chart.grids[28][(player.x + direction[0], player.y + direction[1])] != None:
        if player.inventory[1000][0]:
            vein_info = veins[chart.grids[28][(player.x + direction[0], player.y + direction[1])][1]]
            vein_name = vein_info[2]
            experience_gained = vein_info[9]
            chart.grids[28][(player.x + direction[0], player.y + direction[1])] = None
            player.skills["mining"] = (player.skills["mining"][0], player.skills["mining"][1] + experience_gained)
            return "You mine through the {0}! You gain {1} mining experience.            ".format(vein_name, experience_gained)
        else:
            return "You need a pick to mine the vein.                       "
    else:
        return "You should try mining a vein instead of air.                      "

# Jafinoxal.
