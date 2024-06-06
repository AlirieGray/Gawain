# TODO: button should show when disabled, but be grayed-out...
screen my_button(button_text, button_action, x_position, y_position):
    button:
        xpos x_position
        ypos y_position
        idle_background "gui/custom/button.png"
        hover_background "gui/custom/button_hover.png"
        style "my_button_text"
        xysize (200, 70)
        text button_text xalign 0.5 xfill True yoffset 5 xoffset -25
        action button_action 

screen tooltip(tooltip_text, x_position, y_position, close_button): 
    if tooltip_text[0] != "":
        add "gui/custom/transparent_bg_450_300.png" xpos x_position ypos y_position
        vbox:
            xsize 390
            xpos x_position + 30
            ypos y_position + 20
            spacing 2
            text tooltip_text[0].title() style "special_font"
            text tooltip_text[1] style "tooltip_text"
            if close_button:
                textbutton "Close" action Hide("tooltip") xalign 0.9