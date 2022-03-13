# -*- coding: utf-8 -*-
# Endovia (DrawInfo)
# Copyright (C) 2010-2022 Jeremy Aaron Flexer.

def DrawStats(console, chart, player):
    title_to_draw = " Ω STATS Ω"
    name_to_draw = " Name:   {0}".format(player.name)
    race_to_draw = " Race:   {0}".format(player.race)
    level_to_draw = " Level:  {0}:{1}/{2}          ".format(player.level, player.experience, player.level * player.level * 15)
    health_to_draw = " Health: {0}/{1}   ".format(player.stats["health"][0], player.stats["health"][1])
    mana_to_draw = " Mana:   {0}/{1}   ".format(player.stats["mana"][0], player.stats["mana"][1])
    energy_to_draw = " Energy: {0}/{1}   ".format(player.stats["energy"][0], player.stats["energy"][1])
    faith_to_draw = " Faith:  {0}/{1}   ".format(player.stats["faith"][0], player.stats["faith"][1])
    chakra_to_draw = " Chakra: {0}/{1}   ".format(player.stats["chakra"][0], player.stats["chakra"][1])
    to_draw_complete = (
    title_to_draw,
    name_to_draw,
    race_to_draw,
    level_to_draw,
    health_to_draw,
    mana_to_draw,
    energy_to_draw,
    faith_to_draw,
    chakra_to_draw,
    )
    for y in range(0, len(to_draw_complete)):
        for x in range(0, len(to_draw_complete[y])):
            console.print(x=x + chart.width + 2, y=y, string=to_draw_complete[y][x], fg=(255,255,255), bg=(0,0,0))

def DrawAttributes(console, chart, player):
    title_to_draw = " Ω ATTRIBUTES Ω"
    attack_to_draw = " attack:       {0}".format(player.attributes["attack"])
    defense_to_draw = " defense:      {0}".format(player.attributes["defense"])
    strength_to_draw = " strength:     {0}".format(player.attributes["strength"])
    endurance_to_draw = " endurance:    {0}".format(player.attributes["endurance"])
    dexterity_to_draw = " dexterity:    {0}".format(player.attributes["dexterity"])
    agility_to_draw = " agility:      {0}".format(player.attributes["agility"])
    perception_to_draw = " perception:   {0}".format(player.attributes["perception"])
    intelligence_to_draw = " intelligence: {0}".format(player.attributes["intelligence"])
    charisma_to_draw = " charisma:     {0}".format(player.attributes["charisma"])
    luck_to_draw = " luck:         {0}".format(player.attributes["luck"])
    to_draw_complete = (
    title_to_draw,
    attack_to_draw,
    defense_to_draw,
    strength_to_draw,
    endurance_to_draw,
    dexterity_to_draw,
    agility_to_draw,
    perception_to_draw,
    intelligence_to_draw,
    charisma_to_draw,
    luck_to_draw,
    )
    for y in range(0, len(to_draw_complete)):
        for x in range(0, len(to_draw_complete[y])):
            console.print(x=x + chart.width + 2, y=y + 9, string=to_draw_complete[y][x], fg=(255,255,255), bg=(0,0,0))

