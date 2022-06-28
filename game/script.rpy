# Berkeley Savage
# Capstone Spring 2022

# Name: Murder Mystery (Minus the Murder)
#   (might not be the final name)
# Desription: A visual novel game where you solve the mystery of a broken family heirloom.

# Characters:

define ivy = Character(_("Ivy"), color="#f03611")
define sterling = Character(_("Sterling"), color="#0c88ed")
define ash = Character(_("Ash"), color="#af38ff")
define reagan = Character(_("Reagan"), color="#ccb90a")
define parker = Character(_("Parker"), color="#05b317")

init:
    $ short_dissolve = Dissolve(0.1)

    $ roomList = {
        "kitchen" : False,
        "living_room" : False,
        "library" : False,
        "bedroom" : False,
        "office" : False
    }

    $ clues = {
        "computer" : False,
        "note" : False,
        "scraps" : False,
        "sketch" : False
    }

    $ parker_clues = False

    $ reagan_confront = False

    $ ash_confront = False

    $ parker_confront = False

    $ sterling_confront = False

    $ mystery_solved = {
        "reagan" : False,
        "parker" : False,
        "ash" : False,
        "sterling" : False
    }

    $ ending = False
    # If False: we were not talking to Ash -> realize Ash was in the office and go to her
    # If True: we were talking to Ash -> realize Ash was in the office and ask her right then

    $ firstLoop = True

# Ivy Image Transformations
transform ivyT:
    zoom 0.4
    xzoom -1.0
    xalign 0.0
    yalign 1.0

# Parker Image Transformations
transform parkerT:
    zoom 0.4
    xalign 1.0
    yalign 1.0

# Sterling Image Transformations
transform sterlingT:
    zoom 0.46
    xalign 1.0
    yalign 1.0

# Ash Image Transformations
transform ashT:
    zoom 0.43
    xalign 1.0
    yalign 1.0

# Reagan Image Transformations
transform reaganT:
    zoom 0.4
    xzoom -1.0
    xalign 1.0
    yalign 1.0

# The game starts here.

