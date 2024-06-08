screen inventory:
    add "gui/custom/transparent_bg_600_500.png" xalign .52 yalign .05
    modal True
    text "Inventory" style "special_font" xalign .5 yalign .06

    grid 2 3:
        xalign .52
        top_margin 90
        xspacing 50
        yspacing 50
        for item, amount in g.inventory.items():
            if amount > 0:
                vbox:
                    add shop.get_image_str(item)
                    hbox:
                        text item + ": "
                        text str(amount) 
                    textbutton "Drink Potion" action Function(g.drink, item)

    textbutton "Close" action Hide("inventory") xpos 850 ypos 450