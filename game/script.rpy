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
    define ll = Character("Llud")
    define d = Character("Drunk Man")
    define f = Character("Florian")
    define o = Character("Olive")
    define e = Character("Enid")
    define lun = Character("Lunete")

    # TODO: 50 health is a dev number, should have 10 release
    $ beast_1 = Enemy(Character("Monster"), "Monster", 10, 40, 2, "images/monster.png")

    # handlers
    $ calendar = Calendar()
    $ combat_handler = CombatHandler()


    scene lake

    #####***** INTRO CUTSCENE *****#####


    $ renpy.notify("Click or press spacebar to continue.")

    # jump lluds # TODO DEV JUMP ONLY

    
    # TODO: DEV JUMP ONLY
    # REMOVE FOR BUILD
    # jump first_combat_time
    jump go_to_town

    "In the land of yore, when kings and queens still ruled over all and knights still roamed the kingdom, you, Gawain, fought valiantly to prove yourself worthy of your place at King Arthur's Round Table."
    "You battled fearsome beasts and loathsome sorcerers, traveled far and wide on many a dangerous quest, and wooed many lusty and kind-hearted maidens alike."
    "The name Sir Gawain the True came to mean peace, honor, reliability, and protection among all of King Arthur's peoples."

    "However, that peace has begun to break down, leaving many confused and terrified in its wake."
    "Lady Guinevere ran off with Sir Lancelot, King Arthur abandoned his throne, and all but one knight has melted into the shadows of the kingdom."
    "Worse still, women have begun disappearing from Herefordshire, never to be seen again." 
    "You, Sir Gawain the True, stand alone, left to pick up the crumbling pieces of the kingdom, starting with finding the missing maidens of Herefordshire."
    "Lost and desperately alone, you, now older, wiser, and stronger than in your youth, decide to visit the Lady of the Lake, hoping for sage council as many a knight have been given in the past." 
    
    "You travel for weeks, your companion Ragamuffin, a Ragdoll cat your son had gifted you, on your shoulder the whole journey."
    "You fear you may be lost, or horribly misguided, until you come upon a gorgeous lake populated by many happy kitties and thriving foliage alike."

    show lady at midright_intro

    "Emerging from the center of the lake is a stunning woman - the Lady of the Lake. You are quick to kneel in her presence, head bowed respectfully."

    $ l.c("Sir Gawain the True. Fortune smiles upon you on this fine day. What wisdom do you seek?")

    show gawain at midleft
    hide lady

    $ g.c("My Lady, I seek your sage advice, some I hope you can provide.")

    hide gawain 
    show lady at midright

    "The Lady of the Lake giggles at your properness."

    $ l.c("No need to grovel, dearest knight. What do you seek?")

    hide lady 
    show gawain at midleft

    "Your cheeks burn, eyes glittering with mirth as you rise to your feet."

    $ g.c("I appreciate your candidness, my Lady. I do require your guidance. I'm struggling to find my footing after the dissolution of the Round Table") 
    
    $ g.c("And now women are vanishing from Herefordshire? I am at a loss of how to serve my people when I have no clue where to start.")

    hide gawain
    show lady at midright

    $ l.c("Dearest Gawain, you've been down this path before, haven't you? By Arthur's side, you learned the fates of many a woman.") 
    
    $ l.c("I have full faith you can help these women find home and peace once again.")

    hide lady 
    show gawain at midleft

    $ g.c("...I understand.")

    hide gawain
    show lady at midright

    $ l.c("I fear this wasn't the guidance you were hoping for, was it, dearest Gawain?") 
    
    $ l.c("You are capable and strong, you are the last remaining knight of the Round Table. There is little I can provide that you do not already know.")

    hide lady 
    show gawain at midleft

    $ g.c("My Lady, that cannot possibly be true, your power and wisdom far exceeds mine.")

    hide gawain
    show lady at midright


    $ l.c("I am not disagreeing, dearest knight. Tell me, though, do you miss the guidance of Arthur or do you need my advice on your journey? ")

    hide lady 
    show gawain at midleft

    "You hesitate. You thought you were coming for advice, but... the Lady was right. You've been on this journey before, many, many moons ago, when King Arthur still took the throne and the Round Table was still a seat of honor."
    
    $ g.c("I request your blessing, my Lady. I am to go forth to Herefordshire, though I have little desire to proceed alone.")

    hide gawain
    show lady at midright 

    $ l.c("Well, dearest Gawain, consider this a token of my faith.")

    "The Lady of the Lake offers you a golden, glowing flower teeming with so much arcane energy, your fingertips buzz. You're quick to kneel before her again as you accept her gift, bowing low out of respect."

    $ _window_hide()


    #####***** END CUTSCENE *****#####

    # TODO: show tutorial 

    # TODO: disable skip when in certain menus

    show screen cc_screen

    $ renpy.notify("Hover your mouse over a stat to view a description. Assign all points to continue.")

    show gawain at bottomleft

    $ wait_for_character_creation(cc_points)

    label new_knight:

        scene lake

        show lady at midright_intro

        $ l.c("My dearest knight, go forth with my blessing.")
        
        $ l.c("And never hesitate to return to me when you need more sage advice, or a well-intended ear when the journey gets too lonely.")
        
        $ l.c("Sir Gawain the True, and sweet Ragamuffin, go forth into Herefordshire. May luck be on your side. ")

        hide lady

        jump first_time_in_town

    label first_time_in_town:
        $ calendar.set_next_jump()

        scene town with fade

        "You travel forth into the countryside, finding your journey to Hereford relatively quick." 
        "You would have no qualms about returning to your Lady as frequently as she suggested."
        "Even with Ragamuffin by your side to soothe the lonely ache in your heart, you still find yourself reeling at the dissolution of the Round Table." 
        "Knowing your Lady is there for you despite you no longer being a Knight of the Round Table lets you breathe a sigh of relief, vigor for the journey ahead restored." 
        "You rent a room at the local inn and settle in for some heavy-duty detective work, ready to get to the bottom of the disappearing women of Herefordshire, starting with the main city of Hereford." 
        "Now to start exploring Hereford... which is teeming with cats?"

        $ _window_hide()

        # TODO: tutorial

        show screen town_menus

        $ current_tooltip = ["Selecting Activities", "Each week you can pick one task to earn gold and increase your skills.\nHover over a building to see what the gold and skills reward for completing that task will be.\nClick on a building to set this week's activity."]
        show screen tooltip(current_tooltip, 400, 200, True)

        $ wait_for_status(activities_selected)
    
    label go_to_town:
        $ calendar.set_next_jump()

        scene town
        
        # TODO: different "bark" for each week/month
        show gawain at midleft_intro
        $ g.c("Another week in Hereford. What should I do this week?")
        hide gawain

        show screen town_menus

        $ wait_for_status(activities_selected)

    label tasks_only:
        scene town

        show screen task

        $ wait_for_status(activities_finished)

        hide screen task

        jump go_to_town

    label first_combat_time:

        scene town

        "Suddenly, a loud roar echoes through the town, emanating through the streets with enough power to shake window panes and send birds into flight."

        $ combat_handler.set_enemy(beast_1)

        show screen combat_menus(beast_1)

        while g.current_hp > 0 and combat_handler.current_enemy:
            menu:
                "Sword Attack":
                    $ combat_handler.gawain_attack("swordplay")
                "Bow and Arrow":
                    $ g.attack("archery", beast_1)
                    $ combat_handler.gawain_attack("archery")
            "[str(combat_handler.combat_status_string)]" 

            if combat_handler.current_enemy:

                $ combat_handler.enemy_attack()

                "[str(combat_handler.combat_status_string)]"

        hide screen combat_menus

        jump visit_lake
            
        # TODO: automatically go to the next month 


    ####**** TAVERN SCENES ****####


    label first_tavern_event:
        "You enter the tavern to see a single drunk man alone at the bar." 

        menu:
            "Do you speak to him?"

            "Yes":
                show gawain at midleft_intro
                $ g.c("Excuse me, sir? May I ask you a few questions?")
                hide gawain

                d "Sir? I'm younger than *hic* you. I'll give you one question before I punch you in the mouth for that, *sir*."

                show gawain at midleft
                $ g.c("My apologies, young man. May I ask..? ")

                menu: 
                    "Ask about the missing women":
                        $ g.c("I see you have a wedding ring yourself. Is your wife still living with you?")

                        hide gawain

                        d "My good-for-nothing *hic* wife ran off months ago. Just like her to disappear when the *hic* going gets tough. We’d just had a baby girl."

                        show gawain at midleft

                        $ g.c("So she left you to take care of your daughter?")

                        hide gawain

                        d "Heavens no! *hic* I got rid of that brat first chance I could."
                        
                        d "The blasted thing wouldn’t stop crying. Gave her to the *hic* nunnery a few cities over. Serves my wife right for leavin’. *hic*"

                        show gawain at midleft

                        $ g.c("I see. I’ll leave you to your drink, good sir. Apologies for the intrusion.")

                        hide gawain

                        d "STOP CALLIN’ ME SIR! *hic* "

                    "Ask about the cats":

                        $ g.c("Any idea where all these cats came from?")
                        hide gawain

                        d "You think I care about those *hic* vermin? All I know is my wife got one a few months ago and *hic* now both her and the cat are gone. Just glad I don't have to take care of the damn thing. *hic*"

                        show gawain at midleft
                        $ g.c("So your wife took the cat with her?")
                        hide gawain

                        d "Or the blasted thing ran away. I don't rightly know and I don't rightly *hic* care."

                        show gawain at midleft

                        $ g.c("Well, then. I see. I’ll leave you to your drink and stop asking you questions, good sir.")

                        hide gawain

                        d "STOP CALLIN’ ME SIR! *hic*"
            "No":
                "The bartender gives you a drink on the house."
        $ calendar.set_played('tavern', 0)
        jump tasks_only


    label second_tavern_event:
        "You enter the tavern and see a miserable looking man alone at the bar. He has a wedding ring."

        menu: 
            "Do you talk to him?"

            "Yes":
                show gawain at midleft_intro
                $ g.c ("Hello there, good man, I am Sir Gawain. Pardon my intrusion, may I ask you a few questions about the missing wives in town?")
                
                $ g.c("I see you have a wedding ring yourself; is your wife still in Hereford?")

                hide gawain

                f "No, my bloody wife isn’t still here!"
                
                f "Why would I be here drinking if I could be in the presence of my beautiful, angelic Anglides was still here!"

                show gawain at midleft 
                if g.stats_dict['mettle'] > 10:
                    menu:
                        "Soothe Florian":
                            $ g.c("My, I’m terribly sorry for poking at such a festering wound. May it soothe you that I’m on the hunt for the missing women of Herefordshire.")

                            hide gawain 

                            f "*sniffle* It does. Thank you, Sir Gawain."

                            show gawain at midleft

                            $ g.c("It’s my pleasure, truly. Stay safe, Florian.")

                            hide gawain
                        
                        "Balk":
                            $ g.c("My, no need to get so feisty, Florian. I assure you, I’m on the case.")

                            hide gawain

                            f "Don’t you understand?! My wife is missing, and her little kitty she loved so dearly! I must find her!"

                            "Florian rises to his feet, stumbling out the door and into the street."

                            f "I MUST FIND ANGLIDES!"
                else:
                    menu:
                        "Soothe Florian (NOT ENOUGH METTLE)":
                            "...."
                        
                        "Balk":
                            $ g.c("My, no need to get so feisty, Florian. I assure you, I’m on the case.")

                            hide gawain

                            f "Don’t you understand?! My wife is missing, and her little kitty she loved so dearly! I must find her!"

                            "{i}Florian rises to his feet, stumbling out the door and into the street.{/i}"

                            f "I MUST FIND ANGLIDES!"

            "No":
                "You have a nice meal at the tavern."

        $ calendar.set_played('tavern', 1)
        jump tasks_only

    ####**** WASHING WELL SCENES ****####

    label first_wash_event:
        o "Excuse me, sir? You look new in town - are you here to find the missing women?"

        show gawain at midleft_intro

        $ g.c("Yes I am, miss. My name is Sir Gawain. Have you any information that may help my search?")

        hide gawain

        o "Titled, I see. What an honor. *wink* I’m Olive, pleasure to meet you, Sir Gawain. My mother has joined the missing women."

        show gawain at midleft
        
        $ g.c("Were there any signs she would leave? Was there anything she told you?")

        hide gawain

        o "No, she told me nothing. She left my father and I to care for my siblings alone. She did take her cat, though."

        show gawain at midleft

        $ g.c("She had a cat?")

        hide gawain

        o "Yes, a cat."
        
        o "I’ve had to postpone my wedding to pick up the pieces of our family, and she’s out galavanting with her cat. That’s what Father says, anyways."

        show gawain at midleft
        if g.stats_dict['charm'] > 15:
            menu:
                "Challenge":

                    $ g.c("You don’t think there could have been a less… heartless reason she may have left?")

                    hide gawain

                    "Olive hesitates, seeming caught off-guard."

                    o "Potentially. I do find myself quite exhausted from filling her shoes. Mayhaps she needed a vacation."

                    show gawain at midleft

                    $ g.c("Mayhaps. My sincerest apologies you’ve been left to rise to the occasion when you’re meant to be forming a family of your own.")
                    
                    $ g.c("I’m sure your family appreciates it.")

                    hide gawain

                    o "Thank you, Sir Gawain. I find I understand my mother better after this. Good day."
                    
                "Agree":
                    $ g.c("Well, I’ll be sure to take note of that, then.")

                    hide gawain

                    "{i}Seems the women are fleeing the town, regardless of what family they leave behind.{/i}"
        else:
            menu:
                "Challenge (NOT ENOUGH CHARM)":
                    "..."
                "Agree":
                    $ g.c("Well, I’ll be sure to take note of that, then.")

                    "{i}Seems the women are fleeing the town, regardless of what family they leave behind.{/i}"

        $ calendar.set_played('wash', 0)
        jump tasks_only
           
    label second_wash_event:
        "The cat says nothing, just stares up at you knowingly. He scurries off when you try to pet him." 
        if calendar.scenes_played['first_cat_haven']:
            "There are more cats roaming the city than just the ones you’ve met at the Cat Haven, and they all seem to know you."

        $ calendar.set_played('wash', 1)
        jump tasks_only

    label third_wash_event:
        show gawain at midleft_intro

        $ g.c("Pardon me, ma’am, my name is Sir Gawain. I notice you have a wedding ring on, may I ask if you know anything about the disappearing wives?")

        hide gawain
        
        e "Good day, Sir Gawain. I am Enid, widow of Emrys. I knew all the women who have fled from Hereford."
        
        e "Have you any questions for me?"

        show gawain at midleft

        $ g.c("You call it fleeing, why do you label their disappearances as such? Do you know where they have ‘fled’ to?")

        e "I know not where they are, just… that I don’t blame them for leaving. The men in this town often forget to mind their wives while their wives mind the homes."
        
        e "Have you a wife, Sir Gawain?"

        show gawain at midleft

        $ g.c("I’ve had many wives, yes.")

        hide gawain

        e "And did you love them? Did you tend to them? Did you make them happy?"

        show gawain at midleft

        $ g.c("I did my best to. I loved each of my wives in their own ways.")

        hide gawain

        e "Then you are a rare breed, Sir Gawain."
        
        e "I miss my friends, I miss my sisters, though I do not feel their disappearance is unwarranted. Not everyone can handle their husbands like I."

        show gawain at midleft
        
        $ g.c("...Well, thank you for your time, Enid. I fear I still have much to learn.")

        hide gawain

        $ calendar.set_played('wash', 2)
        jump tasks_only

    label fourth_wash_event:
        "The cat says nothing, just stares up at you knowingly. She scurries off when you try to pet her."

        menu:
            "Follow her":
                "You chase after the cat as she tries to flee, all the way to the forest line. She disappears behind a bush before you can follow."
                
                "Seems the cats live in the forest when not in the city."

                # TODO: + intuition
            "Leave her be":
                "You watch the cat disappear into an alleyway, becoming one with the shadows."
                # TODO + mettle

        $ calendar.set_played('wash', 3)
        jump tasks_only

    label wash_no_event:
        # TODO: randomize barks for no event tasks
        "You learn an old wives’ tale to help you in battle."
        jump tasks_only


    ####**** CAT HAVEN SCENES ****#### 


    ####**** INN SCENES ****####

    label first_inn_event:
        lun "Greetings, traveler! Did you have an issue with your room?"
        
        show gawain at midleft_intro
        
        $ g.c("No, ma’am, my room is quite nice. Thank you for your hospitality. I actually have some questions for you, if you don’t mind my intrusion.")
        
        hide gawain
        
        lun "Of course, ask away!"
        
        show gawain at midleft
        
        $ g.c("I see you have a wedding ring; all the women that have left have been wed. Have you heard any whispers of plans to leave, or anyone approaching these women to ask them to leave?")
        
        hide gawain

        lun "I myself have heard nothing. My husband and I work hard to keep this inn a place of respite from such troubles."
        
        show gawain at midleft
       
        $ g.c("Have you ever considered leaving yourself?")
        
        hide gawain
        
        lun "Leave Aurelius? Oh, heavens, no. I love that man more than life itself, and I’m positive he feels the same."
        
        show gawain at midleft
        
        $ g.c("Do the other women in town have the same security? Could they have been lured by forces you have not?")
        
        hide gawain
        
        lun "…Well, I do see many of their husbands entertaining guests here. I would assume they do not have such a luxury as a man as stable and loving as Aurelius."
        
        show gawain at midleft
        
        $ g.c("And no one has approached you to join or aid them?")
        
        hide gawain
        
        lun "No, but I shall let you know if someone has. Thank you for your dedication, Sir Gawain. Your quest is quite admirable. Have a good night."
        
        show gawain at midleft
        
        $ g.c("You have a good night, too. And thank you for keeping a listening ear out for me.")
        
        hide gawain

        $ calendar.set_played('inn', 0)
        jump tasks_only

    label inn_hunters_moon:
        lun "Sir Gawain! May I speak to you for a moment?"

        show gawain at midleft_intro

        $ g.c("Of course, Lunete. How may I be of service?")
        hide gawain

        lun "I have the information you seek. I was approached by a cat which I named Catthew. I… I am unsure how I came up with the name, it just felt right. "
        show gawain at midleft

        $ g.c("Catthew, yes, I know the cat you speak of. Quite an adorable little guy.")
        hide gawain

        lun "He is quite sweet. But I invited him to live with Aurelius and I, and Catthew was, well, a terror to say the least. He shredded my clothes, ate every loaf of bread I brought home, and expelled his humors on my bed sheets every night! This dress I have on is the only one I have left!"
        show gawain at midleft

        $ g.c("Catthew did all that? But he seemed like such a sweet boy.")
        hide gawain

        lun "Catthew isn’t even the one I’m the most upset with. Aurelius brushed it all off on me, saying it was my fault because I brought the cat in. He didn’t help clean a single hairball this entire time. I’m at my wit’s end with that man! "
        show gawain at midleft

        $ g.c("Really? Aurelius?")
        hide gawain

        lun "I don’t rightly know what’s gotten into him! My Aurelius would never abandon someone while they’re struggling, but… it seems Catthew is his exception. I let Catthew back into the streets, thinking he would be happier not living in our home anymore, but he keeps waiting by our front door each night. My heart aches for that poor, scared kitty, but Aurelius won’t let me let him back in. "
        show gawain at midleft

        $ g.c("Will you and Aurelius be okay?")
        hide gawain

        lun "We’re going to have to be. I’m extremely disappointed in him right now, but… I have nowhere else to go. And our niece, Albiona, needs me while Florian is in such a tizzy. I can’t leave. "
        
        show gawain at midleft

        $ g.c("That makes it seem like you want to.")
        hide gawain

        lun "I don’t know, maybe I do. But my part of our arrangement was fulfilled. You asked me to report if I was approached by anyone, and I was only approached by a cat. I’m too frazzled to be of much help going forward, Sir Gawain. Hopefully this is enough. "
        show gawain at midleft

        $ g.c("I understand, Lunete. You focus on your family. Leave the rest to me. Maybe I’ll see if I can find Catthew…")
        hide gawain

        lun "And don’t bring him back in! The only cat I want to see around these parts is Ragamuffin. "

        "Lunete reaches out to pet Ragamuffin, who purrs happily." 
        
        lun "Good kitty. And thanks for listening, Sir Gawain. "
        
        show gawain at midleft

        $ g.c("It’s my pleasure. Take care, Lunete")
        hide gawain

        $ calendar.set_played('inn', 1)
        jump tasks_only


    label inn_no_event:
        "Rest up for the search ahead."
        jump tasks_only


    label lluds:
        scene town 

        ll "Welcome to Llud's Libations!"

        $ _window_hide()

        show screen shop

        $ wait_for_status(activities_selected)


    label visit_lake:
        scene lake with fade

        show lady at midright_intro

        $ l.c("Welcome back, Sir Gawain.")

        jump go_to_town

        # TODO: wait for user to go back to town? or go back to town ourselves 

    # This ends the game.

    return
