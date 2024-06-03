# TODO: does this work?

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
                    text attribute.title() xpos 10 ypos 9
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
                    text skill.title() xpos 10 ypos 9
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
    # TODO: only allow action if both/all actions are selected
    use my_button("Next Week", [Hide("town_menus"), Function(execute_day), Jump(calendar.next_jump)], 310, 600) #TODO: this is a HACK, this button should not increment day


# TODO: fix bug where first click doesn't increment stat
# TODO: make a more beautiful stat bar...
# TODO: fix day numbering and day/week/month increment...




screen task():
    add "gui/custom/transparent_bg_600_500.png" xalign .455 yalign .33
    use calendar_screen

    default current_day = 0
    default stat_name = calendar.current_day_outcome['stat_name']
    default stat_for_bar = g.stats_dict[stat_name]


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

            text "+" + str(calendar.current_day_outcome['skill_gain'])

        if calendar.current_day < 7:
            use my_button("Next Day", 
                [Function(execute_day), SetScreenVariable('stat_for_bar', stat_for_bar + calendar.current_day_outcome['skill_gain'])],
                20,
                100
            )
        else:
            use my_button("End Week",
                [Function(calendar.increment_day), Hide("task"), Jump(calendar.next_jump)],
                20, 
                100
            )
                