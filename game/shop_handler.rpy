init python:
    class Lluds:
        def __init__(self):
            self.inventory = {
                'Libation of Liveliness': {'stock': 5, 'cost': 4, 'description': '+10 HP, one-time use'},
                'Libation of Life': {'stock': 2, 'cost': 12, 'description': '+25 HP, one-time use'},
                'Libation of Love': {'stock': 1, 'cost': 15, 'description': '+5 permanent increase to HP'},
                'Libation of Leverage': {'stock': 2, 'cost': 12, 'description': 'Increase all attribute gain for one week'},
                'Libation of Liberation': {'stock': 2, 'cost': 12, 'description': 'Increase all skill gain for one week'},
                'Libation of Luck':{'stock': 4, 'cost': 10, 'description': 'Increase chance to dodge incoming attacks'},
                # not using stamina this iteration
                # 'Libation of Longevity': {'stock': 3, 'cost': 3, 'description': '+5 stamina, one-time use'},
            }