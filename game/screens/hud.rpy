screen hud:
    add "gui/custom/transparent_bg_250_120.png" yalign .05 xalign .975
    vbox:
        xalign .975
        yalign .052
        xsize 230
        text calendar.get_day_number() + " of " + calendar.get_current_month_name() size 18
        hbox:
            text "HP: " + str(g.current_hp) + "/" + str(g.max_hp) size 18
            text "Gold: " + str(g.gold) xoffset 25 size 18
        textbutton "Inventory" action Show("inventory") text_size 18

