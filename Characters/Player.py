# Endovia (Player)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

import Basic

class Character(Basic.Character):
    def __init__(self, entity_id, unique_id, chart_id, grid_id, x, y, name, race):
        super(Character, self).__init__(entity_id, unique_id, chart_id, grid_id, x, y)
        self.name = name
        self.race = race
        self.level = 1
        self.stats = { # Current, Max.
        "health": (100, 100),
        "mana": (100, 100),
        "energy": (100, 100),
        }
        self.attributes = {
        "attack": 1,
        "strength": 1,
        "defense": 1,
        "endurance": 1,
        "dexterity": 1,
        "agility": 1,
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

    def _level_up_stat(self, stat):
        if stat not in self.stats.keys():
            return False
        else:
            self.stats[stat] = self.stats[stat](self.stats[stat][0], self.stats[stat][1] + 50)
            return True

    def _level_up_skill(self, skill):
        if skill not in self.skills.keys():
            return False
        else:
            experience_needed = self.skills[skill][0] * self.skills[skill][0] * 10
            if self.skills[skill][1] >= experience_needed and self.skills[skill][0] != 100:
                self.skills[skill] = self.skills[skill](self.skills[0] + 1, self.skills[1])
                return True
            else:
                return False

# Jafinoxal.
