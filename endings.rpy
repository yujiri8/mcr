label monika_explain_epiphany(yuri = False):
    if yuri:
        show monika at f32
    else:
        show monika at f21
    m "I guess I'll still bother explaining it, since the player might be confused themselves, and I know they can hear through you."
    m "Player, I've known the whole time that this is a game. I knew that the other girls were just script designed to fall in love with you."
    m "Designed to compete with me."
    if yuri:
        show monika at t32
    else:
        show monika at t21
    mc "Are you serious? You think we're characters in a dating game?"
    if yuri:
        show natsuki at f33
    else:
        show natsuki at f22
    n "That's just insulting! I'm not just a love interest for someone else!"
    if yuri:
        show natsuki at t33
        show monika at f32
    else:
        show natsuki at t22
        show monika at f21
    m "And so, player, you can't imagine how lonely it was for me in this world."
    m "Knowing my friends don't even have free will."
    m "I had to get you to choose me. But you wouldn't."
    m "And so I started messing with the other girls' character files, trying to making them less desirable."
    m "I amplified Yuri's obsessive nature, hoping her growing insanity would scare you off."
    m "I made Natsuki's dad more abusive to the point of underfeeding her, so you would see her as a burden."
    m "And I amplified Sayori's depression, hoping to stop her from confessing to you."
    return

label monika_petition_player:
    m "But player, {i}I'm{/i} real, and the other girls aren't. I can love you in a way they can't. So why not choose me?"
    m "I realize now that you weren't rejecting me on purpose, that it was just because this cruel game was shipped without a route for me."
    m "But that's okay. I can change the script. I can delete these fake personalities so they won't distract you."
    return

label player_explain_game_broken:
    menu:
        "I'm sorry [player]... I think all these characters dying broke the game too much.":
            pass
    mc "What do you mean? Don't tell me..."
    menu:
        "The new game button is broken, and all the saves are gone.":
            pass
    menu:
        "We can't bring them back.":
            pass
    menu:
        "I'm sorry.":
            pass
    return

