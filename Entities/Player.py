# Endovia (Player)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import Basic

class Character(Basic.Character):
    def __init__(self, chart_id, grid_id, entity_id, unique_id, x, y, name, race):
        super(Character, self).__init__(chart_id, grid_id, entity_id, unique_id, x, y)
        self.dead = False
        self.name = name
        self.race = race
        self.level = 1
        self.experience = 0
        self.inventory = { # Tools.
        1000: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0, 22:0,
              }, # Ores.
        1001: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0,
              }, # Ingots.
        1002: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0,
              }, # Clumps.
        1003: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0,
              }, # UncutGems.
        1004: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0,
              }, # CutGems.
        1005: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0,
              }, # RawFish.
        1006: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0,
              }, # CookedFish.
        1007: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0,
              }, # Herbs.
        1008: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0,
              }, # Mushrooms.
        1009: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0,
              }, # Berries.
        1010: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0,
              }, # Flowers.
        1011: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0,
              }, # Ingredients.
        1012: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0, 22:0,
               23:0, 24:0, 25:0,
              }, # Potions.
        1013: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0, 22:0,
               23:0, 24:0, 25:0, 26:0, 27:0,
              }, # Logs.
        1014: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0, 22:0,
              }, # Necklaces.
        1015: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0,
              }, # Rings.
        1016: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0,
              }, # Bracelets.
        1017: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0,
              }, # Stones.
        1018: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0,
              }, # Arrows.
        1019: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0,
              }, # Bolts.
        1020: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0,
              }, # Pies.
        1021: {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0,
               12:0, 13:0, 14:0,
              },
        1022: {},
        1023: {},
        1024: {},
        1025: {},
        1026: {},
        1027: {},
        1028: {},
        1029: {},
        1030: {},
        1031: {},
        1032: {},
        1033: {},
        1034: {},
        1035: {},
        1036: {},
        1037: {},
        1038: {},
        }
        self.stats = { # Current, Max.
        "health": (100, 100),
        "mana": (100, 100),
        "energy": (100, 100),
        "faith": (100, 100),
        "chakra": (100, 100),
        }
        self.attributes = {
        "attack": 1,
        "strength": 1,
        "defense": 1,
        "endurance": 1,
        "dexterity": 1,
        "agility": 1,
        "perception": 1,
        "intelligence": 1,
        "luck": 1,
        "charisma": 1,
        }
        self.skills = { # Level, Experience.
        "melee": (1, 0),
        "ranged": (1, 0),
        "magic": (1, 0),
        "gunning": (1, 0),
        "prayer": (1, 0),
        "speech": (1, 0),
        "barter": (1, 0),
        "thieving": (1, 0),
        "forestry": (1, 0),
        "kindling": (1, 0),
        "fletching": (1, 0),
        "mining": (1, 0),
        "smithing": (1, 0),
        "crafting": (1, 0),
        "fishing": (1, 0),
        "cooking": (1, 0),
        "hunter": (1, 0),
        "summoning": (1, 0),
        "construction": (1, 0),
        "alchemy": (1, 0),
        }

    def _assign_stat(self, stat, amount):
        if stat not in self.stats.keys():
            return False
        else:
            self.stats[stat][0] = amount
            self.stats[stat][1] = amount
            return True

    def _assign_skill(self, skill, amount):
        if skill not in self.skills.keys():
            return False
        else:
            self.skills[skill][0] = amount
            self.skills[skill][1] = (amount -1) * amount * 10
            return True

# Jafinoxal.
