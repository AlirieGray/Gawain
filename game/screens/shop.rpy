screen shop:
    add "images/town.png"
    add "gui/custom/transparent_bg_600_500.png" xalign .57 yalign .05
    use stats_left
    use hud

    vbox:
        xalign .6 yalign .165
        spacing 12
        xsize 580
        xfill True
        text "Llud's Libations" style "special_font" xalign .5
        use tooltip(current_tooltip, 50, 90, False)

        # TODO: this could be a grid
        # TODO yoffset not the most elegant way to adust padding
        hbox:
            spacing 10
            xfill True
            xalign 0.5
            for i in range(3):
                vbox:
                    add "images/red_potion.png" xalign 0.5
                    text shop.item_names[i] style "medium_text"  
                    text shop.inventory[shop.item_names[i]]['description'] style "little_font" yoffset -10
                    # TODO show description on hover
                    text "Price: " + str(shop.inventory[shop.item_names[i]]['price']) style "little_font" yoffset -20
                    text "Stock: " + str(shop.inventory[shop.item_names[i]]['stock']) style "little_font" yoffset -30
                    textbutton "Purchase" yoffset -45 xalign 0.5 action If((g.gold >= shop.inventory[shop.item_names[i]]['price'] and shop.inventory[shop.item_names[i]]['stock'] > 0), Function(shop.purchase_item, shop.item_names[i]))

        hbox:
            spacing 10
            xfill True
            xalign 0.5
            for j in range(3, 6):
                vbox:
                    add "images/red_potion.png" xalign 0.5
                    text shop.item_names[j] style "medium_text"
                    text shop.inventory[shop.item_names[i]]['description'] style "little_font" yoffset -10
                    text "Price: " + str(shop.inventory[shop.item_names[j]]['price']) style "little_font" yoffset -20
                    text "Stock: " + str(shop.inventory[shop.item_names[j]]['stock']) style "little_font" yoffset -30
                    textbutton "Purchase" yoffset -45 xalign 0.5 action If((g.gold >= shop.inventory[shop.item_names[j]]['price'] and shop.inventory[shop.item_names[j]]['stock'] > 0), Function(shop.purchase_item, shop.item_names[j]))


        textbutton "Close" xalign 0.94 yoffset -50 action[Hide("shop"), Jump("leaving_lludds")]
            