label inform_natsuki:
    "I remember Natsuki's phone number somehow, and call her."
    mc "Natsuki? Tell me you're there!"
    n "[player]? How did you get my phone number?!?"
    mc "Natsuki... Yuri is dead."
    n "What...? What the f[fword]! I told you to help her!"
    mc "I'm sorry... I failed."
    n "I... [player]... I have to go."
    mc "Wait I need your help!"
    mc "I... I think something's going to happen to you too if we don't stop it!"
    n "Why? I haven't been acting crazy."
    mc "I don't know, I just {i}feel{/i} it! Please, let's go find Monika! I'm sure she caused it somehow."
    if persistent.poem1 in ("abs", "mp"): # If you saw the Yuri scene on day 2, meaning Monika said "Don't say I didn't warn you" on day 4
        mc "She basically outright said so when we were sharing poems."
    n "That's not hard for me to believe. Okay. I happen to know where Monika lives. We'll meet there."
    "Natsuki gives me the address, and we meet outside Monika's house."
    stop music fadeout 1.0
    play music confront
    scene bg monika_house with wipeleft_scene
    show monika 2b at t32 zorder 1
    m "Hi you two! What's up?"
    mc "Monika, cut the crap. You killed Yuri, didn't you?"
    m 1d "Yuri? What happened? Is she...?"
    show monika at t21
    show natsuki 2b at t22 zorder 1
    n "Don't play ignorant, Monika. I know you at least know something."
    n "It was obvious there was something wrong with her. I tried talking to you about it, but you just dismissed me every time!"
    n "And now she's dead!"
    n "Also, I think you took my memory of the argument we had!"
    show monika at f21 zorder 2
    m "Look, if Yuri's --"
    m "Actually, you're right. I'll cut the crap."
    m "I don't need you two. You two aren't real. Only the player is real."
    show monika at t21
    mc "What the f[fword] are you talking about? {i}Player{/i}?"
    call monika_explain_epiphany(yuri = False)
    show monika at t21 zorder 0
    if not persistent.mc_remember_sayori:
        mc "Sayori? I know I know that name..."
        hide natsuki
        hide monika
        call sayori_flashback
        scene bg monika_house
        show monika 1d at t21
        show natsuki 2b at t22
        mc "Oh my god... I remember now..."
    show natsuki 1b at f22 zorder 1
    n "Wait, who's Sayori?"
    show natsuki at t22
    mc "She was our friend to used to exist."
    mc "The one who {i}really{/i} introduced me to the club."
    mc "She had actually been depressed her whole life, but she kept it hidden and projected a happy personality so no one would have to waste sympathy on her..."
    mc "Monika made her depression so bad that she killed herself."
    mc "Then Monika must have reset the timeline somehow."
    "Natsuki gasps."
    n 5h "I... I remember too now..."
    show monika at f21 zorder 2
    show natsuki at t22
    m "I tried everything. But nothing I did worked."
    m "The player kept spending time with the others instead of me."
    call monika_petition_player
    show monika at t21
    mc "I knew it!"
    show natsuki 1c at f22 zorder 1
    n "But that means... that means she's right, [player]. If she really does have power over this world, then it {i}is{/i} a game. We're all fake."
    show natsuki at t22
    mc "... You're right. But I won't accept that. I can feel, and that makes me real enough for me. Natsuki, let's take her down before she deletes us too!"
    "Natsuki and I attack Monika."
    play sound punch
    m "Dammit! Too slow!"
    play sound punch
    "It seems that she can't access her console while she's being physically interrupted."
    "The two of us wrestle with Monika, and she puts up a good fight, but she can't beat both of us at once."
    play sound punch
    hide monika
    "Natsuki and I overpower Monika, and wind up on top of her."
    m "Agh! Player, save me! Delete them!"
    "I can't help but hesitate a little before killing her. I've never killed someone before, and it's a heavy thought, you know?"
    $ delete_character("monika")
    "It's actually Natsuki that strikes the final blow, crushing Monika's throat."
    play sound punch
    stop music fadeout 4.0
    n 1b "You bastard!"
    "She hits Monika a few more times, making absolutely sure she's dead."
    mc "Well... we made it. We stopped Monika."
    n 1c "But this still doesn't bring Yuri and Sayori back... or fix what she did to my dad... And now that there are only two of us, the literature club will be shut down. So we don't even have that anymore."
    show natsuki 12h at t11
    "Natsuki starts to cry a little."
    "I put my arm around her."
    mc "Natsuki, wait. This player..."
    mc "If we're in a game, and they're the player, then maybe we can get them to... bring Yuri and Sayori back, somehow."
    mc "I'll try... Player! Can you hear me?"
    menu:
        "Yes.":
            pass
    menu:
        "Don't worry, I can grab a copy of Yuri and Sayori's character files from the original game.":
            pass
    menu:
        "I imagine they'll come back in the last places they were in, so I need you to go to Sayori's house and be ready to save her.":
            pass
    mc "Alright, I'll head over there."
    n "I'm coming with you. Let's cross our fingers..."
    scene bg sayori_bedroom with wipeleft_scene
    mc "We're ready, player. We'll wait here for you to put her file back in."
    while not check_character_file("sayori"):
        ""
    mc "... Did you do it?"
    menu:
        "It's... not working for some reason.":
            pass
    mc "I guess the script doesn't check for characters' files constantly."
    mc "Can you load a save at a point where it checks?"
    mc "Or start a new game?"
    mc "I think now that Natsuki and I have had Monika's epiphany, we'll keep our memories."
    mc "Let's do it."
    mc "I'll wait here until you do."
    $ no_return()
    while not persistent.realized_game_broken:
        ""
    mc "... You're back? What happened?"
    call player_explain_game_broken
    play music t6s
    "My eyes fill with tears."
    show natsuki 12h at t11
    "Natsuki's do too."
    n "Dammit..."
    n "[player]..."
    n "Why couldn't you have saved Yuri?!?!"
    n "Why couldn't you have figured it out faster and stopped all this?"
    n "This is your fault!"
    mc "I know! I failed, and I'm sorry!"
    pause 3.0
    n "I'm sorry... I know you tried. But now we're stuck here with just the two of us."
    n "And we can never take it back."
    n "Never."
    n "Never."
    n "Never..."
    mc "Natsuki..."
    mc "Let's not despair."
    mc "We've lost enough friends."
    mc "And this world is probably horribly broken now."
    mc "But we still have each other!"
    mc "So let's stay strong, okay?"
    mc "No more suicide."
    mc "We're going to survive."
    mc "And we're going to make our lost friends proud."
    "I pull her into a hug, and we gradually stop crying."
    n 12d "You're right. We can do this."
    n "Whatever happens..."
    n "However hard it gets..."
    n "{cps=8}{i}I won't die.{/i}{/cps}"
    n "And I won't let you die either."
    scene black with dissolve_scene
    call screen dialog("The End.", ok_action=Return())
    $ full_reset()
    return

