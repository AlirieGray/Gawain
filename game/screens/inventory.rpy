screen inventory:
    add "gui/custom/transparent_bg_600_500.png" xalign .52 yalign .05
    grid 2 3:
        xalign .52 yalign .05
        for item, amount in g.inventory.items():
            if amount > 0:
                hbox:
                    text item + ": "
                    text str(amount) 