# -*- coding: utf-8 -*-
# Endovia (DrawMenu)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def DrawBorderStatChoice(library):
    library.console_set_char_foreground(0, 2, 2, library.Color(255, 255, 255))
    library.console_set_char_background(0, 2, 2, library.Color(0, 0, 0))
    library.console_set_char(0, 2, 2, '\xc9')
    library.console_set_char_foreground(0, 25, 2, library.Color(255, 255, 255))
    library.console_set_char_background(0, 25, 2, library.Color(0, 0, 0))
    library.console_set_char(0, 25, 2, '\xbb')
    library.console_set_char_foreground(0, 2, 9, library.Color(255, 255, 255))
    library.console_set_char_background(0, 2, 9, library.Color(0, 0, 0))
    library.console_set_char(0, 2, 9, '\xc8')
    library.console_set_char_foreground(0, 25, 9, library.Color(255, 255, 255))
    library.console_set_char_background(0, 25, 9, library.Color(0, 0, 0))
    library.console_set_char(0, 25, 9, '\xbc')
    for y in range(3, 9):
        library.console_set_char_foreground(0, 2, y, library.Color(255, 255, 255))
        library.console_set_char_background(0, 2, y, library.Color(0, 0, 0))
        library.console_set_char(0, 2, y, '\xba')
        library.console_set_char_foreground(0, 25, y, library.Color(255, 255, 255))
        library.console_set_char_background(0, 25, y, library.Color(0, 0, 0))
        library.console_set_char(0, 25, y, '\xba')
    for x in range(3, 25):
        library.console_set_char_foreground(0, x, 2, library.Color(255, 255, 255))
        library.console_set_char_background(0, x, 2, library.Color(0, 0, 0))
        library.console_set_char(0, x, 2, '\xcd')
        library.console_set_char_foreground(0, x, 9, library.Color(255, 255, 255))
        library.console_set_char_background(0, x, 9, library.Color(0, 0, 0))
        library.console_set_char(0, x, 9, '\xcd')

def DrawBorderCombatChoice(library):
    library.console_set_char_foreground(0, 2, 2, library.Color(255, 255, 255))
    library.console_set_char_background(0, 2, 2, library.Color(0, 0, 0))
    library.console_set_char(0, 2, 2, '\xc9')
    library.console_set_char_foreground(0, 25, 2, library.Color(255, 255, 255))
    library.console_set_char_background(0, 25, 2, library.Color(0, 0, 0))
    library.console_set_char(0, 25, 2, '\xbb')
    library.console_set_char_foreground(0, 2, 9, library.Color(255, 255, 255))
    library.console_set_char_background(0, 2, 9, library.Color(0, 0, 0))
    library.console_set_char(0, 2, 9, '\xc8')
    library.console_set_char_foreground(0, 25, 9, library.Color(255, 255, 255))
    library.console_set_char_background(0, 25, 9, library.Color(0, 0, 0))
    library.console_set_char(0, 25, 9, '\xbc')
    for y in range(3, 9):
        library.console_set_char_foreground(0, 2, y, library.Color(255, 255, 255))
        library.console_set_char_background(0, 2, y, library.Color(0, 0, 0))
        library.console_set_char(0, 2, y, '\xba')
        library.console_set_char_foreground(0, 25, y, library.Color(255, 255, 255))
        library.console_set_char_background(0, 25, y, library.Color(0, 0, 0))
        library.console_set_char(0, 25, y, '\xba')
    for x in range(3, 25):
        library.console_set_char_foreground(0, x, 2, library.Color(255, 255, 255))
        library.console_set_char_background(0, x, 2, library.Color(0, 0, 0))
        library.console_set_char(0, x, 2, '\xcd')
        library.console_set_char_foreground(0, x, 9, library.Color(255, 255, 255))
        library.console_set_char_background(0, x, 9, library.Color(0, 0, 0))
        library.console_set_char(0, x, 9, '\xcd')

def DrawBorderInventoryChoice(library):
    library.console_set_char_foreground(0, 2, 2, library.Color(255, 255, 255))
    library.console_set_char_background(0, 2, 2, library.Color(0, 0, 0))
    library.console_set_char(0, 2, 2, '\xc9')
    library.console_set_char_foreground(0, 40, 2, library.Color(255, 255, 255))
    library.console_set_char_background(0, 40, 2, library.Color(0, 0, 0))
    library.console_set_char(0, 40, 2, '\xbb')
    library.console_set_char_foreground(0, 2, 69, library.Color(255, 255, 255))
    library.console_set_char_background(0, 2, 69, library.Color(0, 0, 0))
    library.console_set_char(0, 2, 69, '\xc8')
    library.console_set_char_foreground(0, 40, 69, library.Color(255, 255, 255))
    library.console_set_char_background(0, 40, 69, library.Color(0, 0, 0))
    library.console_set_char(0, 40, 69, '\xbc')
    for y in range(3, 69):
        library.console_set_char_foreground(0, 2, y, library.Color(255, 255, 255))
        library.console_set_char_background(0, 2, y, library.Color(0, 0, 0))
        library.console_set_char(0, 2, y, '\xba')
        library.console_set_char_foreground(0, 40, y, library.Color(255, 255, 255))
        library.console_set_char_background(0, 40, y, library.Color(0, 0, 0))
        library.console_set_char(0, 40, y, '\xba')
    for x in range(3, 40):
        library.console_set_char_foreground(0, x, 2, library.Color(255, 255, 255))
        library.console_set_char_background(0, x, 2, library.Color(0, 0, 0))
        library.console_set_char(0, x, 2, '\xcd')
        library.console_set_char_foreground(0, x, 69, library.Color(255, 255, 255))
        library.console_set_char_background(0, x, 69, library.Color(0, 0, 0))
        library.console_set_char(0, x, 69, '\xcd')