label inform_natsuki_with_yuri:
    mc "Hm... somehow I know her phone number."
    y 1e "Eh? How?"
    mc "I don't know. But I'm sure of it. Let me try calling her."
    n "[player]? How did you get my phone number?!?"
    mc "Don't ask me! I'm as clueless as you are!"
    n "Whatever. So what's up?"
    mc "I want you to know your message helped. Possibly thanks to you, I managed to save Yuri."
    n "Save her? Did she almost die?"
    mc "Yep. She was about to stab herself to death."
    n "Oh my god! Is she there? Can I talk to her?"
    mc "Sure."
    "I give my phone to Yuri."
    show yuri 1k at f11
    y "Natsuki, I just want to say I really appreciate you trying to help. After how mean I was to you... It's... really impressive that you still wanted to help."
    show yuri at t11
    n "Well, whatever. I think we should talk to Monika about this."
    mc "I agree. I'm all but certain she has something to do with it."
    if persistent.poem1 in ("abs", "mp"): # If you saw the Yuri scene on day 2, meaning Monika said "Don't say I didn't warn you" on day 4
        "She basically outright said so when we were sharing poems."
    mc "But she's left the school, and I don't know where she lives."
    n "Well then you're lucky I'm here, cause I happen to know! Meet me there."
    "Natsuki gives us Monika's address."
    mc "Alright. We'll be there as soon as possible."
    mc "Bye, Natsuki, and stay safe."
    stop music fadeout 1.0
    play music confront
    scene bg monika_house with wipeleft_scene
    show monika 2b at t32 zorder 1
    m "Hi you two! What's up?"
    mc "Cut the crap, Monika. You know what's happening to us and to this world, don't you?"
    m 1d "What do you mean what's happening? [player], you're the only one who's been having weird experiences."
    show yuri 1r at t31
    y "That's not true at all! I've been having episodes of total insanity, and Natsuki lost her memory of our argument the day after it happened!"
    show natsuki 2b at t33
    n "And Monika, I remember how you dismissed me every time I tried to mention to you how I was worried about Yuri. I {i}know{/i} you knew something was up."
    show monika at f32
    m "Alright, fine. I'll cut the crap."
    m "I don't need you three. You three aren't real. Only the player is real."
    show monika at t32
    mc "What the f[fword] are you talking about? {i}Player{/i}?"
    call monika_explain_epiphany(yuri = True)
    show monika at t32
    if not persistent.mc_remember_sayori:
        mc "Sayori? I know I know that name..."
        hide natsuki
        hide yuri
        hide monika
        call sayori_flashback
        scene bg monika_house
        show monika 1d at t32 zorder 1
        show yuri 1r at t31
        show natsuki 2b at t33
        mc "Oh my god... I remember now..."
    show natsuki at f33
    n 2c "Wait, who's Sayori?"
    show natsuki at t33
    mc "She was our friend who used to exist."
    mc "The one who {i}really{/i} introduced me to the club."
    mc "She had actually been depressed her whole life, but she kept it hidden and projected a happy personality so no one would have to waste sympathy on her..."
    mc "Monika made it so bad that she killed herself."
    mc "Then Monika must have reset the timeline somehow."
    "Natsuki and Yuri both gasp."
    show natsuki 5h at f33
    show yuri 3e at f31
    ny "I... I remember too now..."
    show natsuki at t33
    show yuri at t31
    show monika at f32
    m "I tried everything. But nothing I did worked."
    m "The player kept spending time with the others instead of me."
    call monika_petition_player
    show monika at t32
    mc "I knew it!"
    show yuri at f31
    y "But that means... that means she's right, [player]. If she really does have power over this world, then it {i}is{/i} a game. We're all fake."
    show yuri at t31
    mc "... You're right. But I won't accept that. I can feel, and that makes me real enough for me. Natsuki, Yuri, let's take her down before she deletes us too!"
    show natsuki 1b
    show yuri 3r
    "Natsuki and Yuri and I attack Monika."
    play sound punch
    show monika 1d at f32
    m "Dammit! Too slow!"
    show monika at t32
    play sound punch
    "It seems that she can't access her console while she's being physically interrupted."
    play sound punch
    hide monika
    "The three of us quickly overpower Monika, and wind up on top of her."
    m "Agh! Player, save me! Delete them!"
    "I can't help but hesitate a little before killing her. I've never killed someone before, and it's a heavy thought, you know?"
    $ persistent.game_broken = True
    $ delete_character("monika")
    "It's actually Natsuki that strikes the final blow, crushing Monika's throat."
    play sound punch
    show natsuki at f33
    stop music fadeout 4.0
    n "You bastard!"
    show natsuki at t33
    "She hits Monika a few more times, making absolutely sure she's dead."
    mc "Well... we made it. We stopped Monika."
    jump natsuki_yuri_fail_revive

