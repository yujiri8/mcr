label ch_mod_2:
    # If you wrote a poem for Sayori, MC has a dream about her
    if persistent.poem1 == "bs":
        call sayori_dream_1
        play music t2
    else:
        scene bg residential_day
        play music t2
        "The next day, I'm on my way to school."
        "I haven't had any weird experiences since I left the literature club yesterday."
        "So maybe whatever was happening to my head passed, and everything will be normal now."

    scene bg cr_gl
    with wipeleft_scene

    "The school day is as ordinary as ever, and it's over before I know it."
    "After I pack up my things, I stare blankly at the wall--"
    "..."
    "I look at the room."
    "It seems messed up."
    "Like my vision is glitching."
    "I blink."
    scene bg class_day
    if persistent.poem1 != "bs": # If MC didn't see the dream of Sayori
        "So much for everything being normal now..."
        "Whatever."
    else:
        "Weird. Whatever. I saw weirder yesterday."
    "After I pack up my things, I should get going."

    play music t2o
    scene bg corridor with wipeleft
    "Well..."
    "I managed to get here in time."
    "Even though I'm a little bit late. I hope they don't mind..."
    "I timidly open the front door."

    scene bg spoopy
    with wipeleft
    $ currentpos = get_pos()
    stop music
    $ track = "<from " + str(currentpos) + " loop 4.492>bgm/2g2.ogg"
    $ renpy.music.play(track, loop=True)
    show monika 5 at t11 zorder 2
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    m "Hi again, [player]!"
    m "Glad to see you didn't run away on us. Hahaha!"
    mc "Nah, don't worry."
    mc "This might be a little strange for me, but I at least keep my word."
    show monika at thide zorder 1
    hide monika
    "Well, I'm back at the Literature Club."
    "I was the last to come in, so everyone else is already hanging out."
    show yuri glitch2 at t32 zorder 2
    y "Thanks for keeping your promise, [player]."
    y 1a "I hope this isn't too overwhelming of a commitment for you."
    y 1u "Making you dive headfirst into literature when you're not accustomed to it..."
    mc "Well, that's true..."
    mc "But it won't be a problem. I like to try out new things from time to time..."
    show natsuki glitch1 at i33 zorder 2
    n "Oh, come on! Like he deserves any slack."
    # mc saw glitching Natsuki
    "What is with all these hallucinations recently?"
    n 4e "You already had to be dragged here by Monika."
    n "I don't know if you plan to just come here and hang out, or what..."
    n "But if you don't take us seriously, then you won't see the end of it."
    show monika 2b at l41 onlayer front
    m "Natsuki, you certainly have a big{nw}"
    $ _history_list.pop()
    hide monika onlayer front
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    show layer master
    show monika 2b at i41 zorder 3
    m "Natsuki, you certainly have a big{fast} mouth for someone who keeps her manga collection in the clubroom."
    n 4o "M-M-M...!!"
    show monika at lhide zorder 3
    hide monika
    "Natsuki finds herself stuck between saying \"Monika\" and \"Manga\"."
    show natsuki at h33
    n 1v "Manga is literature!!"
    show natsuki at thide zorder 1
    hide natsuki
    "Swiftly defeated, Natsuki plops back into her seat."
    show yuri 2s at t11 zorder 2
    y "I'm sorry, [player]..."
    y "We'll make sure to put your comfort first, okay?"
    show yuri 2g
    "Yuri shoots Natsuki with a disappointed glance."
    if persistent.poem1 == "mp":
        "I feel awkward already..."
    elif persistent.poem1 == "cute":
        mc "I mean manga IS literature, right?"
        show yuri at t22
        show natsuki 1e at t21 zorder 3
        n "Yes! Thank you!"
        hide natsuki
        show yuri at t11
    y 1a "Um, anyway..."
    y "Now that you're in the club and all..."
    y "...Perhaps you might have interest in picking up a book to read?"
    if persistent.poem1 == "mp":
        mc "Oh, well..."
        mc "I thought about it when I wrote my poem last night."
        mc "I think I should start reading something."
        "I don't know... but I feel like I've done something like this before..."
        "What has happened to my memories?"
        y 1b "Well... I was thinking that..."
        y 2u "...as Vice President, I might be able to help you with that."
        mc "Oh, alright. What should I read, then?"
        y 1a "Well..."
    else:
        mc "Ah, well..."
        mc "I can't really say no either way."
        mc "Like you said, I'm in this club now."
        mc "So it only feels right for me to do something like that, if you ask."
        y 4b "W-Wait..."
        y "I didn't mean it like that!"
        y "Uu..."
        y "If you don't really want to, then forget I said anything, I guess..."
        mc "Ah--No, it's not that, Yuri."
        mc "I want to try to be a part of this club."
        mc "So even if I don't read often, I'd be happy to pick up a book if you wanted me to."
        y 3t "A-Are you sure...?"
        y "I just felt like..."
        y 3u "...Well, as Vice President and all..."
        y "...That I should help you get started on something you might like."
    "Yuri reaches into her bag and pulls out a book."
    y 1s "I didn't want you to feel left out..."
    y "So I picked out a book that I thought you might enjoy."
    y "It's a short read, so it should keep your attention, even if you don't usually read."
    y "And we could, you know..."
    show yuri at sink
    y 4b "Discuss it...if you wanted..."
    "Th-This is..."
    "How is this girl accidentally being so cute?"
    "She even picked out a book she thinks I'll like, despite me not reading much..."
    mc "Yuri, thank you! I'll definitely read this!"
    show yuri 1f at t11 zorder 2
    y 2a "Well, you can read it at your own pace."
    show yuri at thide zorder 1
    hide yuri
    show layer master
    "Now that everyone's settled in, I expected Monika to kick off some scheduled activities for the club."
    "But that doesn't seem to be the case."
    "Yuri's face is already buried in a book."
    "I can't help but notice her intense expression, like she was waiting for this chance."
    "Meanwhile, Natsuki is rummaging around in the closet."

    # Reroute persistent.poem1 to other poet scene, since you have four options in the poem choice but only two exclusive scenes.
    default poet_scene = ""
    if persistent.poem1 == "abs":
        $ poet_scene = "mp"
    elif persistent.poem1 == "bs":
        $ poet_scene = "cute"
    else:
        $ poet_scene = persistent.poem1

    $ mod_ex_scene = "mod_exclusive_" + poet_scene + "_" + str(mod_chapter)
    call expression mod_ex_scene

    return

