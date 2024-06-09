screen combat_menus(enemy):
    add "gui/custom/transparent_bg_600_500.png" xalign .57 yalign .05
    # use hud
    use stats_left

    vbox:
        xalign .5
        yalign 0.01
        hbox:
            ypos 20
            xpos 50
            vbox:
                text enemy.get_name()
                hbox:
                    bar value StaticValue(enemy.hp, enemy.max_hp):
                        xmaximum 200
                        ymaximum 40
                        left_bar Frame('gui/custom/health_bar_full.png', 10, 0)
                        right_bar Frame('gui/custom/health_bar_empty.png', 10, 0)
                    text str(enemy.hp) + "/" + str(enemy.max_hp) + "    " 
            vbox:
                text "Gawain"
                hbox:
                    bar value StaticValue(g.current_hp, g.max_hp):
                        xmaximum 200
                        ymaximum 40
                        left_bar Frame('gui/custom/health_bar_full.png', 10, 0)
                        right_bar Frame('gui/custom/health_bar_empty.png', 10, 0)
                    text str(g.current_hp) + "/" + str(g.max_hp)
        imagebutton:
            idle "images/backpack.png"
            hover "images/backpack.png"
            action Show('inventory')
        textbutton "Inventory" action Show('inventory')
        add enemy.get_image() xpos 150



                #     vbox:
                # text "Gawain: "
                # bar value VariableValue(g.current_hp, g.max_hp)