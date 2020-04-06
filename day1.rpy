label ch_mod_1a:
    $ gtext = glitchtext(48)
    stop music
    $ config.window_hide_transition = None
    scene black with trueblack
    pause 0.01
    scene bg residential_day
    with dissolve_scene_half
    $ config.window_hide_transition = Dissolve(.2)
    play music t2g
    queue music t2g2

    $ s_name = glitchtext(12)
    $ gtext = glitchtext(80)
    s "[gtext]"
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    "That girl is [s_name], my neighbor and good friend since we were children."
    "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
    "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
    "But if she's going to chase after me like this, I almost feel better off running away."
    "However, I just sigh and idle in front of the crosswalk and let [s_name] catch up to me."

    show sayori glitch at t11 zorder 2
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/2.ogg"
        renpy.music.play(track, loop=True)
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    window hide(None)
    window auto
    scene black with trueblack
    $ persistent.playthrough = 2
    $ persistent.anticheat = renpy.random.randint(100000, 999999) # why not
    $ anticheat = persistent.anticheat

    $ del _history_list[0:]
    scene bg residential_day
    with dissolve_scene_half
    play music t2
    jump ch_mod_1

label ch_mod_1b:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    if not persistent.sayori_revived:
        play music t2
        jump ch_mod_1
    else:
        $ no_return()
        jump save_sayori

