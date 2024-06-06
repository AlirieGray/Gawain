init python:
    import math
    import time
    class Gawain:
        def __init__(self, character):
            self.c = character
            self.gold = 0
            self.hp = 10 + math.floor(5 / 2)
            self.stamina = 10
            self.stats_dict = {
                "piety": 1,
                "honor": 1,
                "mettle": 5,
                "fortitude": 5,
                "archery": 5,
                "swordplay": 5,
                "charm": 5,
                "brawling": 5,
                "intuition": 5,
                "medicine": 5,
            }
            

        def change_stat(self, stat, val):
            self.stats_dict[stat] = self.stats_dict[stat] + val

            if stat == 'mettle':
                self.hp = 10 + math.floor(self.stats_dict[stat] / 2)

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
            attack_modifier = self.stats_dict[attack_type]
            to_hit = roll(100, attack_modifier)

            # roll to hit, then roll for damage if roll beats target ac
            if to_hit > target.ac:
                damage_modifier = math.floor(attack_modifier / 2)
                combat_handler.apply_damage(roll(3, damage_modifier))
            else:
                combat_handler.apply_damage(0) # miss!

        def apply_damage(self, damage):
            self.hp = self.hp - damage
            # handle death/game over :( 

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
                combat_handler.apply_damage(roll(3, self.attack_modifier))
            else:
                combat_handler.apply_damage(0) # miss!


        def apply_damage(self, damage):
            new_hp = self.hp - damage
            if new_hp < 0:
                self.hp = 0
            else:
                self.hp = self.hp - damage
            if self.hp < 1:
                self.img = "images/monster_dead.png"
    
    # TODO: apply all of these stats in the gameplay...
    stat_descriptions = {
        "mettle": "Mettle is a knight's resolve, his ability to stand courageously in the face of danger and hardship.\nThis attribute increases your total health point maximum.",
        "fortitude": "A knight's duty is often arduous and grueling, he must therefore possess fortitude of both mind and body.\nThis attribute increases your total stamina maximum, which is spent for attacks and special abilities.",
        "intuition": "There is much in this world that lies beneath the surface, hidden to all but those with a trained eye and a still mind.\nThis attribute increases your chance of dodging incoming attacks.",
        "charm": "A knight must comport himself with charm and courtesy, in accordance with the chivalric virtues.\nThis attribute increased your chance of success in social scenarios.",
        "archery": "From a young age, a knight trains his skill with a bow for both sport and warfare.\nThis skill increases your damage and chance to hit with a bow and arrow attack.",
        "swordplay": "A knight's weapon is his life. You have studied the blade since you were a young page.\nThis skill increases your damage and chance to hit with a sword attack.",
        "brawling": "At times, a knight must defend himself without a weapon. His skill with his fists is then tested.\nThis skill increases your damage and chance to hit with unarmed attacks.",
        "medicine": "In the midst of battle, a knight's knowledge of field medicine means the difference between life and death.\nThis skill increases your health regeneration rate."
    }
    attributes = ["mettle", "fortitude", "intuition", "charm"]
    skills = ["archery", "swordplay", "brawling", "medicine"]