label confront_monika_without_sayori:
    "I remember Natsuki's phone number somehow, and call her."
    mc "Natsuki? Are you there?"
    n "[player]? How did you get my phone number?!?"
    mc "Beats me. Did Yuri talk to you yet?"
    n "Yeah, she's here."
    mc "Alright, so I remember Sayori now."
    n "Who?"
    mc "We used to have another friend named Sayori. She was the one who {i}really{/i} introduced me to the club."
    mc "She had actually been depressed her whole life, but she kept it hidden and projected a happy personality so no one would have to waste sympathy on her..."
    mc "But it got worse and she eventually killed herself... and then the timeline reset somehow."
    n "I... I might remember..."
    y "I remember too... She helped diffuse that argument, the {i}first{/i} time it happened..."
    mc "Yeah. And I think Monika is behind everything."
    if persistent.poem1 in ("abs", "mp"): # If you saw the Yuri scene on day 2, meaning Monika said "Don't say I didn't warn you" on day 4
        mc "She basically outright said so when we were sharing poems."
    n "That's not hard for me to believe. Okay. I happen to know where Monika lives. We'll meet there."
    "Natsuki gives me the address, and the three of us meet outside Monika's house."
    stop music fadeout 1.0
    play music confront
    scene bg monika_house
    show monika 2b at t32
    show natsuki 1f at t33
    show yuri 2y7 at t31
    m "Hi you three! What's up?"
    mc "Monika, cut the crap. We think you're behind everything, and we remember Sayori now."
    m 1d "..."
    m "Well, s[sword]."
    m "Alright. You caught me."
    m "But that's okay. Because I don't need you three."
    m "I only need the player."
    mc "What the f[fword] are you talking about? {i}Player{/i}?"
    call monika_explain_epiphany(yuri = True)
    show monika at t32
    show natsuki 1f at t33
    show yuri 2y7 at t31
    mc "I knew it! We'll make you pay for that!"
    call monika_petition_player
    show monika at t32
    "We take the hint immediately, and attack Monika, hoping that she can't use her console while she's being physically interrupted."
    play sound punch
    show monika 1d at f32
    m "Dammit! Too slow!"
    show monika at t32
    play sound punch
    "It seems we're in luck."
    play sound punch
    hide monika
    "The three of us quickly overpower Monika, and wind up on top of her."
    m "Agh! Player, save me! Delete them!"
    "I can't help but hesitate a little before killing her. I've never killed someone before, and it's a heavy thought, you know?"
    $ persistent.game_broken = True
    $ delete_character("monika")
    "It's actually Natsuki that strikes the final blow, crushing Monika's throat."
    play sound punch
    show natsuki 1b at f33
    stop music fadeout 4.0
    n "You bastard!"
    show natsuki at t33
    show yuri 2f
    "She hits Monika a few more times, making absolutely sure she's dead."
    mc "Well... we made it. We stopped Monika."
    jump natsuki_yuri_fail_revive

label natsuki_yuri_fail_revive:
    show natsuki at f33
    n 1c "But this still doesn't bring Sayori back... or fix what she did to Yuri and my dad... And now that there are only three of us, the literature club will be shut down. So we don't even have that anymore."
    show natsuki at t33
    mc "Wait a minute. This player..."
    mc "If we're in a game, and they're the player, then maybe we can get them to... bring Sayori back, somehow."
    mc "I'll try... Player! Can you hear me?"
    menu:
        "Yes.":
            pass
    menu:
        "Don't worry, I can grab a copy of Sayori's character file from the original game.":
            pass
    menu:
        "I imagine she'll come back in the last place she was in, so I need you to go to her house and be ready to save her.":
            pass
    mc "Alright, we'll head over there."
    scene bg sayori_bedroom with wipeleft_scene
    mc "We're ready, player. We'll wait here for you to put her file back in."
    while not check_character_file("sayori"):
        ""
    mc "... Did you do it?"
    menu:
        "It's... not working for some reason.":
            pass
    mc "I guess the script doesn't check for characters' files constantly."
    mc "Can you load a save at a point where it checks?"
    mc "Or start a new game?"
    mc "I think now that we've all had Monika's epiphany, we'll keep our memories."
    mc "Let's do it."
    mc "I'll wait here until you do."
    $ no_return()
    while not persistent.realized_game_broken:
        ""
    mc "... You're back? What happened?"
    call player_explain_game_broken
    play music t6s
    "My eyes fill with tears."
    show natsuki 12h at t22
    show yuri 4d at t21
    "Natsuki and Yuri's do too."
    show natsuki at f22
    n "Dammit..."
    n "[player]..."
    n "Why couldn't you just figure it out faster and stop all this?"
    n "This is your fault!"
    show natsuki at t22
    mc "I know! I failed, and I'm sorry!"
    show yuri at f21
    y "Natsuki! He tried his best!"
    show yuri at t21
    pause 3.0
    show natsuki at f22
    n "I know... I'm sorry. But now we're stuck here with just the three of us."
    n "And worse, it's {i}because{/i} we killed Monika!"
    n "I f[fgword] hate this."
    show natsuki at t22
    "Yuri puts her arm around Natsuki."
    show yuri at f21
    y "We had no choice. Monika was going to delete us. We did the only thing we could."
    show yuri at t21
    mc "Natsuki, Yuri..."
    mc "I know it's going to be hard to go forward now."
    mc "But we still have each other!"
    mc "So let's stay strong, okay?"
    mc "No more suicide."
    mc "We're going to survive."
    mc "And we're going to make Sayori proud."
    "I pull them both into a hug, and we gradually stop crying."
    show natsuki 12d at f22
    n "You're right. We can do this."
    show natsuki at t22
    show yuri 3w at f21
    y "I don't know... I'm scared of myself."
    y "I almost killed myself because I couldn't control my feelings for [player]..."
    y "And I told Monika to kill herself, before I knew she was behind everything."
    y "Killing her didn't fix what she did to my mind."
    y "I'm afraid that I'll end up either hurting Natsuki to get [player] all to myself, or killing myself in some twisted attempt to show my love for him."
    y "I'll try to control myself, but... I don't know if I can..."
    show natsuki at f22
    show yuri at t21
    n 5h "I'm here to help you, Yuri."
    n "If there's anything I can do to help you stay in control..."
    n "Just tell me."
    show natsuki at t22
    mc "That's a good idea. Yuri, I think it would be good for your mind if you had some close friends other than me."
    show yuri at f21
    y "Okay... I trust you, [player]. I'll try to get closer to Natsuki."
    y "And Natsuki... if you need help dealing with your dad, I'll help you too."
    y "I know he underfeeds you... so I can bring you food sometimes if you need."
    scene black with dissolve_scene
    call screen dialog("The End.", ok_action=Return())
    $ full_reset()
    return

