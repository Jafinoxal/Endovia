# -*- coding: utf-8 -*-
# Endovia (LevelingHandler)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _level_up_main(player):
    experience_needed = player.level * player.level * 15
    if player.experience >= experience_needed and player.level != 1000:
        player.level += 1
        return "Your main level went from {1} to {2}!".format(self.level - 1, self.level)
    else:
        return False

def _level_up_stat(player, stat):
    if stat not in player.stats.keys():
        return False
    else:
        player.stats[stat] = player.stats[stat](player.stats[stat][0], player.stats[stat][1] + 50)
        return "Your total {0} went from {1} to {2}!".format(stat, player.stats[stat][1] - 50, player.stats[stat][1])

def _level_up_attribute(player, attribute):
    if attribute not in player.attributes.keys():
        return False
    else:
        player.attributes[attribute] += 1
        return "Your {0} level went from {1} to {2}!".format(attribute, player.attributes[attribute] - 1, player.attributes[attribute])

def _level_up_skill(player, skill):
    if skill not in player.skills.keys():
        return False
    else:
        experience_needed = player.skills[skill][0] * player.skills[skill][0] * 30
        if player.skills[skill][1] >= experience_needed and player.skills[skill][0] != 100:
            player.skills[skill] = player.skills[skill](player.skills[0] + 1, player.skills[1])
            return "Your {0} level went from {1} to {2}!".format(skill, player.skills[skill][0] - 1, player.skills[0])
        else:
            return False

def LevelCharacter(player):
    messages = []
    messages.append(_level_up_main(player))
    if not messages[-1]:
        messages.pop()
    # Iterate through each skill and see if it meets the level up requirement.
    for skill in player.skills.keys():
        messages.append(_level_up_skill(player, skill))
        # If the skill returns False instead of a message remove it from messages.
        if not messages[-1]:
            messages.pop()
    return messages

# Jafinoxal.
