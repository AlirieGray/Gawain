
#TODO: standardize margins and UI layout across game, standardize corner rounding on bgs
# TODO: reset health after combat ends??
# TODO: buttons to take potion, inventory on side screen or in hud
screen stats_left:
    add "gui/custom/transparent_bg_300_700.png" xalign 0.04 yalign 0.2 
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
    add "images/town.jpg"
    add "gui/custom/transparent_bg_600_650.png" xalign .52 yalign .165
    use hud
    use stats_left

    # enemy name and health bar
    vbox:
        xalign 0.5
        yalign 0.1
        text enemy.get_name()
        text "Health: " + str(enemy.hp)
        add enemy.get_image()
        text combat_handler.get_combat_status_string()

    # action buttons
    # TODO: once enemy dies, replace this with a "continue" button
    if combat_handler.player_turn and combat_handler.current_enemy is not None:
        use my_button("Sword Attack", Function(g.attack, attack_type="swordplay", target=enemy), 400, 600)
        use my_button("Bow and Arrow", Function(g.attack, attack_type="archery", target=enemy), 575, 600)
        use my_button("Brawl", Function(g.attack, attack_type="brawling", target=enemy), 750, 600)
    elif combat_handler.current_enemy is None:
        use my_button("Continue", Jump(calendar.next_jump), 750, 600)