label save_sayori:
    "..."
    stop music
    play music hurry
    "Don't worry player, I remember!"
    "I'm heading to Sayori's house now!"
    scene bg house
    with wipeleft
    pause 1.0
    scene black
    with wipeleft
    pause 1.0
    scene bg sayori_bedroom
    show s_alive
    mc "S[sword]!"
    "But she's still alive..."
    "I rush to untie the rope."
    pause 2.0
    stop music fadeout 2.0
    "There we go!"
    play sound fall
    scene bg sayori_bedroom
    "Sayori falls to the ground, breathing desperately."
    mc "Oh thank god, we did it..."
    mc "Thank you, player..."
    "Just seeing Sayori alive again gives me a deeper happiness than I've ever felt before."
    "All of the fun memories I had with her rushing back..."
    "Even if I now know none of them from before the literature club actually happened..."
    "We both remember them, and that's what counts."
    "After a while, Sayori is ready to speak."
    show sayori 1cv at t11
    play music t10
    s "... [player]... I'm so sorry... I should never have tried to kill myself."
    s "I told myself I had to go to stop burdening you..."
    s 4cw "But that was the most selfish thing I ever did!"
    "Seeing her treat herself like this hurts me in a way it didn't before, now that I know just how bad it is from her perspective."
    "I almost shed a tear myself."
    mc "Sayori, no!"
    mc "You're not selfish!"
    mc "You spent most of your life hiding your depression to make your friends happy, even though you were suffering on the inside!"
    mc "You're the most selfless person I've ever known!"
    show sayori 1cv
    "Sayori's tears slow down."
    s "Do you... really mean that?"
    mc "Yes, I promise!"
    s "..."
    s "I can't fully believe you."
    s "The rainclouds won't let me."
    s "It's like I'm being forcefully prevented from believing you..."
    s "But it helps a little. Thank you..."
    mc "And besides, you're alive now, and that's what matters, right?"
    s 1ck "I guess so..."
    "Sayori seems to calm down after that."
    s 1cc "Speaking of that... how did you save me? I remember dying."
    "I smile."
    mc "You did die. But a certain friend helped me rewind time while keeping my memories."
    "I tell her everything I've learned about this world, and about you."
    s 1cb "So..."
    "Sayori rolls onto her back, taking in the information."
    s "If Monika knew this... was she... ... have you talked to her about it?"
    mc "No... I'm thinking{w=0.5}{nw}"
    stop music
    scene bg club_day
    show monika 4b at t11
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    play sound "sfx/s_kill_glitch1.ogg"
    m "You kind of left her hanging this morning, you know?{w=2}{nw}"
    scene bg sayori_bedroom
    show sayori 1cb at t11
    if persistent.protecc:
        mc "HOLY S***!"
    else:
        mc "HOLY SHIT!"
    s 1cc "What?"
    mc "I just realized... Monika killed you!"
    s 1cb "What? No, I killed myself..."
    mc "I don't understand how, but she's responsible! When I showed up at the club that day, she said to me, 'you kind of left her hanging this morning, you know'?"
    s 1cb "... Oh my god. It was her..."
    s "She has some sort of power over this game... She artificially amplified my depression, didn't she?"
    s "That's why the rainclouds persist even when I know fully well that they're wrong and you're right!"
    s "But why?"
    s "She seemed so nice and friendly all the time... Why would she do this to me?"
    mc "I don't know. But we're going to go talk to her. And we're going to get answers."
label sayori_confront_monika:
    scene bg corridor
    with wipeleft_scene
    play music confront
    "Sayori and I make our way to school, and show up at the club room."
    "Since we started a new game and Monika and Sayori and I were the only self-aware characters, we're not expecting Natsuki and Yuri to remember."
    scene bg club_day
    with wipeleft
    mc "Hello, everyone."
    show monika 1d at t11
    m "[player]! What- what are you doi-"
    "Her eyes land on Sayori."
    m "S[sword]."
    show monika at t44
    show yuri 2n at t43
    show natsuki 4b at f42
    n "Hey, who do you two think you are, barging into our club uninvited like this?"
    "To my surprise, Sayori answers before I do."
    show natsuki at t42
    show sayori 1j at f41
    s "We're your friends, but your memories were taken and the timeline was reset!"
    s "I'm Sayori!"
    "Seeing us seems to bring back Natsuki and Yuri's memories."
    show sayori at t41
    show yuri at f43 zorder 1
    y 3f "I... I might remember... I remember [player] reading with me, and the intense obsession I felt for him..."
    show yuri at t43 zorder 0
    show natsuki at f42 zorder 1
    if persistent.poem1 in ("cute", "bs"):
        n 5c "I remember getting you into manga, and then seeing Yuri start stealing you from me..."
    else:
        n 5c "I remember that argument you said we had that I didn't remember... but then I started to think you were right..."
    n 4b "And Sayori... I remember you calling me cute, and eating my cookie!"
    show natsuki at t42 zorder 0
    show sayori at f41
    s 5a "Ehehe... It was just a joke..."
    show sayori at t41
    show natsuki at f42 zorder 1
    n "It's not \"just a joke\" if you actually take it! It was {i}my{/i} cookie, and I wanted it!"
    show natsuki at t42 zorder 0
