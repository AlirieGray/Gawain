# character creation
default cc_points = 30 # dev value, change to 30 for release
default activities_selected = False
default activities_finished = False
default current_tooltip = ["", ""]
default town_tutorial = ["Selecting Activities", "Each week you can visit one location to visit to learn more about the mysteries surrounding Hereford, as well as earn gold and increase your skills.", "You can also visit Llud's Libations at any time to buy potions that will help you in battle.", "Hover over a building to see what skills you can improve by spending the week at that location.", "Click on a building to set this week's activity, then press the Start Week button."]
default end_month_tutorial = [
    "Ending the Month",
    "This month is coming to an end. Press the End Month button to return to the lake and seek the counsel of your Lady.",
    "Your time in Hereford has been peaceful so far, but you've heard rumors of foul beasts that show themselves around the full moon.\nIf you wish to stock up on any potions, stop by Llud's Libations before ending the month.",
]
default flirted_with_lady = False

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
    define s = Character("Shrimp")
    define m = Character("Mittens")
    define cm = Character("Crying Man")
    define b = Character("Bryan")
    define c = Character("Crisea")
    define who = Character("??")
    define morg = Character("Morgana")
    define i = Character("Isoude")


    $ beast_1 = Enemy(Character("Monster"), "Monster", 10, 40, 2, "images/monster.png")
    $ beast_2 = Enemy(Character("Monster"), "Monster", 20, 40, 2, "images/monster.png")
    $ beast_3 = Enemy(Character("Monster"), "Monster", 35, 40, 2, "images/monster.png")
    $ beast_4 = Enemy(Character("Monster"), "Monster", 50, 40, 2, "images/monster.png")
    $ beast_5 = Enemy(Character("Monster"), "Monster", 75, 40, 2, "images/monster.png")
    $ big_boss = Enemy(Character("Monster"), "Monster", 100, 40, 2, "images/monster.png")

    # handlers
    $ calendar = Calendar()
    $ combat_handler = CombatHandler()
    $ shop = Shop()


    scene lake

    #####***** INTRO CUTSCENE *****#####


    $ renpy.notify("Click or press spacebar to continue.")

    
    # TODO: DEV JUMP ONLY
    # REMOVE FOR BUILD
    # jump first_combat_time
    # jump go_to_town
    # jump first_time_in_town
    # jump lluds

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

        show screen town_menus

        show screen tutorial_modal(town_tutorial)

        $ wait_for_status(activities_selected)
    
    label go_to_town:
        $ calendar.set_next_jump()

        scene town

        if calendar.current_week == 4:
            if calendar.current_month == 0:
                "Another month comes to an end..."

                show screen tutorial_modal(end_month_tutorial)

            else:
                "Another month comes to an end..."

            show screen town_menus_month_end

        else:
        
            # TODO: different "bark" for each week/month
            show gawain at midleft
            $ g.c("Another week in Hereford. What should I do this week?")
            hide gawain

            show screen town_menus

        $ wait_for_status(activities_selected)

    ####**** COMBATS/BATTLES ****####

    label first_combat:

        scene town
        
        "You see Lunete, the Innkeeper, run up to you as you’re on an evening stroll." 
        
        lun "Sir Gawain! There’s a beast eating Enid’s cows! You have to come protect them!"
        
        "Just as you’re about to rush off, Lunete reaches to catch your arm." 
        
        lun "Do you need me to watch Ragamuffin while you do so? I’d hate for her to get hurt."
        
        $ g.c("Thank you, Lunete, but she’s my trusted companion. We’ve faced many beasts together; I watch her back and she watches mine. I need her by my side.")
        
        lun "That’s… really adorable. Good luck, Sir Gawain and Ragamuffin."

        $ combat_handler.set_enemy(beast_1)

        jump combat

    label second_combat:
        "You see Olive, a citizen of Hereford, run up to you as you’re on an evening stroll. "
        
        o "Sir Gawain! There’s a fearsome beast eating all of Bryan’s cows! Please, you must save them!"

        $ combat_handler.set_enemy(beast_2)

        jump combat

    label third_combat:
        "You’re enjoying a hearty meal in the tavern with Ragamuffin when the sounds of screams outside draw your attention."
        
        "A beast is wreaking havoc on the town square, though thankfully no one looks hurt yet."

        $ combat_handler.set_enemy(beast_3)

        jump combat

    label fourth_combat:
        "You’re asleep in the dead of night when a deathly roar echoes through the town."
        
        "A beast is once again ravaging the town square, causing tons of destruction."

        $ combat_handler.set_enemy(beast_4)

        jump combat

    label fifth_combat:
        "As you’re letting Ragamuffin stretch her legs and play in the brush on the edge of the forest, a huge beast leaps in front of you, looking to pounce at Ragamuffin!"

        $ combat_handler.set_enemy(beast_5)
        
        jump combat

    label boss_fight:
        "A young girl alone picking flowers on the edge of town screams once she sees she’s in the cat’s sights, scrambling to her feet as she desperately tries to get away."
        
        "You draw your sword; you don't even hesitate for a moment before you’re charging into the fray, sprinting forward to put yourself between the giant cat and the innocent little child." 
        
        $ combat_handler.set_enemy(big_boss)
        
        show screen combat_menus(combat_handler.current_enemy)

        while g.current_hp > 0 and combat_handler.current_enemy:
            menu:
                "Sword Attack":
                    $ combat_handler.gawain_attack("swordplay")
                "Bow and Arrow":
                    $ g.attack("archery", combat_handler.current_enemy)
                    $ combat_handler.gawain_attack("archery")
            "[str(combat_handler.combat_status_string)]" 

            if combat_handler.current_enemy:

                $ combat_handler.enemy_attack()

                "[str(combat_handler.combat_status_string)]"

        hide screen combat_menus
        
        "You stand panting over the corpse of your enemy, looking back over your shoulder to see the young girl safe, cowering behind her older sister. They look terrified of you - they all do. That was something you never got over: the fear in peoples’ eyes as you slayed beasts to protect them. The little girl hesitates before tugging her arm out of her sister’s grasp and walks up to you, offering you two flowers. You lean down to take the first flower and the action only serves to bring Ragamuffin closer to the little girl."
        
        "She smiles sweetly, tucking the second flower behind Ragamuffin’s fluffy ear. The cat purrs her thanks, making the little girl giggle." 
        
        "You know what you must do to protect these people: you must venture into the forest, slaying any beasts that threaten this beautiful, struggling town any further."
        
        "You rise to your full height, tuck your flower behind your ear to match Ragamuffin, and with one last, longing look over the town you’ve been residing in for so long, you head deeper into the forests surrounding Hereford."

        jump morgana_ending

    label morgana_combat:
        $ g.c("No, I refuse to believe these dedicated women would abandon their families so callously. You must have them enchanted, under some spell, Morgana")

        morg "Me? Spell? I would never."
        
        "She’s teasing you now, challenging you outright. "
        
        $ g.c("Prepare to be vanquished, foul sorceress. I will set these women free and return them to their proper homes.")
        
        morg "Make this quick, Sir Gawain. I have little time for such humorous outbursts."

    label combat:
        show screen combat_menus(combat_handler.current_enemy)

        while g.current_hp > 0 and combat_handler.current_enemy:
            menu:
                "Sword Attack":
                    $ combat_handler.gawain_attack("swordplay")
                "Bow and Arrow":
                    $ g.attack("archery", combat_handler.current_enemy)
                    $ combat_handler.gawain_attack("archery")
            "[str(combat_handler.combat_status_string)]" 

            if combat_handler.current_enemy:

                $ combat_handler.enemy_attack()

                "[str(combat_handler.combat_status_string)]"

        hide screen combat_menus

        jump visit_lake
            
        # TODO: automatically go to the next month 


    ####**** TAVERN SCENES ****####
    # skills: charm, mettle

    label tavern_first_event:
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

                "You gain +2 Charm"

                # TODO: use a special pop-up screen for skill gains through dialog?
                $ g.change_stat('charm', 2)

        $ calendar.set_played('tavern', 0)
        $ calendar.increment_week()
        jump go_to_town

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
                if g.get_stat('mettle') > 10:
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
        "You gain +3 Charm."
        $ g.change_stat('charm', 3)

        $ calendar.set_played('tavern', 1)
        $ calendar.increment_week()
        jump go_to_town

    label tavern_no_event:
        $ r = roll(2, 0)
        if r == 1:
            "The bartender gives you a drink on the house."
            "You gain +2 Charm."

            $ g.change_stat('charm', 2)
            $ g.change_stat('mettle', -1)
        else:
            "You have a nice meal at the tavern."
            "You gain +3 Mettle."
            $ g.change_stat('mettle', 3)
        $ calendar.increment_week()
        jump go_to_town


    ####**** WASHING WELL SCENES ****####
    # skills: mettle, swordplay

    label wash_first_event:
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
        if g.get_stat('charm') > 15:
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

        "You pass the rest of the afternoon training with your sword."

        "Gain +4 Swordplay."

        $ g.change_stat('swordplay', 4)

        $ calendar.set_played('wash', 0)
        $ calendar.increment_week()
        jump go_to_town
           
    label second_wash_event:
        "The cat says nothing, just stares up at you knowingly. He scurries off when you try to pet him." 
        if calendar.scenes_played['cat'][0]:
            "There are more cats roaming the city than just the ones you’ve met at the Cat Haven, and they all seem to know you."

        $ calendar.set_played('wash', 1)
        $ calendar.increment_week()
        jump go_to_town

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
        $ calendar.increment_week()
        jump go_to_town

    label fourth_wash_event:
        "The cat says nothing, just stares up at you knowingly. She scurries off when you try to pet her."

        menu:
            "Follow her":
                "You chase after the cat as she tries to flee, all the way to the forest line. She disappears behind a bush before you can follow."
                
                "Seems the cats live in the forest when not in the city."

                "You gain +5 intuition."
                $ g.change_stat('intuition', 5)

            "Leave her be":
                "You watch the cat disappear into an alleyway, becoming one with the shadows."
                "You gain +5 mettle."
                $ g.change_stat('mettle', 5)

        $ calendar.set_played('wash', 3)
        $ calendar.increment_week()
        jump go_to_town

    label wash_no_event:
        $ r = roll(2, 0)
        if r == 1:
            "You learn an old wives’ tale to help you in battle."
            "You gain +2 Swordplay skill."
            $ g.change_stat('swordplay', 2)

        else:
            "Get a pep talk from a kind old woman."
            "You gain +2 Mettle and +1 Swordplay skill."
            $ g.change_stat('swordplay', 1)
            $ g.change_stat('mettle', 2)
        
        "You pass the week doing odd jobs around town and earn +10 gold."

        $ g.change_gold(5)

        $ calendar.increment_week()
        jump go_to_town

    # TODO: need some dialogs that increase archery skill

    ####**** CAT HAVEN SCENES ****#### 

    label cat_haven_no_event:
        $ r = roll(3, 0)
        if r == 1:
            "Pet them kitties!"

            "You gain +3 Intuition."
            $ g.change_stat('intuition', 3)
        elif r == 2:
            "Have a sword fight with Sir Hiss!"
            "Gain +4 Swordplay skill."
            $ g.change_stat('swordplay', 4)
        else:
            "Have a tea party with Mittens and Shrimp!"
            "Gain +3 Mettle."
            $ g.change_stat('mettle', 3)
        $ calendar.increment_week()
        jump go_to_town

    label cat_haven_first_event:
        # TODO: add cutscene here
        $ calendar.set_played('cat', 0)
        
        jump cat_haven_no_event

    label cat_haven_second_event:
        s "Sir Meowain, Sir Meowain!!"

        show gawain at midleft_intro
        $g.c("Hello there, Shrimp. How are you on this fine day? ")
        hide gawain

        s "I have the most dangerous quest for you, will you accept?"

        show gawain at midleft

        if g.get_stat('mettle') > 20 and g.get_stat('intuition') > 15:
            menu:
                "Accept":
                    jump accept_shrimps_quest
                "Ask for more details":
                    $ g.c ("What is this quest you so desire to send me on, Shrimp?")

                    s "I want some salmon from the market! Will you get me some?"

                    $ g.c ("You want me to buy you some salmon to eat?")

                    s "Yes, yes, yes, I do! Oh! And I have some gold for you that Sir Hiss gave me to buy salmon with!"

                    "Shrimp gives you the gold and you head into town and purchase some raw salmon. When you return, all members of the Cat Coven feast and share Shrimp’s spoils."

                    "You gain +10 Mettle and +5 Intuition."

                    $ g.change_stat('mettle', 10)

                    $ g.change_stat('intuition', 5)

                "Decline":
                    jump decline_shrimps_quest
        elif g.get_stat('mettle') > 20 and g.get_stat('intuition') < 15:
            menu:
                "Accept":
                    jump accept_shrimps_quest
                "Ask for more details (NOT ENOUGH INTUITION)":
                    "..."
                "Decline":
                    jump decline_shrimps_quest
        elif g.get_stat('mettle') < 20 and g.get_stat('intuition') > 15:
            menu:
                "Accept (NOT ENOUGH METTLE)":
                    "..."
                "Ask for more details":
                    $ g.c ("What is this quest you so desire to send me on, Shrimp?")

                    s "I want some salmon from the market! Will you get me some?"

                    $ g.c ("You want me to buy you some salmon to eat?")

                    s "Yes, yes, yes, I do! Oh! And I have some gold for you that Sir Hiss gave me to buy salmon with!"

                    "Shrimp gives you the gold and you head into town and purchase some raw salmon. When you return, all members of the Cat Coven feast and share Shrimp’s spoils."

                    "You gain +10 Mettle and +5 Intuition."

                    $ g.change_stat('mettle', 10)

                    $ g.change_stat('intuition', 5)

                "Decline":
                    jump decline_shrimps_quest
        else:
            menu:
                "Accept (NOT ENOUGH METTLE)":
                    "..."
                "Ask for more details (NOT ENOUGH INTUITION)":
                    "..."
                "Decline":
                    jump decline_shrimps_quest

        $ calendar.set_played('cat', 1)
        $ calendar.increment_week()
        jump go_to_town

    label accept_shrimps_quest:
        $ g.c("I accept, Shrimp. What journey are you sending me on?")

        hide gawain 

        s "I want salmon! Purchase some from the market for me?"

        if g.gold >= 5:
            "You head into town and purchase some raw salmon for Shrimp. When you return, all members of the Cat Coven feast and share Shrimp’s spoils."
            "You spent 5 gold on the salmon."
            "You gain + 10 Mettle and +5 Intuition."
            $ g.change_gold(-5)
        elif g.gold > 0:
            "You head into town and purchase some raw salmon for Shrimp. When you return, all members of the Cat Coven feast and share Shrimp’s spoils."
            "You spend [g.gold] on the salmon."
            "You gain + 10 Mettle and +5 Intuition."
            $ g.change_stat('mettle', 10)
            $ g.change_stat('intuition', 5)
            $ g.changegold(-(g.gold))
        else:
            "You don't have any money to buy salmon with."
            # TODO: go fishing? or decline quest

        $ calendar.set_played('cat', 1)
        $ calendar.increment_week()
        jump go_to_town

    label decline_shrimps_quest:
        $ g.c("I’m sorry, Shrimp. I don’t think this quest is quite my focus at the moment.")

        hide gawain

        s "I see, Sir Meowain. Be on your way then. Sorry to bother you." 
        "Shrimp sulks off to be comforted by Mittens, who glares at you for hurting Shrimp’s feelings."
        "You lose 5 Intuition and 5 Charm."
        $ g.change_stat('intuition', -5)
        $ g.change_stat('charm', -5)
        $ calendar.set_played('cat', 1)
        $ calendar.increment_week()
        jump go_to_town


    label cat_haven_third_event:
        m "Sir Meowain! Do you have a moment?"

        show gawain at midleft_intro
        
        $ g.c("Of course, Mittens. How may I be of service?")

        hide gawain
        
        m "Why can’t Ragamuffin talk? I want to play with her but she does not understand me."
        
        "Ragamuffin perks up at the sound of her name." 

        show gawain at midleft
        
        $ g.c("Ragamuffin is but a regular cat, not a magical one like you.")

        hide gawain
        
        m "I’m not magical... am I?"

        show gawain at midleft
        
        $ g.c("Aren’t you?")

        hide gawain

        m "I’m confused… can Ragamuffin play or not?"

        menu:
            "Let her play":
                "Ragamuffin hops off your shoulder to play with Mittens. They spend the afternoon chasing butterflies and playing with balls of yarn."
                "You gain +4 Mettle."
                $ g.change_stat('mettle', 4)
            "Leave":
                "You choose not to trust Mittens. She is a talking cat, after all. Who knows what kind of magic is afoot? You keep on walking instead."
                "You gain +5 Intuition, and lose 2 Charm."
                $ g.change_stat('intuition', 5)
                $ g.change_stat('charm', -2)                

        $ calendar.set_played('cat', 2)
        $ calendar.increment_week()
        jump go_to_town


    ####**** INN SCENES ****####
    # Skills: Intuition, swordplay

    label inn_first_event:
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

        "You gain +3 Swordlplay."

        $ g.change_stat('swordplay', 3)

        $ calendar.set_played('inn', 0)
        $ calendar.increment_week()
        jump go_to_town

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

        "You gain +2 Intuition."

        $ g.change_stat('intuition', 2)

        $ calendar.set_played('inn', 1)
        $ calendar.increment_week()
        jump go_to_town


    label inn_no_event:
        "Rest up for the search ahead."

        "You gain +2 Swordplay."
        $ g.change_stat('swordplay', 2)

        $ calendar.increment_week()
        jump go_to_town


    ####**** COTTAGES SCENES ****####
    # skills: archery and intuition, + gain gold
    label cottages_no_event:
        $ r = roll(3, 0)

        if r == 1:
            "Spend the day connecting with the locals."

            "Gain +3 Intuition."

            $ g.change_stat('intuition', 4)

        else:
            "A local invites you to practice archery with her."

            "Gain +4 archery."

            $ g.change_stat('archery', 5)

        "You help a local with some tasks and earn +10 gold for your trouble."
        
        $ g.change_gold(5)
        $ calendar.increment_week()

    label cottages_first_event:
        show gawain at midleft_intro
        $ g.c("Pardon me, I am Sir Gawain and I’m looking to find the missing wives. Are you wed, sir?")
        hide gawain

        b "Me? No, I am not married yet. I am betrothed to the beautiful Olive, though. We are to be married in Weed Month."
        
        show gawain at midleft
        $ g.c("Well, many blessings be upon you and yours!")
        hide gawain

        b "You are too kind, Sir. We shall take all the blessings we get. We were to be wed many months ago, but Olive’s mother vanished and left her family completely helpless."
        
        show gawain at midleft
        $ g.c("And did you have any clues as to why she left? Or where she went, mayhaps?")
        hide gawain

        b "Not the foggiest idea. She had the perfect life - children, a home to lord over, her spinning. What else could she have wanted? Olive was crushed when her mother left."
        
        show gawain at midleft
        $ g.c("Seems this is leaving the families of Hereford in ruins.")
        hide gawain

        b "Once I marry Olive, our family will befall no such fate. She’s staying put, I’ll make sure of it."
        
        show gawain at midleft
        $ g.c("Then I wish you the wisdom to keep her home and the heart to keep her happy.")
        hide gawain

        b "Right. Happy. Marriage is not for the faint of heart, not in these times."
        
        show gawain at midleft
        $ g.c("No, it quite certainly is not. Never has been. Good day, Bryan.")
        hide gawain

        "You pass the rest of the afternoon practicing with your bow. Gain +2 Archery skill."

        $ g.change_stat('archery', 2)

        $ calendar.set_played('cottages', 0)
        $ calendar.increment_week()
        jump go_to_town

    label cottages_second_event:
        "You turn a corner to see a man sitting in the dirt by his front door, crying his eyes out. Do you comfort him?"

        menu:
            "Comfort Him":
                show gawain at midleft_intro
                $ g.c("Sir, may I ask why you’re crying? Anything I may assist you with?")
                hide gawain
                
                cm "My Wife! She’s gone! We went to bed side-by-side and by the time I awoke, she was gone!"
                
                show gawain at midleft
                $ g.c("My, that’s quite the misfortune. Any ideas where she may have gone?")
                
                "{i}Leaving with the moon so high can only mean a penchant for secrecy.{/i}"

                hide gawain
                
                cm "No! I don’t understand! Where is my wife?! And her little kitty, too?!"
                
                show gawain at midleft

                $ g.c("I’ll work tirelessly to find her, sir. You have my word.")
                hide gawain
                
                cm "My wife! Where is my wife?!"

            "Walk On":
                "You walk on, taking a nice stroll through the countryside."

                "You gain +2 intuition."

                $ g.change_stat('intuition', 2)
        $ calendar.set_played('cottages', 1)
        $ calendar.increment_week()
        jump go_to_town

    label cottages_third_event:
        "You happen upon a lovely cottage, kept to perfection. In the front yard picking veggies is a forlorn woman. Do you approach her?"

        menu:
            "Attempt conversation":
                show gawain at midleft_intro
                $ g.c("Ma’am, may I ask why you look so down? Maybe I can assist you.")
                hide gawain
                
                c "Oh, Sir Gawain the True! I’ve heard of you poking about town. I am Crisea, lovely to finally meet you. I’m afraid it’s nothing you can assist with fine knight."
                if (g.get_stat('intuition') > 20):
                    menu:
                        "Persist":
                            $ g.c("Are you sure? Nothing even a listening ear can help soothe?")
                            
                            c "…Well, if you insist. I’ve heard whispers of beasts in the forest on the outskirts of town. I fear I may have been visited one."
                            
                            $ g.c("I specialize in beating back ghoulish beasts. Mayhaps if you describe it, I can hunt it down and ensure you will be safe once more?")
                            
                            c "No, no, this isn’t a beast like that. She’s smarter than to be tracked like a brainless animal."
                            
                            $ g.c("...She?")
                            
                            c "She."
                            
                            $ g.c("And she is...?")
                            
                            c "She is none of your concern. Just leave her be. And me, for that matter. Your ear is no longer required. Good day, Sir Gawain."
                            
                            $ g.c("Good day to you too, ma’am...")

                            $ "You pass the rest of the afternoon practicing with your bow. You gain +4 archery."

                            $ g.change_stat('archery', 4)
                            
                        "Leave her be":
                            $ g.c("My apologies for the intrusion. Have a lovely day, ma’am.")
                            
                            hide gawain 

                            "She ignores you, heading back inside with her full basket."

                else:
                    menu:
                        "Persist (NOT ENOUGH INTUITION)":
                            "..."
                        "Leave her be":
                            $ g.c("My apologies for the intrusion. Have a lovely day, ma’am.")
                            
                            hide gawain 

                            "She ignores you, heading back inside with her full basket."
            "Walk on":
                "You go for a walk about the countryside instead, leaving the woman be."

                "You gain +4 intuition."

                $ g.change_stat('intuition', 4)
        $ calendar.set_played('cottages', 2)
        $ calendar.increment_week()
        jump go_to_town
                        

    label lluds:
        # scene town 

        ll "Welcome to Llud's Libations!"

        $ _window_hide()

        show screen shop

        $ wait_for_status(activities_selected)

    label leaving_lluds:
        ll "Let’s meet again later, loyal customer!"

        $ wait_for_status(activities_selected)

    label visit_lake:
        scene lake with fade

        show lady at midright_intro

        $ g.reset_health()

        if calendar.current_month == 0:
            $ l.c("Hello, my dearest Gawain. I offer you another blessing to aid you on your quest.")

            # TODO Allow user to pick which stat they want a bonus to

            "You gain +10 Archery."

            $ g.change_stat('archery', 10)

            if g.get_stat('charm') > 10:
                menu:
                    "Ask for Advice":
                        $ l.c("You can visit each location more than once. There are many new people to meet that may have valuable information, dear knight.")
                        hide lady
                    "Flirt":
                        hide lady
                        show gawain at midleft

                        $ g.c("Your blessings are a kindness I haven’t known in a very long time, my Lady. I am forever in your debt.")
                        hide gawain

                        show lady at midright

                        $ l.c ("I have little need for debts or payments, dear Gawain. Stay true on your path, that’s all I ask of you.")
                    "Return to Town":
                        jump go_to_town
            else:
                menu:
                    "Ask for Advice":
                        $ l.c("You can visit each location more than once. There are many new people to meet that may have valuable information, dear knight.")

                    "Flirt (NOT ENOUGH CHARM)":
                        "..."
                    "Return to town":
                        jump go_to_town
        elif calendar.current_month == 1:
            $ l.c("Hello, my dearest Gawain. I offer you another blessing to aid you on your quest")
            
            if g.get_stat('charm') > 15:

                menu:
                    "Ask for Advice":
                        $ l.c ("You can buy potions at Lludd’s Libations to increase your stats or aid you in battle!")
                        hide lady
                    "Flirt":
                        "Ragamuffin leaps off your shoulder to play with Mochi, the Lady of the Lake’s cat. They splash about the shallows, trying to pounce on each other." 
                        
                        show gawain at midleft
                        
                        $ g.c("Seems they’re fast friends. I wonder if this is a sign, my Lady, that our paths were meant to cross this way.")
                        
                        hide gawain

                        show lady at midright

                        $ l.c("They are quite cute playing so, aren’t they?")

                        hide lady

                        show gawain at midleft
                        
                        $ g.c("I find Ragamuffin has much stronger insight than I. If she’s so close with Mochi, then I feel we are to be close, as well.")
                        
                        hide gawain 

                        show lady at midright

                        $ l.c("Seems so, dearest Gawain. Seems so.")
                        hide lady

                        $ flirted_with_lady = True
                    "Return to town":
                        jump go_to_town
            else:
                menu:
                    "Ask for Advice":
                        $ l.c ("You can buy potions at Lludd’s Libations to increase your stats or aid you in battle!")
                        hide lady
                    "Flirt (NOT ENOUGH CHARM)":
                        "..."
                    "Return to town":
                        jump go_to_town
            
        elif calendar.current_month == 2:
            $ l.c("Hello, my dearest knight. I offer you yet another blessing to aid you on your quest.")

            "You gain +10 Mettle."

            $ g.change_stat('mettle', 10)

            hide lady

            if flirted_with_lady:
                menu:
                    "Ask for Advice":
                        $ l.c("Some people will approach you for your wisdom on their own, no need to worry about going to them.")
                        hide lady
                    "Flirt":
                        $ l.c("You seem to be hitting your stride. Are you finding peace in Hereford yet?")
                        
                        hide lady

                        show gawain at midleft
                        
                        $ g.c("I am, my Lady, though I find the most respite when I am here in your company.")

                        hide gawain

                        show lady at midright
                        
                        "The Lady of the Lake laughs, hiding her blush behind her hand."  
                        
                        $ l.c("Well, I’m glad I can bring you some joy.")

                        hide lady

                        show gawain at midleft
                        
                        $ g.c("I assure you, my Lady, it’s not just some. The sigh of relief I breathe the moment I see your face is a more than welcome addition to my routine.")

                        hide gawain

                        show lady at midright
                        
                        "The Lady of the Lake seems stunned, blushing darker still." 
                        
                        $ l.c("Well, my dearest Gawain, you may stay until the sun sets, if it brings you such peace to be here. I won’t say no to the company.")
                        
                        hide lady

                        show gawain at midleft

                        $ g.c("If it pleases my Lady, then it shall be so.")

                        hide gawain

                        show lady at midright
                        
                        "The Lady of the Lake doesn’t say much else, but the two of you watch the sunset together before you return to town."

                        hide lady
                    "Return to town":
                        jump go_to_town
            else:
                menu:
                    "Ask for advice":
                        $ l.c("Some people will approach you for your wisdom on their own, no need to worry about going to them.")
                    "Return to town":
                        jump go_to_town
        elif calendar.current_month == 3:
            show lady at midright_intro
            $ l.c("Hello, my dearest knight. I offer you yet another blessing to aid you on your quest.")
            
            if flirted_with_lady:
                menu:
                    "Ask for Advice":
                        $ l.c("Keep your stats balanced, dearest Gawain. You’ll never know when you need high " + g.get_min_stat() + ".")
                        hide lady
                    "Flirt":
                        hide lady
                        
                        show gawain at midleft

                        $ g.c("My Lady, I’ve brought you a flower. It’s a simple daisy, nothing as illustrious as the flowers of your blessings, but something to show my eternal gratitude for your aid.")
                        
                        hide gawain

                        show lady at midright
                        
                        $ l.c("My, dear Gawain, aren’t you quite the charmer.")
                        
                        hide lady
                        
                        show gawain at midleft
                        
                        $ g.c("With you, my Lady, it comes easy. I find I desire nothing more than to charm you.")
                        
                        hide gawain
                        
                        show lady at midright
                        "She laughs, blush returning to her cheeks as it so often seems to when you are around. "
                        
                        $ l.c("Well, rest assured I am quite charmed. I enjoy your company, my dearest knight. I’m quite glad you’ve chosen to be on this journey with me.")
                        
                        $ l.c("Care to watch the sunset again? I find I’ve quite missed your company.")

                        "The two of you watch the sunset, talking still even as the moon is high. You don’t make your way back to town until the wee hours of the morning, heart full and smile broad."

                        hide lady
                    "Return to town":
                        jump go_to_town
            else:
                menu:
                    "Ask for Advice":
                        $ l.c("Keep your stats balanced, dearest Gawain. You’ll never know when you need high " + g.get_min_stat() + ".")
                    "Return to town":
                        jump go_to_town
        elif calendar.current_month == 4:
            show lady at midright_intro
            $ l.c("Hello, my dearest knight. I offer you yet another blessing to aid you on your quest.")

            if flirted_with_lady:
                menu:
                    "Ask for Advice":
                        $ l.c("Those cats down at the Cat Haven seem to have a lot to say. Have you visited them lately?")
                        hide lady
                    "Flirt":
                        show gawain at midleft
                        
                        $ g.c("My Lady, I’ve brought you a full bouquet of daisies this time, since you liked the last flower so much.")
                        
                        $ g.c("Anything that brings you joy is something I’ll always find time to do for you.")
                        
                        hide gawain

                        show lady at midright
                        
                        "The Lady of the Lake accepts your bouquet, smiling affectionately at the delicate flowers. She waves her hand over them and they turn to the same glowing gold as the blessings she gives you each month." 
                        
                        $ l.c("There, now they shall last forever.")
                        
                        "This gives you pause - little in your life has ever lasted “forever”. No matter how many times you shared your heart, it seems the life of a knight is rife with instability and solitude." 
                        
                        $ l.c("My dearest Gawain, you seem a bit down. Did I say something to upset you?")
                        
                        show gawain at midleft
                        
                        $ g.c("No, my Lady, it’s just… I am a lonely, broken man. It’s been me, my son, and Ragamuffin for a very long while. ")
                        
                        $ g.c("I fear letting you in reminds me of how long it truly has been since I’ve loved another so true.")
                        
                        hide gawain 

                        show lady at midright
                        
                        $ l.c("...You love me?")

                        show gawain at midleft
                        
                        $ g.c("I find I do, yes. I haven’t felt this way since Ragnell passed, and it scares me to be this... vulnerable. ")
                        
                        hide gawain
                        
                        $ l.c("Why does this scare you so, dear knight? Are you afraid of me?")

                        hide lady

                        show gawain at midleft
                        
                        $ g.c("Heavens no, my Lady. I’m scared to lose you, is all. I’m scared to give you my heart and lose you just as I did Ragnell. ")
                        
                        hide lady
                        
                        show gawain at midleft
                        
                        $ l.c("Well, if it’s any consolation, dear Gawain, I’m much harder to kill than Ragnell.")
                        
                        "Her light-hearted joke makes you both laugh. She had a way of easing your woe with such ease." 

                        hide lady
                        
                        show gawain at midleft
                        
                        $ g.c("I guess that does ease my worries, then. Consider my heart light once more.")

                        hide gawain

                        show lady at midright
                        
                        "She laughs again, bright as birdsong on a summer’s day. You wish you could hear that sound every moment of every day - and it would still never be enough." 
                        
                        $ l.c("Watch the sunset with me again?")

                        hide lady
                        
                        show gawain at midleft
                        
                        $ g.c("Always, my Lady.")
                        hide gawain
                    "Return to town":
                        jump go_to_town
            else:
                menu:
                    "Ask for Advice":
                        $ l.c("Those cats down at the Cat Haven seem to have a lot to say. Have you visited them lately?")
                        hide lady
                    "Return to town":
                        jump go_to_town
        else:
            $ l.c("Hello, my dearest Gawain. I offer you one final blessing to aid you on your quest.")
            
            if flirted_with_lady:
                menu:
                    "Ask for Advice":
                        $ l.c("These beasts seem to be coming from the forest. Maybe the forest will give you answers on the missing women of Herefordshire.")
                    "Flirt":
                        hide lady 
                        show gawain at midleft
                        $ g.c("One final blessing? Are our paths never to cross again?")

                        hide gawain
                        show lady at midright
                        
                        $ l.c("My dearest Gawain, I thought you much smarter than this. You may visit me whenever you please.")
                        
                        hide lady 
                        show gawain at midleft

                        $ g.c("And you will be here to greet me?")

                        hide gawain
                        show lady at midright
                        
                        $ l.c("I will be here to do much more than greet you, my dear knight.")
                        
                        "She reaches out with one delicate hand to caress your cheek. You feel the warmth of her fingertips as they skate across your skin - remnants of the arcane magic she possesses."
                        
                        "You reach up to place your hand over hers, leaning into the touch." 
                        
                        hide lady 
                        show gawain at midleft
                        
                        $ g.c("It’s been too long since I’ve felt a touch so tender.")

                        hide gawain
                        show lady at midright
                        
                        $ l.c("Well, if our paths continue to cross as we both desire, I will work hard to ensure that loneliness doesn’t return.")
                        
                        "You turn your head to press a kiss to the inside of her wrist as your eyes close."
                        
                        "You let yourself just drink in the moment, basking in the light of your Lady. She brings her other hand up to card through your hair, relaxing you further still." 
                        
                        $ l.c("And you’ll still stay to watch the sunset?")
                        
                        hide lady 
                        show gawain at midleft

                        $ g.c("Anything to please you, my Lady. My heart only aches when we are apart.")

                        hide gawain 

                        show lady at midright
                        
                        "She sits beside you on the edge of the lake as you watch the sunset, her hand gently resting over yours where it rests in the dirt."
                        
                        "You eventually make your way back to town, and for the first time in a long time, sleep comes free of nightmares and anguish." 
                        
                        "You awake well rested to the point you decide to go for a stroll about town, just drinking in the sunlight of a brand new day in Hereford."
                    
                    "Return to town":
                        jump boss_fight
            else:
                menu:
                    "Ask for Advice":
                        $ l.c("These beasts seem to be coming from the forest. Maybe the forest will give you answers on the missing women of Herefordshire.")
                    
                    "Return to town":
                        jump boss_fight
        jump boss_fight