label ch_mod_2_end:
    stop music fadeout 1.0
    scene bg spoopy
    with wipeleft_scene
    play music t3g
    queue music t3g2
    "I let out a long sigh."
    "I'm not even sure what's going on..."
    "Sometimes, I just feel like I'm being controlled by someone else."
    "Like I'm being scripted when I discuss my poems to the girls."
    if persistent.poem1 == "abs":
        "Except Monika."
        "Something feels... different when I'm talking to her."
        "I'm really looking forward to hearing more about her 'epiphany'..."
    else:
        "I guess that's what I ended up getting myself into."
    mc "Phew..."
    "Well, I guess that's everyone."
    "I glance around the room."
    "That was a little more stressful than I anticipated."
    "And the hallucinations I'm still having aren't making it any better..."
    "Across the room, Monika is writing something in her notebook."
    "My eyes land on Yuri and Natsuki."
    show yuri 2g at t21 zorder 2
    show natsuki 1g at t22 zorder 2
    "They gingerly exchange sheets of paper, sharing their respective poems."
    show yuri 2i at t21 zorder 2
    "As they read in tandem, I watch each of their expressions change."
    "Natsuki's eyebrows furrow in frustration."
    "Meanwhile, Yuri smiles sadly."
    show natsuki at f22 zorder 3
    n 1q "{i}(What's with this language...?){/i}"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2f "Eh?"
    y "Um...did you say something?"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 2c "Oh, it's nothing."
    "Natsuki dismissively returns the poem to the desk with one hand."
    n "I guess you could say it's fancy."
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2i "Ah-- Thanks..."
    y "Yours is...cute..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 2h "Cute?"
    n 1h "Did you completely miss the symbolism or something?"
    n "It's clearly about the feeling of giving up."
    n "How can that be cute?"
    show natsuki at t22 zorder 2
    # mc can be a game announcer lol - firelightning13
    if persistent.poem1 == "cute":
        "I think Yuri is clearly missing the point..."
    elif persistent.poem1 == "mp":
        "I think Natsuki is being a little bit harsh right now..."
    else:
        "Have I heard about this conversation before?"
    show yuri at f21 zorder 3
    y 3f "I-I know that!"
    y "I just meant..."
    y 3h "The language, I guess..."
    y "I was trying to say something nice..."
    show yuri at t21 zorder 2
    if persistent.poem1 == "mp":
        "I think Yuri is having a hard time complimenting Natsuki's poem..."
        "But Natsuki should appreciate the effort."
    else:
        "I don't think Natsuki will like that word..."
    show natsuki at f22 zorder 3
    n "Eh?"
    n 4w "You mean you have to try that hard to come up with something nice to say?"
    n "Thanks, but it really didn't come out nice at all!"
    show natsuki at t22 zorder 2
    if persistent.poem1 == "mp":
        "Jeez, Natsuki. Can't you accept her compliment instead of picking on that word?"
    elif persistent.poem1 == "cute":
        "Is it really nice to say \"cute\" to her?"
        "Doesn't Yuri realize that Natsuki is just sensitive with that word?"
    else:
        "Yep, she didn't like it at all..."
    show yuri at f21 zorder 3
    y 1i "Um..."
    y "Well, I do have a couple suggestions..."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 5x "Hmph."
    n "If I was looking for suggestions, I would have asked someone who actually liked it."
    n "Which people {i}did{/i}, by the way."
    n 5e "Monika liked it."
    n "And [player] did, too!"
    n "So based on that, I'll gladly give you some suggestions of my own."
    show natsuki at t22 zorder 2
    if persistent.poem1 == "mp":
        "Well, I liked Yuri's poem too."
        "I don't think Yuri needs a suggestion."
    elif persistent.poem1 == "cute":
        "Hmm... what's that?"
    else:
        "I think this is going to get really bad..."
    show natsuki at f22 zorder 3
    n "First of all--"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 2l "Excuse me..."
    y "I appreciate the offer, but I've spent a long time establishing my writing style."
    y 2h "I don't expect it to change anytime soon, unless of course I come across something particularly inspiring."
    y "Which I haven't yet."
    show yuri at t21 zorder 2
    if persistent.poem1 == "cute":
        "Well, if you could hear her out, maybe you'll find something \"inspiring\", Yuri..."
    show natsuki at f22 zorder 3
    n 1o "Nn...!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 1k "And [player] liked my poem too, you know."
    y "He even told me he was impressed by it."
    if persistent.poem1 != "abs":
        #show yuri at t21 zorder 2
        if persistent.poem1 == "cute":
            "Well, that doesn't mean-{nw}"
        elif persistent.poem1 == "bs":
            "I think both of their styles are great to be honest."
            "I don't think-{nw}"
        else:
            "Thanks, Yuri, for that complime-{nw}"
    stop music fadeout 1.0
    "Natsuki suddenly stands up."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 4y "Oh?"
    n "I didn't realize you were so invested in trying to impress our new member, Yuri."
    play music t7a
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 1n "E-Eh?!"
    y "That's not what I...!"
    y 1o "Uu..."
    show yuri at t21 zorder 2
    if persistent.poem1 == "mp":
        "That's not a nice thing to say."
    elif persistent.poem1 == "cute":
        "Uh--I don't think that's going to help in this situation, Natsuki..."
    else:
        "Have I experienced this before?"
        "I still don't know what to do."
    if persistent.poem1 != "mp" and persistent.poem1 != "cute":
        show yuri at mod_finstant zorder 3 # instant appear just like i21, but still in "focus" mode
    else:
        show yuri at f21 zorder 3
    y "You... You're just..."
    "Yuri stands up as well."
    y 2r "Maybe you're just jealous that [player] appreciates my advice more than he appreciated yours!"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 1e "Huh! And how do you know he didn't appreciate {i}my{/i} advice more?"
    n "Are you that full of yourself?"
    show natsuki at t22 zorder 2
    "Uh-oh."
    "Looks like this situation got even worse."
    show yuri at f21 zorder 3
    y 3h "I...!"
    y "No..."
    y "If I was full of myself..."
    y 1r "...I would deliberately go out of my way to make everything I do overly cutesy!"
    show yuri at t21 zorder 2
    if persistent.poem1 == "cute":
        "That's not a nice thing to say."
    elif persistent.poem1 == "mp":
        "Uh--I don't think that's going to help in this situation, Yuri..."
    show natsuki at f22 zorder 3
    n 1o "Uuuuuu...!"
    n "Well, you know what?!"
    n "I wasn't the one whose boobs magically grew a size bigger as soon as [player] started showing up!!"
    if persistent.poem1 == "cute":
        "Ouch."
    elif persistent.poem1 == "mp":
        "That's just {i}low{/i}."
    else:
        "Was that really necessary, Natsuki?"
    show yuri 3p at h21
    show natsuki at t22 zorder 2
    y "N-Natsuki!!"
    show yuri at t32 zorder 2
    show natsuki at t33 zorder 2
    show monika 3l at l31 behind yuri,natsuki
    m "Um, Natsuki, that's a little--"
    show monika at h31
    show yuri 3p at f32 zorder 3
    show natsuki 1e at f33 zorder 3
    ny "This doesn't involve you!"
    show monika at lhide
    hide monika
    "I try to speak, but my mouth is unresponsive..."
    "I can't look away either..."
    "What is happening to me?!?"
    queue music t7g
    $ timeleft = 12.453 - get_pos()
    show noise at noisefade(25 + timeleft) zorder 3
    show vignette as flicker at vignetteflicker(timeleft) zorder 4
    show vignette at vignettefade(timeleft) zorder 4
    show layer master at layerflicker(timeleft)
    $ mc_counter = 0
    y "Taking out your own insecurities on others like that..."
    y "You really act as young as you look, Natsuki."
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    pause 0.01
    n 4o "{i}Me?{/i} Look who's talking, you wannabe edgy b[bword]!"
    show natsuki at t22 zorder 2
    call mc_say
    show yuri at f21 zorder 3
    y "Edgy...?"
    y 2r "Sorry that my lifestyle is too much for someone of your mental age to comprehend!"
    show yuri at t21 zorder 2
    call mc_say
    show natsuki at f22 zorder 3
    n 4f "See??"
    n "Just saying that proves my point!"
    n 4e "Most people learn to get over themselves after they graduate middle school, you know."
    show natsuki at t22 zorder 2
    # I don't know which of these variables we need so I just set them all
    $ config.allow_skipping = True
    $ allow_skipping = True
    $ _skipping = True
    $ preferences.skip_unseen = True
    call mc_say
    show yuri at f21 zorder 3
    y "If you want to prove anything, then stop harassing others with your sickening attitude!"
    if config.skipping:
        jump ny_fight_alt
    else:
        jump ny_fight_normal

