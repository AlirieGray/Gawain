screen calendar_screen:
    add "gui/custom/transparent_bg_250_120.png" yalign .05 xalign .975
    vbox:
        xalign .975
        yalign .052
        xsize 230
        text str(calendar.get_day_number()) + " of " + calendar.get_current_month_name() 
