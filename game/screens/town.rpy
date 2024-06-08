
# TODO: clean up unused transparent backgrounds... or use im.Scale() isntead of a new image each time?
screen town_menus:
    use stats_left
    add "gui/custom/transparent_bg_500_150.png" xalign 0.53 yalign .05 
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
        action [Function(calendar.add_activity, activity="Visit the Shop")]


    imagebutton:
        idle "images/cottage_idle.png"
        hover "images/cottage_hover.png"
        xpos 540
        ypos 502
        action [Function(calendar.add_activity, activity="Visit Cottages")]

    text "This week's task:" xalign 0.4 yalign 0.08
    add "gui/custom/square_rectangle_empty.png" xalign 0.6 yalign 0.08
    text calendar.activity_slots[0] xalign 0.6 yalign 0.09
    # TODO: only allow action if both/all actions are selected
    use my_button("Start Week", If(calendar.activity_slots[0] != "*none selected*", [Hide("town_menus"), Jump(calendar.next_jump)]), 585, 150)
