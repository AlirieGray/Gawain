init python:
    class Shop:
        def __init__(self):
            self.inventory = {
                'Libation of Liveliness': {'stock': 5, 'price': 4, 'description': '+10 HP, one-time use'},
                'Libation of Life': {'stock': 2, 'price': 12, 'description': '+25 HP, one-time use'},
                'Libation of Love': {'stock': 1, 'price': 15, 'description': '+5 permanent increase to HP'},
                'Libation of Leverage': {'stock': 2, 'price': 12, 'description': 'Increase all attribute gain for one week'},
                'Libation of Liberation': {'stock': 2, 'price': 12, 'description': 'Increase all skill gain for one week'},
                'Libation of Luck': {'stock': 4, 'price': 10, 'description': 'Increase chance to dodge incoming attacks'},
                # not using stamina this iteration
                # 'Libation of Longevity': {'stock': 3, 'price': 3, 'description': '+5 stamina, one-time use'},
            }
            self.item_names = ['Libation of Liveliness', 'Libation of Life', 'Libation of Love', 'Libation of Leverage', 'Libation of Liberation', 'Libation of Luck']

        def purchase_item(self, item):
            if self.inventory[item]['stock'] > 1:
                # purchase
                g.change_gold(-(self.inventory[item]['price']))
                g.add_inventory(item)
                self.inventory[item]['stock'] = self.inventory[item]['stock'] - 1
            else:
                return "You don't have enough gold for this item!"