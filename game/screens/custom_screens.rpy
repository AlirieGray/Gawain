style spacing:
    spacing 10

screen cc_screen:
    add "gui/lake.jpg"
    hbox:
        xalign .76
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
            text "health"
            text "stamina"
            text "Points Remaining " + str(cc_points)