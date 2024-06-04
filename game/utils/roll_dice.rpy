init python:
    import math
    import random 
    
    def roll(sides, modifier):
        return random.randint(1, sides) + modifier

    # TODO: make this fancy math lol
    # skills progress WAY too fast....
    def get_modifier(stat):
        return math.floor(stat / 10)
