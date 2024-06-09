screen combat_menus(enemy):
    add "gui/custom/transparent_bg_600_500.png" xalign .57 yalign .05
    # use hud
    use stats_left

    vbox:
        xalign .42
        yalign 0.05
        hbox:
            text enemy.get_name()
            text " HP: " + str(enemy.hp)
        hbox:
            text " Gawain "
            text "HP: " + str(g.current_hp)
        imagebutton:

            idle "images/backpack.png"
            hover "images/backpack.png"
            action Show('inventory')
        textbutton "Inventory" action Show('inventory')
        add enemy.get_image() xalign .75