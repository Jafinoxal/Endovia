# Endovia (SkillHandler)
# Copyright (C) 2010-2022 Jeremy Aaron Flexer.

from . import Constant

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
            vein_level = Constant.VEIN_LEVELS[vein_info[1]]
            if vein_level > player.skills["mining"][0]:
                return "You need a mining level of {0} to mine the {1}.              ".format(vein_level, vein_name)
            experience_gained = vein_info[9]
            chart.grids[28][(player.x + direction[0], player.y + direction[1])] = None
            player.skills["mining"] = (player.skills["mining"][0], player.skills["mining"][1] + experience_gained)
            return "You mine through the {0}! You gain {1} mining experience.            ".format(vein_name, experience_gained)
        else:
            return "You need a pick to mine the vein.                       "
    else:
        return "You should try mining a vein instead of air.                      "

def ChopTree(chart, player, direction, trees):
    if chart.grids[27][(player.x + direction[0], player.y + direction[1])] != None:
        if player.inventory[1000][1]:
            tree_info = trees[chart.grids[27][(player.x + direction[0], player.y + direction[1])][1]]
            tree_name = tree_info[2]
            tree_level = Constant.TREE_LEVELS[tree_info[1]]
            if tree_level > player.skills["forestry"][0]:
                return "You need a forestry level of {0} to chop the {1}.            ".format(tree_level, tree_name)
            experience_gained = tree_info[9]
            chart.grids[27][(player.x + direction[0], player.y + direction[1])] = None
            player.skills["forestry"] = (player.skills["forestry"][0], player.skills["forestry"][1] + experience_gained)
            return "You chop down the {0}! You gain {1} forestry experience.             ".format(tree_name, experience_gained)
        else:
            return "You need a hatchet to chop the tree.                    "
    else:
        return "You should try chopping a tree instead of air.                    "

# Jafinoxal.
