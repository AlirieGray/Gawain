init python:
    import math
    class Gawain:
        def __init__(self, character):
            self.c = character
            self.gold = 0
            self.stats_dict = {
                "hp": 20,
                "stamina": 10,
                "piety": 1,
                "honor": 1,
                "mettle": 5,
                "grit": 5,
                "archery": 5,
                "swordplay": 5,
                "charm": 5,
                "brawling": 5,
                "intuition": 5,
                "medicine": 5,
            }

        def change_stat(self, stat, val):
            self.stats_dict[stat] = self.stats_dict[stat] + val

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
                return roll(3, damage_modifier)
            return 0 # miss!


    class Lady:
        def __init__(self, character):
            self.c = character

    class Enemy:
        def ___init__(self, character, hp, ac, attack):
            self.c = character
            self.hp = hp
            self.ac = ac
            self.attack_modifier = attack
    
    stat_descriptions = {"mettle": "Mettle is a knight's resolve, his ability to stand firm in the face of danger and hardship. This attribute reduces damage from all phyiscal sources."}
    attributes = ["mettle", "grit", "intuition", "charm"]
    skills = ["archery", "swordplay", "brawling", "medicine"]