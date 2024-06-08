init python:
    import math
    import time

    dev_default = 9
    prod_default = 5

    # TODO: max out stats (at 100?)

    class Gawain:
        def __init__(self, character):
            self.c = character
            self.gold = 100 # TODO DEV VALUE, prod start at 0-10
            self.max_hp = 10 + math.floor(5 / 2)
            self.current_hp = 10 + math.floor(5 / 2)
            self.stats_dict = {
                "piety": 1,
                "honor": 1,
                "mettle": dev_default,
                "archery": dev_default,
                "swordplay": dev_default,
                "charm": dev_default,
                "intuition": dev_default
            }
            self.inventory = { # TODO DEV VALUE prod all potions 0
                'Libation of Liveliness':  2,
                'Libation of Life': 1,
                'Libation of Love': 1,
                'Libation of Leverage': 1,
                'Libation of Liberation': 1,
                'Libation of Luck': 1
            }
        

        def add_inventory(self, item):
            self.inventory[item] = self.inventory[item] + 1

        def remove_inventory(self, item):
            self.inventory[item] = self.inventory[item] - 1

        def change_stat(self, stat, val):
            if (self.get_stat(stat) + val) >= 100:
                self.stats_dict[stat] = 100

                if stat == 'mettle':
                    self.max_hp = 10 + math.floor(self.stats_dict[stat] / 2)
            
            # elif self.get_stat(stat) < 100:
            #     self.stats_dict[stat] = self.stats_dict[stat] + val

            #     if stat == 'mettle':
            #         self.max_hp = 10 + math.floor(self.stats_dict[stat] / 2)



        def get_stat(self, stat):
            return self.stats_dict[stat]

        def change_gold(self, val):
            self.gold = self.gold + val

        def get_gold(self, val):
            return self.gold

        def attack(self, attack_type, target):
            # returns an hp loss for target (Enemy class)
            # target then applies that hp loss
            # also spends some stamina, depends on the type of attack or special ability

            # get attack modifier
            attack_modifier = get_attack_modifier(self.get_stat(attack_type))
            to_hit = roll(100, attack_modifier)

            # roll to hit, then roll for damage if roll beats target ac
            if to_hit > target.ac:
                damage_modifier = math.floor(attack_modifier / 2)
                return roll(3, damage_modifier)
            else:
                return 0 # miss!

        def take_damage(self, damage):
            self.current_hp = self.current_hp - damage

            if self.current_hp < 1:
                self.current_hp = 0
                combat_handler.gawain_defeated()

    class Lady:
        def __init__(self, character):
            self.c = character

    class Enemy:
        def __init__(self, character, name, hp, ac, attack_modifier, img):
            self.c = character
            self.hp = hp
            self.ac = ac
            self.attack_modifier = attack_modifier
            self.img = img
            self.name = name

        def get_image(self):
            return self.img

        def get_name(self):
            return self.name

        def attack(self):
            to_hit = roll(100, self.attack_modifier)
            # TODO: calculate Gawain's AC based on mettle stat
            # TODO: use different attack and damage modifiers 
            if to_hit > 50:
                return roll(3, self.attack_modifier)
            else:
                return 0 # miss!


        def take_damage(self, damage):
            new_hp = self.hp - damage
            if new_hp < 0:
                self.hp = 0
            else:
                self.hp = self.hp - damage
            if self.hp < 1:
                self.img = "images/monster_dead.png"
    
    # TODO: apply all of these stats in the gameplay...
    stat_descriptions = {
        "mettle": "A knight's duty is often arduous and grueling, he must therefore possess the mettle to stand courageously in the face of danger and hardship.\nThis attribute increases your total health point maximum.",
        "intuition": "There is much in this world that lies beneath the surface, hidden to all but those with a trained eye and a still mind.\nThis attribute increases your chance of dodging incoming attacks.",
        "charm": "A knight must comport himself with charm and courtesy, in accordance with the chivalric virtues.\nThis attribute increased your chance of success in social scenarios and lowers the cost of items in the shop.",
        "archery": "From a young age, a knight trains his skill with a bow for both sport and warfare.\nThis skill increases your damage and chance to hit with a bow and arrow attack.",
        "swordplay": "A knight's weapon is his life. You have studied the blade since you were a young page.\nThis skill increases your damage and chance to hit with a sword attack.",
    }
    attributes = ["mettle", "intuition", "charm"]
    skills = ["archery", "swordplay"]