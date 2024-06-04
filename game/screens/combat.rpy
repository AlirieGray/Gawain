screen stats_left:
    vbox:
        xalign .08
        yalign .09
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


screen combat_menus:
    add "images/town.jpg"
    add "gui/custom/transparent_bg_300_680.png" yalign 0.05
    use calendar_screen
    use stats_left

