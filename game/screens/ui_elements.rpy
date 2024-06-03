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