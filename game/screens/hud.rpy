screen hud:
    add "gui/custom/transparent_bg_250_120.png" yalign .05 xalign .975
    vbox:
        xalign .975
        yalign .052
        xsize 230
        text calendar.get_day_number() + " of " + calendar.get_current_month_name() 
        # for dev use
        # text "next jump " + (calendar.next_jump)
        # TODO: use bars for health and stamina
        hbox:
            text "HP: " + str(g.current_hp) + "/" + str(g.max_hp)
            text "Gold: " + str(g.gold) xoffset 25

