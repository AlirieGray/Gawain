init python:
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

    class Lady:
        def __init__(self, character):
            self.c = character

    class Enemy:
        def ___init__(self, character, hp, ac, attack):
            self.c = character
            self.hp = hp
            self.ac = ac
            # attack is a modifier to dice rolls
            self.attack = attack
    
    stat_descriptions = {"mettle": "Mettle is a knight's resolve, his ability to stand firm in the face of danger and hardship. This attribute reduces damage from all phyiscal sources."}
    attributes = ["mettle", "grit", "intuition", "charm"]
    skills = ["archery", "swordplay", "brawling", "medicine"]