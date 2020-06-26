# -*- coding: utf-8 -*-
# Endovia (DrawMenu)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def DrawBorder1(library):
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

def DrawBorder2(library):
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

def DrawFiller1(library):
    for y in range(3, 9):
        for x in range(3, 25):
            library.console_set_char_foreground(0, x, y, library.Color(255, 255, 255))
            library.console_set_char_background(0, x, y, library.Color(0, 0, 0))
            library.console_set_char(0, x, y, ' ')

def DrawFiller2(library):
    for y in range(3, 69):
        for x in range(3, 40):
            library.console_set_char_foreground(0, x, y, library.Color(255, 255, 255))
            library.console_set_char_background(0, x, y, library.Color(0, 0, 0))
            library.console_set_char(0, x, y, ' ')

def DrawStatChoice(library, choice):
    choices = {
    0: "+ Choose +",
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
                choices[2 + item_index] = "[{0}] x{1}      ".format(items[choice[0]][item_id][2], inventory[choice[0]][item_id])
            else:
                choices[2 + item_index] = "[Empty]"
        else:
            if item_amount > 0:
                choices[2 + item_index] = "{0} x{1}      ".format(items[choice[0]][item_id][2], inventory[choice[0]][item_id])
            else:
                choices[2 + item_index] = "Empty"
        item_index += 1
    for key, value in choices.items():
        for index in range(0, len(value)):
            library.console_set_char_foreground(0, 3 + index, 3 + key, library.Color(255, 255, 255))
            library.console_set_char_background(0, 3 + index, 3 + key, library.Color(0, 0, 0))
            library.console_set_char(0, 3 + index, 3 + key, value[index])

# Jafinoxal.
