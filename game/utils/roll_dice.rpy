init python:
    import math
    import random 
    
    def roll(sides, modifier):
        return random.randint(1, sides) + modifier

    # TODO: make this fancy math lol
    # skills progress WAY too fast....
    def get_modifier(stat):
        if stat < 90:
            return 1
        if stat < 150:
            return 2
        if stat < 190:
            return 3
        return 4

    def get_attack_modifier(stat):
        return math.floor(stat / 2)
