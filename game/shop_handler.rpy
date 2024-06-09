init python:
    class Shop:
        def __init__(self):
            self.inventory = {
                # TODO: different images for each potion
                'Libation of Liveliness': {'stock': 2, 'price': 4, 'description': '+10 HP, one-time use', 'image': 'images/red_potion.png'},
                'Libation of Life': {'stock': 2, 'price': 12, 'description': '+25 HP, one-time use', 'image': 'images/red_potion.png'},
                'Libation of Love': {'stock': 1, 'price': 15, 'description': '+5 permanent HP increase', 'image': 'images/red_potion.png'},
                'Libation of Leverage': {'stock': 2, 'price': 12, 'description': 'Increase all your stats by 1', 'image': 'images/red_potion.png'},
                'Libation of Luck': {'stock': 3, 'price': 15, 'description': 'Increase rewards from your next successful battle.', 'image': 'images/red_potion.png'},
                'Libation of Liberation': {'stock': 1, 'price': 25, 'description': 'Increase chance to dodge incoming attacks', 'image': 'images/red_potion.png'},
                # not using stamina this iteration
                # 'Libation of Longevity': {'stock': 3, 'price': 3, 'description': '+5 stamina, one-time use'},
            }
            self.item_names = ['Libation of Liveliness', 'Libation of Life', 'Libation of Love', 'Libation of Leverage', 'Libation of Liberation', 'Libation of Luck']

        def get_image_str(self, item):
            return self.inventory[item]['image']

        def purchase_item(self, item):
            if self.inventory[item]['stock'] > 0:
                g.change_gold(-(self.inventory[item]['price']))
                g.add_inventory(item)
                self.inventory[item]['stock'] = self.inventory[item]['stock'] - 1
            else:
                return "You don't have enough gold for this item!"

        def restock_shop(self):
            self.inventory['Libation of Liveliness']['stock'] = 2