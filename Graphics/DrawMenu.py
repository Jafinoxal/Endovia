# -*- coding: utf-8 -*-
# Endovia (DrawMenu)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def DrawBorderStatChoice(console):
    console.print(x=2, y=2, string='╔', fg=(255,255,255), bg=(0,0,0))
    console.print(x=27, y=2, string='╗', fg=(255,255,255), bg=(0,0,0))
    console.print(x=2, y=9, string='╚', fg=(255,255,255), bg=(0,0,0))
    console.print(x=27, y=9, string='╝', fg=(255,255,255), bg=(0,0,0))
    for y in range(3, 9):
        console.print(x=2, y=y, string='║', fg=(255,255,255), bg=(0,0,0))
        console.print(x=27, y=y, string='║', fg=(255,255,255), bg=(0,0,0))
    for x in range(3, 27):
        console.print(x=x, y=2, string='═', fg=(255,255,255), bg=(0,0,0))
        console.print(x=x, y=9, string='═', fg=(255,255,255), bg=(0,0,0))

def DrawBorderCombatChoice(console):
    console.print(x=2, y=2, string='╔', fg=(255,255,255), bg=(0,0,0))
    console.print(x=25, y=2, string='╗', fg=(255,255,255), bg=(0,0,0))
    console.print(x=2, y=9, string='╚', fg=(255,255,255), bg=(0,0,0))
    console.print(x=25, y=9, string='╝', fg=(255,255,255), bg=(0,0,0))
    for y in range(3, 9):
        console.print(x=2, y=y, string='║', fg=(255,255,255), bg=(0,0,0))
        console.print(x=25, y=y, string='║', fg=(255,255,255), bg=(0,0,0))
    for x in range(3, 25):
        console.print(x=x, y=2, string='═', fg=(255,255,255), bg=(0,0,0))
        console.print(x=x, y=9, string='═', fg=(255,255,255), bg=(0,0,0))

def DrawBorderInventoryChoice(console):
    console.print(x=2, y=2, string='╔', fg=(255,255,255), bg=(0,0,0))
    console.print(x=40, y=2, string='╗', fg=(255,255,255), bg=(0,0,0))
    console.print(x=2, y=69, string='╚', fg=(255,255,255), bg=(0,0,0))
    console.print(x=40, y=69, string='╝', fg=(255,255,255), bg=(0,0,0))
    for y in range(3, 69):
        console.print(x=2, y=y, string='║', fg=(255,255,255), bg=(0,0,0))
        console.print(x=40, y=y, string='║', fg=(255,255,255), bg=(0,0,0))
    for x in range(3, 40):
        console.print(x=x, y=2, string='═', fg=(255,255,255), bg=(0,0,0))
        console.print(x=x, y=69, string='═', fg=(255,255,255), bg=(0,0,0))

def DrawBorderMagicChoice(console):
    console.print(x=2, y=2, string='╔', fg=(255,255,255), bg=(0,0,0))
    console.print(x=40, y=2, string='╗', fg=(255,255,255), bg=(0,0,0))
    console.print(x=2, y=69, string='╚', fg=(255,255,255), bg=(0,0,0))
    console.print(x=40, y=69, string='╝', fg=(255,255,255), bg=(0,0,0))
    for y in range(3, 69):
        console.print(x=2, y=y, string='║', fg=(255,255,255), bg=(0,0,0))
        console.print(x=40, y=y, string='║', fg=(255,255,255), bg=(0,0,0))
    for x in range(3, 40):
        console.print(x=x, y=2, string='═', fg=(255,255,255), bg=(0,0,0))
        console.print(x=x, y=69, string='═', fg=(255,255,255), bg=(0,0,0))

def DrawFillerStatChoice(console):
    for y in range(3, 9):
        for x in range(3, 25):
            console.print(x=x, y=y, string=' ', fg=(255,255,255), bg=(0,0,0))

def DrawFillerCombatChoice(console):
    for y in range(3, 9):
        for x in range(3, 25):
            console.print(x=x, y=y, string=' ', fg=(255,255,255), bg=(0,0,0))

def DrawFillerInventoryChoice(console):
    for y in range(3, 69):
        for x in range(3, 40):
            console.print(x=x, y=y, string=' ', fg=(255,255,255), bg=(0,0,0))

def DrawFillerMagicChoice(console):
    for y in range(3, 69):
        for x in range(3, 40):
            console.print(x=x, y=y, string=' ', fg=(255,255,255), bg=(0,0,0))