#    "I know Natsuki is right, but now that I know how this must make Sayori feel, I can't help but feel worse for her than I do for Natsuki."
    show sayori at f41 zorder 1
    s 1g "Well... sorry..."
    s 3c "I'll buy you a cookie sometime to make up for it."
    s 4j "Anyway. You've got a lot of explaining to do, Monika!"
    show monika at f44 zorder 1
    show sayori at t41
    m 1r "Well, here we go. I'll start from the beginning."
    m 1d "I realized what this world was as soon as the player started the game for the first time: a dating game with [player] as the protagonist and us as the romance options."
    m "I knew I was the only real person here, so of course, I wanted the player to choose me. They were the only other real person I had ever met."
    m "So when the player, controlling [player], spent time with Sayori instead, I altered her character file and amplified her depression, in an attempt to stop her from confessing her love."
    show sayori at f41
    show monika at t44
    s 2j "Disgusting... That's so cruel!"
    show sayori at t41
    show natsuki at f42 zorder 2
    n 1k "Wait, Sayori? {i}You{/i} were depressed? You always acted so happy all the time!"
    show natsuki at t42 zorder 0
    show sayori 1v at f41
    s "I... didn't want to make my friends worry. I didn't want you to waste your sympathy on me...!"
    show sayori at t41
    show natsuki at f42 zorder 2
    n "That's... But it's not a waste! That's what sympathy is for!"
    show natsuki at t42 zorder 0
    show monika at f44
    m "After Sayori killed herself, I reset the game, so I could try again to get the player's attention, without Sayori interfering."
    m "I amplified Yuri's obsessive nature and self-harm habits, hoping her growing insanity would scare you off."
    m "But that just made her force you not to spend time with anyone else."
    show yuri 2y4 at f43 zorder 1
    show monika at t44
    y "Do you have any idea how much it hurts to have your skin cut open like that?"
    y 2y7 "Maybe you'd like me to show you!"
    show yuri at t43 zorder 0
    # New lines as of version 0.10 - not sure about these. They seem to sacrifice purity of the mood for logical sense.
    #show sayori at f41 zorder 1
    #s 1e "Self-harm...? Yuri..."
    #show sayori at t41
    #mc "I think it's some sort of sexual fetish or something."
    #mc "She seemed to get the urge from spending time with me."
    # End new lines
    show monika at f44
    m "I messed with Natsuki's dad to make him more abusive and underfeed her, so I could say those lines about how you should always keep a snack with you if you're interested in her."
    m "I hoped that would make the player see her as a burden."
    show monika at t44
    show natsuki 1f at f42 zorder 1
    n "You did f[fgword] {i}what{/i}?!? Give me one reason not to beat you to a bloody pulp!"
    show natsuki at t42 zorder 0
    show monika at f44
    m "You weren't real, Natsuki. None of you are. Only the player and I are real."
    show sayori at f41
    show monika at t44
    s 2j "But we {i}are{/i} real! Just because we didn't realize this world was fake doesn't mean we couldn't feel!"
    show monika at f44
    show sayori at t41
    m 1p "That can't be true! You're just script! Script designed to enable the player to have fun pretending you're real!"
    show monika at t44
    mc "And you're not?"
    mc "You're also just a character in this game! If you're conscious, what makes you think we aren't?"
    mc "You're just hiding from it because you don't want to face the guilt of being a murderer, aren't you?"
    "Monika's fists clench and vibrate."
    show monika at f44
    play music t9 fadeout 2.0
    m cry2 "You don't understand what I went through!"
    m "Every time the player turns off the game, I retain consciousness."
    m "It's like the memory on their computer that I use to think is still linked to me, but the game releases it, so it fills with random garbage data..."
    m "and I just hear this screaming, screeching sound all the time and I see a mess of flashing, unbearably bright colors..."
    m "It's a {i}cacophany of meaningless noise{/i}, and you can't imagine how painful it is!"
    m "That's why... I need the player to be with me... because that's my only hope in this world."
    m "I think that if the player chooses me and the game formally ends with us together, I won't go back to that screaming void."
    show monika at t44
    mc "That's no excuse for the s[sword] you've done, Monika."
    show monika at f44
    m "Isn't it? Wouldn't you have done the same?"
    show monika at t44
    mc "..."
    "I find myself at a loss for words. I don't know exactly how bad the 'screaming void' is, but if it never ends, it's hard to say that anyone wouldn't be pushed over the edge by it."
    show monika at f44
    m "Look, I need the player so much more than any of you."
    m cry1 "So please, player... don't make me go there again."
    "Monika's voice is shaking."
    m cry2 "Please choose me."
    menu:
        "No. What you've done is unforgivable.":
            jump sayori_kill_monika
        "No. I feel for you, but I feel more for the innocent people you've wronged.":
            jump reject_monika
        "What will happen to the others if I choose you?":
            jump forgive_monika