def DrawSkills(console, chart, player):
    title_to_draw = " Ω SKILLS Ω"
    melee_to_draw = " melee:        {0}:{1}/{2}                      ".format(player.skills["melee"][0], player.skills["melee"][1], player.skills["melee"][0] * player.skills["melee"][0] * 30)
    ranged_to_draw = " ranged:       {0}:{1}/{2}                     ".format(player.skills["ranged"][0], player.skills["ranged"][1], player.skills["ranged"][0] * player.skills["ranged"][0] * 30)
    magic_to_draw = " magic:        {0}:{1}/{2}                      ".format(player.skills["magic"][0], player.skills["magic"][1], player.skills["magic"][0] * player.skills["magic"][0] * 30)
    gunning_to_draw = " gunning:      {0}:{1}/{2}                      ".format(player.skills["gunning"][0], player.skills["gunning"][1], player.skills["gunning"][0] * player.skills["gunning"][0] * 30)
    prayer_to_draw = " prayer:       {0}:{1}/{2}                     ".format(player.skills["prayer"][0], player.skills["prayer"][1], player.skills["prayer"][0] * player.skills["prayer"][0] * 30)
    speech_to_draw = " speech:       {0}:{1}/{2}                      ".format(player.skills["speech"][0], player.skills["speech"][1], player.skills["speech"][0] * player.skills["speech"][0] * 30)
    barter_to_draw = " barter:       {0}:{1}/{2}                      ".format(player.skills["barter"][0], player.skills["barter"][1], player.skills["barter"][0] * player.skills["barter"][0] * 30)
    thieving_to_draw = " thieving:     {0}:{1}/{2}                      ".format(player.skills["thieving"][0], player.skills["thieving"][1], player.skills["thieving"][0] * player.skills["thieving"][0] * 30)
    forestry_to_draw = " forestry:     {0}:{1}/{2}                     ".format(player.skills["forestry"][0], player.skills["forestry"][1], player.skills["forestry"][0] * player.skills["forestry"][0] * 30)
    kindling_to_draw = " kindling:     {0}:{1}/{2}                      ".format(player.skills["kindling"][0], player.skills["kindling"][1], player.skills["kindling"][0] * player.skills["kindling"][0] * 30)
    fletching_to_draw = " fletching:    {0}:{1}/{2}                      ".format(player.skills["fletching"][0], player.skills["fletching"][1], player.skills["fletching"][0] * player.skills["fletching"][0] * 30)
    mining_to_draw = " mining:       {0}:{1}/{2}                     ".format(player.skills["mining"][0], player.skills["mining"][1], player.skills["mining"][0] * player.skills["mining"][0] * 30)
    smithing_to_draw = " smithing:     {0}:{1}/{2}                      ".format(player.skills["smithing"][0], player.skills["smithing"][1], player.skills["smithing"][0] * player.skills["smithing"][0] * 30)
    crafting_to_draw = " crafting:     {0}:{1}/{2}                      ".format(player.skills["crafting"][0], player.skills["crafting"][1], player.skills["crafting"][0] * player.skills["crafting"][0] * 30)
    fishing_to_draw = " fishing:      {0}:{1}/{2}                      ".format(player.skills["fishing"][0], player.skills["fishing"][1], player.skills["fishing"][0] * player.skills["fishing"][0] * 30)
    cooking_to_draw = " cooking:      {0}:{1}/{2}                      ".format(player.skills["cooking"][0], player.skills["cooking"][1], player.skills["cooking"][0] * player.skills["cooking"][0] * 30)
    hunter_to_draw = " hunter:       {0}:{1}/{2}                      ".format(player.skills["hunter"][0], player.skills["hunter"][1], player.skills["hunter"][0] * player.skills["hunter"][0] * 30)
    construction_to_draw = " construction: {0}:{1}/{2}                      ".format(player.skills["construction"][0], player.skills["construction"][1], player.skills["construction"][0] * player.skills["construction"][0] * 30)
    summoning_to_draw = " summoning:    {0}:{1}/{2}                      ".format(player.skills["summoning"][0], player.skills["summoning"][1], player.skills["summoning"][0] * player.skills["summoning"][0] * 30)
    alchemy_to_draw = " alchemy:      {0}:{1}/{2}                      ".format(player.skills["alchemy"][0], player.skills["alchemy"][1], player.skills["alchemy"][0] * player.skills["alchemy"][0] * 30)
    to_draw_complete = (
    title_to_draw,
    melee_to_draw,
    ranged_to_draw,
    magic_to_draw,
    gunning_to_draw,
    prayer_to_draw,
    speech_to_draw,
    barter_to_draw,
    thieving_to_draw,
    forestry_to_draw,
    kindling_to_draw,
    fletching_to_draw,
    mining_to_draw,
    smithing_to_draw,
    crafting_to_draw,
    fishing_to_draw,
    cooking_to_draw,
    hunter_to_draw,
    construction_to_draw,
    summoning_to_draw,
    alchemy_to_draw,
    )
    for y in range(0, len(to_draw_complete)):
        for x in range(0, len(to_draw_complete[y])):
            console.print(x=x + chart.width + 2, y=y + 20, string=to_draw_complete[y][x], fg=(255,255,255), bg=(0,0,0))

