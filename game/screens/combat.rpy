
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


screen combat_menus(enemy):
    # TODO: use scary forest image
    add "images/town.png"
    add "gui/custom/transparent_bg_800_500.png" xalign .8 yalign .04
    # use hud
    use stats_left

    # enemy name and health bar
    vbox:
        xalign 0.7
        yalign 0.05
        hbox:
            text enemy.get_name()
            text " HP: " + str(enemy.hp)
            text "                  Gawain "
            text "HP: " + str(g.current_hp)
        add enemy.get_image()