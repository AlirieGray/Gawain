screen cc_screen:
    add "images/lake.jpg"
    add "gui/custom/transparent_bg_cc.png" xalign .95 yalign .2
    add "images/gawain_portrait.png" yanchor 1.0 yalign 1.0 
    use tooltip(current_tooltip, 100, 100)


    # for i, attribute in enumerate(attributes):
    #     mousearea:
    #         # area (500, 0 + (i * 100), 100, 100)
    #         hovered set_tooltip(attribute, stat_descriptions[attribute])
    #         # unhovered set_tooltip("", "")


    hbox:
        xalign 1.0
        yalign .22
        spacing 120
        vbox:
            style "spacing"
            text "Attributes:" xpos -20 style "special_font"
            for attribute in attributes:
                vbox:
                    spacing 1
                    textbutton attribute.title():
                        xalign 0.5 
                        text_style "cc_label_text"
                        hovered SetVariable("current_tooltip", [attribute, stat_descriptions[attribute]])
                        unhovered SetVariable("current_tooltip", ["", ""])   
                        action SetVariable("current_tooltip", [attribute, stat_descriptions[attribute]])            
                    hbox:
                        # TODO: make arrows flush with stat box, with transparent margins, so tooltip doesn't disappear when mousing over
                        imagebutton:
                            yalign 0.5 xpos -10
                            idle "gui/button/l_arrow_idle.png"
                            hover "gui/button/l_arrow.png"
                            hovered SetVariable("current_tooltip", [attribute, stat_descriptions[attribute]])
                            unhovered SetVariable("current_tooltip", ["", ""])              
                            if g.get_stat(attribute) > 1:
                                action [Function(g.change_stat, stat=attribute, val=-1), SetVariable("cc_points", cc_points + 1)]
                        
                        imagebutton: 
                            xpos 0
                            idle 'gui/custom/round_square_empty.png' 
                            hover 'gui/custom/round_square_empty.png' 
                            hovered SetVariable("current_tooltip", [attribute, stat_descriptions[attribute]])
                            unhovered SetVariable("current_tooltip", ["", ""])                 
                            action SetVariable("current_tooltip", [attribute, stat_descriptions[attribute]])

                        text str(g.stats_dict[attribute]) xpos -28 yalign 0.5
                        
                        imagebutton:
                            yalign 0.5 
                            idle "gui/button/r_arrow_idle.png"
                            hover "gui/button/r_arrow.png"
                            hovered SetVariable("current_tooltip", [attribute, stat_descriptions[attribute]])
                            unhovered SetVariable("current_tooltip", ["", ""])              
                            if cc_points > 0:
                                action [Function(g.change_stat, stat=attribute, val=1), SetVariable("cc_points", cc_points - 1)]
        vbox:
            style "spacing"
            text "Skills:" xpos -20 style "special_font"
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