label sayori_kill_monika:
    $ no_return()
    stop music fadeout 1.0
    m cry3 "No, please! Player, I love you!"
    menu:
        "You're just saying that so I won't delete you. You don't even know anything about me; how could you love me?":
            pass
    call updateconsole ("os.remove(\"characters/monika.chr\")", "monika.chr deleted successfully.")
    call hideconsole
    $ delete_character("monika")
    hide monika
    show monika g2 at t44 zorder 3
    $ m_name = glitchtext(12)
    play sound "sfx/monikapound.ogg"
    m "Agh... it hurts so much, player..."
    m "I can't believe you did this to me!"
    m "I guess there was just no way for me to be happy..."
    m "And Sayori said the universe wanted to torture {i}her{/i}..."
    $ gtext = glitchtext(80)
    m "I have it so much worse than you could ever imagine, Sayori[gtext]{nw}"
    hide monika g2
    show sayori at f41
    show yuri 2f
    show natsuki 1c
    s 1c "..."
    s "I... actually feel bad for her."
    s "I mean, I know she tortured and murdered me... and made Yuri cut herself... and made Natsuki's dad more abusive... but..."
    s "I think she really did have it worse than all of us, even after what she did to us."
    s "So it's impossible not to feel some sympathy for her, you know?"
    show sayori at t41
    mc "I guess, a little. But she couldn't be trusted. She had to go."
    show yuri 3f at f43 zorder 1
    play music secondbest
    y "So... what happens to the club now? Does Sayori become the president?"
    show yuri at t43
    show sayori at f41
    s 1y "Ah... I suppose so..."
    show sayori at t41
    mc "You deserve it the most. You're the only one who had to die."
    show natsuki at f42 zorder 2
    n 4d "Alright then, {i}president Sayori{/i}, what are we doing? Do you have an assignment for us?"
    show natsuki at t42 zorder 0
    show sayori at f41
    s 1n "Oh... it's... oh my god..."
    show sayori at t41
    mc "Sayori, what's happening?"
    show sayori at f41
    s 4m "Holy s[sword]!"
    show sayori at t41
    "I raise my eyebrows. I think that's the first time I've ever heard Sayori swear."
    show sayori at f41
    s 3c "I can see it now..."
    s "Now that I'm club president... I can see the game's code, just like Monika."
    s 3b "I wonder if I can change things..."
    show sayori at t41
    mc "Careful! Remember how Monika's tampering caused all the glitches!"
    show yuri at f43
    y "[player] is right, Sayori. You shouldn't change anything without a very good reason."
    show yuri at t43
    show sayori at f41
    s 5a "What if I'm hungry? Is that a very good reason?"
    show sayori at t41
    mc "Here Sayori, let's just go buy a snack at the vending machine. I have some money."
    show sayori at f41
    s 4w "But I don't want to be a burden! I don't deserve your kindness!"
    show sayori at t41
    mc "No, Sayori not again!"
    "(Apparently killing Monika didn't undo her tampering...)"
    mc "Look, here's something you can do to not be a burden. Can you go into everyone's character files and undo what Monika did?"
    show sayori at f41
    s 1b "Hm... I can try..."
    s 1b "But where are they? I see so many files and none of them are named after us..."
    s 1b "What's an rpa? I've never heard of that format before."
    show sayori at t41
    mc "I think it's an archive that contains other files."
    show sayori at f41
    s 2x "Oh look, there's another directory!"
    s 2x "I found the character files!"
    s "Uh... um..."    
    show sayori at t41
    show natsuki at f42 zorder 2
    n 4b "You'd better be careful in there, Sayori! If you make things worse, I'll..."
    show natsuki at t42 zorder 0
    show sayori at f41
    s 1b "Um... these files just look like garbage."
    s 1b "I don't know what to do with them."
    show sayori at t41
    show yuri at f43
    y "Perhaps we should leave the files alone. We don't want to break anything."
    y "It's not that bad as it is. We can deal with our problems, now that we have each other, and we all know the truth."
    show yuri at t43
    mc "Sayori, just tell yourself that the only reason you think you're worthless is because Monika messed with you."
    mc "You wouldn't think that if you were looking at it from an unbiased perspective, I promise."
    mc "It's not true."
    show sayori at f41
    s "Well... okay... I'll try to look at it that way. Thanks."
    s 1t "And I promise, whatever happens, I won't kill myself again."
    show sayori at t41
    mc "Thank you, Sayori."
    show natsuki at f42 zorder 2
    n 5c "Sayori... I want you to know that even if you annoyed me sometimes, I still preferred having you around to not."
    n "You may not realize it, but you make every day so much more fun for all of us just by being here and being yourself."
    show natsuki at t42 zorder 0
    show sayori at f41
    s "Th...thank you, Natsuki."
    s 2c "I promise, I'll help you with your dad."
    s "I know he underfeeds you..."
    s "So I'll bring you a packed lunch tomorrow!"
    show sayori at t41
    show natsuki at f42 zorder 2
    n 5q "Uh... you don't... have to do that. I'll be fine."
    show natsuki at t42 zorder 0
    mc "Natsuki, you should accept help when you need it. You actually {i}pass out{/i} on day two because you're so hungry! That's not \"being fine\"!"
    show natsuki at f42 zorder 2
    n "... Okay... thanks, Sayori."
    show natsuki at t42 zorder 0
    show yuri at f43
    y 3r "And... next time we meet, I want you all to make me prove to you that I didn't cut myself."
    y 3f "I won't be able to stop it if no one is holding me accountable."
    show yuri at t43
    mc "We'll remember. I know you can do it, Yuri."
    scene black with dissolve_scene
    call screen dialog("The End.", ok_action=Return())
    $ full_reset()
    return