label start:

    # SCENE - something blank and creepy i guess? lmao

    show bg black:
        zoom 3

    "How is it that mysteries usually start? 'It was a dark and stormy night' or something equally dramatic?"

    "Sorry, this is my first time solving a mystery and I'm a bit excited."

    show ivy_neutral at center:
        zoom 0.4
    with short_dissolve

    "My name's Ivy, and it's my job to figure out who ruined my family's scrapbook."

    hide ivy_neutral
    with short_dissolve

    "A few friends and I were staying the weekened at my parents vacation home to celebrate my 23rd birthday. While the weekend started so fun..."

    "... I had no idea the betrayal which was on the horizon."

    "I trusted each of my friends without question. It's hard to imagine someone so close to you betraying that trust."

    "Four friends, four suspects:"

    show sterling_neutral at center:
        zoom 0.46
    with short_dissolve

    "Sterling, a.k.a. 'The Loving Boyfriend'. We've been dating for years now, and friends for longer... but would he lie to me?"

    hide sterling_neutral
    with short_dissolve

    show ash_neutral at center:
        zoom 0.43
    with short_dissolve

    "Ash, a.k.a. 'The Mean Confidant'. She's a bit sarcastic and frankly rude, but loyal to a fault... could she break my trust?"

    hide ash_neutral
    with short_dissolve

    show parker_neutral at center:
        zoom 0.4
    with short_dissolve

    "Parker, a.k.a. 'The Snarky Weasel'. He can cause messes and doesn't like getting into trouble... but would he cause this mess?"

    hide parker_neutral
    with short_dissolve

    show reagan_neutral at center:
        zoom 0.4
        xzoom -1.0
    with short_dissolve

    "And Reagan, a.k.a. 'The Anxious Sunshine'. She's always looking for ways to help others... could she do something so selfish?"

    hide reagan_neutral
    with short_dissolve

    "With questions and no answers, I must take upon myself the role of investigator and discover the truth."

    "It all started just before dinner that night..."

    # SCENE CHANGE - Dining room

    show bg dining room:
        zoom 2
        yalign 1.0

    show reagan_happy at reaganT
    with short_dissolve

    reagan "Food is ready! Everyone come eat!"

    hide reagan_happy
    with short_dissolve

    "Everyone pilled into the dining room, excited for the delicious meal Reagan had prepared."

    "The dishes had already been set, circling around the still steaming noodles and garlic bread Regan set out for everyone."

    "Even as everyone clamored to get their food, the room settled into light conversation - until a cellphone ringing cut through the air."

    show sterling_neutral at sterlingT
    with short_dissolve

    sterling "Oh, that's me. Sorry, I've got to take this real quick."

    hide sterling_neutral
    with short_dissolve

    "Sterling stepped out of the room, though I became distracted by the food in front of me. Before I could even take a bite, I was interupted again."

    show ash_neutral at ashT
    with short_dissolve

    ash "Hey Parker, could you get my water bottle from the office?"

    show parker_angry:
        zoom 0.4
        xzoom -1.0
        xalign 0.0
        yalign 1.0
    show ash_inactive at ashT
    with short_dissolve
    
    parker "What? You've got legs of your own, stupid."

    show parker_inactive:
        zoom 0.4
        xzoom -1.0
        xalign 0.0
        yalign 1.0
    hide ash_inactive
    hide parker_angry
    with short_dissolve

    ash "But you're closer to the door!"

    hide parker_inactive
    show ash_inactive at ashT
    show ivy_neutral at ivyT
    with short_dissolve

    ivy "Settle down guys, I'll go get it."

    hide ash_inactive
    hide ash_neutral
    hide ivy_neutral
    with short_dissolve

    "With a sigh, I got up and headed for the office, determined to find the water bottle and return to my food."

    # SCENE CHANGE - Office

    show bg office:
        zoom 1.75
        yalign 1.0
    
    "But a vastly different scene greeted my eyes as the door opened. Sitting upon the desk in the room was my family's scrapbook."

    "However, it was covered dark liquid stains, and pages were ripped out and tossed beside it."

    show ivy_sad at ivyT
    with short_dissolve

    ivy "Oh no... my parents are going to kill me."

    hide ivy_sad
    with short_dissolve

    "Okay okay, this is fine. All I need to do is figure out who ruined it and work from there."

    "Quickly snatching up the water bottle, I rushed back to the dining room. The air was filled with light conversation between everyone, as Sterling had returned."

    # SCENE CHANGE - Dining room

    show bg dining room:
        zoom 2
        yalign 1.0

    show ivy_neutral at ivyT
    with short_dissolve

    ivy "Hey, guys."

    show ivy_inactive at ivyT
    with short_dissolve

    "The conversation quieted, as all attention was directed to me."

    show ivy_sad at ivyT
    hide ivy_inactive
    with short_dissolve

    ivy "Look, I found my family's scrapbook absoultely destroyed in the office."

    hide ivy_sad
    with short_dissolve

    ivy "Now, I'm not angry, I just want to figure out who did it so we can fix it. So, who ruined the scrapbook?"

    show ivy_inactive at ivyT
    with short_dissolve
    
    "The room fell into a deafening silence, as each of my friends glanced at one another nervously, suspciously."

    hide ivy_inactive
    with short_dissolve

    ivy "Come on guys, who broke it. Just tell me."

    show ivy_inactive at ivyT
    with short_dissolve

    "Everyone is quiet again... until-"

    show parker_neutral at parkerT
    with short_dissolve

    parker "Well, I know Reagan was in the office alone for some time."

    show parker_inactive at parkerT
    hide parker_neutral
    hide ivy_inactive
    hide ivy_neutral
    show reagan_sad:
        zoom 0.4
        xalign 0.0
        yalign 1.0
    with short_dissolve

    reagan "W-What? Why are you accusing me?"

    hide reagan_sad
    show ash_neutral:
        zoom 0.43
        xzoom -1.0
        xalign 0.0
        yalign 1.0
    with short_dissolve

    ash "Come on Parker, calm down. Besides, were you not also alone in the office?"

    show ash_inactive:
        zoom 0.43
        xzoom -1.0
        xalign 0.0
        yalign 1.0
    hide parker_inactive
    hide ash_neutral
    show parker_angry at parkerT
    with short_dissolve

    parker "I was never alone in the office! What are you suggesting?"

    hide parker_angry
    hide ash_inactive
    with short_dissolve

    "Ash and Parker continue yelling at one another, while Reagan and Sterling attempt to settle them down."

    show ivy_angry at ivyT
    with short_dissolve

    ivy "That's it! Everybody quiet down!"

    hide ivy_angry
    show ivy_neutral at ivyT
    with short_dissolve

    ivy "If no one will just tell me they broke it, I'll find out who broke it. The mystery of the family scrapbook, or something like that."

    hide ivy_neutral
    with short_dissolve
    
    "I tried to keep cool about solving a mystery, but I was pretty excited to solve this myself. I love a good mystery story, and now I've got one."

    "First step: I should isolate each of the suspects so they can't talk to one another. I'll send them off to separate rooms:"

    show bg kitchen:
        zoom 0.9
        xalign 1.0

    show reagan_neutral at center:
        zoom 0.4
        xzoom -1.0
    with short_dissolve

    "Reagan to the kitchen," # Show Reagan sprite in the kitchen, centered

    hide reagan_neutral
    with short_dissolve

    show bg library:
        zoom 1.0
        xalign 1.0

    show parker_neutral at center:
        zoom 0.4
    with short_dissolve

    "Parker to the library," # Show Parker sprite in the library, centered

    hide parker_neutral
    with short_dissolve

    show bg bedroom:
        zoom 0.8
        xalign 1.0

    show sterling_neutral at center:
        zoom 0.46
    with short_dissolve

    "Sterling to the bedroom," # Show Sterling sprite in the bedroom, centered

    hide sterling_neutral
    with short_dissolve

    show bg living room:
        zoom 1.0
        xalign 1.0

    show ash_neutral at center:
        zoom 0.43
    with short_dissolve

    "and Ash to the living room." # Show Ash sprite in the living room, centered.

    # END OF BEGINNING - Investigation really begins.

    jump invest_loop

    label invest_loop:

        # Show just a hallway or something
        # scene bg street bushes

        scene bg hallway

        if firstLoop == True:
            "With the suspects separated, I should investigate the scene of the crime and then begin interogations..."
            $ firstLoop = False

        jump locations

    menu locations:

        "Which room should I go to?"

        "The office.":
            jump office

        "The library.":
            jump library

        "The living room.":
            jump living_room

        "The bedroom.":
            jump bedroom

        "The kitchen.":
            jump kitchen

    label kitchen:

        $ explored = True
        # URL: https://wallpaperaccess.com/anime-kitchen
        scene bg kitchen:
            zoom 0.9
            xalign 1.0

        # Ask the player whether they want to search the room or talk to the suspect here.
        # If they've already searched the room, the Dictionary value will be True

        if roomList["kitchen"] == False:
            menu kitchen_search:

                "Here's the kitchen, where Reagan is. Should I search the room or talk to her?"

                "Search the room.":

                    "The kitchen is a little messy after just having dinner prepared, but it's not a disaster."

                    "Some dishes are left on the counter, most of them in the sink... and what's this?"

                    "There's some crumpled up paper tossed to the side. Drawn on it are some sketches which resemble the family scrapbook."

                    "If I can figure out who this sketch belongs to, I should ask them what's going on."

                    $ roomList["kitchen"] = True
                    $ clues["sketch"] = True

                    menu kitchen_post_search:

                        "Everything else seems to be normal. Should I talk to Reagan or go investigate another room?"

                        "Talk to Reagan.":
                            jump reagan_talk
                        
                        "Go to another room.":
                            jump invest_loop
                
                "Talk to Reagan.":
                    jump reagan_talk
        else:
            "I've already searched the room, I need to talk to Reagan."
            jump reagan_talk
        
    label reagan_talk:

        show ivy_inactive at ivyT
        show reagan_sad at reaganT
        with short_dissolve

        reagan "Hey Ivy. Look, I'm sorry about the scrapbook being ruined. I hope your investigation is going well, at least."

        hide reagan_sad
        show reagan_neutral at reaganT
        with short_dissolve

        menu reagan_qs:

            reagan "How can I help?"

            "Did you break it?" if parker_clues == False or reagan_confront == False:
                
                show reagan_sad at reaganT
                hide reagan_neutral
                with short_dissolve
                
                reagan "I-I didn't, but I can pay for it. I don't wanna cause trouble if this is taking too long."

                show ivy_neutral at ivyT
                hide ivy_inactive
                show reagan_inactive at reaganT
                hide reagan_sad
                with short_dissolve

                ivy "Reagan, I'm not looking for someone to pay for it. I just want to know who broke it."

                show ivy_inactive at ivyT
                hide ivy_neutral
                show reagan_neutral at reaganT
                hide reagan_inactive
                with short_dissolve

                reagan "Oh... well, it wasn't me."

                jump reagan_qs
            
            "What was your schedule like today?" if parker_clues == False or reagan_confront == False:
                reagan "Well, I hung out with Parker in the office at around 1:00, and then I was preparing dinner in the kitchen after 3:00."

                show reagan_inactive at reaganT
                hide reagan_neutral
                with short_dissolve

                "Hmm, interesting. I'll have to talk to Parker and see if he can confirm this."

                show reagan_neutral at reaganT
                hide reagan_inactive
                with short_dissolve

                jump reagan_qs
            
            "Is there anything you know that might help me?" if parker_clues == False or reagan_confront == False:
                reagan "Hmm, I'm not sure. What kind of information are you looking for?"

                show ivy_neutral at ivyT
                show reagan_inactive at reaganT
                hide reagan_neutral
                with short_dissolve

                ivy "Well, maybe if someone was acting suspicious, or behaving oddly. Anything to help narrow the suspects."

                show reagan_sad at reaganT
                show ivy_inactive at ivyT
                hide ivy_neutral
                hide reagan_inactive
                with short_dissolve

                reagan "Well, it feels a little mean to point fingers... but Ash came into the office when I left, and she was alone."

                show reagan_neutral at reaganT
                hide reagan_sad
                with short_dissolve

                jump reagan_qs
            
            "Can I ask you about this item I found?" if parker_clues == False or reagan_confront == False:
                reagan "Sure, what is it?"

                menu reagan_clues:
                    "Show her the computer searches." if clues["computer"] == True:
                        reagan "Oh, th-these? Yeah, um, they're my searches. While I was in the office."

                        show reagan_inactive at reaganT
                        hide reagan_neutral
                        show ivy_neutral at ivyT
                        hide ivy_inactive
                        with short_dissolve

                        ivy "Well, what's up with these searches? Is there a secret you're trying to hide?"

                        show reagan_sad at reaganT
                        hide reagan_inactive
                        show ivy_inactive at ivyT
                        hide ivy_neutral
                        with short_dissolve

                        reagan "Well, I just... I thought someone else was lying to me, so that's what I searched..."

                        show reagan_inactive at reaganT
                        hide reagan_sad
                        with short_dissolve

                        if parker_clues == False:
                            "Hm... that's a werid answer. I should find more clues before confronting her."
                        else:
                            "Parker said Reagan was in the office alone, and it's obvious she's hiding something... I should confront her for the truth."

                        $ reagan_confront = True

                        show reagan_neutral at reaganT
                        hide reagan_inactive
                        with short_dissolve

                        jump reagan_qs
                    
                    "Show her the crumpled up 'Sorry' note." if clues["note"] == True and parker_confront == False:
                        reagan "It's not mine, I don't recognize the writing either. Sorry..."

                        jump reagan_qs
                    
                    "Show her the glue and scraps." if clues["scraps"] == True and ash_confront == False:
                        reagan "I'm not sure what these are supposed to be, they're not mine."

                        jump reagan_qs
                    
                    "Show her the messy scrapbook sketches." if clues["sketch"] == True and sterling_confront == False:
                        reagan "I've never seen this sketch before, I'm not sure what it's for."

                        jump reagan_qs
                    
                    "Nevermind.":
                        jump reagan_qs
            
            "Reagan, we need to talk." if reagan_confront == True and parker_clues == True and mystery_solved["reagan"] == False:

                show ivy_inactive at ivyT
                show reagan_inactive at reaganT
                with short_dissolve

                "Reagan is obviously hiding something, with her answer about the computer sketches. Plus, Parker said she was in the office alone. I need to find the truth."

                show ivy_neutral at ivyT
                with short_dissolve
                
                ivy "Alright Reagan, I know you're lying. The computer search history is obviously yours about your own secret, and I know you were in the office alone."

                show ivy_sad at ivyT
                hide ivy_neutral
                with short_dissolve

                ivy "What's going on?"

                hide ivy_sad
                show reagan_angry at reaganT
                with short_dissolve

                reagan "H-How dare you accuse me of...! I-I didn't...!"

                reagan "..."

                hide reagan_angry
                show reagan_sad at reaganT
                with short_dissolve

                reagan "Okay yes, I was lying. I'm so, so sorry for lying to you Ivy. I've been hiding something from not just you, but all of my friends..."

                reagan "... which is that I've enrolled to study abroad next semester. I'll be gone and busy for a while, and I didn't want to let anyone down."

                reagan "But the longer I kept it secret, the more it worried me and I was scared to tell anyone."

                hide reagan_sad
                with short_dissolve
                
                "Reagan seems ashamed and remorseful, I have little doubt that she's lying about this."

                show ivy_happy at ivyT
                with short_dissolve

                ivy "Hey, it's okay, Reagan. I'm glad to hear you're going to be exploring the world and I hope you have fun!"

                hide ivy_happy
                show ivy_neutral at ivyT
                with short_dissolve

                ivy "However, maybe next time you should admit that first when I'm investigating a \"crime\" like this."

                hide ivy_neutral
                show reagan_sad at reaganT
                
                reagan "I-I'm sorry! I know I should've been truthful from the start... I hope you do find the real culprit though!"

                $ mystery_solved["reagan"] = True

                if mystery_solved["ash"] == True and mystery_solved["parker"] == True and mystery_solved["sterling"] == True:
                    $ ending = False
                    
                    hide ivy_inactive
                    hide reagan_neutral
                    hide reagan_inactive
                    hide reagan_sad
                    with short_dissolve
                    
                    jump solving
                else:

                    hide reagan_sad
                    with short_dissolve

                    "Well, Reagan has a pretty good explanation... I'll have to talk wit the other suspects."
                    jump invest_loop

            "That's all for now.":
                show reagan_happy at reaganT
                hide reagan_neutral
                with short_dissolve

                reagan "I'll be around if you need anything else from me. Good luck, Ivy!"

                jump invest_loop

        jump invest_loop

    label bedroom:

        $ explored = True
        scene bg bedroom:
            zoom 0.8
            xalign 1.0

        # Ask the player whether they want to search the room or talk to the suspect here.
        # If they've already searched the room, the Dictionary value will be True

        if roomList["bedroom"] == False:
            menu bedroom_search:

                "Here's the bedroom, where Sterling is. Should I search the room or talk to him?"

                "Search the room.":
                    "The guest bedroom is a bit messy, just from friends staying here the past few days. The bed isn't made, and there's luggage spread across the room."

                    "I should probably avoid going through peoples stuff, but if push comes to shove... to be safe though, I'll start just looking around the room."

                    "The nightstands are full of useless junk, and the desk cabinet is empty... wait a second, the trash can is full though!"

                    "Looks like a bunch of crumpled up papers... I can't read them very well, but they seem to be attempts of an apology letter."

                    "Whoever was writing these was frustrated trying to word it properly, I wonder if they were the one who ruined the scrapbook? I should ask around."

                    $ roomList["bedroom"] = True

                    $ clues["note"] = True
                    
                    menu bedroom_post_search:

                        "Nothing else seems important around the room. Should I talk to Sterling or go to another room?"

                        "Talk to Sterling.":
                            jump sterling_talk
                        
                        "Go to another room.":
                            jump invest_loop
                
                "Talk to Sterling.":
                    jump sterling_talk
        else:
            "I've already searched the room, I need to talk with Sterling."
            jump sterling_talk

    label sterling_talk:
        
        show sterling_happy at sterlingT
        show ivy_inactive at ivyT
        with short_dissolve

        sterling "Hey there Ivy! How's the mystery solving going? I'm sure you'll have it solved in no time."
        
        show sterling_neutral at sterlingT
        hide sterling_happy
        with short_dissolve

        menu sterling_qs:
            
            sterling "What questions do ya got for me, babe?"

            "Did you break it?" if parker_clues == False or sterling_confront == False:
                
                show sterling_sad at sterlingT
                with short_dissolve

                sterling "No, I didn't. I know how important that scrapbook was to your family."

                hide sterling_sad
                with short_dissolve

                jump sterling_qs
            
            "What was your schedule like today?" if parker_clues == False or sterling_confront == False:
                sterling "Well, I got a snack from the kitchen around 1:00, then I mostly just hung out for the rest of the day up until dinner."

                show sterling_inactive at sterlingT
                show ivy_neutral at ivyT
                with short_dissolve
                
                ivy "Babe, I love you, but I need you to be more specific than that for me."

                hide sterling_inactive
                hide ivy_neutral
                with short_dissolve

                sterling "R-Right, sorry. Let's see... I started in the bedroom first, hung out there until 3 ish. After that, I hung out in the library, and finally the office."

                show sterling_happy at sterlingT
                with short_dissolve

                sterling "I hope that's a bit more specific for ya!"

                hide sterling_happy
                with short_dissolve

                jump sterling_qs
            
            "Is there anything you know that might help me?" if parker_clues == False or sterling_confront == False:
                sterling "Hmm... I don't think anything too suspicious caught my eye."

                sterling "Oh! When I left the kitchen, Ash and Parker came in. They were whispering, and immediately went quiet when they saw me."

                show sterling_angry at sterlingT
                with short_dissolve

                sterling "They were quite rude, and I left quickly after that."

                hide sterling_angry
                with short_dissolve

                jump sterling_qs
            
            "Can I ask you about this item I found?" if parker_clues == False or sterling_confront == False:
                sterling "Of course, what do you got for me?"

                menu sterling_clues:
                    "Show him the computer searches." if clues["computer"] == True and reagan_confront == False:
                        sterling "These searches aren't mine, I didn't touch the computer when I was in the office."

                        jump sterling_qs
                    
                    "Show him the crumpled up 'Sorry' note." if clues["note"] == True and parker_confront == False:
                        sterling "Geez, this handwriting is so messy. I don't know what this is."

                        jump sterling_qs
                    
                    "Show him the glue and scraps." if clues["scraps"] == True and ash_confront == False:
                        sterling "Sorry babe, I can't tell what these are supposed to be."

                        jump sterling_qs
                    
                    "Show him the messy scrapbook sketches." if clues["sketch"] == True:
                        sterling "Oh, I do, uh, know what these are."

                        show sterling_inactive at sterlingT
                        show ivy_neutral at ivyT
                        with short_dissolve

                        ivy "Okay, what are they? Did you sketch them?"

                        hide ivy_neutral
                        hide sterling_inactive
                        with short_dissolve

                        sterling "N-No! My friend gave me this, he said it was a novel I should read. I must've dropped it somewhere"

                        show sterling_inactive at sterlingT
                        show ivy_neutral at ivyT
                        with short_dissolve

                        ivy "A novel? But the sketch looks eerily similar to my family's scrapbook..."

                        hide ivy_neutral
                        hide sterling_inactive
                        with short_dissolve

                        sterling "I guess they do look kinda alike, but that's just what my friend gave me."

                        show sterling_inactive at sterlingT
                        with short_dissolve

                        if parker_clues == False:
                            "His answer is weird, but plausible. I need more information to determine whether he's guilty or not."
                        else:
                            "Parker mentioned Sterling avoiding him, and now he's being fishy about this \"friend's\" book recommendation. I gotta figure out what's really going on."

                        hide sterling_inactive
                        with short_dissolve

                        $ sterling_confront = True

                        jump sterling_qs
                    
                    "Nevermind.":
                        jump sterling_qs
            
            "Sterling, we have to talk." if sterling_confront == True and parker_clues == True and mystery_solved["sterling"] == False:
                
                show sterling_inactive at sterlingT
                with short_dissolve

                "If Sterling really has been avoiding people all day, and lying about the sketches, he must be hiding something big."

                show ivy_angry at ivyT
                with short_dissolve

                ivy "Sterling, babe. I need you to tell me the truth right now, okay? Cause something isn't adding up."

                hide ivy_angry
                show sterling_sad at sterlingT
                with short_dissolve

                sterling "Ivy, I'm sorry this seemes suspicious but I'm not lying. I really did get a book recommendation from my friend."

                hide sterling_sad
                show sterling_happy at sterlingT
                with short_dissolve

                sterling "Look, maybe this will help. I couldn't remember the title of the novel he recommended, so I asked him about it. He said the title is \"Pride and Prejudice\"."

                hide sterling_happy
                show ivy_neutral at ivyT
                with short_dissolve

                ivy "Wait... your friend recommended you \"Pride and Prejudice\"?"

                hide sterling_inactive
                hide ivy_neutral
                with short_dissolve

                sterling "Yeah! What, is that weird?"

                show ivy_neutral at ivyT
                show sterling_inactive at sterlingT
                with short_dissolve

                ivy "I mean, it's a good book. I'm just a little surprised, is all."

                hide ivy_neutral
                hide sterling_inactive
                with short_dissolve

                sterling "So I've heard! Hah..."

                show sterling_sad at sterlingT
                with short_dissolve
                
                sterling "..."

                hide sterling_sad
                show sterling_inactive at sterlingT
                show ivy_neutral at ivyT
                with short_dissolve

                ivy "Hey, what's up? You're awfully quiet..."

                hide ivy_neutral
                hide sterling_inactive
                with short_dissolve

                sterling "I've... got something to tell you. I feel bad, but, when I went into the office at 4:00 I found... I found the scrapbook already ruined."

                show sterling_inactive at sterlingT
                show ivy_angry at ivyT
                with short_dissolve

                ivy "What? And you didn't think to tell me that before? Sterling!"

                hide ivy_angry
                hide sterling_inactive
                with short_dissolve

                sterling "I'm sorry, I'm sorry! But I'm not sure who was in the office before me, so I didn't want to point fingers wildly! I can't just accuse someone randomly!"

                show ivy_neutral at ivyT
                show sterling_inactive at sterlingT

                ivy "Hm... well, that's fair. Thank you for telling me now at least, that is helpful."

                $ mystery_solved["sterling"] = True
                
                if mystery_solved["ash"] == True and mystery_solved["parker"] == True and mystery_solved["reagan"] == True:
                    $ ending = False

                    hide ivy_inactive
                    hide ivy_neutral
                    hide sterling_neutral
                    hide sterling_inactive
                    with short_dissolve

                    jump solving
                else:

                    hide ivy_neutral
                    with short_dissolve

                    "If Sterling found the scrapbook already ruined, I need to find who else has been in the office today."
                    jump invest_loop

            "That's all for now.":
                show sterling_happy at sterlingT
                with short_dissolve

                sterling "Sounds good! Go find the culprit, babe!"

                jump invest_loop

        jump invest_loop

    label library:

        $ explored = True
        scene bg library:
            zoom 1.0
            xalign 1.0

        if roomList["library"] == False:
            menu library_search:

                "Here's the library, where Parker is. Should I search the room or talk to him?"

                "Search the room.":
                    "The library has stayed nice and neat while everyone's been here. At least, all the books are in the right spots."

                    "One of the desks is nearly spotless, while the other seems to have been the scene of a crafting crime! There's glue and tape everywhere!"

                    "Hold on... the paper scraps left around look like one of the patterns from the scrapbook. I wonder if someone tried to repair the scrapbook!"

                    "Or, they ruined it on purpose... but I hope none of my friends would do something like that."

                    "Regardless, I should figure out who these scraps were left by and what they were working on."

                    $ roomList["library"] = True

                    $ clues["scraps"] = True
                    
                    menu library_post_search:

                        "Everything else seems normal. Should I talk to Parker or go to another room?"

                        "Talk to Parker.":
                            jump parker_talk
                        
                        "Go to another room.":
                            jump invest_loop
                
                "Talk to Parker.":
                    jump parker_talk
        else:
            "I've already searched the room, let's talk to Parker."
            jump parker_talk

    label parker_talk:

        show ivy_inactive at ivyT
        show parker_neutral at parkerT
        with short_dissolve

        parker "Oh, hey Ivy. How's the \"investigation\" going? Is it almost over?"

        menu parker_qs:

            parker "What do you wanna know?"

            "Did you break it?" if parker_clues == False or parker_confront == False:
                
                show parker_angry at parkerT
                with short_dissolve

                parker "No, I didn't. God, I don't know why everyone thinks I did!"

                hide parker_angry
                show parker_inactive at parkerT
                show ivy_neutral at ivyT
                with short_dissolve

                ivy "Parker, I'm not accusing you. I've asked everyone if they broke it."

                hide ivy_neutral
                hide parker_inactive
                with short_dissolve

                parker "Oh. Well, it still wasn't me."

                jump parker_qs
            
            "What was your schedule like today?" if parker_clues == False or parker_confront == False:
                parker "Well, I was with Reagan in the office around 1:00 today, then I went to the kitchen with Ash, before chilling in the bedroom before dinner."

                jump parker_qs
            
            "Is there anything you know that might help me?" if parker_clues == False or parker_confront == False:
                
                show parker_happy at parkerT
                with short_dissolve

                parker "Well, now that you mention it... since everyone has been trying to accuse me, I've actually got some interesting details."

                hide parker_happy
                with short_dissolve

                parker "For one, when I left the office at about 2:00, Reagan stayed behind. She was alone in there, who knows what she was doing..."

                show parker_inactive at parkerT
                with short_dissolve

                if reagan_confront == False:
                    "Reagan was in the office alone... that's interesting, but I probably want some more clues before confronting her."
                else:
                    "With Reagan's computer searches and being alone in the office, she must be hiding something. I should find out what."

                hide parker_inactive
                with short_dissolve

                parker "And Sterling, it was so weird, I never really saw him all day! It might have been him avoiding people, for some reason..."

                show parker_inactive at parkerT
                with short_dissolve

                if sterling_confront == False:
                    "While Sterling isn't very outgoing, it's weird for him to be avoidant... I should find some more clues before confronting him."
                else:
                    "First the \"book recommendation\", and now he's avoiding people. I should confront him for more information."

                hide parker_inactive
                with short_dissolve

                parker "Plus, Ash was a bit weird today. While I was chilling in the bedroom, she did actually come in, but left as soon as she saw me."

                show parker_inactive at parkerT
                with short_dissolve

                if ash_confront == False:
                    "That is odd behavior for Ash, considering she and Parker are good friends... I should search for more clues before confronting her."
                else:
                    "She was acting cagey about the craft scraps, and now hiding things. I need to confront her and get to the bottom of this."

                show parker_happy at parkerT
                with short_dissolve

                parker "That's all the important stuff, but I hope it was helpful."

                hide parker_happy
                with short_dissolve

                $ parker_clues = True

                if parker_confront == False:
                    "It's kinda suspicious how quickly Parker threw everyone else under the bus... but I have to find more clues before confronting him."
                else:
                    "After finding his \"Sorry\" letter and he's now shifting blame, Parker's definitely hiding something. And I intend to discover what."

                hide parker_inactive
                with short_dissolve

                jump parker_qs
            
            "Can I ask you about this item I found?" if parker_clues == False or parker_confront == False: # add check for confrontation time
                parker "Yeah, let me take a look."

                menu parker_clues:
                    "Show him the computer searches." if clues["computer"] == True and reagan_confront == False:
                        parker "These searches are so pathetic! They're not mine, obviously."

                        jump parker_qs
                    
                    "Show him the crumpled up 'Sorry' note." if clues["note"] == True:
                        
                        show parker_sad at parkerT
                        with short_dissolve

                        parker "..."

                        show parker_inactive at parkerT
                        with short_dissolve

                        "When I held up the note for him, he went white as a sheet."

                        hide parker_inactive
                        with short_dissolve

                        parker "... Yeah, that's mine. I thought I-I threw it away."

                        show parker_inactive at parkerT
                        show ivy_neutral at ivyT
                        with short_dissolve

                        ivy "Well, as if a good detective wouldn't go through the garbage."

                        hide ivy_neutral
                        hide parker_inactive
                        with short_dissolve

                        parker "Heh, fair enough. Look, it's quite... personal, why I was writing that. Please just, ignore it, or something."

                        show parker_inactive at parkerT
                        with short_dissolve

                        if parker_clues == False:
                            "He's definitely shaken that I have his note... I need more information to figure out why though."
                        else:
                            "After he tried blaming everyone else, and now a shifty response to his note? I gotta confront him for the truth."

                        hide parker_inactive
                        hide parker_sad
                        with short_dissolve

                        $ parker_confront = True
                        
                        jump parker_qs
                    
                    "Show him the glue and scraps." if clues["scraps"] == True and ash_confront == False:
                        parker "What the hell is this? Just looks like some trash."

                        jump parker_qs
                    
                    "Show him the messy scrapbook sketches." if clues["sketch"] == True and sterling_confront == False:
                        parker "What, just some drawings of a book? That's weird, but not mine."

                        jump parker_qs
                    
                    "Nevermind.":
                        parker "Sure, whatever."

                        jump parker_qs

            "Parker, we need to talk." if parker_confront == True and parker_clues == True and mystery_solved["parker"] == False:
                
                show parker_inactive at parkerT
                with short_dissolve
                
                "All this blame shifting and frankly werid behavior... Parker is definitely hiding something."

                show ivy_neutral at ivyT
                with short_dissolve

                ivy "Look Parker, I'm going to be real with you. You've been so suspicious, what's going on?"

                hide ivy_neutral
                show parker_angry at parkerT
                with short_dissolve

                parker "W-what? I have not! Tell me one time I was being suspicious!"

                show ivy_neutral at ivyT
                hide parker_angry
                with short_dissolve

                ivy "Well, you did sell out all your friends..."

                hide ivy_neutral
                show parker_angry at parkerT
                with short_dissolve

                parker "You asked for information! I provided some!"

                hide parker_angry
                show ivy_neutral at ivyT
                with short_dissolve

                ivy "... plus, there's your 'Sorry' note I found. You still haven't told me what that's all about."

                hide ivy_neutral
                show parker_angry at parkerT
                with short_dissolve
                
                parker "I certainly don't have to! That's a private matter, thank you very much."

                hide parker_angry
                show ivy_neutral at ivyT
                with short_dissolve

                ivy "Parker please, I need to know you didn't ruin my family scrapbook. Please, just... be honest."

                hide parker_inactive
                hide ivy_neutral
                with short_dissolve

                parker "I just... well, it's that..."

                show parker_sad at parkerT
                with short_dissolve                

                parker "I'm sorry, I shouldn't be yelling. Look, my bio mom is in the hospital. I got a letter from her a few days ago..."

                show parker_inactive at parkerT
                show ivy_neutral at ivyT
                with short_dissolve

                ivy "Your bio mother? Haven't you guys been no contact for the last few years?"

                hide ivy_neutral
                hide parker_inactive
                with short_dissolve

                parker "Yeah... and still are really, minus the letter I got. I don't know, hearing that she wasn't well..."

                parker "... it felt like I had to say something, you know? She wasn't a good mom, but I wasn't exactly the best child either."

                show parker_inactive at parkerT
                show ivy_neutral at ivyT
                with short_dissolve

                ivy "So the note, it was for her?"

                hide ivy_neutral
                hide parker_inactive
                with short_dissolve

                parker "Well, it was going to be. I never figured out quite how to write it the way I wanted it to be."

                parker "I'm sorry I lied to you, but I really didn't want anyone else to know."

                show parker_inactive at parkerT
                show ivy_neutral at ivyT
                with short_dissolve

                ivy "Don't worry, I won't tell anyone else. Thank you for being honest, Parker."

                $ mystery_solved["parker"] = True

                if mystery_solved["ash"] == True and mystery_solved["reagan"] == True and mystery_solved["sterling"] == True:
                    $ ending = False

                    hide ivy_inactive
                    hide ivy_neutral
                    hide parker_neutral
                    hide parker_sad
                    hide parker_inactive
                    with short_dissolve

                    jump solving
                else:

                    hide ivy_neutral
                    with short_dissolve

                    "Parker is definitely going through a lot, I don't think he would've ruined the scrapbook with all this going on."

                    "I should talk to the other suspects to find who did it."

                    jump invest_loop

            "That's all for now.":
                parker "Alright, sounds like a plan. See ya around, Ivy."

                jump invest_loop

        jump invest_loop

    label living_room:

        $ explored = True
        scene bg living room:
            zoom 1.0
            xalign 1.0

        if roomList["living_room"] == False:
            menu living_room_search:

                "Here's the living room, where Ash is. Should I search the room or talk to her?"

                "Search the room":

                    "The living room is quite messy, as it's where they've spent the most time this weekend. The TV and games certainly kept people busy."

                    "Beyond the mess, there's not much else around the room. Makes sense for no clues here, cause it's been so busy."

                    $ roomList["living_room"] = True
                    
                    menu living_room_post_search:

                        "The room has been searched. Should I talk to Ash or go to another room?"

                        "Talk to Ash.":
                            jump ash_talk
                        
                        "Go to another room.":
                            jump invest_loop
                
                "Talk to Ash.":
                    jump ash_talk
        else:
            "I've already searched the room, let's talk to Ash."
            jump ash_talk

    label ash_talk:

        show ivy_inactive at ivyT
        show ash_neutral at ashT
        with short_dissolve

        ash "Ah, hi Ivy. I was wondering when you'd come question me."

        menu ash_qs:

            ash "What's up?"

            "Did you break it?" if parker_clues == False or ash_confront == False:
                
                show ash_angry at ashT
                with short_dissolve

                ash "Absolutely not. I'm appalled you'd even ask me."

                hide ash_angry
                show ash_inactive at ashT
                show ivy_neutral at ivyT
                with short_dissolve

                ivy "Look Ash, I've asked everyone."

                hide ash_inactive
                hide ivy_neutral
                with short_dissolve

                ash "Yeah, sure."

                jump ash_qs
            
            "What was your schedule like today?" if parker_clues == False or ash_confront == False:
                
                show ash_angry at ashT
                with short_dissolve

                ash "What? Why?"

                hide ash_angry
                show ash_inactive at ashT
                show ivy_neutral at ivyT
                with short_dissolve

                ivy "I'm trying to track down where people where so I can figure out who ruined the scrapbook."

                hide ivy_neutral
                hide ash_inactive
                with short_dissolve
                
                ash "Sure, sure. Well, I hung out in the bedroom, the kitchen, the office, and then the library."

                show ivy_neutral at ivyT
                show ash_inactive at ashT
                with short_dissolve
                
                ivy "Okay, sounds good. Were you always alone, or did you see anyone else?"

                hide ivy_neutral
                hide ash_inactive
                with short_dissolve

                ash "I hung out with Parker in the kitchen, but rather than that I was alone."

                jump ash_qs
            
            "Is there anything you know that might help me?" if parker_clues == False or ash_confront == False:
                
                show ash_angry at ashT
                with short_dissolve

                ash "Look, I know Reagan is all about kindness and being a good friend, but come on!"

                ash "She's got to be hiding something! There's no way she's not lying just to make herself look like a better person."

                hide ash_angry
                show ash_inactive at ashT
                show ivy_angry at ivyT
                with short_dissolve
                
                ivy "Well, that's quite rude to assume. Is there anything suspicious she's done for you to think so?"

                hide ash_inactive
                hide ivy_angry
                with short_dissolve
                
                ash "She just gives off that vibe, you know? Look, I can tell. Talk to her and find out more."

                jump ash_qs
            
            "Can I ask you about this item I found?" if parker_clues == False or ash_confront == False:
                ash "Sure, what is it?"

                menu ash_clues:
                    "Show her the computer searches." if clues["computer"] == True and reagan_confront == False:
                        ash "Hah, lame. These searches are stupid, and not mine."

                        jump ash_qs
                    
                    "Show her the crumpled up 'Sorry' note." if clues["note"] == True and parker_confront == False:
                        ash "Oh wow, what attrotious writing, did you get this from a third grader?"

                        jump ash_qs
                    
                    "Show her the glue and scraps." if clues["scraps"] == True:
                        ash "What? Where did you find these?"

                        show ash_inactive at ashT
                        show ivy_neutral at ivyT
                        with short_dissolve

                        ivy "Oh, just in the library. Do you recognize them?"

                        hide ash_inactive
                        hide ivy_neutral
                        with short_dissolve

                        ash "No, they just look filthy. I'd just throw them away, why keep that trash around?"

                        show ash_inactive at ashT
                        show ivy_neutral at ivyT
                        with short_dissolve

                        ivy "These are obviously a clue, the paper pattern is very similar to the family scrapbook."

                        hide ash_inactive
                        hide ivy_neutral
                        with short_dissolve
                        
                        ash "Hmm... I don't see it. Just throw them away, Ivy."

                        show ash_inactive at ashT
                        show ivy_neutral at ivyT
                        with short_dissolve

                        ivy "I'm not throwing away a clue Ash, calm down."

                        show ash_angry at ashT
                        hide ivy_neutral
                        with short_dissolve

                        ash "Just. Throw it away. I swear, you've become so obsessive over this \"mystery\"."

                        hide ash_angry
                        show ivy_neutral at ivyT
                        with short_dissolve

                        ivy "Yeah, whatever. Thanks for looking at them..."

                        hide ivy_neutral
                        with short_dissolve

                        if parker_clues == False:
                            "She probably wants me to throw away the scraps cause they were hers, but I'm going to need more information before I confront her."
                        else:
                            "If Ash really was hiding something from everyone, even Parker, and is insisting these scraps be thrown away, I need to figure out the truth."

                        $ ash_confront = True

                        hide ash_inactive
                        with short_dissolve

                        jump ash_qs
                    
                    "Show her the messy scrapbook sketches." if clues["sketch"] == True and sterling_confront == False:
                        ash "Hm, never seen these before."

                        jump ash_qs
                    
                    "Nevermind.":
                        ash "Nevermind then, huh?"

                        jump ash_qs
            
            "Ash, we need to talk." if ash_confront == True and parker_clues == True and mystery_solved["ash"] == False:
                
                show ash_inactive at ashT
                with short_dissolve
                
                "Ash was so insistent I throw away these scraps, they have to be hers."

                show ivy_neutral at ivyT
                with short_dissolve

                ivy "Ash, I know the scrapbook scraps are yours. And, I know you've been hiding something from everyone."

                ivy "It's time to tell the truth."

                hide ivy_neutral
                hide ash_inactive
                with short_dissolve

                ash "What? No, you're wrong."

                show ash_inactive at ashT
                show ivy_neutral at ivyT
                with short_dissolve

                ivy "Really? Can you explain these scraps then? No one else recognized them, except for you."

                hide ivy_neutral
                show ash_angry at ashT
                with short_dissolve

                ash "I didn't recognize them, I just insisted you throw away the trash."

                hide ash_angry
                show ivy_neutral at ivyT
                with short_dissolve

                ivy "Well, you did also avoid Parker in the bedroom once you saw him there. What could you be hiding, even from him?"

                show ash_angry at ashT
                hide ivy_neutral
                with short_dissolve
                
                ash "Nothing. I'm not hiding anything."
                
                show ivy_angry at ivyT
                hide ash_angry
                with short_dissolve

                ivy "Ash you're just shutting down on me. You can't avoid this, I know you're hiding something!"

                hide ivy_angry
                show ash_angry at ashT
                with short_dissolve

                ash "I'm not."

                hide ash_angry
                show ivy_angry at ivyT
                with short_dissolve

                ivy "Oh don't pull that on me, I know you are. Fess up."

                hide ivy_angry
                show ash_angry at ashT
                with short_dissolve

                ash "..."

                hide ash_angry
                show ivy_angry at ivyT
                with short_dissolve

                ivy "Well? I'm not leaving until I know the truth. Unless you'd like me to assume you ruined the scrapbook."

                ivy "Or worse, that you ruined it on purpose."

                show ash_sad at ashT
                hide ivy_angry
                with short_dissolve

                ash "Ivy, you know I'd never do that to you or your family!"

                hide ash_sad
                show ivy_neutral at ivyT
                with short_dissolve

                ivy "Maybe, but you're acting so weird that it's a possibility."

                hide ivy_neutral
                show ash_angry at ashT
                hide ash_inactive
                with short_dissolve

                ash "Look..."

                show ash_sad at ashT
                hide ash_angry
                with short_dissolve

                ash "Yeah, I've been lying for a while. I got fired a few weeks ago. There was an issue with intellectual property with the software I made."

                ash "Rather than pay me adequately, they just fired me. I've been talking with lawyers about it, but until then..."

                ash "I didn't want to let you guys know I was struggling. I could barely afford the trip out here this weekend."

                show ivy_sad at ivyT
                hide ash_sad
                show ash_inactive at ashT
                with short_dissolve
                
                ivy "Ash... you certainly didn't have to lie about this, I'm sorry. If I'd known it was a burden, we could've figured something out."

                show ash_sad at ashT
                hide ivy_sad
                with short_dissolve
                
                ash "I didn't want the help, or to feel like I was causing issues."

                show ivy_neutral at ivyT
                hide ash_sad
                with short_dissolve

                ivy "I get it, really. Wait, what were the scraps all about then? Were they yours?"

                hide ash_inactive
                hide ivy_neutral
                with short_dissolve

                ash "Yeah... since I was strapped for cash I attempted to create my own scrapbook page for you, as your birthday gift."

                ash "I even used your family scrapbook as a bit of inspiration, but I put it back right after."

                show ash_inactive at ashT
                show ivy_neutral at ivyT
                with short_dissolve
                
                ivy "Ah, guess that makes sense why the page pattern looked so similar."

                $ mystery_solved["ash"] = True

                if mystery_solved["reagan"] == True and mystery_solved["parker"] == True and mystery_solved["sterling"] == True:
                    $ ending = True
                    jump solving
                else:

                    hide ivy_neutral
                    with short_dissolve

                    "Ash used the scrapbook, but she says she didn't ruin it. I should keep investigating the other suspects."
                    jump invest_loop

            "That's all for now.":
                ash "Cool, let's hope you don't have to come bother me again."

                jump invest_loop

        jump invest_loop

    label office:

        $ explored = True
        scene bg office:
            zoom 1.75
            yalign 1.0
        
        if roomList["office"] == False:

            "Here's the office, the scene of the crime. I should take a look around."

            "The scrapbook is still sitting on the desk, with paper shreds and wet pages all around it."

            "I still feel so bad that it got ruined, hopefully I can figure out what happened."

            "Everything else in the room is surprisingly clean and well kept."

            "The computer seems to be off as well... no, just asleep. The screen lit up when I wiggled the mouse."

            "Hold on... whoever was using the computer last had a bunch of tabs open."

            "They were searching 'how to lie', 'how to keep secrets', and other variations of that question."

            "How odd, why would someone be looking to lie? I should write these down and ask the suspects about them."

            "Nothing else seems to be important in this room, and there's no one here. I should head for a different one."

            $ roomList["office"] = True

            $ clues["computer"] = True

            jump invest_loop

        else:
            "I've already searched this room, there's nothing else to do here."
            jump invest_loop
    
        jump invest_loop

    label solving:
        
        if ending == True:
            
            hide ash_inactive
            hide ivy_neutral
            hide ash_neutral
            hide ivy_inactive
            show ivy_neutral at ivyT
            show ash_inactive at ashT
            with short_dissolve

            ivy "Wait a second... you put the scrapbook away right after? Was it damaged at all?"

            show ivy_inactive at ivyT
            show ash_neutral at ashT
            with short_dissolve

            ash "Huh? No, it was in pristine condition. Why?"

            hide ash_neutral
            hide ivy_inactive
            with short_dissolve

            ivy "Well, Sterling said he found it ruined when he entered the office at 4:00, and you were in there just before him."

        else:
            "Geez, everyone's alibis seem pretty thorough. But, luckily I know that Sterling found the scrapbook ruined around 4:00."

            "If I remember correctly, I believe Ash was in the office before him. I should go talk to her."

            # SCENE CHANGE - Living Room w/Ash

            show bg living room:
                zoom 1.0
                xalign 1.0

            show ivy_inactive at ivyT
            show ash_neutral at ashT
            with short_dissolve

            ash "Ah, welcome back. How's the investigation?"

            show ivy_neutral at ivyT
            show ash_inactive at ashT
            with short_dissolve

            ivy "Fine, but I'm running out of clues. I've got one more lead though."

            hide ivy_neutral
            hide ash_inactive
            with short_dissolve

            ash "Oh? And I'm guessing it has something to do with me?"

            show ivy_neutral at ivyT
            show ash_inactive at ashT
            with short_dissolve

            ivy "Yes, it does. Look, Sterling confessed to me that he found the scrapbook ruined when he entered the office around 4:00."

            ivy "From looking at everyone's schedules, the person who was just there before him was... you."

            hide ivy_neutral
            hide ash_inactive
            with short_dissolve
            
            ash "Wait, so you think I ruined the scrapbook? And just left it there?"

            show ivy_neutral at ivyT
            show ash_inactive at ashT
            hide ash_neutral
            hide ivy_inactive
            with short_dissolve
            
            ivy "I mean, it's the last solid clue I've got, so... yeah, I think so."
        
        show ivy_inactive at ivyT
        show ash_angry at ashT
        with short_dissolve

        ash "What?! No, I left the room spotless!"

        show ash_neutral at ashT
        hide ash_angry
        with short_dissolve

        ash "Hold on, you don't need my word on that. I took a few pictures of the scrapbook for my inspiration."

        hide ash_neutral
        with short_dissolve
        
        "Ash holds up her phone for me, and she's got a few pictures of the family scrapbook, like she said. It looks perfectly unruined."

        hide ivy_inactive
        with short_dissolve
        
        ivy "Alright, so it wasn't ruined while you were in there. And you just put it away right after?"

        show ivy_inactive at ivyT
        show ash_neutral at ashT
        with short_dissolve

        ash "Yes! I swear I did."

        hide ash_neutral
        with short_dissolve

        "Hmm... the pictures certainly don't lie. I should go ask Sterling about this new information."

        hide ash_inactive
        hide ivy_inactive
        hide ivy_neutral
        with short_dissolve

        # SCENE CHANGE - Bedroom w/Sterling

        show bg bedroom:
            zoom 0.8
            xalign 1.0

        show sterling_neutral at sterlingT
        show ivy_inactive at ivyT
        with short_dissolve

        sterling "Hey, Ivy. What brings you back around?"

        show ivy_neutral at ivyT
        show sterling_inactive at sterlingT
        with short_dissolve

        ivy "Alright Sterling, I know something is up."

        hide ivy_neutral
        hide sterling_inactive
        with short_dissolve

        sterling "W-What? What does that mean?"

        show ivy_neutral at ivyT
        show sterling_inactive at sterlingT
        with short_dissolve

        ivy "I talked to Ash about you finding the scrapbook ruined, since she was in the office before you. She says it wasn't her."

        hide ivy_neutral
        hide sterling_inactive
        with short_dissolve

        sterling "Oh, she said so? How do you know she's telling the truth?"

        show ivy_neutral at ivyT
        show sterling_inactive at sterlingT
        with short_dissolve

        ivy "Well, she had pictures confirming it was unruined in her care."

        hide ivy_neutral
        hide sterling_inactive
        show sterling_sad at sterlingT
        with short_dissolve

        sterling "Oh..."

        sterling "Well, what if she ruined it after?"

        hide sterling_sad
        show sterling_inactive at sterlingT
        show ivy_neutral at ivyT
        with short_dissolve

        ivy "I don't think so, she insists it was in prisine condition when she left."

        hide ivy_neutral
        hide sterling_inactive
        with short_dissolve

        sterling "I know she's your friend, but I know what I saw, Ivy."

        show ivy_neutral at ivyT
        show sterling_inactive at sterlingT
        with short_dissolve

        ivy "Do you? Cause I'm finding it hard to argue with photo evidence. Do you have any other facts to support what you saw?"

        hide ivy_neutral
        hide sterling_inactive
        with short_dissolve
        
        sterling "I, uh... I saw Parker leaving the office, a few minutes before I went in. Maybe Ash is just covering for him, you know?"

        show ivy_neutral at ivyT
        show sterling_inactive at sterlingT
        with short_dissolve
        
        ivy "I don't see how that's possible when Parker had been in the bedroom to see Ash come in after she left the office."

        hide ivy_neutral
        hide sterling_inactive
        with short_dissolve

        sterling "O-Oh, umm..."

        show sterling_inactive at sterlingT
        show ivy_angry at ivyT
        with short_dissolve

        ivy "Sterling. What is going on? Out of everyone I never thought it'd be you, but here we are."

        hide ivy_angry
        hide sterling_inactive
        with short_dissolve
        
        sterling "Ivy, babe... I..."

        show sterling_inactive at sterlingT
        with short_dissolve

        "He lets out a bit of nervous laughter, watching my expression intently."

        hide sterling_inactive
        with short_dissolve

        sterling "Alright, it was me. I ruined the scrapbook."

        show sterling_inactive at sterlingT
        show ivy_angry at ivyT
        with short_dissolve

        ivy "W-What? Are you serious?"

        hide ivy_angry
        hide sterling_inactive
        with short_dissolve

        sterling "Wait, just a second before you yell at me please!"

        sterling "I've already reached out to your parents about the ruined scrapbook, and we're figuring out what to do."

        sterling "That was actually the call I got earlier at dinner."

        show sterling_inactive at sterlingT
        show ivy_neutral at ivyT
        with short_dissolve

        ivy "Really? Since when were you in contact with my parents about this situation?"

        hide ivy_neutral
        hide sterling_inactive
        with short_dissolve

        sterling "Well... I had asked them about it before this weekend."

        show sterling_inactive at sterlingT
        show ivy_neutral at ivyT
        with short_dissolve

        ivy "Okay... why? You still haven't answered my question, Sterling."

        hide ivy_neutral
        hide sterling_inactive
        with short_dissolve

        sterling "I just... I was..."

        show sterling_inactive at sterlingT
        with short_dissolve

        "He lets out a sigh, shoulders sinking in disappointment."

        show sterling_sad at sterlingT
        with short_dissolve

        sterling "I've been secretly trying to figure out how to propose to you. Your parents actually brought up the scrapbook..."

        sterling "... as they thought it could help give some inspiration for me. So, when I got the chance, I snuck into the office to look at it."

        sterling "It was fine, at first. I saw some cute pictures, and all that fun stuff. But, everything went wrong when I spilled the soda on it."

        sterling "I-I tried to sop it up with my jacket, but realized I was just smudging it all around and even ripped some pages."

        sterling "By the time I realized the damage I had done, it was a mess. I frantically tried to call your parents then, to explain what I'd done."

        sterling "But, then Reagan was calling everyone in for dinner and I just... left it there. I thought it would go undetected for the night."

        sterling "Obviously, that didn't work. I'm sorry Ivy, it was all my fault."

        hide sterling_sad
        with short_dissolve

        "Honestly, I was feeling quite the range of emotions. Angry at his lies, flustered he wanted to propose, my head was spinning."

        show ivy_sad at ivyT
        with short_dissolve

        ivy "I... Sterling... what? I'm happy you wanted to propose, but... why lie about all of this? You could've told me earlier!"

        hide ivy_sad
        hide sterling_inactive
        with short_dissolve
        
        sterling "Well... my reasoning for that is a bit selfish. I put up this whole act, the lying and the accusing..."

        show sterling_happy at sterlingT
        with short_dissolve

        sterling "... because I know you love mystery podcasts and shows, and I thought you'd enjoy solving one for yourself."
        
        hide sterling_happy
        show sterling_inactive at sterlingT
        show ivy_happy at ivyT
        with short_dissolve

        ivy "Oh, babe, that's so sweet... and I did have a bit of fun, I gotta admit."

        hide ivy_happy
        show ivy_neutral at ivyT
        with short_dissolve

        ivy "But next time, don't lie to me, you idiot."

        hide ivy_neutral
        show sterling_happy at sterlingT
        with short_dissolve

        sterling "Alright, I promise I won't."

        hide sterling_happy
        show sterling_inactive at sterlingT
        with short_dissolve

        "Well, that certainly wasn't the outcome I was expecting. But, with the mystery solved and only making fun of Sterling a little..."

        "... I had a lot of fun that weekend. What a crazy birthday!"

        return

    return