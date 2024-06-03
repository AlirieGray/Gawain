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

screen calendar_screen:
    add "gui/custom/transparent_bg_300_200.png" yalign .05 xalign .97
    vbox:
        xalign .94
        yalign .052
        xsize 250
        text calendar.get_current_month_name()
        text "Week " + str(calendar.get_current_week())

screen town_screen: 
    add "images/town_without_building.png"

    imagebutton:
        idle "images/town_building.png"
        hover "images/town_building.png"
        xpos 720
        ypos 280

# TODO: use separate transparent box images over town image
# TODO: refactor UI elements to be modular ("use __ screen" syntax?)
screen town_menus:
    add "images/town_menus_without_building.png"
    use calendar_screen

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
        text "Start Week" style "dark_text" # TODO: only allow action if both/all actions are selected
        action [Hide("town_menus"), Jump(calendar.next_jump)]


# TODO: fix bug where first click doesn't increment stat
# TODO: make a more beautiful stat bar...
# TODO: fix day numbering and day/week/month increment...


screen task(cal, gawain):
    add "gui/custom/transparent_bg_600_500.png" xalign .455 yalign .33
    use calendar_screen

    default current_day = 0
    default stat_name = cal.current_day_outcome['stat_name']
    default stat_for_bar = gawain.stats_dict[stat_name]


    vbox:
        xalign 0.5
        yalign 0.5

        hbox:
            text stat_name.title()
            bar value AnimatedValue(stat_for_bar, 100):
                xmaximum 200
                ymaximum 40
                left_bar Frame("gui/custom/round_rectangle_full.png", 10, 0)
                right_bar Frame("gui/custom/round_rectangle_empty.png", 10, 0)
            text "+" + str(cal.current_day_outcome['skill_gain'])
        
        textbutton "Next Day":
            if cal.current_day < 6:
                action [Function(execute_day, cal=cal, gawain=gawain), SetScreenVariable('stat_for_bar', stat_for_bar + cal.current_day_outcome['skill_gain'])]
            if cal.current_day >= 6:
                action [Hide("task"), Jump(calendar.next_jump)]

