# -*- coding: utf-8 -*-
# Endovia (CombatHandler)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import random

import Constant

def _attack_enemy(chart, player, enemies, enemy_x, enemy_y, entities):
    # Iterate through all characters.
    for enemy in enemies.values():
        # Make sure it's the enemy we're in combat with.
        if (enemy.x, enemy.y) == (enemy_x, enemy_y):
            name = entities[enemies[enemy.unique_id].grid_id][enemies[enemy.unique_id].entity_id][2]
            damage = (player.attributes["strength"] + player.skills["melee"][0])
            player.experience += damage * 5
            enemies[enemy.unique_id].health -= damage
            return "You punch the {0} and deal {1} damage. Enemy at ({2},{3}).                        ".format(name, damage, enemy.x, enemy.y)

def _attack_player(chart, player, enemies, enemy_x, enemy_y, entities):
    # Iterate through all characters.
    for enemy in enemies.values():
        # Make sure it's the enemy we're in combat with.
        if (enemy.x, enemy.y) == (enemy_x, enemy_y):
            name = entities[enemies[enemy.unique_id].grid_id][enemies[enemy.unique_id].entity_id][2]
            attack = random.choice(entities[enemies[enemy.unique_id].grid_id][enemies[enemy.unique_id].entity_id][11])
            damage = random.randint(Constant.ATTACKS[attack][1], Constant.ATTACKS[attack][2])
            plural = Constant.ATTACKS[attack][0]
            player.stats["health"] = (player.stats["health"][0] - damage, player.stats["health"][1])
            return "The {0} {1} you and deals {2} damage. Enemy at ({3},{4}).                          ".format(name, plural, damage, enemy.x, enemy.y)

def _health_below_zero(characters):
    # Iterate through all characters.
    for character in characters.values():
        # Player health is different to access than enemy health.
        if not character.unique_id:
            if character.stats["health"][0] < 0:
                character.stats["health"] = (0, character.stats["health"][1])
        # If an enemy.
        else:
            if character.health < 0:
                character.health = 0

def _dead_character(chart, characters, entities):
    # Iterate through all characters.
    for character in characters.values():
        # Once again accessing health in the player is different from an enemy.
        if not character.unique_id:
            if character.stats["health"] <= 0 and character.dead == False:
                character.dead = True
                return "You have died!                                                             "
        # If an enemy.
        else:
            if character.health <= 0 and character.dead == False:
                character.dead = True
                chart.grids[character.grid_id][(character.x, character.y)] = None
                character.x = None
                character.y = None
                return "The {0} has died!                                                          ".format(entities[characters[character.unique_id].grid_id][characters[character.unique_id].entity_id][2])
    return False

def FightCharacter(chart, player, characters, enemy_x, enemy_y, entities):
    messages = []
    messages.append(_attack_enemy(chart, player, characters, enemy_x, enemy_y, entities))
    messages.append(_attack_player(chart, player, characters, enemy_x, enemy_y, entities))
    _health_below_zero(characters)
    something_died = _dead_character(chart, characters, entities)
    if something_died:
        messages.append(something_died)
    return messages

# Jafinoxal.
