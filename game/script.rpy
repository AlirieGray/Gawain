# character creation
default cc_points = 2 # dev value, change to 30 for release
default activities_selected = False
default activities_finished = False

# styles
transform midleft_intro:
    alpha 0.3
    xcenter 0.33
    yalign 0.85
    easein 0.5 alpha 1.0 yalign .63

transform midright_intro:
    alpha 0.3
    xcenter 0.67
    yalign 0.85
    easein 0.5 alpha 1.0 yalign .63

transform midright:
    yalign 0.63
    xcenter .67

transform midleft:
    xcenter 0.33
    yalign 0.63

# The game starts here.

label start:
    # characters
    $ g = Gawain(Character("Gawain", who_xpos = 100))
    $ l = Lady(Character("Lady of the Lake", who_xpos = 600))

    # handlers
    $ calendar = Calendar()


    scene lake

    #####***** INTRO CUTSCENE *****#####

    "In the land of yore, when kings and queens still ruled over all and knights still roamed the kingdom, young Gawain fought valiantly to prove himself worthy of his place at King Arthur's Round Table." 

    # TODO: show tooltip indicating click or press spacebar to continue...
    
    "He battled fearsome beasts and loathsome sorcerers, traveled far and wide on many a dangerous quest, and wooed many lusty and kind-hearted maidens alike." 
    
    "The name Sir Gawain the True came to mean peace, honor, reliability, and protection among all of King Arthur's peoples." 
    
    "However, that peace has begun to break down, leaving many confused and terrified in its wake." 

    "Lady Guinevere ran off with Sir Lancelot, King Arthur abandoned his throne, and all but one knight has melted into the shadows of the kingdom." 

    "Worse still, women have begun disappearing from Herefordshire, never to be seen again." 

    "Sir Gawain the True stands alone, left to pick up the crumbling pieces of the kingdom, starting with finding the missing maidens of Herefordshire. "

    "Lost and desperately alone, Sir Gawain, now older, wiser, and stronger than in his youth, decides to visit the Lady of the Lake, hoping for sage council as many a knight have been given in the past."

    $ _window_hide()

    #####***** END CUTSCENE *****#####

    # $ g.c("The name's Gawain. Sir Gawain.")

    # TODO: show tutorial 

    show screen cc_screen

    # show gawain at midleft

    $ wait_for_character_creation(cc_points)

    label new_knight:

        scene lake

        show lady at midright_intro

        $ l.c("I am the Lady of the Lake, and this is the introductory scene.")

        hide lady

        show gawain at midleft

        $ g.c("Hello, Lady of the Lake.")

        jump go_to_town

    
    label go_to_town:
        $ calendar.set_next_jump()

        show screen town_screen
        
        # TODO: different "bark" for each week/month
        $ g.c("This is the town, where I can do activities.")

        show screen town_menus

        $ wait_for_status(activities_selected)

    label tasks_only:
        $ g.c("I wonder what awaits me this week...")

        show screen task

        $ wait_for_status(activities_finished)

        $ g.c("okay moving on....")

        hide screen task

        jump go_to_town

    label first_story_event:
        $ g.c("Haha! My test worked!")

        $ g.c("Time for my first task....")

        # $ week_outcomes = execute_week(calendar, g)

        show screen task

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
