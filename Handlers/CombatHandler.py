# -*- coding: utf-8 -*-
# Endovia (CombatHandler)
# Copyright (C) 2010-2022 Jeremy Aaron Flexer.

import random

from . import Constant

def _attack_enemy_melee(chart, player, enemies, enemy_x, enemy_y, characters):
    # Iterate through all characters.
    for enemy in enemies.values():
        # Make sure it's the enemy we're in combat with.
        if (enemy.x, enemy.y) == (enemy_x, enemy_y):
            name = characters[enemies[enemy.unique_id].grid_id][enemies[enemy.unique_id].entity_id][2]
            damage = player.attributes["strength"] + player.skills["melee"][0]
            player.experience += damage * 5
            player.skills["melee"] = (player.skills["melee"][0], player.skills["melee"][1] + damage * 2)
            enemies[enemy.unique_id].health -= damage
            return "You punch the {0} and deal {1} damage. Enemy at ({2},{3}).                        ".format(name, damage, enemy.x, enemy.y)

def _attack_enemy_magic(chart, player, enemies, enemy_x, enemy_y, characters):
    # Iterate through all characters.
    for enemy in enemies.values():
        # Make sure it's the enemy we're in combat with.
        if (enemy.x, enemy.y) == (enemy_x, enemy_y):
            spell = Constant.DESTRUCTION_SPELLS[player.active_destruction_spell[1]][Constant.SPELLS_NAME]
            name = characters[enemies[enemy.unique_id].grid_id][enemies[enemy.unique_id].entity_id][2]
            damage = player.attributes["intelligence"] + player.skills["magic"][0] + Constant.DESTRUCTION_SPELLS[player.active_destruction_spell[1]][Constant.SPELLS_DAMAGE]
            player.experience += damage * 5
            player.skills["magic"] = (player.skills["magic"][0], player.skills["magic"][1] + damage * 2)
            enemies[enemy.unique_id].health -= damage
            return "You cast {0} on the {1} and deal {2} damage. Enemy at ({3},{4}).             ".format(spell, name, damage, enemy.x, enemy.y)

def _attack_player(chart, player, enemies, enemy_x, enemy_y, characters):
    # Iterate through all characters.
    for enemy in enemies.values():
        # Make sure it's the enemy we're in combat with.
        if (enemy.x, enemy.y) == (enemy_x, enemy_y):
            name = characters[enemies[enemy.unique_id].grid_id][enemies[enemy.unique_id].entity_id][2]
            attack = random.choice(characters[enemy.grid_id][enemy.entity_id][11])
            damage = random.randint(Constant.ATTACKS[attack][1], Constant.ATTACKS[attack][2])
            plural = Constant.ATTACKS[attack][0]
            player.stats["health"] = (player.stats["health"][0] - damage, player.stats["health"][1])
            return "The {0} {1} you and deals {2} damage. Enemy at ({3},{4}).                          ".format(name, plural, damage, enemy.x, enemy.y)

def _health_below_zero(enemies):
    # Iterate through all characters.
    for enemy in enemies.values():
        # Player health is different to access than enemy health.
        if not enemy.unique_id:
            if enemy.stats["health"][0] < 0:
                enemy.stats["health"] = (0, enemy.stats["health"][1])
        # If an enemy.
        else:
            if enemy.health < 0:
                enemy.health = 0

def _dead_entity(chart, enemies, characters):
    # Iterate through all characters.
    for enemy in enemies.values():
        # Once again accessing health in the player is different from an enemy.
        if not enemy.unique_id:
            if enemy.stats["health"][0] <= 0 and enemy.dead == False:
                enemy.dead = True
                return "You have died!                                                             "
        # If an enemy.
        else:
            if enemy.health <= 0 and enemy.dead == False:
                enemy.dead = True
                chart.grids[enemy.grid_id][(enemy.x, enemy.y)] = None
                enemy.x = None
                enemy.y = None
                return "The {0} has died!                                                          ".format(characters[enemy.grid_id][enemy.entity_id][2])
    return False

def _in_combat(chart, enemy_x, enemy_y, enemies):
    for enemy in enemies.values():
        if (enemy.x, enemy.y) == (enemy_x, enemy_y):
            return enemy.unique_id
        else:
            return 0

def DetectEnemyFight(chart, enemy_x, enemy_y, enemies):
    return _in_combat(chart, enemy_x, enemy_y, enemies),

def FightCharacter(chart, player, enemies, enemy_x, enemy_y, characters):
    messages = []
    if player.combat_style == Constant.ATTACK_MELEE:
        messages.append(_attack_enemy_melee(chart, player, enemies, enemy_x, enemy_y, characters))
    elif player.combat_style == Constant.ATTACK_RANGED:
        messages.append("Ranged combat not implemented.")
    elif player.combat_style == Constant.ATTACK_MAGIC:
        messages.append(_attack_enemy_magic(chart, player, enemies, enemy_x, enemy_y, characters))
    elif player.combat_style == Constant.ATTACK_JUTSU:
        messages.append("Jutsu combat not implemented.")
    elif player.combat_style == Constant.ATTACK_ARMS:
        messages.append("Arms combat not implemented.")
    else:
        messages.append("How did you get here? O.o")
    messages.append(_attack_player(chart, player, enemies, enemy_x, enemy_y, characters))
    _health_below_zero(enemies)
    something_died = _dead_entity(chart, enemies, characters)
    if something_died:
        messages.append(something_died)
    return messages

# Jafinoxal.
