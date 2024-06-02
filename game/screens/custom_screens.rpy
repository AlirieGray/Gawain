style spacing:
    spacing 10

style dark_text:
    color "#181818"

screen cc_screen:
    add "images/lake_cc.jpg"
    hbox:
        xalign .8
        yalign .15
        spacing 50
        vbox:
            style "spacing"
            text "Attributes:"
            for attribute in attributes:
                text attribute.title()
                hbox:
                    imagebutton:
                        idle "gui/button/l_arrow_idle.png"
                        hover "gui/button/l_arrow.png"
                        if g.get_stat(attribute) > 1:
                            action [Function(g.change_stat, stat=attribute, val=-1), SetVariable("cc_points", cc_points + 1)]
                    text str(g.stats_dict[attribute])
                    imagebutton:
                        idle "gui/button/r_arrow_idle.png"
                        hover "gui/button/r_arrow.png"
                        if cc_points > 0:
                            action [Function(g.change_stat, stat=attribute, val=1), SetVariable("cc_points", cc_points - 1)]
        vbox:
            style "spacing"
            text "Skills:"
            for skill in skills:
                text skill.title()
                hbox:
                    imagebutton:
                        idle "gui/button/l_arrow_idle.png"
                        hover "gui/button/l_arrow.png"
                        if g.get_stat(skill) > 1:
                            action [Function(g.change_stat, stat=skill, val=-1), SetVariable("cc_points", cc_points + 1)]
                    text str(g.stats_dict[skill])
                    imagebutton:
                        idle "gui/button/r_arrow_idle.png"
                        hover "gui/button/r_arrow.png"
                        if cc_points > 0:
                            action [Function(g.change_stat, stat=skill, val=1), SetVariable("cc_points", cc_points - 1)]
            
        vbox:
            xsize 250
            text "Health"
            text "Stamina"
            text "Points Remaining " + str(cc_points)

    textbutton "Continue":
        xalign .7
        yalign .7
        if cc_points <1:
            action [Hide("cc_screen"), Jump("new_knight")]



screen town_screen: 
    add "images/town_without_building.png"

    imagebutton:
        idle "images/town_building.png"
        hover "images/town_building.png"
        xpos 720
        ypos 280

screen town_menus:
    add "images/town_menus_without_building.png"

    imagebutton:
        idle "images/town_building.png"
        hover "images/town_building_hover.png"
        xpos 720
        ypos 280
        action Function(calendar.add_activity, activity="Visit Tavern")

    hbox:
        xalign .08
        yalign .09
        spacing 50
        vbox:
            spacing 10
            for attribute in attributes:
                vbox:
                    spacing 1
                    text attribute.title()
                    hbox:
                        spacing 6
                        bar value StaticValue(g.stats_dict[attribute], 100):
                            xmaximum 200
                            ymaximum 40
                            left_bar Frame("gui/custom/round_rectangle_full.png", 10, 0)
                            right_bar Frame("gui/custom/round_rectangle_empty.png", 10, 0)
                        text str(g.stats_dict[attribute]) yalign 0.5
        vbox:
            spacing 10
            for skill in skills:
                vbox:
                    spacing 1
                    text skill.title()
                    hbox:
                        spacing 6
                        bar value StaticValue(g.stats_dict[skill], 100):
                            xmaximum 200
                            ymaximum 40
                            left_bar Frame("gui/custom/round_rectangle_full.png", 10, 0)
                            right_bar Frame("gui/custom/round_rectangle_empty.png", 10, 0)
                        text str(g.stats_dict[skill]) yalign 0.5


    text "This week's activities:" xpos 68 ypos 440
    add "gui/custom/square_rectangle_empty.png" xpos 70 ypos 500
    text calendar.activity_slots[0] xpos 90 ypos 510 
    add "gui/custom/square_rectangle_empty.png" xpos 300 ypos 500
    text calendar.activity_slots[1] xpos 310 ypos 510 
    button:
        xpos 310
        ypos 600
        idle_background "gui/custom/button.png"
        hover_background "gui/custom/button_hover.png"
        xysize (200, 70)
        text "Start Week" style "dark_text"
        action [Hide("town_menus"), Jump(calendar.next_jump)]

screen task:
    add "gui/custom/transparent_bg_600_500.png" xalign .5 yalign .05

