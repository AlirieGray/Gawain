screen calendar_screen:
    add "gui/custom/transparent_bg_300_150.png" yalign .05 xalign .97
    vbox:
        xalign .94
        yalign .052
        xsize 250
        text str(calendar.get_day_number()) + " of " + calendar.get_current_month_name()