label ch_mod_1:
    "It's an ordinary school day, like any other."
    "Mornings are usually the worst, being surrounded by couples and friend groups walking to school together."
    "Meanwhile, I've always walked to school alone."
    $ currentpos = get_pos()
    stop music
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    "Wait, wasn't I thinking just a second ago about someone I was walking with?"
    "But why would I be thinking that? I'm not walking with anyone. Like I said, I've {i}always{/i} walked to school alone."
    "Probably nothing, I guess..."
    $ del _history_list[-3:]
    $ audio.t2 = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
    play music t2
    "I always tell myself it's about time I meet some girls or something like that..."
    "But I have no motivation to join any clubs."
    "After all, I'm perfectly content just getting by on the average while spending my free time on games and anime."
    window auto
    scene bg class_day
    with wipeleft_scene
    "The school day is as ordinary as ever, and it's over before I know it."
    "After I pack up my things, I stare blankly at the wall, looking for an ounce of motivation."
    mc "Clubs..."
    "There really aren't any that interest me."
    "Besides, most of them would probably be way too demanding for me to want to deal with."
    "I guess I have no choice but to start with the anime club..."

    # Glitched Monika appears
    $ currentpos = get_pos()
    stop music
    $ config.keymap['dismiss'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    mc "\"What the hell is that?!\"{w=1.0}{nw}"
    "{cps=*1.5}The \"thing\" is starting to approach me.{/cps}{w=0.5}{nw}"
    "{cps=*1.5}It's getting closer and closer now...{/cps}{w=0.5}{nw}"
    "{cps=*1.5}Ah, what is happening to this world?!!?!{/cps}{w=0.2}{nw}"
    mc "{cps=*1.5}WHAT THE F{/cps}{nw}"
    show monika g2 at t11 zorder 2
    $ gtext = glitchtext(80)
    $ style.say_dialogue = style.edited
    mc "{cps=*1.5}WHAT THE F{fast}[gtext]{/cps}{nw}"
    $ style.say_dialogue = style.normal
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    hide monika
    window show(None)
    $ config.keymap['dismiss'] = dismiss_keys
    $ renpy.display.behavior.clear_keymap_cache()
    $ style.say_dialogue = style.normal
    $ del _history_list [-6:]
    $ track = "<from " + str(currentpos) + " loop 4.499>bgm/2.ogg"
    $ renpy.music.play(track, loop=True)
    $ m_name = "???"
    show monika 1a at t11 zorder 2
    m "...[player]?"
    $ m_name = "Monika"
    m 1b "Oh my goodness, I totally didn't expect to see you here!"
    m 5 "It's been a while, right?"
    mc "Ah..."
    "What did I just witness?"
    mc "Yeah, it has."
    "Monika smiles sweetly."
    "We do know each other - well, we rarely talked, but we were in the same class last year."
    "Huh?"
    "I feel like I met her here not long ago..."
    "But I know I didn't."
    "What is happening to my head right now?"
    mc "What did you come in here for, anyway?"
    m 1a "Oh, I've just been looking for some supplies to use for my club."
    m 1d "Do you know if there's any construction paper in here?"
    m "Or markers?"
    mc "I guess you could check the closet."

    # MC remembers the literature club
    mc "...You're in the literature club, right?"
    "Wait, what? Why did I say that? I know she's in the debate club. I must have misspoken somehow... weird."
    m "Aha- wait. What did you say?"
    mc "Uh, I mean the debate club."
    m 5 "Ahaha, about that..."
    m "I actually quit the debate club."
    mc "Really? You quit...?"
    m "Yeah..."
    m 2e "To be honest, I can't stand all of the politics around the major clubs."
    m "It feels like nothing but arguing about the budget and publicity and how to prepare for events..."
    m "I'd much rather take something I personally enjoy and make something special out of it."
    mc "In that case, what club did you decide to join?"
    m 1b "Actually, I'm starting a new one!"
    m "A literature club!"
    "No way... What a coincidence..."
    mc "Literature...?"
    mc "How many members do you have so far?"
    m "Ahaha..."
    m "It's kind of embarrassing, but there are only three of us so far."
    m "It's really hard to find new members for something that sounds so boring..."
    mc "Well, I can see that..."
    m 3d "But it's really not boring at all, you know!"
    m "Literature can be anything. Reading, writing, poetry..."
    m 3e "I mean, one of my members even keeps her manga collection in the clubroom..."
    mc "Wait...really?"
    m 2k "Yeah, it's funny, right?"
    m 2e "She always insists that manga is literature, too."
    m "I mean, she's not wrong, I guess..."
    m "And besides, a member's a member, right?"
    "...Did Monika say \"she\"?"
    "Hmm..."
    m 1a "Hey, [player]..."
    m "By any chance...are you still looking for a club to join?"
    mc "Ah--"
    mc "I mean, I guess so, but..."
    m "In that case..."
    m 5 "Is there any chance you could do me a big favor?"
    m "I won't ask you to join, but..."
    m "If you could at the very least visit my club, it would make me really happy."
    m "Please?"
    mc "Um..."
    menu:
        "Well, I guess I have no reason to refuse..."
        "Visit her club":
            $ no_return()
            $ persistent.mc_awareness[0] = False
            mc "Sure, I guess I could check it out."
        "Don't visit her club":
            $ no_return()
            mc "Sorry, but I don't think -"
            "Wait, what? That wasn't what I wanted to say! I feel like my mouth just opened on its own!"
            mc "I mean, yeah, I guess I could check it out."
            $ persistent.mc_awareness[0] = True
    m 1k "Aah, awesome!"
    m 1b "You're really sweet, [player], you know that?"
    m 1a "Shall we go, then?"
    m "I'll look for the materials another time - you're more important."

    stop music fadeout 2.0
    scene bg corridor
    with wipeleft_scene
    "And thus, today marks the day I sold my soul to Monika and her irresistible smile."
    "I timidly follow Monika across the school and upstairs - a section of the school I rarely visit, being generally used for third-year classes and activities."
    "Monika, full of energy, swings open the classroom door."

    scene bg club_day
    with wipeleft
    play music t3

    # Monika's image is glitched
    show monika g1 at l31
    m "I'm back~!"
    m "And I brought a guest with me!"
    "What the heck did I just see?"
    show yuri 2t at t33 zorder 2
    show screen invert(0.15, 0.3)
    $ y_name = "Girl 1"
    y "Eh?"
    y "A...a guest?"
    show natsuki 4c at t32 zorder 2
    $ n_name = "Girl 2"
    n "Seriously? You brought a boy?"
    n "Way to kill the atmosphere."
    mc "Excuse me?"
    show monika 3m at f31 zorder 3
    m "Don't be mean, Natsuki..."
    m 3b "...But anyway, welcome to the club, [player]!"
    show monika 3a at t31 zorder 2
    mc "..."
    "Hmm..."
    "I guess this club is alright..."
    "Why do I feel empty seeing their cute faces?"
    "I don't even understand my own feelings."
    show natsuki at f32 zorder 3
    n 5c "So, let me guess..."
    n "You're Monika's boyfriend, right?"
    mc "W-What?"
    mc "What gives you that idea?"
    show natsuki at t32 zorder 2
    show yuri at f33 zorder 3
    y 2l "Natsuki..."
    show yuri at t33 zorder 2
    $ n_name = 'Natsuki'
    "The girl with the sour attitude, whose name is apparently Natsuki, is one I don't recognize."
    "Her small figure makes me think she's probably a first-year."
    "Wait, I should've introduced you when Monika said \"Don't be mean, Natsuki...\""
    $ _history_list.pop()
    "What am I talking about?"
    $ _history_list.pop()
    show monika at f31 zorder 3
    m 2l "A-Anyway, this is Natsuki, energetic as usual..."
    m 2b "And this is Yuri, the Vice President!"
    $ y_name = 'Yuri'
    show monika 2a at t31 zorder 2
    show yuri at f33 zorder 3
    y 4 "I-It's nice to meet you..."
    "Yuri, who appears comparably more mature and timid, seems to have a hard time keeping up with someone like Natsuki."
    show yuri at t33 zorder 2
    show natsuki at f32 zorder 3
    n 4e "Wait! Monika!"
    n "Didn't I tell you to let me know in advance before bringing anyone new?"
    n 4q "I was going to...well, you know..."
    show natsuki at t32 zorder 2
    show monika at f31 zorder 3
    m 1e "Sorry, sorry!"
    m "I didn't forget that, but I just happened to run into him."
    show monika at t31 zorder 2
    show yuri at f33 zorder 3
    y 1a "In that case, I should at least make some tea, right?"
    show yuri at t33 zorder 2
    mc "Ah, thanks."
    show monika at f31 zorder 3
    m 1b "Yeah, that would be great!"
    m "Why don't you come sit down, [player]?"
    mc "Sure..."
    hide monika
    hide natsuki
    hide yuri
    with wipeleft

    "The girls have a few desks arranged to form a table."
    "Yuri walks to the corner of the room and opens the closet."
    "Meanwhile, Monika and Natsuki sit across from each other."
    "I take a seat next to Monika."
    show monika 1a at t11 zorder 2
    m "So, I know you didn't really plan on coming here..."
    m "But we'll make sure you feel right at home, okay?"
    m 1j "As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!"
    mc "I'm surprised there aren't more people in the club yet."
    mc "It must be hard to start a new club."
    m 3b "You could put it that way."
    m "Not many people are very interested in putting out all the effort to start something brand new..."
    m "Especially when it's something that doesn't grab your attention, like literature."
    m "You have to work hard to convince people that you're both fun and worthwhile."
    m "But it makes school events, like the festival, that much more important."
    m 2k "We'll figure that out soon enough, I'm confident that we can all really grow this club before we graduate!"
    m "Right, Natsuki?"
    show monika at t22 zorder 2
    show natsuki 4q at t21 zorder 2
    n "Well..."
    n "...I guess."
    "Natsuki reluctantly agrees."
    "Well, I guess literature isn't really that hard."
    "Despite it being kind of dull, it's worth it to make a poem, share it with your friends and to find inspiration from other people."
    "The basic fundamental of literature is to express yourself."
    "I don't know, I feel like I've done this before."
    "Yuri returns to the table, carrying a tea set."
    "She carefully places a teacup in front of each of us before setting down the teapot in the middle."
    show natsuki at thide zorder 1
    show monika at thide zorder 1
    hide natsuki
    hide monika
    show yuri 1a at t21 zorder 2
    mc "You keep a whole tea set in this classroom?"
    show yuri 1a at f21 zorder 3
    y "Don't worry, the teachers gave us permission."
    y "After all, doesn't a hot cup of tea help you enjoy a good book?"
    show yuri 1a at t21 zorder 2
    mc "Ah... I guess you're right, Yuri."
    show monika 4a at f22 zorder 3
    m "Ehehe, don't let yourself get intimidated, Yuri's just trying to impress you."
    show monika at t22 zorder 2
    show yuri at hf21
    y 3n "Eh?! T-That's not..."
    "Insulted, Yuri looks away."
    y 4b "I meant that, you know..."
    show yuri at t21 zorder 2
    mc "I believe you."
    mc "Well, tea and reading might not be a pastime for me, but I at least enjoy tea."
    show yuri at f21 zorder 3
    y 2u "I'm glad..."
    show yuri at t21 zorder 2
    "Yuri faintly smiles to herself in relief."
    show monika at thide zorder 1
    hide monika
    show yuri 1a at t32 zorder 2
    y "So, [player], what kinds of things do you like to read?"
    mc "Well... Ah..."
    "Considering how little I've read these past few years, I don't really have a good way of answering that."
    menu:
        "I guess I'll be honest, the one thing I do read is..."
        "Manga":
            $ no_return()
            $ persistent.mc_awareness[1] = False
            $ horror = False
        "Horror":
            $ no_return()
            $ horror = True
            "For some reason, I find the word 'horror' about to roll off my tongue."
            "Where did that come from? I've barely ever read any horror."
    mc "...Manga..."
    "I mutter quietly to myself, half-joking."
    show natsuki 1c at t41 zorder 2
    "Natsuki's head suddenly perks up for some reason."
    "It looks like she wants to say something, but she keeps quiet."
    show natsuki at thide zorder 1
    hide natsuki
    y 3u "N-Not much of a reader, I guess..."
    mc "Ah..."
    mc "Don't say that, you're making it sound like a big deal or something."
    "I say that because of Yuri's sad smile."
    "It's up to me to save this situation."
    mc "I do like reading sometimes."
    mc "If there's any book that tells an interesting story, then I usually enjoy reading it."
    y 3v "I see..."
    "I can tell I relieved her a little bit."
    mc "Anyway, what about you, Yuri?"
    y 1l "Well, let's see..."
    "Yuri traces the rim of her teacup with her finger."
    y 1a "My favorites are usually novels that build deep and complex fantasy worlds."
    y "The level of creativity and craftsmanship behind them is amazing to me."
    y 1f "And telling a good story in such a foreign world is equally impressive."
    "Yuri goes on, clearly passionate about her reading."
    "She seemed so reserved and timid since the moment I walked in, but it's obvious by the way her eyes light up that she finds her comfort in the world of books as I imagined, not people."
    y 2m "But you know, I like a lot of things."
    y "Stories with deep psychological elements usually immerse me as well."
    "Something seems fishy about this conversation. Every sentence she says sounds familiar."
    y 2a "Isn't it amazing how a writer can so deliberately take advantage of your own lack of imagination to completely throw you for a loop?"
    y "Anyway, I've been reading a lot of horror lately..."
    mc "Ah, I read a horror book once..."
    if horror:
        mc "I think it ended with the main character's girlfriend hanging herself out of depression."
        "A wave of nausea passes over me. I put my hand on my stomach."
        window hide(None)
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        window show(None)
        "But almost instantly it's over."
        "I can't even remember the details of that story, but for some reason just thinking about it makes me sick."
        $ persistent.mc_awareness[1] = True
    else:
        "I desperately grasp something I can relate to at the minimal level."
        "At this rate, Yuri might as well be having a conversation with a rock."
    show monika 1j at f33 zorder 3
    m "Ahaha. I'd expect that from you, Yuri."
    m 1a "It suits your personality."
    show monika at t33 zorder 2
    show yuri at f32 zorder 3
    y 1a "Oh, is that so?"
    y "Really, if a story makes me think, or takes me to another world, then I really can't put it down."
    y "Surreal horror is often very successful at changing the way you look at the world, if only for a brief moment."
    show yuri at t32 zorder 2
    show natsuki 5q at f31 zorder 3
    n "Ugh, I hate horror..."
    show natsuki at t31 zorder 2
    show yuri at f32 zorder 3
    y 1f "Oh? Why's that?"
    show yuri at t32 zorder 2
    show natsuki at f31 zorder 3
    n 5c "Well, I just..."
    "Natsuki's eyes dart over to me for a split second."
    show natsuki at t31 zorder 2
    mc "Huh?"
    show natsuki at f31 zorder 3
    n 5q "Never mind."
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 1a "That's right, you usually like to write about cute things, don't you, Natsuki?"
    show monika at t33 zorder 2
    show natsuki 1o at f31 zorder 3
    n "W-What?"
    n "What gives you that idea?"
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 3b "You left a piece of scrap paper behind last club meeting."
    m "It looked like you were working on a poem called--"
    show monika at t33 zorder 2
    show natsuki 1p at f31 zorder 3
    n "Don't say it out loud!!"
    n "And give that back!"
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m 1j "Fine, fine~"
    show monika 1a at t33 zorder 2
    mc "Natsuki, you write your own poems?"
    "I have an incredibly strong feeling that I've had this exact conversation before."
    "What is wrong with my mind today?"
    show natsuki at f31 zorder 3
    n 1c "Eh? Well, I guess sometimes."
    n "Why do you care?"
    show natsuki at t31 zorder 2
    mc "I think that's impressive."
    mc "Why don't you share them sometime?"
    show natsuki at f31 zorder 3
    n 5q "N-No!"
    "Natsuki averts her eyes."
    n "You wouldn't...like them..."
    show natsuki at t31 zorder 2
    mc "Ah...not a very confident writer yet?"
    show yuri at f32 zorder 3
    y 2f "I understand how Natsuki feels."
    y "Sharing that level of writing takes more than just confidence."
    y 2k "The truest form of writing is writing to oneself."
    y "You must be willing to open up to your readers, exposing your vulnerabilities and showing even the deepest reaches of your heart."
    show yuri at t32 zorder 2
    show monika 2a at f33 zorder 3
    m "Do you have writing experience too, Yuri?"
    m "Maybe if you share some of your work, you can set an example and help Natsuki feel comfortable enough to share hers."
    show yuri at s32
    y 3o "..."
    mc "Well, I guess it's the same for Yuri..."
    "We all sit in silence for a moment."
    show monika at f33 zorder 3
    m 5a "Hey, I just got an idea!"
    m "How about this?"
    show monika at t33 zorder 2
    show natsuki 2k at f31 zorder 3
    show yuri 3e at f32 zorder 3
    ny "...?"
    "Natsuki and Yuri look quizzically at Monika."
    "I guess I should look at Monika, too."
    show natsuki at t31 zorder 2
    show yuri at t32 zorder 2
    show monika at f33 zorder 3
    m 2b "Let's all go home and write a poem of our own!"
    m "Then, next time we meet, we'll all share them with each other."
    m "That way, everyone is even!"
    "Didn't I hear this idea before?"
    show monika 2a at t33 zorder 2
    show natsuki at f31 zorder 3
    n 5q "U-Um..."
    show natsuki at t31 zorder 2
    show yuri 3v at f32 zorder 3
    y "..."
    show yuri at t32 zorder 2
    show monika 2m at f33 zorder 3
    m "Ah..."
    m "I mean, I thought it was a good idea..."
    show monika at t33 zorder 2
    show yuri at f32 zorder 3
    y 2l "Well..."
    y "...I think you're right, Monika."
    y 2f "We should probably start finding activities for all of us to participate in together."
    y 2h "I did decide to take on the responsibility of Vice President, after all..."
    y "I need to do my best to nurture the club as well as its members."
    y 2a "Besides, now that we have a new member..."
    y "It seems like a good step for us to take."
    y "Do you agree as well, [player]?"
    show yuri at t32 zorder 2
    menu:
        mc "Well, uh...?"
        "Accept their invitation":
            $ no_return()
            $ accepts_invite = True
            call mod_ch1_accepts
        "Reject their invitation":
            $ no_return()
            $ persistent.mc_awareness[2] = False
            $ accepts_invite = False
            call mod_ch1_rejects
    show monika at f33 zorder 3
    m "I'll do everything I can to give you a great time, okay?"
    if accepts_invite:
        mc "Ah. Alright then..."
    else:
        mc "Ah...thanks, I guess...?"
    show yuri at thide zorder 1
    show natsuki at thide zorder 1
    show monika at t11 zorder 2
    hide yuri
    hide natsuki
    m 3b "Okay, everyone!"
    m "I think with that, we can officially end today's meeting on a good note."
    m "Everyone remember tonight's assignment:"
    m "Write a poem to bring to the next meeting, so we can all share!"
    "Monika looks over at me once more."
    m 1a "[player], I look forward to seeing how you express yourself."
    show monika 5 at hop
    m "Ehehe~"
    "Did she just jump?"
    "Her ecstatic mood seems to be overflowing inside her head."
    "But I begin to understand that it is hard to get a new member. So..."
    mc "Yeah, sure. Looking forward to it."
    show monika at thide zorder 1
    hide monika
    "Can I really impress the class star Monika with my mediocre writing skills?"
    "And will I keep having these weird experiences?"
    "I feel the anxiety welling up inside me."
    "What's going on?"
    "Meanwhile, the girls continue to chit-chat as Yuri cleans up the tea set."
    mc "Alright, Monika."
    mc "See you tomorrow."
    show monika 5a at t11 zorder 2
    m "Okay!"
    m "I'll see you tomorrow too!"
    m "I can't wait~!"
    hide monika

    scene bg residential_day
    with wipeleft_scene
    window auto

    "With that, I depart the clubroom and make my way home."
    "The whole way, my mind wanders{nw}"
    window show(None)
    $ currentpos = get_pos()
    stop music
    $ track = "<from " + str(currentpos) + " loop 4.618>mod_assets/sfx/3l.ogg" 
    $ renpy.music.play(track, loop=True)
    scene bg res_gl
    "The whole way, my mind wanders{fast} back and forth between the three girls:"
    window auto
    show natsuki 4a at t31 zorder 2
    "Natsuki,"
    show yuri 1a at t32 zorder 2
    "Yuri,"
    show monika 1a at t33 zorder 2
    "and, of course, {w}Monika."
    scene bg residential_day
    $ currentpos = get_pos()
    stop music
    $ track = "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
    $ renpy.music.play(track, loop=True)
    "Will I really be happy spending every day after school in a literature club?"
    "Perhaps I'll have the chance to grow closer to one of these girls..."
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "Alright!"
    "I'll just need to make the most of my circumstances, and I'm sure good fortune will find me."
    "And I guess that starts with writing a poem tonight..."

    stop music fadeout 2.0
    scene black with dissolve_scene_full
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False

    # its a joke, pls dont kill me
    call screen confirm("This mod has profanity filter mode.\nDo you want to enable it?", Return(True), Return(False))
    if _return:
        $ persistent.protecc = True
        $ renpy.call_screen("dialog", "Profanity filter is enabled.", ok_action=Return())
    else:
        $ persistent.protecc = False
        $ renpy.call_screen("dialog", "What the fuck, why didn't you enable the goddamn profanity filter?", ok_action=Return())
    if persistent.protecc:
        $ fword = "***"
        $ fgword = "******"
        $ bword = "****"
        $ aword = "******"
        $ sword = "***"
    return

label mod_ch1_accepts:
    "I was going to say no, but suddenly I get this urge to accept their invitation."   
    "Before I can stop myself, I find my mouth opening."
    mc "Yeah..."
    mc "I mean it could be fun, right?"
    mc "Sharing our poems with each other..."
    "What the hell! I was not going to say that!"
    $ persistent.mc_awareness[2] = True
    show monika 1d at f33 zorder 3
    "Monika looks at me quizzically."
    "She seems to agree that it's out of character for me."
    m "Wait, [player]?"
    mc "Yes?"
    "She stares into my eyes for a good 3 seconds long.{w=3}{nw}"
    "Well, now that I think about it, maybe it'll end up being a good decision."
    "I mean, I was telling myself earlier how it's time I meet some girls or something, and this seems like as good an opportunity as any."
    mc "Eh, I mean..."
    mc "You know...."
    m 1b "Oh my goodness!"
    m 5a "You really mean it, don't you?"
    "Monika smiles sweetly."
    show monika at t33 zorder 2
    mc "Yeah, I decided to join your club anyway."
    mc "I guess literature isn't really that bad for me."
    show monika at f33 zorder 3
    m "[player], I'm so happy..."
    m 1k "We can become an official club now!"
    m 1e "Thank you so much for this. You're really amazing."
    show monika at t33 zorder 2
    show natsuki 5w at f31 zorder 3
    n "Hmph. I really thought you didn't want to join our club."
    n 5e "You would be a complete jerk if you did that. Not join, that is."
    mc "Yeah, yeah."
    show natsuki 5a at t31 zorder 2
    show yuri 1a at f32 zorder 3
    y "That is a wise decision."
    y 3m "I am so happy that you joined our club before the festival..."
    show yuri at t32 zorder 2
    mc "Ah, thank you."
    mc "It was my own choice after all."
    "I hope she's okay with me here."
    return

label mod_ch1_rejects:
    mc "Hold on...there's still one problem."
    show monika at f33 zorder 3
    m 1d "Eh? What's that?"
    show monika at t33 zorder 2
    mc "I never said I would join this club!"
    mc "Monika may have convinced me to stop by, but I never made any decision."
    mc "I still have other clubs to look at, and...um..."
    show monika 1g
    show natsuki 4g
    show yuri 2e
    "I don't know why, but I feel kind of guilty after seeing their dejected eyes."
    "I feel bad for them."
    show monika at s33
    m 1p "B-But..."
    show yuri at s32
    y 2v "I'm sorry, I thought..."
    show natsuki at s31
    n 5s "Hmph."
    mc "Eh...?"
    "The girls exchange glances before Monika turns back to me."
    show monika at f33 zorder 3
    m 1m "I...guess I need to tell you the truth, [player]."
    m "The thing is..."
    m 1p "...We don't have enough members yet to form an official club."
    m "We need four..."
    m "And I've been trying really, really hard to find new members."
    m "And if we don't find one more before the festival..."
    show monika at t33 zorder 2
    mc "..."
    mc "I, uh..."
    mc "*Sigh*"
    "I feel like I'm defenseless against these girls."
    "Not to mention my best friend..."
    $ _history_list.pop()
    "Wait, who is my best friend? I don't have any close friends, remember?"
    $ _history_list.pop()
    "Well, they are really cute..."
    "And I would feel terrible for letting everyone down in this situation..."
    "So, if writing poems is the price I need to pay in order to spend every day with these beautiful girls..."
    mc "...Right."
    mc "Okay, I've decided, then."
    mc "I'll join the Literature Club."
    show monika 1e at t33 zorder 2
    show yuri 3f at t32 zorder 2
    show natsuki 1k at t31 zorder 2
    "One by one, the girls' eyes light up."
    show monika at f33 zorder 3
    m "Oh my goodness, really?"
    m "Do you really mean that, [player]?"
    show monika at t33 zorder 2
    mc "Yeah..."
    mc "It could be fun, right?"
    show yuri at f32 zorder 3
    y 1m "You really did scare me for a moment..."
    show yuri at t32 zorder 2
    show natsuki at f31 zorder 3
    n 5q "I mean, if you really just left after all this, I would be super pissed."
    mc "Yeah, yeah..."
    show natsuki at t31 zorder 2
    show monika at f33 zorder 3
    m "[player], I'm so happy..."
    m 1k "We can become an official club now!"
    m 1e "Thank you so much for this. You're really amazing."
    return
