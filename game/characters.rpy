init python:
    import math
    import time

    dev_default = 20
    prod_default = 10

    class Gawain:
        def __init__(self, character):
            self.c = character
            self.gold = 5
            self.max_hp = 10 + math.floor(prod_default / 2)
            self.current_hp = 10 + math.floor(prod_default / 2)
            self.luck_potion_active = False
            self.ac_bonus = 0
            self.hp_bonus = 0
            self.ac = 50
            self.stats_dict = {
                # "piety": 1,
                # "honor": 1,
                "mettle": prod_default,
                "archery": prod_default,
                "swordplay": prod_default,
                "charm": prod_default,
                "intuition": prod_default
            }
            self.inventory = {
                'Libation of Liveliness': 0,
                'Libation of Life': 0,
                'Libation of Love': 0,
                'Libation of Leverage': 0,
                'Libation of Liberation': 0,
                'Libation of Luck': 0
            }

        def drink(self, potion):
            self.inventory[potion] = self.inventory[potion] - 1

            if potion == 'Libation of Liveliness':
                if self.current_hp + 10 > self.max_hp:
                    self.current_hp = self.max_hp
                else:
                    self.current_hp = self.current_hp + 10
                renpy.notify("You feel the liveliness course through you, your bruises and aches fade away! You have recovered +10 Hp.")

            elif potion == 'Libation of Life':
                if self.current_hp + 25 > self.max_hp:
                    self.current_hp = self.max_hp
                else:
                    self.current_hp = self.current_hp + 10
                renpy.notify("You feel a burst of life and vigor, your wounds mending! You have recoverd +25 HP.")
            elif potion == 'Libation of Love':
                new_max = self.max_hp + 5
                if self.current_hp == self.max_hp:
                    self.max_hp = new_max
                    self.current_hp = new_max
                else:
                    self.max_hp = new_max
                self.hp_bonus = self.hp_bonus + 5
                renpy.notify("You feel the power of love beating in your heart. Your maximum HP has permanently increased by 5.")
            
            elif potion == 'Libation of Luck':
                self.luck_potion_active = True
                renpy.notify("It's your lucky week! The spoils of your next battle will get a boost.")
            elif potion == 'Libation of Liberation':
                self.ac_bonus = self.ac_bonus +5
                renpy.notify("The sensation of liberation opens your mind and your heart. You now have an increased chance to dodge enemy attacks!")
            elif potion == 'Libation of Leverage':
                renpy.notify("You feel more powerful! All your stats increase by 1.")
                g.change_stat('mettle', 1)
                g.change_stat('charm', 1)
                g.change_stat('intuition', 1)
                g.change_stat('archery', 1)
                g.change_stat('swordplay', 1)
        
        def get_min_stat(self):
            return min(self.stats_dict, key = self.stats_dict.get)
        
        def reset_health(self):
            g.current_hp = g.max_hp

        def add_inventory(self, item):
            self.inventory[item] = self.inventory[item] + 1

        def remove_inventory(self, item):
            self.inventory[item] = self.inventory[item] - 1

        def change_stat(self, stat, val):
            if (self.get_stat(stat) + val) >= 100:
                self.stats_dict[stat] = 100

                if stat == 'mettle':
                    new_max = 10 + math.floor(self.stats_dict[stat] / 2) + self.hp_bonus
                    self.max_hp = new_max
                    self.current_hp = new_max
                elif stat == 'intuition': 
                    self.ac = 50 + math.floor(self.stats_dict[stat] / 4) + self.ac_bonus
                return
            
            self.stats_dict[stat] = self.stats_dict[stat] + val

            if stat == 'mettle':
                new_max = 10 + math.floor(self.stats_dict[stat] / 2) + self.hp_bonus
                self.max_hp = new_max
                self.current_hp = new_max
            elif stat == 'intuition': 
                self.ac = 50 + math.floor(self.stats_dict[stat] / 4) + self.ac_bonus
            elif stat == 'charm':
                shop.give_charm_discount(math.floor(self.stats_dict[stat] / 25))
                

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

    # TODO refactor we don't need this
    class Lady:
        def __init__(self, character):
            self.c = character

    class Enemy:
        def __init__(self, character, name, hp, ac, attack_modifier, reward, img):
            self.c = character
            self.max_hp = hp
            self.hp = hp
            self.ac = ac
            self.attack_modifier = attack_modifier
            self.img = img
            self.name = name
            self.reward = reward

        def get_image(self):
            return self.img

        def get_name(self):
            return self.name

        def attack(self):
            to_hit = roll(100, self.attack_modifier)

            # TODO: use different attack and damage modifiers 
            if to_hit > g.ac:
                return roll(3, self.attack_modifier)
            else:
                return 0 # miss!

        def take_damage(self, damage):
            new_hp = self.hp - damage
            if new_hp < 0:
                self.hp = 0
            else:
                self.hp = self.hp - damage
            # if self.hp < 1:
            #     self.img = "images/monster_dead.png"
    
    # TODO: apply all of these stats in the gameplay...
    stat_descriptions = {
        "mettle": "A knight's duty is often arduous and grueling, he must therefore possess the mettle to stand courageously in the face of danger and hardship.\nThis attribute increases your total health point maximum.",
        "intuition": "There is much in this world that lies beneath the surface, hidden to all but those with a trained eye and a still mind.\nThis attribute increases your chance of dodging incoming attacks and helps you in some social scenarios.",
        "charm": "A knight must comport himself with charm and courtesy, in accordance with the chivalric virtues.\nThis attribute increased your chance of success in social scenarios and lowers the cost of items in the shop.",
        "archery": "From a young age, a knight trains his skill with a bow for both sport and warfare.\nThis skill increases your damage and chance to hit with a bow and arrow attack.",
        "swordplay": "A knight's weapon is his life. You have studied the blade since you were a young page.\nThis skill increases your damage and chance to hit with a sword attack.",
    }
    attributes = ["mettle", "intuition", "charm"]
    skills = ["archery", "swordplay"]