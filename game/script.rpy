# character creation
default cc_points = 2 # dev value, change to 30 for release
default activities_selected = False
default activities_finished = False

# The game starts here.

label start:
    # characters
    $ g = Gawain(Character("Gawain"))
    $ l = Lady(Character("Lady of the Lake"))

    # handlers
    $ calendar = Calendar()

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
        
        # TODO: different "bark" for each week/month
        $ g.c("This is the town, where I can do activities.")

        show screen town_menus

        $ wait_for_status(activities_selected)

    label first_story_event:
        $ g.c("Haha! My test worked!")

        $ g.c("Time for my first task....")

        # $ week_outcomes = execute_week(calendar, g)

        show screen task(calendar, g)

        $ wait_for_status(activities_finished)

        $ g.c("okay moving on....")

        # increment week and go back to town

        # $ calendar.increment_week()

        hide screen task

        jump go_to_town

    label second_story_event:
        $ g.c("This should be running IFF it's blood month or whatever")

    # This ends the game.

    return
