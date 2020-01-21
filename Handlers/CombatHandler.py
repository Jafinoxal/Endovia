# -*- coding: utf-8 -*-
# Endovia (CombatHandler)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import random

import Constant

def _attack_enemy(chart, player, enemies, enemy_x, enemy_y, entities):
    for enemy in enemies:
        if (enemy.x, enemy.y) == (enemy_x, enemy_y):
            name = entities[enemies[enemy.unique_id].grid_id][enemies[enemy.unique_id].entity_id][2]
            damage = (player.attribute["strength"] + player.skill["melee"][0])
            enemies[enemy.unique_id].health -= damage
            return "You punch the {0} and deal {1} damage. Enemy at ({2},{3}).                        ".format(name, damage, enemy.x, enemy.y)

def _attack_player(chart, player, enemies, enemy_x, enemy_y, entities):
    for enemy in enemies:
        if (enemy.x, enemy.y) == (enemy_x, enemy_y):
            name = entities[enemies[enemy.unique_id].grid_id][enemies[enemy.unique_id].entity_id][2]
            attack = random.choice(entities[enemies[enemy.unique_id].grid_id][enemies[enemy.unique_id].entity_id][11])
            damage = random.randint(Constant.ATTACKS[attack][1], Constant.ATTACKS[attack][2])
            plural = Constant.ATTACKS[attack][0]
            player.stats["health"] -= damage
            return "The {0} {1} you and deals {2} damage. Enemy at ({3},{4}.                          )".format(name, plural, damage, enemy.x, enemy.y)

def FightCharacter(chart, player, enemies, enemy_x, enemy_y, entities):
    messages = []
    messages.append(_attack_enemy(chart, player, enemies, enemy_x, enemy_y, entities))
    messages.append(_attack_player(chart, player, enemies, enemy_x, enemy_y, entities))
    return messages

# Jafinoxal.