def DrawStatChoice(console, choice):
    choices = {
    0: "+ Choose Stat Increase +",
    1: " Health    ",
    2: " Mana    ",
    3: " Energy    ",
    4: " Faith    ",
    5: " Chakra    ",
    }
    if choice == 0:
        choices[1] = " [Health]"
    elif choice == 1:
        choices[2] = " [Mana]"
    elif choice == 2:
        choices[3] = " [Energy]"
    elif choice == 3:
        choices[4] = " [Faith]"
    elif choice == 4:
        choices[5] = " [Chakra]"
    else:
        return False
    for key, value in choices.items():
        for index in range(0, len(value)):
            console.print(x=3 + index, y=3 + key, string=value[index], fg=(255,255,255), bg=(0,0,0))

def DrawCombatChoice(console, choice):
    choices = {
    0: "+ Choose Combat Style +",
    1: " Melee     ",
    2: " Ranged   ",
    3: " Magic     ",
    4: " Jutsu    ",
    5: " Arms    ",
    }
    if choice == 0:
        choices[1] = " [Melee]"
    elif choice == 1:
        choices[2] = " [Ranged]"
    elif choice == 2:
        choices[3] = " [Magic]"
    elif choice == 3:
        choices[4] = " [Jutsu]"
    elif choice == 4:
        choices[5] = " [Arms]"
    else:
        return False
    for key, value in choices.items():
        for index in range(0, len(value)):
            console.print(x=3 + index, y=3 + key, string=value[index], fg=(255,255,255), bg=(0,0,0))

def DrawInventoryChoice(console, choice, inventory, items):
    category_type = items[choice[0]][choice[1]][3]
    selected_item = items[choice[0]][choice[1]][1]
    choices = {0: "+ Inventory +     ",
              1: "= {0} =    ".format(category_type),
              }
    item_index = 0
    for item_id, item_amount in inventory[choice[0]].items():
        if item_id == selected_item:
            if item_amount > 0:
                choices[2 + item_index] = " [{0}] x{1}      ".format(items[choice[0]][item_id][2], inventory[choice[0]][item_id])
            else:
                choices[2 + item_index] = " [Empty]"
        else:
            if item_amount > 0:
                choices[2 + item_index] = " {0} x{1}      ".format(items[choice[0]][item_id][2], inventory[choice[0]][item_id])
            else:
                choices[2 + item_index] = " Empty"
        item_index += 1
    for key, value in choices.items():
        for index in range(0, len(value)):
            console.print(x=3 + index, y=3 + key, string=value[index], fg=(255,255,255), bg=(0,0,0))

def DrawMagicChoice(console, choice, destruction_spells, restoration_spells, player):
    category_type = choice[0]
    selected_spell = choice[1]
    if category_type not in ("destruction", "restoration"):
        return 1
    choices = {0: "+ Magic +     ",
              1: "= {0} =    ".format(category_type),
              }
    spell_index = 0
    if category_type == "destruction":
        for spell_id, spell_info in destruction_spells.items():
            if spell_id == selected_spell:
                if player.skills["magic"][0] >= spell_info[1]:
                    choices[2 + spell_index] = " [{0}] (LVL:{1})     ".format(spell_info[0], spell_info[1])
                else:
                    choices[2 + spell_index] = " [Unknown]"
            else:
                if player.skills["magic"][0] >= spell_info[1]:
                    choices[2 + spell_index] = " {0} (LVL:{1})     ".format(spell_info[0], spell_info[1])
                else:
                    choices[2 + spell_index] = " Unknown"
            spell_index += 1
    if category_type == "restoration":
        for spell_id, spell_info in restoration_spells.items():
            if spell_id == selected_spell:
                if player.skills["magic"][0] >= spell_info[1]:
                    choices[2 + spell_index] = " [{0}] (LVL:{1})     ".format(spell_info[0], spell_info[1])
                else:
                    choices[2 + spell_index] = " [Unknown]"
            else:
                if player.skills["magic"][0] >= spell_info[1]:
                    choices[2 + spell_index] = " {0} (LVL:{1})     ".format(spell_info[0], spell_info[1])
                else:
                    choices[2 + spell_index] = " Unknown"
            spell_index += 1
    for key, value in choices.items():
        for index in range(0, len(value)):
            console.print(x=3 + index, y=3 + key, string=value[index], fg=(255,255,255), bg=(0,0,0))

def DrawMainMenu(console, choice):
    choices = {
    0: "Endovia /Alpha/",
    1: " New           ",
    2: " Load           ",
    3: " Construct        ",
    4: " Credits          ",
    5: " Exit           ",
    }
    if choice == 0:
        choices[1] = " [New]"
    elif choice == 1:
        choices[2] = " [Load]"
    elif choice == 2:
        choices[3] = " [Construct]"
    elif choice == 3:
        choices[4] = " [Credits]"
    elif choice == 4:
        choices[5] = " [Exit]"
    else:
        return False
    for key, value in choices.items():
        for index in range(0, len(value)):
            console.print(x=1 + index, y=1 + key, string=value[index], fg=(255,255,255), bg=(0,0,0))

# Jafinoxal.
