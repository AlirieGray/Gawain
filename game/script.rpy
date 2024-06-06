# character creation
default cc_points = 2 # dev value, change to 30 for release
default activities_selected = False
default activities_finished = False
default current_tooltip = ["", ""]

# styles
transform midleft_intro:
    alpha 0.3
    xcenter 0.33
    yalign 0.85
    easein 0.4 alpha 1.0 yalign .4

transform midright_intro:
    alpha 0.3
    xcenter 0.67
    yalign 0.85
    easein 0.4 alpha 1.0 yalign .4

transform midright:
    yalign 0.4
    xcenter .67

transform midleft:
    xcenter 0.33
    yalign 0.4

transform bottomleft:
    xalign 0.5
    yalign 0.5

# The game starts here.

label start:
    # characters
    $ g = Gawain(Character("Gawain"))
    $ l = Lady(Character("Lady of the Lake"))
    # TODO: 50 health is a dev number, should have 10 release
    $ beast_1 = Enemy(Character("Monster"), "Monster", 50, 40, 2, "images/monster.png")

    # handlers
    $ calendar = Calendar()
    $ combat_handler = CombatHandler()


    scene lake

    #####***** INTRO CUTSCENE *****#####


    $ renpy.notify("Click or press spacebar to continue.")

    # "{i}In the land of yore, when kings and queens still ruled over all and knights still roamed the kingdom, you, Gawain, fought valiantly to prove yourself worthy of your place at King Arthur's Round Table.{/i}"
    # "{i}You battled fearsome beasts and loathsome sorcerers, traveled far and wide on many a dangerous quest, and wooed many lusty and kind-hearted maidens alike.{/i}"
    # "{i}The name Sir Gawain the True came to mean peace, honor, reliability, and protection among all of King Arthur's peoples.{/i}"

    # "{i}However, that peace has begun to break down, leaving many confused and terrified in its wake.{/i}"
    # "{i}Lady Guinevere ran off with Sir Lancelot, King Arthur abandoned his throne, and all but one knight has melted into the shadows of the kingdom.{/i}"
    # "{i}Worse still, women have begun disappearing from Herefordshire, never to be seen again.{/i}" 
    # "{i}You, Sir Gawain the True, stand alone, left to pick up the crumbling pieces of the kingdom, starting with finding the missing maidens of Herefordshire.{/i}"
    # "{i}Lost and desperately alone, you, now older, wiser, and stronger than in your youth, decide to visit the Lady of the Lake, hoping for sage council as many a knight have been given in the past.{/i}" 
    
    # "{i}You travel for weeks, your companion Ragamuffin, a Ragdoll cat your son had gifted you, on your shoulder the whole journey.{/i}"
    # "{i}You fear you may be lost, or horribly misguided, until you come upon a gorgeous lake populated by many happy kitties and thriving foliage alike.{/i}"

    # show lady at midright_intro

    # "{i}Emerging from the center of the lake is a stunning woman - the Lady of the Lake. You are quick to kneel in her presence, head bowed respectfully.{/i}"

    # $ l.c("Sir Gawain the True. Fortune smiles upon you on this fine day. What wisdom do you seek?")

    # show gawain at midleft
    # hide lady

    # $ g.c("My Lady, I seek your sage advice, some I hope you can provide.")

    # hide gawain 
    # show lady at midright

    # "{i}The Lady of the Lake giggles at your properness.{/i}"

    # $ l.c("No need to grovel, dearest knight. What do you seek?")

    # hide lady 
    # show gawain at midleft

    # "{i}Your cheeks burn, eyes glittering with mirth as you rise to your feet.{/i}"

    # $ g.c("I appreciate your candidness, my Lady. I do require your guidance. I'm struggling to find my footing after the dissolution of the Round Table") 
    
    # $ g.c("And now women are vanishing from Herefordshire? I am at a loss of how to serve my people when I have no clue where to start.")

    # hide gawain
    # show lady at midright

    # $ l.c("Dearest Gawain, you've been down this path before, haven't you? By Arthur's side, you learned the fates of many a woman.") 
    
    # $ l.c("I have full faith you can help these women find home and peace once again.")

    # hide lady 
    # show gawain at midleft

    # $ g.c("...I understand.")

    # hide gawain
    # show lady at midright

    # $ l.c("I fear this wasn't the guidance you were hoping for, was it, dearest Gawain?") 
    
    # $ l.c("You are capable and strong, you are the last remaining knight of the Round Table. There is little I can provide that you do not already know.")

    # hide lady 
    # show gawain at midleft

    # $ g.c("My Lady, that cannot possibly be true, your power and wisdom far exceeds mine.")

    # hide gawain
    # show lady at midright


    # $ l.c("I am not disagreeing, dearest knight. Tell me, though, do you miss the guidance of Arthur or do you need my advice on your journey? ")

    # hide lady 
    # show gawain at midleft

    # "{i}You hesitate. You thought you were coming for advice, but... the Lady was right. You've been on this journey before, many, many moons ago, when King Arthur still took the throne and the Round Table was still a seat of honor.{/i}"
    
    # $ g.c("I request your blessing, my Lady. I am to go forth to Herefordshire, though I have little desire to proceed alone.")

    # hide gawain
    show lady at midright 

    $ l.c("Well, dearest Gawain, consider this a token of my faith.")

    "{i}The Lady of the Lake offers you a golden, glowing flower teeming with so much arcane energy, your fingertips buzz. You're quick to kneel before her again as you accept her gift, bowing low out of respect.{/i}"

    $ _window_hide()


    #####***** END CUTSCENE *****#####

    # TODO: show tutorial 

    # TODO: disable skip when in certain menus

    show screen cc_screen

    $ renpy.notify("Hover your mouse over a stat to view a description. Assign all points to continue.")

    # TODO: gawain not showing here....?

    show gawain at bottomleft

    $ wait_for_character_creation(cc_points)

    label new_knight:

        # TODO: DEV JUMP ONLY
        # REMOVE FOR BUILD
        jump first_combat_time

        scene lake

        show lady at midright_intro

        $ l.c("My dearest knight, go forth with my blessing.")
        
        # $ l.c("And never hesitate to return to me when you need more sage advice, or a well-intended ear when the journey gets too lonely.")
        
        # $ l.c("Sir Gawain the True, and sweet Ragamuffin, go forth into Herefordshire. May luck be on your side. ")

        hide lady

        jump first_time_in_town

    label first_time_in_town:
        $ calendar.set_next_jump()

        show screen town_screen with fade

        "{i}You travel forth into the countryside, finding your journey to Hereford relatively quick.{/i}" 
        # "{i}You would have no qualms about returning to your Lady as frequently as she suggested.{/i}"
        # "{i}Even with Ragamuffin by your side to soothe the lonely ache in your heart, you still find yourself reeling at the dissolution of the Round Table.{/i}" 
        # "{i}Knowing your Lady is there for you despite you no longer being a Knight of the Round Table lets you breathe a sigh of relief, vigor for the journey ahead restored.{/i}" 
        # "{i}You rent a room at the local inn and settle in for some heavy-duty detective work, ready to get to the bottom of the disappearing women of Herefordshire, starting with the main city of Hereford.{/i}" 
        # "{i}Now to start exploring Hereford... which is teeming with cats?{/i}"

        $ _window_hide()

        # TODO: tutorial

        show screen town_menus

        $ wait_for_status(activities_selected)
    
    label go_to_town:
        $ calendar.set_next_jump()

        show screen town_screen
        
        # TODO: different "bark" for each week/month
        $ g.c("This is the town, where I can do activities.")

        show screen town_menus

        $ wait_for_status(activities_selected)

    label tasks_only:
        show screen town_screen

        $ g.c("I wonder what awaits me this week...")

        show screen task

        $ wait_for_status(activities_finished)

        $ g.c("okay moving on....")

        hide screen task

        jump go_to_town

    label first_combat_time:

        $ (" Suddenly, a loud roar echoes through the town, emanating through the streets with enough power to shake window panes and send birds into flight.")

        $ combat_handler.set_enemy(beast_1)

        show screen combat_menus(beast_1)

        # TODO: automatically go to the next month 
        # combat should actually happen at the END of the fourth week, not the beginning

        $ wait_for_status(activities_finished)

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

    label visit_lake:
        scene lake

        show lady at midright_intro

        $ l.c("Welcome back, Sir Gawain.")

        # TODO: wait for user to go back to town? or go back to town ourselves 

    # This ends the game.

    return