#####
                # menu:
                #     "Ask for Advice":
                #         "..."
                #     "Flirt":
                #         "..."
                #     "Return to town":
                #         jump go_to_town

                # menu:
                #     "Ask for Advice":
                #         "..."
                #     "Return to town":
                #         jump go_to_town



        jump go_to_town

        # TODO: wait for user to go back to town? or go back to town ourselves 


    label blood_month_lake_event:
        scene lake
        jump boss_fight

    ####**** ENDINGS ****####
    label morgana_ending:
        "You race after the sound of beasts echoing through the forest, seeming to come from all around you."
        
        "You hear the rhythmic thundering of heavy paws right on your tail, but when you turn, there’s nothing there."
        
        "You’re doing your best to follow the trail of sound, hell-bent on finding the source to save Hereford once and for all, but the source seems to be coming from all around you."

        "You chance upon a clearing, a large meadow illuminated with brilliant rays of... moonlight? How long have you been running?"
        
        "The meadow is eerily silent, even the birds don’t sing their songs here. You stumble out into the middle of the meadow, breathing heavily."

        "The chase has worn you out, and despite how unsettling the source, any respite is welcome." 

        "After a few moments of peace, the hair on the back of your neck rises - you’re being watched."

        "You desperately search the treeline, but nothing shows its face."
        
        "The air takes on a deathly chill, and Ragamuffin shivers on your shoulder."

        $ g.c("Do you see anyone, dear girl?") 

        "Ragamuffin looks around, too, ready to help you. But she finds nothing, and just nuzzles closer to comfort you." 
        
        who "Gawaaaaaiiiinnnnn~"
        
        "A voice echoes through the clearing, sing-songy and strangely chipper for such a chilling situation." 
        
        $ g.c("Who goes there? Reveal yourself now.")
        
        who "Gawaaaaaiiiiiiinnnnnnn~"
        
        "It almost sounded happier, like it's glad it's getting to you. You clear your throat, doing your best to sound braver." 
        
        $ g.c("Reveal yourself, voice. I command you as… uh, a Knight of the Round Table.")
        
        "That title used to hold authority, years ago before King Arthur abandoned the throne. It’s the last shred of notoriety you have left - your allegiance to a long-deserted coalition that invokes only wistful memory today." 
        
        "You hear the voice giggle, amused by your attempt at showmanship, by your plea to be respected." 
        
        who "Sir Gawain the True, are you alone?"
        
        "The voice sounds more human, less ghastly and unnerving. It still echoes through the meadow, surrounding you with sound in a way that makes it impossible to find the source. "
        
        $ g.c("It’s just Ragamuffin and I.")
        
        "You find yourself compelled to tell the truth when in such a vulnerable position. "
        
        "Still, you’ve fought many battles with just Ragamuffin by your side. You trust that with her, you can get through anything." 
        
        "Ragamuffin perks up, looking towards your left. You follow her gaze just in time to see an ethereal woman emerge from the treeline with a cat on her shoulder."
        
        "She smiles warmly at you and opens her arms wide. Arcane magic glows from her fingertips and the meadow seems to bloom around her." 
        
        "The sun returns to the sky, casting warm beams down onto your face. The birds resume their songs, fluttering through the air above you. Bees and butterflies meander through the daisies at your feet. "
        
        "Ragamuffin leaps off your shoulder to chase the butterflies, enjoying the sudden return of sunshine. The woman’s cat jumps off her shoulder to join Ragamuffin, and the two start playing in the sun together." 
        
        morg "Sir Gawain, Ragamuffin, what an honor to meet you both. I am the sorceress Morgana, half-sister of the former king, Arthur, and this is my cat, Teschio. We’ve taken up residence in the forest of Herefordshire. It seems you have finally found me, valiant knight. "
        
        "You bow in greeting, watching carefully as Ragamuffin traipses up to Morgana. She leans down to pet her, giggling as Ragamuffin purrs." 

        $ g.c("What have you been doing here in the forest? Any particular reason to be so close to Herefordshire?")
        
        "Morgana seems amused by your inquiry as she presses a kiss to the top of Ragamuffin’s head. She gives her one last scratch behind the ear before guiding Ragamuffin to return to you." 
        
        "Ragamuffin is quick to leap back up onto your shoulder, snuggling up to you once again. Her fur is warm and extra soft, like Morgana’s pets had made her fur softer." 
        
        "Morgana spreads her arms wide, face upturned to the bright sun. Her hands glow with golden energy, like pure sunlight."
        
        "She’s smiling, eyes closed and shoulders relaxed. A veil of arcane energy wraps around the treeline until a glowing wall of magic encases you and Morgana in the meadow." 
        
        "You’re about to protest when Morgana’s eyes snap open. Her eyes glow gold as she speaks." 
        
        morg "Coven, join us!"
        
        "Through the wall of light, the missing women of Herefordshire step into the meadow, kitties by their side. Morgana looks around the circle of women, pride shining clear." 
        
        morg "This is my coven: the beautiful, talented women of Herefordshire. I gave the Cat Coven the gift of speech to guide these women home to me. They’ve been a great help as I grow my coven of sorceresses and enchantresses."
        
        "You look around the circle. Every missing woman is here, smiling placidly at you... very placidly." 
        
        $ g.c("And did they want to join you? They weren’t… lured away?")
        
        morg "I’d never force a woman to do anything against her will, Gawain. Don’t you see how happy they are?"
        
        "The women continue to smile just as placidly, their arms outstretched to form a chain around the meadow. Their kitties sit obediently by their sides, watching you carefully." 
        
        morg "Isoude, tell him how happy you are."
        
        "A woman who looks familiar blinks at the sound of her name, almost like she was being roused from a daydream. You realize she looks just like Olive in Hereford, and this must be her missing mother." 
        
        i "Yes. Happy." 
        
        "Isoude’s smile only grows as the kitty beside her rubs against her leg. She looks either dazed by a magic spell or blissfully content to the point of complete peace."

        menu:
            "Press Morgana for details":
                $ g.c("These women have homes and families in Herefordshire. They miss their mothers, wives, daughters, and sisters. Why take them? Why the secrecy? Their families would love to know where they went.")

                "Morgana hesitates, like she doesn’t want to reveal her true motives. But, Teschio leaps off her shoulder, rushing to you. He rubs against your legs to show his trust."
                
                "You lean down to let Ragamuffin join him, and the two of them resume chasing butterflies and playing in the sun. "
                
                morg "Any friend of my darling Teschio is a friend of mine. I must trust you, Sir Gawain, as my and Teschio's bond requires."

                "She lowers her arms, yet the wall of light does not waver."
                
                "The women around the circle all have glowing hands, the same way Morgana did. They have arcane magic, likely trained by Morgana."

                morg "Since my brother’s disappearance, the throne of Camelot has remained empty. As Arthur’s sister, I desire to make a bid for queen. Queen Morgana... doesn’t it have a nice ring to it?"

            "Fight Morgana":
                jump morgana_combat


    # This ends the game.

    return