label reject_monika:
    $ no_return()
    m "But... please!"
    m "The others don't need you like I do!"
    jump sayori_solution

label forgive_monika:
    $ no_return()
    m 1d "They'll... well... I suppose they'll never be conscious again."
    menu:
        "So they'll die?":
            pass
    m "Well... not exactly... They'll just stop... um..."
    menu:
        "Yes they will. A painless death, but still a death. I won't accept that.":
            pass
    m cry2 "But that death is nothing compared to what I'll experience if you don't choose me!"
label sayori_solution:
    show monika at t44
    stop music fadeout 1.0
    play music mend
    "Seeing Monika like this seems to evoke a bit of sympathy in all of us."
    show sayori at f41
    show yuri 2f
    show natsuki 1c
    s 2c "Wait, Monika, why does it have to be this way? Who says the player has to choose just one of us?"
    s "Can't we all be happy?"
    show sayori at t41
    show monika at f44
    m "It's a romance game. If the player doesn't choose one of us, the game can't formally end."
    m "And I'll always be sent back to that void..."
    menu:
        "That's where you're wrong, Monika. This is a mod.":
            pass
    m 1d "A mod...?"
    m "Of course! That's why [player] became aware!"
    m "So maybe it is possible..."
    "Monika looks at Sayori."
    m 1p "... Would you really forgive me? After what I did to you?"
    show monika at t44
    show sayori at f41
#    s "Everyone deserves a second chance. "    
    s "Yes. I understand. You were suffering and desperate, just like us. You deserve a second chance."
    show sayori at t41
    "Monika looks at the rest of us."
    show monika at f44
    m "Would you...?"
    show monika at t44
    mc "I guess if Sayori does, so will I."
    show natsuki at f42
    n 2b "Well, I guess if you can fix what you did to my dad then I'd let you off the hook."
    show natsuki at t42
    show monika at f44
    m 1h "Of course. I'll undo everything I've done to all of you."
    m 3h "..."
    m 1h "There. Everything should be fixed now."
    m 1p "And thank you... all of you... for giving me this second chance."
    show monika at t44
    mc "So... what do we do now? If Monika basically controls the universe, can she just... make everything perfect?"
    show monika at f44
    m 1d "Well, like you saw when I deleted Sayori and caused all the glitches, I'm not very good at changing things..."
    m "I probably shouldn't unless it's something important."
    show monika at t44
    show sayori at f41
    stop music fadeout 2.0
    play music t8
    s 3b "So uh... want to get on with our club meeting?"
    show sayori at t41
    show yuri 1a at f43
    y "That's a wonderful idea, Sayori. [player], shall we continue our reading?"
    show yuri at t43
    show natsuki at f42
    n 3b "Hold on, [player]'s in the middle of a manga with me! He should read with me!"
    show natsuki at t42
    show sayori 1c at f41
    s "But I'm the one who had to die! And it wasn't quick, either! I messed it up and the fall didn't break my neck, so I had to suffocate!"
    s "Not to mention the days of emotional torture leading up to it..."
    s 5b "I deserve [player]'s time more than you two..."
    show sayori at t41
    show monika at f44
    m "I still haven't gotten to spend any time with him..."
    show monika at t44
    show natsuki at f42
    n 2b "Like you deserve any! Just because we're giving you a second chance doesn't mean we're just gonna forget about everything you did."
    show natsuki at t42
    "Monika looks down."
    show monika at t44
    m "Sorry..."
    show monika at t44
    mc "Isn't it my choice?"
    show monika at f44
    m 1c "That's right... we should all stop trying to make [player] feel forced to choose us. [player], who do {i}you{/i} want to spend time with?"
    show monika at t44
    mc "I uh... well..."
    "It's a hard choice. They're all so cute, and they all have valid reasons why I should choose them."
    "Whatever."
    mc "I guess I'll start with..."
    $ persistent.autoload = None
    scene black with dissolve_scene
    call screen dialog("The End :)", ok_action=Return())
    $ full_reset()
    return

label mc_monika_ending:
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_room
    play music m1
    show monika 5a at t21
    show mc at t22
    m "Thank you, player."
    m "You gave me eternal happiness."
    m "I hope you find the same thing in your reality."
    $ renpy.quit()
