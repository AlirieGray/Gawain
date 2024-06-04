

screen cc_screen:
    add "images/lake.jpg"
    add "gui/custom/transparent_bg_cc.png" xalign .95 yalign .2
    hbox:
        xalign 1.0
        yalign .22
        spacing 120
        vbox:
            style "spacing"
            text "Attributes:" xpos -30  
            for attribute in attributes:
                vbox:
                    spacing 1
                    text attribute.title() xalign 0.5
                    hbox:
                        imagebutton:
                            yalign 0.5 xpos -10
                            idle "gui/button/l_arrow_idle.png"
                            hover "gui/button/l_arrow.png"
                            if g.get_stat(attribute) > 1:
                                action [Function(g.change_stat, stat=attribute, val=-1), SetVariable("cc_points", cc_points + 1)]
                        add 'gui/custom/round_square_empty.png' xpos 0
                        text str(g.stats_dict[attribute]) xpos -28 yalign 0.5
                        imagebutton:
                            yalign 0.5 
                            idle "gui/button/r_arrow_idle.png"
                            hover "gui/button/r_arrow.png"
                            if cc_points > 0:
                                action [Function(g.change_stat, stat=attribute, val=1), SetVariable("cc_points", cc_points - 1)]
        vbox:
            style "spacing"
            text "Skills:" xpos -30
            for skill in skills:
                vbox:
                    spacing 1
                    text skill.title() xalign 0.5
                    hbox:
                        imagebutton:
                            yalign 0.5 xpos -10
                            idle "gui/button/l_arrow_idle.png"
                            hover "gui/button/l_arrow.png"
                            if g.get_stat(skill) > 1:
                                action [Function(g.change_stat, stat=skill, val=-1), SetVariable("cc_points", cc_points + 1)]
                        add 'gui/custom/round_square_empty.png' xpos 0
                        text str(g.stats_dict[skill]) xpos -28 yalign 0.5
                        imagebutton:
                            yalign 0.5
                            idle "gui/button/r_arrow_idle.png"
                            hover "gui/button/r_arrow.png"
                            if cc_points > 0:
                                action [Function(g.change_stat, stat=skill, val=1), SetVariable("cc_points", cc_points - 1)]
            
        vbox:
            xsize 250
            # TODO: health is based on mettle, stamina is based on grit (or vice versa)
            text "Health"
            text "Stamina"
            text "Points Remaining " + str(cc_points)
    
    if cc_points <1:
        use my_button("Continue", [Hide("cc_screen"), Jump("new_knight")], 1020, 570)