#TODO: standardize margins and UI layout across game, standardize corner rounding on bgs
# TODO: reset health after combat ends??
# TODO: buttons to take potion, inventory on side screen or in hud
screen stats_left:
    add "gui/custom/transparent_bg_300_500.png" xalign 0.03 yalign 0.05 
    vbox:
        xalign .08
        yalign .09
        spacing 7
        for attribute in attributes:
            vbox:
                spacing 1
                text attribute.title() xpos 10 ypos 9
                hbox:
                    spacing 6
                    bar value StaticValue(g.get_stat(attribute), 100):
                        xmaximum 200
                        ymaximum 40
                        left_bar Frame("gui/custom/round_rectangle_full.png", 10, 0)
                        right_bar Frame("gui/custom/round_rectangle_empty.png", 10, 0)
                    text str(g.get_stat(attribute)) yalign 0.5
        for skill in skills:
            vbox:
                spacing 1
                text skill.title() xpos 10 ypos 9
                hbox:
                    spacing 6
                    bar value StaticValue(g.get_stat(skill), 100):
                        xmaximum 200
                        ymaximum 40
                        left_bar Frame("gui/custom/round_rectangle_full.png", 10, 0)
                        right_bar Frame("gui/custom/round_rectangle_empty.png", 10, 0)
                    text str(g.get_stat(skill)) yalign 0.5


# TODO: disabled button styling for other buttons besides start week
screen my_button(button_text, button_action, x_position, y_position):
    if button_action:
        button:
            xpos x_position
            ypos y_position
            idle_background "gui/custom/button.png"
            hover_background "gui/custom/button_hover.png"
            style "my_button_text"
            xysize (200, 70)
            text button_text xalign 0.5 xfill True yoffset 5 xoffset -25
            action button_action 
    else:
        add "gui/custom/button_disabled.png" xpos x_position ypos (y_position - 35)
        text button_text xpos (x_position + 25) ypos (y_position - 30) style "disabled_button"

screen tooltip(tooltip_text, x_position, y_position, close_button): 
    if tooltip_text[0] != "":
        add "gui/custom/transparent_bg_450_300.png" xpos x_position ypos y_position
        vbox:
            xsize 390
            xpos x_position + 30
            ypos y_position + 20
            spacing 2
            text tooltip_text[0].title() style "special_font"
            text tooltip_text[1] style "medium_text"
            if close_button:
                textbutton "Close" action Hide("tooltip") xalign 0.9

# TODO should be a way to set modal with a screen parameter?
screen tooltip_modal(tooltip_text, x_position, y_position): 
    modal True
    if tooltip_text[0] != "":
        add "gui/custom/transparent_bg_450_300.png" xpos x_position ypos y_position
        vbox:
            xsize 390
            xpos x_position + 30
            ypos y_position + 20
            spacing 2
            text tooltip_text[0].title() style "special_font"
            text tooltip_text[1] style "medium_text"
    textbutton "Close" action Hide("tooltip_modal") xpos x_position + 385 ypos y_position + 255