def DrawBorderMagicChoice(library):
    library.console_set_char_foreground(0, 2, 2, library.Color(255, 255, 255))
    library.console_set_char_background(0, 2, 2, library.Color(0, 0, 0))
    library.console_set_char(0, 2, 2, '\xc9')
    library.console_set_char_foreground(0, 40, 2, library.Color(255, 255, 255))
    library.console_set_char_background(0, 40, 2, library.Color(0, 0, 0))
    library.console_set_char(0, 40, 2, '\xbb')
    library.console_set_char_foreground(0, 2, 69, library.Color(255, 255, 255))
    library.console_set_char_background(0, 2, 69, library.Color(0, 0, 0))
    library.console_set_char(0, 2, 69, '\xc8')
    library.console_set_char_foreground(0, 40, 69, library.Color(255, 255, 255))
    library.console_set_char_background(0, 40, 69, library.Color(0, 0, 0))
    library.console_set_char(0, 40, 69, '\xbc')
    for y in range(3, 69):
        library.console_set_char_foreground(0, 2, y, library.Color(255, 255, 255))
        library.console_set_char_background(0, 2, y, library.Color(0, 0, 0))
        library.console_set_char(0, 2, y, '\xba')
        library.console_set_char_foreground(0, 40, y, library.Color(255, 255, 255))
        library.console_set_char_background(0, 40, y, library.Color(0, 0, 0))
        library.console_set_char(0, 40, y, '\xba')
    for x in range(3, 40):
        library.console_set_char_foreground(0, x, 2, library.Color(255, 255, 255))
        library.console_set_char_background(0, x, 2, library.Color(0, 0, 0))
        library.console_set_char(0, x, 2, '\xcd')
        library.console_set_char_foreground(0, x, 69, library.Color(255, 255, 255))
        library.console_set_char_background(0, x, 69, library.Color(0, 0, 0))
        library.console_set_char(0, x, 69, '\xcd')

def DrawFillerStatChoice(library):
    for y in range(3, 9):
        for x in range(3, 25):
            library.console_set_char_foreground(0, x, y, library.Color(255, 255, 255))
            library.console_set_char_background(0, x, y, library.Color(0, 0, 0))
            library.console_set_char(0, x, y, ' ')

def DrawFillerCombatChoice(library):
    for y in range(3, 9):
        for x in range(3, 25):
            library.console_set_char_foreground(0, x, y, library.Color(255, 255, 255))
            library.console_set_char_background(0, x, y, library.Color(0, 0, 0))
            library.console_set_char(0, x, y, ' ')

def DrawFillerInventoryChoice(library):
    for y in range(3, 69):
        for x in range(3, 40):
            library.console_set_char_foreground(0, x, y, library.Color(255, 255, 255))
            library.console_set_char_background(0, x, y, library.Color(0, 0, 0))
            library.console_set_char(0, x, y, ' ')

def DrawFillerMagicChoice(library):
    for y in range(3, 69):
        for x in range(3, 40):
            library.console_set_char_foreground(0, x, y, library.Color(255, 255, 255))
            library.console_set_char_background(0, x, y, library.Color(0, 0, 0))
            library.console_set_char(0, x, y, ' ')


def DrawStatChoice(library, choice):
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
            library.console_set_char_foreground(0, 3 + index, 3 + key, library.Color(255, 255, 255))
            library.console_set_char_background(0, 3 + index, 3 + key, library.Color(0, 0, 0))
            library.console_set_char(0, 3 + index, 3 + key, value[index])

def DrawCombatChoice(library, choice):
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
            library.console_set_char_foreground(0, 3 + index, 3 + key, library.Color(255, 255, 255))
            library.console_set_char_background(0, 3 + index, 3 + key, library.Color(0, 0, 0))
            library.console_set_char(0, 3 + index, 3 + key, value[index])

def DrawInventoryChoice(library, choice, inventory, items):
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
            library.console_set_char_foreground(0, 3 + index, 3 + key, library.Color(255, 255, 255))
            library.console_set_char_background(0, 3 + index, 3 + key, library.Color(0, 0, 0))
            library.console_set_char(0, 3 + index, 3 + key, value[index])

def DrawMagicChoice(library, choice, destruction_spells, restoration_spells, player):
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
            library.console_set_char_foreground(0, 3 + index, 3 + key, library.Color(255, 255, 255))
            library.console_set_char_background(0, 3 + index, 3 + key, library.Color(0, 0, 0))
            library.console_set_char(0, 3 + index, 3 + key, value[index])


def DrawMainMenu(library, choice):
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
            library.console_set_char_foreground(0, 1 + index, 1 + key, library.Color(255, 255, 255))
            library.console_set_char_background(0, 1 + index, 1 + key, library.Color(0, 0, 0))
            library.console_set_char(0, 1 + index, 1 + key, value[index])
# Jafinoxal.
