
screen town_menus:
    add "gui/custom/transparent_bg_500_150.png" xalign 0.53 yalign .05 
    use stats_left
    use hud

    imagebutton:
        idle "images/tavern_idle.png"
        hover "images/tavern_hover.png"
        xpos 985
        ypos 382
        action [Function(calendar.add_activity, activity="Visit Tavern")]

    imagebutton:
        idle "images/wash_idle.png"
        hover "images/wash_hover.png"
        xpos 640
        ypos 420
        action [Function(calendar.add_activity, activity="Visit Washing Well")]


    imagebutton:
        idle "images/inn_idle.png"
        hover "images/inn_hover.png"
        xpos 780
        ypos 342
        action [Function(calendar.add_activity, activity="Hang out at the Inn")]


    imagebutton:
        idle "images/cat_idle.png"
        hover "images/cat_hover.png"
        xpos 1135
        ypos 374
        action [Function(calendar.add_activity, activity="Check out Cat Haven")]


    imagebutton:
        idle "images/shop_idle.png"
        hover "images/shop_hover.png"
        xpos 1107
        ypos 505
        action [Jump('lludds')]


    imagebutton:
        idle "images/cottage_idle.png"
        hover "images/cottage_hover.png"
        xpos 540
        ypos 502
        action [Function(calendar.add_activity, activity="Visit Cottages")]

    text "This week's task:" xalign 0.4 yalign 0.08
    add "gui/custom/square_rectangle_empty.png" xalign 0.6 yalign 0.08
    text calendar.activity_slots[0] xalign 0.6 yalign 0.09

    use my_button("Start Week", If(calendar.activity_slots[0] != "*none selected*", [Hide("town_menus"), Jump(calendar.next_jump)]), 585, 150)


screen town_menus_month_end:
    add "gui/custom/transparent_bg_500_100.png" xalign 0.53 yalign .05 
    use stats_left
    use hud

    imagebutton:
        idle "images/shop_idle.png"
        hover "images/shop_hover.png"
        xpos 1107
        ypos 505
        action [Jump('lludds')]


    use my_button("End Month", [Hide('town_menus_month_end'), Jump(calendar.next_jump)], 585, 100)