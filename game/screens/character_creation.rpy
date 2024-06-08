screen cc_screen:
    add "images/lake.png"
    add "gui/custom/transparent_bg_cc.png" xalign .95 yalign .2
    add "images/gawain_portrait.png" yanchor 1.0 yalign 1.0 
    use tooltip(current_tooltip, 50, 90, False)


    # TODO: refeactor the cc screen to be modular, it's way too long
    hbox:
        xalign 1.0
        yalign .25
        spacing 100
        vbox:
            style "spacing"
            text "Attributes:" xpos -10 style "special_font" 
            for attribute in attributes:
                vbox:
                    textbutton attribute.title():
                        xalign 0.5 
                        text_style "cc_label_text"
                        hovered SetVariable("current_tooltip", [attribute, stat_descriptions[attribute]])
                        unhovered SetVariable("current_tooltip", ["", ""])   
                        action SetVariable("current_tooltip", [attribute, stat_descriptions[attribute]])            
                    hbox:
                        imagebutton:
                            yalign 0.5
                            idle "gui/button/l_arrow_idle.png"
                            hover "gui/button/l_arrow.png"
                            hovered SetVariable("current_tooltip", [attribute, stat_descriptions[attribute]])
                            unhovered SetVariable("current_tooltip", ["", ""])              
                            if g.get_stat(attribute) > 1:
                                action [Function(g.change_stat, stat=attribute, val=-1), SetVariable("cc_points", cc_points + 1)]
                        
                        imagebutton: 
                            # xpos 0
                            idle 'gui/custom/round_square_empty.png' 
                            hover 'gui/custom/round_square_empty.png' 
                            hovered SetVariable("current_tooltip", [attribute, stat_descriptions[attribute]])
                            unhovered SetVariable("current_tooltip", ["", ""])                 
                            action SetVariable("current_tooltip", [attribute, stat_descriptions[attribute]])

                        if g.get_stat(attribute) < 10:
                            text "  " + str(g.get_stat(attribute)) xoffset -35 yalign 0.5 

                        else:
                            text str(g.get_stat(attribute)) xoffset -36 yalign 0.5 
                        
                        imagebutton:
                            yalign 0.5 
                            xpos -21
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
                    textbutton skill.title():
                        xalign 0.5 
                        text_style "cc_label_text"
                        hovered SetVariable("current_tooltip", [skill, stat_descriptions[skill]])
                        unhovered SetVariable("current_tooltip", ["", ""])   
                        action SetVariable("current_tooltip", [skill, stat_descriptions[skill]])   
                    hbox:
                        imagebutton:
                            yalign 0.5
                            idle "gui/button/l_arrow_idle.png"
                            hover "gui/button/l_arrow.png"
                            hovered SetVariable("current_tooltip", [skill, stat_descriptions[skill]])
                            unhovered SetVariable("current_tooltip", ["", ""])   
                            if g.get_stat(skill) > 1:
                                action [Function(g.change_stat, stat=skill, val=-1), SetVariable("cc_points", cc_points + 1)]
                        
                        imagebutton: 
                            xpos 0
                            idle 'gui/custom/round_square_empty.png' 
                            hover 'gui/custom/round_square_empty.png' 
                            hovered SetVariable("current_tooltip", [skill, stat_descriptions[skill]])
                            unhovered SetVariable("current_tooltip", ["", ""])                 
                            action SetVariable("current_tooltip", [skill, stat_descriptions[skill]])
                        

                        if g.get_stat(skill) < 10:
                            text "  " + str(g.get_stat(skill)) xoffset -35 yalign 0.5 

                        else:
                            text str(g.get_stat(skill)) xoffset -36 yalign 0.5 

                        imagebutton:
                            yalign 0.5
                            xpos -21
                            idle "gui/button/r_arrow_idle.png"
                            hover "gui/button/r_arrow.png"
                            hovered SetVariable("current_tooltip", [skill, stat_descriptions[skill]])
                            unhovered SetVariable("current_tooltip", ["", ""])   
                            if cc_points > 0:
                                action [Function(g.change_stat, stat=skill, val=1), SetVariable("cc_points", cc_points - 1)]
    
        vbox:
            xsize 250
            yalign .2
            style "spacing" 

            vbox:
                text "Health" 
                hbox:
                    add 'gui/custom/round_square_empty.png' xpos 5
                    text str(g.max_hp) xpos -30 yalign 0.5
            # vbox:
            #     text "Stamina" 
            #     hbox:
            #         add 'gui/custom/round_square_empty.png' xpos 5
            #         text str(g.stamina) xpos -30 yalign 0.5
            
            text "Points Remaining " + str(cc_points)
    
    if cc_points <1:
        use my_button("Continue", [Hide("cc_screen"), Jump("new_knight")], 1020, 570)