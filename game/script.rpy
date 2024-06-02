# character creation
default cc_points = 2 # dev value, change to 30 for release
default ready_for_week = False


# The game starts here.

label start:
    # characters
    $ g = Gawain(Character("Gawain"))
    $ l = Lady(Character("Lady of the Lake"))

    scene lake_cc

    # $ g.c("The name's Gawain. Sir Gawain.")

    show screen cc_screen

    $ wait_for_character_creation(cc_points)

    label new_knight:

        scene lake

        $ l.c("I am the Lady of the Lake, and this is the introductory scene.")

        jump go_to_town

    
    label go_to_town:
        show screen town_screen
        
        $ g.c("This is the town, where I can do activities.")

        $ wait_for_activity_selection(ready_for_week)

        show screen town_menus


    # This ends the game.

    return
