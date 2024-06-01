# character creation
default cc_points = 20


# The game starts here.

label start:
    # characters
    $ g = Gawain(Character("Gawain"))
    $ l = Lady(Character("Lady of the Lake"))

    scene lake

    # $ g.c("The name's Gawain. Sir Gawain.")

    # $ l.c("I am the Lady of the Lake, and this is the introductory scene.")

    show screen cc_screen

    $ wait_for_character_creation(cc_points)

    # This ends the game.

    return
