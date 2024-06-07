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