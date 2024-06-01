init python:
    class Gawain:
        def __init__(self, character):
            self.c = character
            self.stats_dict = {
                "hp": 20,
                "stamina": 10,
                "piety": 1,
                "honor": 1,
                "mettle": 1,
                "grit": 1,
                "archery": 1,
                "swordplay": 1,
                "charm": 1,
                "brawling": 1,
                "intuition": 1,
                "medicine": 1,
            }

        def change_stat(self, stat, val):
            self.stats_dict[stat] = self.stats_dict[stat] + val

        def get_stat(self, stat):
            return self.stats_dict[stat]

    class Lady:
        def __init__(self, character):
            self.c = character
    
    stat_descriptions = {"mettle": "Mettle is a knight's resolve, his ability to stand firm in the face of danger and hardship. This attribute reduces damage from all phyiscal sources."}
    attributes = ["mettle", "grit", "intuition", "charm"]
    skills = ["archery", "swordplay", "brawling", "medicine"]