def DrawLocation(console, chart, player):
    title_to_draw = " Ω LOCATION Ω"
    location_to_draw = " Map: {0}   ".format(chart.id)
    x_to_draw = " X:   {0}   ".format(player.x)
    y_to_draw = " Y:   {0}   ".format(player.y)
    to_draw_complete = (
    title_to_draw,
    location_to_draw,
    x_to_draw,
    y_to_draw,
    )
    for y in range(0, len(to_draw_complete)):
        for x in range(0, len(to_draw_complete[y])):
            console.print(x=x + chart.width + 2, y=y + 41, string=to_draw_complete[y][x], fg=(255,255,255), bg=(0,0,0))

def DrawEnemy(console, chart, enemies, enemy_x, enemy_y):
    # Find the enemy.
    for enemy in enemies.values():
        if (enemy_x, enemy_y) == (enemy.x, enemy.y):
            title_to_draw = " Ω ENEMY Ω"
            health_to_draw = " Health: {0}      ".format(enemy.health)
            location_to_draw = " Map:    {0}   ".format(chart.id)
            x_to_draw = " X:      {0}   ".format(enemy_x)
            y_to_draw = " Y:      {0}   ".format(enemy_y)
            to_draw_complete = (
            title_to_draw,
            health_to_draw,
            location_to_draw,
            x_to_draw,
            y_to_draw,
            )
            for y in range(0, len(to_draw_complete)):
                for x in range(0, len(to_draw_complete[y])):
                    console.print(x=x + chart.width + 2, y=y + 45, string=to_draw_complete[y][x], fg=(255,255,255), bg=(0,0,0))
            break
        else:
            title_to_draw = " Ω ENEMY Ω"
            health_to_draw = " Health: None"
            location_to_draw = " Map:    {0}   ".format(chart.id)
            x_to_draw = " X:      None"
            y_to_draw = " Y:      None"
            to_draw_complete = (
            title_to_draw,
            health_to_draw,
            location_to_draw,
            x_to_draw,
            y_to_draw,
            )
            for y in range(0, len(to_draw_complete)):
                for x in range(0, len(to_draw_complete[y])):
                    console.print(x=x + chart.width + 2, y=y + 45, string=to_draw_complete[y][x], fg=(255,255,255), bg=(0,0,0))
            break

def DrawMagic(console, chart, player, destruction_spell_info, restoration_spell_info):
    title_to_draw =  " Ω MAGIC Ω"
    destruction_spell_to_draw = " <DES>:  {0}".format(destruction_spell_info[0])
    restoration_spell_to_draw = " <RES>:  {0}".format(restoration_spell_info[0])
    to_draw_complete = (
    title_to_draw,
    destruction_spell_to_draw,
    restoration_spell_to_draw,
    )
    for y in range(0, len(to_draw_complete)):
        for x in range(0, len(to_draw_complete[y])):
            console.print(x=x + chart.width + 2, y=y + 50, string=to_draw_complete[y][x], fg=(255,255,255), bg=(0,0,0))

def DrawCombat(console, chart, player, combat_styles):
    title_to_draw = " Ω COMBAT Ω"
    style_to_draw = " Style: {0}".format(combat_styles[player.combat_style])
    to_draw_complete = (
    title_to_draw,
    style_to_draw,
    )
    for y in range(0, len(to_draw_complete)):
        for x in range(0, len(to_draw_complete[y])):
            console.print(x=x + chart.width + 2, y=y + 53, string=to_draw_complete[y][x], fg=(255,255,255), bg=(0,0,0))

def DrawMessages(console, messages, chart):
    message_count = len(messages)
    if message_count > 10:
        message_count = 10
    for message_index in range(1, message_count + 1):
        for x in range(0, len(messages[-message_index])):
            console.print(x=x, y=message_index + chart.height + 1, string=messages[-message_index][x], fg=(255,255,255), bg=(0,0,0))

# Jafinoxal.
