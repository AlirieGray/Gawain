screen inventory:
    add "gui/custom/transparent_bg_600_500.png" xalign .52 yalign .05
    modal True
    vbox:
        xalign .55 yalign .165
        spacing 12
        xsize 580
        xfill True
        text "Inventory" style "special_font" xalign .5

    grid 2 3:
        xalign .52 yalign .05
        for item, amount in g.inventory.items():
            if amount > 0:
                hbox:
                    text item + ": "
                    text str(amount) 

    textbutton "close" action Hide("inventory") xpos 800 ypos 800