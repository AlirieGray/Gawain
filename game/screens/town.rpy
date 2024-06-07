
# TODO: clean up unused transparent backgrounds... or use im.Scale() isntead of a new image each time?
screen town_menus:
    use stats_left
    add "gui/custom/transparent_bg_500_150.png" xalign 0.5 yalign .95 
    use hud

    imagebutton:
        idle "images/town_building.png"
        hover "images/tavern_hover.png"
        xpos 750
        ypos 150
        action [Function(calendar.add_activity, activity="Visit Tavern")]

    imagebutton:
        idle "images/town_building.png"
        hover "images/wash_hover.png"
        xpos 515
        ypos 150
        action [Function(calendar.add_activity, activity="Visit Washing Well")]


    imagebutton:
        idle "images/town_building.png"
        hover "images/inn_hover.png"
        xpos 355
        ypos 195
        action [Function(calendar.add_activity, activity="Hang out at the Inn")]


    imagebutton:
        idle "images/town_building.png"
        hover "images/cat_hover.png"
        xpos 950
        ypos 220
        action [Function(calendar.add_activity, activity="Check out Cat Haven")]

    text "This week's task:" xalign 0.4 yalign 0.84
    add "gui/custom/square_rectangle_empty.png" xalign 0.6 yalign 0.84
    text calendar.activity_slots[0] xalign 0.6 yalign 0.836
    # TODO: only allow action if both/all actions are selected
    if calendar.activity_slots[0] != "*none selected*":
        use my_button("Start Week", [Hide("town_menus"), Jump(calendar.next_jump)], 585, 655) #TODO: this is a HACK, this button should not increment day