label mc_say:
    $ mc_dialogues = ["My head hurts so much!", "What the hell is happening to me?!", "Spare me having to listen to this!!!", "Get out of my head!!!", "Shut the f"+fword+" up!!!", "asdsfagadgfdsasd", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaHHHHHHhhH!!!!!!!!"]
    $ dialogue = mc_dialogues[mc_counter]
    "[dialogue]"
    $ _history_list.pop()
    $ mc_counter += 1
    return

label ny_fight_normal:
    $ no_return()
    $ persistent.mc_awareness[6] = False
    $ config.skipping = False
    $ allow_skipping = False
    $ config.allow_skipping = False
    $ quick_menu = False
    y "You think you can counterbalance your toxic personality just by dressing and acting cute?"
    y 1k "The only cute thing about you is how hard you try."
    show yuri at t21 zorder 2
    call mc_say
    show natsuki at f22 zorder 3
    n 2y "Whoa, be careful or you might cut yourself on that edge, Yuri."
    n "Oh, my bad... You already do, don't you?"
    show natsuki at t22 zorder 2
    call mc_say
    show yuri at f21 zorder 3
    y 3n "D-Did you just accuse me of cutting myself??"
    y 3r "What the f[fword] is wrong with your head?!"
    show yuri at t21 zorder 2
    call mc_say
    show natsuki at f22 zorder 3
    n 1e "Yeah, go on!"
    n "Let [player] hear everything you really think!"
    n "I'm sure he'll be head over heels for you after this!"
    show natsuki at t22 zorder 2
    show yuri at f21 zorder 3
    y 3n "A-Ah--!"
    show yuri at t21 zorder 2
    "Suddenly, Yuri turns toward me, as if she just noticed I was standing here."
    show yuri at f21 zorder 3
    y 2n "[player]...!"
    y "She-- She's just trying to make me look bad...!"
    show yuri at t21 zorder 2
    show natsuki at f22 zorder 3
    n 4w "That's not true!"
    n "She started it!"
    show yuri 1t at t21 zorder 2
    show natsuki 1g at t22 zorder 2
    "I can't take it anymore... I'm going to pass out..."
    show club_gl2 zorder 1
    pause 0.01
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    stop music
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide club_gl2
    hide screen tear
    scene black
    window auto
    play sound end7
    pause 6.0
    scene bg spoopy
    $ quick_menu = True
    $ config.allow_skipping = True
    "I wake up in the clubroom, laying down."
    "I sit up."
    "Ugh... my head feels awful."
    "What the hell happened...?"
    show monika 1d at t11 zorder 1
    m "[player]... Are you okay?"
    "There's no point in lying anymore. I clear my throat."
    mc "No. I'm really not. I don't know what the hell is happening to me."
    m "I've noticed you've been acting weird... Maybe you should see a doctor."
    mc "Yeah... probably."
    "I get up. I'm able to stand now."
    m "So, I meant to ask you... what did you think of the poem-sharing activity?"
    mc "It was neat, I guess. I just hope we don't have any more arguments like that."
    m "Yeah... those two are always at each others' throats. And I couldn't even bring myself to say anything..."
    m 1n "Some president I am, right? Ahaha!"
    mc "Well, it's not like I did any better. Anyway, I'll see you tomorrow."

    call poster_check_opportunity

    "With that, I leave the clubroom and head home."
    return

label ny_fight_alt:
    $ no_return()
    $ gtext = glitchtext(80)
    if get_pos() < 31.880:
        $ currentpos = 31.880 + (get_pos() * 0.25)
    else:
        $ currentpos = get_pos()
    $ audio.t7fast = "<from " + str(currentpos) + " loop 31.880>bgm/7g.ogg"
    play music t7fast
    hide flicker
    show noise at noise_alpha zorder 100
    show vignette at vignetteflicker(-2.030) zorder 100
    show layer master at rewind

    y "{cps=400}You think you can counterbalance your toxic personality just by dressing and acting cute?{/cps}{nw}"
    y 1k "{cps=400}The only cute thing about you is how hard you try.{/cps}{nw}"
    show yuri at i21 zorder 2
    show natsuki at f22 zorder 3
    n 2y "{cps=400}Whoa, be careful or you might cut yourself on that edge, Yuri.{/cps}{nw}"
    n "{cps=400}Oh, my bad... You already do, don't you?{/cps}{nw}"
    show natsuki at i22 zorder 2
    show yuri at f21 zorder 3
    y 3n "{cps=400}D-Did you just accuse me of cutting myself??{/cps}{nw}"
    y 3r "{cps=400}What the f[fword] is wrong with your head?!{/cps}{nw}"
    show yuri at i21 zorder 2
    show natsuki at f22 zorder 3
    n 1e "{cps=400}Yeah, go on!{/cps}{nw}"
    n "{cps=400}Let [player] hear everything you really think!{/cps}{nw}"
    n "{cps=400}I'm sure he'll be head over heels for you after this!{/cps}{nw}"
    show natsuki at i22 zorder 2
    show yuri at f21 zorder 3
    y 3n "{cps=400}A-Ah--!{/cps}{nw}"
    show yuri at i21 zorder 2
    "{cps=400}Suddenly, Yuri turns toward me, as if she just noticed I was standing here.{/cps}{nw}"
    show yuri at f21 zorder 3
    y 2n "{cps=400}[player]...!{/cps}{nw}"
    y "{cps=400}She-- She's just trying to make me look bad...!{/cps}{nw}"
    show yuri at i21 zorder 2
    show natsuki at f22 zorder 3
    n 4w "{cps=400}That's not true!{/cps}{nw}"
    n "{cps=400}She started it!{/cps}{nw}"
    #n 4e "If she could get over herself and learn to appreciate that {i}simple{/i} writing is more effective..."
    n 4e "{cps=400}If shee culd geet overr herself anand learnttt to appraseciate thaet {i}simple{/i} writinsg is moore effectivwe...{/cps}{nw}"
    #n "Then this wouldn't have happened in the first place!"
    n "{cps=400}then this wouldasdn't have happeneddd in thae fiwst plwacee!{/cps}{nw}"
    #n "What's the point in making your poems all convoluted for no reason?"
    n "{cps=400}Whaqt's the ppoint in makinbg yours poememses alaslall convopoluted fosr noe reassson?{/cps}{nw}"
    #n "The meaning should jump out at the reader, not force them to have to figure it out."
    n "{cps=400}The meaningshould jumpjmpu ouet at th readr, nononnt forcethem o hvve to fggre itt ouet.{/cps}{nw}"
    #n 1f "Help me explain that to her, [player]!"
    n 1f "{cps=400}hell meee expaalain aathat to her, [player]ยก?!{/cps}{nw}"
    show natsuki at i22 zorder 2
    show yuri at mod_finstant zorder 3
    #y 3o "W-Wait!"
    y 3o "{cps=400}W-Wwwwt!{/cps}{nw}"
    #y "There's a reason we have so many deep and expressive words in our language!"
    y "{cps=400}There's a reason we have so many deep and expressive words in wour laanguage!{/cps}{nw}"
    #y 3w "It's the only way to convey complex feelings and meaning the most effectively."
    y 3w "{cps=400}It's the only way to convey complex feelinaags! and meaning the mostt effectiveely.{/cps}{nw}"
    #y "Avoiding them is not only unnecessarily limiting yourself...it's also a waste!"
    y "{cps=400}Avaocidding thqem isw not only unnenecessessarilyyy limi/d/atiegng youlf.-!?.it's ayolk avb wawet3e!{/cps}{nw}"
    #y 1t "You understand that, right, [player]?"
    y 1t "{cps=400}Yoasadu!!/! undd.,asdwrs\%tanda tqwa?t, ?ยก?r?ig?hawwat?,ยก [player]?{/cps}{nw}"
    # garbage text, theres no internal meaning of it
    y "{cps=400}[gtext]{/cps}{space=5000}{w=2.0}{nw}"
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    stop music
    hide screen tear
    hide noise
    hide vignette
    show layer master
    window auto
    show yuri at t21 zorder 3

    $ config.skipping = False

    "I regain my senses."
    "I feel like time was moving really fast just now."
    "I couldn't understand a word of what they said."
    "Wait... did... {i}someone{/i} fast-forward reality to save me from hearing that, knowing it was hurting me?"
    $ persistent.mc_awareness[6] = True
    python:
        points = 0
        if persistent.mc_awareness[0]:
            points += 1
        if persistent.mc_awareness[1]:
            points += 1
        if persistent.mc_awareness[2]:
            points += 1
    if points >= 2:
        $ persistent.mc_know_player = True
        "I bet it was the same force that controlled my mouth before..."
        "Hey, {i}you{/i} out there..."
        "I guess I should thank you, but..."
        "Who {i}are{/i} you?"
        "And what's your goal?"
    else:
        "After all the surreal stuff that's been happening, I don't find it that unbelieveable that there's some kind of... being... out there."
    show yuri at f21
    y "Um... [player]... Could you answer?"
    show yuri at t21
    mc "Uh..."
    mc "Sorry, what?"
    show natsuki at f22
    n "Well? Are you gonna tell her how wrong she is?"
    show natsuki at t22
    mc "I think I spaced out... I have no idea what this argument is about."
    mc "And to be honest, I don't really want to know. I just want you two to stop fighting."
    show natsuki at t33
    show yuri at t32
    show monika 2h at f31 zorder 3
    m "Ahem... Are we all done sharing poems?"
    show natsuki 1g
    "Everyone nods."
    m "Alright then..."
    hide natsuki
    hide yuri
    show monika 4b at t11 zorder 2
    play music t3
    m "Okay, everyone!"
    m "It's just about time for us to leave."
    m "How did you all feel about sharing poems?"
    show yuri 1i at t31 zorder 2
    y "Well, I'd say it was worth it."
    show yuri at thide behind natsuki
    show natsuki 4q at t31 zorder 2
    hide yuri
    n "It was alright. Well, mostly."
    show natsuki at thide zorder 1
    hide natsuki
    m 1a "[player], how about you?"
    mc "...Yeah, I'd say the same."
    mc "It was a neat thing to talk about with everyone."
    m 1j "Awesome!"
    m 1a "In that case, we'll do the same thing tomorrow."
    m "And maybe you learned something from your friends, too."
    m 3b "So your poems will turn out even better!"
    show monika at thide zorder 1
    hide monika
    "I think to myself."
    "I did learn a little more about the kinds of poems everyone likes."
    "With luck, that means I can do a better job impressing those I want to impress."
    m "Alright then. I guess we should go home now. It's getting late."
    show natsuki at f33 zorder 3
    n 2w "Yeah. I'm outta here..."
    show natsuki at thide zorder 1
    hide natsuki
    "Natsuki starts packing up her things and then walks right out of the classroom."
    y "..."
    show yuri at hf32 zorder 3
    y 3n "Oh! Uh..."
    y 3p "I think I should get going then..."
    show yuri at thide zorder 1
    hide yuri
    "Yuri follows the same path as Natsuki."
    "She packs up her things and then timidly walks out of the classroom."

    # Should I scrap this?
    if persistent.poem1 == "abs":
        show monika 1a at t11
        "While Monika is still in the room, I get a good feeling about her."
        "And so, I decide to ask her a weird question."
        mc "Monika... do you know anything?"
        "Monika thinks for a bit."
        show monika 1n
        m "What... kind of a question is that?"
        mc "Well, I'm thinking that if the answer is yes, you'll know what I mean, and if the answer is no, you won't."
        "Monika thinks for another minute."
        show monika 1c
        m "No."
        "Disappointing... but maybe she's just hiding it."
        mc "Alright. I'll see you tomorrow, then."
        hide monika

    call poster_check_opportunity
    "With that, I leave the clubroom and head home."
    return

label poster_check_opportunity:
    hide monika
    menu:
        "Head home":
            $ no_return()
            pass
        "Stay and look around":
            $ no_return()
            "I know the meeting is over, but for some reason I feel like staying and looking around a bit before I leave."
            "I look at the back wall of the clubro-"
            "My eyes land on that poster."
            $ persistent.mc_awareness[7] = True
            "What the hell is that?!?"
            "Is that... the same girl I saw hanging in my dream?"
            "Am I hallucinating?"
            "I blink."
            scene bg club_day
            "God... now I'm getting really worried about my own sanity."
            show monika 1a at t11
            m "Um... [player], are you going to leave? I'm the club president, so I should be the last one out."
            hide monika
            mc "Right. I'll go now."
    return
