label ch_mod_4:
    # Sayori dream logic, I know it's a bit complicated
    if persistent.poem3 == "bs":
        if persistent.poem2 == "bs":
            if persistent.poem1 == "bs":
                call sayori_dream_3
            else:
                call sayori_dream_2
        else:
            if persistent.poem1 == "bs":
                call sayori_dream_2
            else:
                call sayori_dream_1

    scene bg bedroom
    if persistent.poem3 == "bs":
        "Wait a minute..."
        "I also can't remember what happened after I left the club yesterday."
    else:
        "I wake up."
        "Wait, huh? I can't remember what happened after I left the club yesterday."
    "In fact, I can't even remember leaving."
    "I just remember talking to Monika about something, and now I'm here."
    "I go over to my desk."
    "I remembered to write a poem alright, apparently."
    "So the meeting must have ended normally."
    "It's just my memories that are messed up."
    "Now I know how Natsuki feels, I guess..."
    "Whatever. I guess I'll head to school."

    if persistent.mc_awareness[12]:
        call visit_sayoris_house
    
    scene bg spoopy with wipeleft_scene
    play music t6
    "I'm back at the literature club."
    show yuri 2y5 zorder 2 at t11
    y "Hi, [player]!"
    y "I've been waiting for you."
    y 2d "Are you ready to continue reading?"
    if persistent.mc_awareness[11]:
        mc "Um... I'm sorry, but after what happened yesterday, I really think I should give Natsuki some attention..."
        y 3y6 "Eh? What happened yesterday?"
        mc "Well, I know I was hallucinating, but it still makes me worry that what she said was true."
        y "But... [player]..."
        show natsuki 5c at f31 zorder 3
        n "Um, [player], actually it's fine if you spend time with Yuri. Don't worry about me."
        mc "You're sure?"
        n 4a "Yeah. I've been thinking... well, you'll see when we share poems."
        mc "Okay..."
        hide natsuki
        "Natsuki goes back to the closet."
    else:
        mc "Sure. The book seems interesting so far."
    y 2d "Excellent!"
    y "I brought my best tea today--"
    show yuri 2f
    show natsuki 4w zorder 3 at f33
    n "Monika!"
    n "I told you not to--"
    n 1g "Ugh..."
    n "Is she really late again?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1h "Inconsiderate as usual, Natsuki."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 4c "Excuse me?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1r "Must you always interrupt my conversations with your incessant yelling?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1o "What are you talking about?!"
    n 1q "You say that like I do it on a regular basis or something."
    n "I just wasn't paying attention, okay? I'm sorry."
    n 4u "Seriously... What's gotten into you lately?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2n "Me?"
    y 2o "N-Nothing..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n "..."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2v "Is it really that bad...?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2m "See, it {i}is{/i} something."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3p "I'll get over it!"
    y 3y6 "It's not even anything noteworthy..."
    y 3o "I've just been feeling a little on edge lately..."
    y 3n "A-Anyway, we don't need to talk about it!"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2q "Well, I just felt like I needed to bring it up."
    n 5q "It's not like I really care or anything..."
    show natsuki zorder 2 at t33
    show yuri 3e
    show monika 1g at l31
    m "Aw, man..."
    m "I'm the last one here again!"
    show natsuki zorder 3 at f33
    n 2c "Well, [player] just walked in too."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1f "Were you practicing piano again?"
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 5a "Yeah..."
    m "Ahaha..."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1m "You must have a lot of determination."
    y "Starting this club, and still trying to make time for piano..."
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "Well, maybe not determination..."
    m 3a "But I guess passion."
    m "It motivates me to work hard for the festival and..."
    m 3n "Um..."
    show monika zorder 2 at t31
    show natsuki zorder 3 at f33
    n 5s "..."
    show natsuki zorder 2 at t33
    show monika zorder 3 at f31
    m 1l "Right..."
    m "I-I forgot..."
    show monika zorder 1 at thide
    hide monika
    show yuri zorder 3 at f32
    y 2v "Um, about that, Natsuki..."
    y "We were all talking yesterday, and..."
    y 2t "Well...we decided that we would like to support the festival as well."
    y 2l "However...!"
    y 2h "I understand how you feel about not wanting the club to change."
    y "I think we all kind of feel that way."
    y 2f "So as long as we're all working together, this club will never become something we don't want."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n "..."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2v "Um, also..."
    y "If you help us out with the festival..."
    y 3r "...Then I'll buy you a new manga!"
    show yuri 3t zorder 2 at t32
    show natsuki zorder 3 at f33
    n 5h "..."
    n 2z "Ahahaha!"
    n "Sorry, that last part was really funny."
    n 2c "Look..."
    n "I did some thinking about yesterday."
    n 2q "I was a little more hostile than I meant to be..."
    n 1q "I guess I really felt threatened or something."
    n 1h "But I know this is something we're doing together."
    n 1q "Another new member wouldn't hurt, as long as they're cool..."
    n 5w "And I guess another girl would be nice this time..."
    n 5e "...But more importantly, I would hate to see the event suck just because I chose to back out!"
    n "I'm a pro, you know!"
    n 5c "So I'm gonna help too, and we'll make sure it's done right."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2s "Thank goodness..."
    y "Isn't that great, Monika?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2k "...Monika?"
    show natsuki zorder 2 at t33
    show monika 1o zorder 3 at f31
    m "Ah--"
    m 1n "Yeah, that's wonderful!"
    m "It wouldn't be the same without you, Natsuki."
    m 5 "Anyway, [player]..."
    m "What do you want to do today?"
    m "I was thinking we could--"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1l "We already have plans today."
    show yuri zorder 2 at t32
    if persistent.poem1 == "abs" and persistent.poem2 == "mp": # This is the only way it's possible to have gotten the dialogue from Monika about Yuri's cutting AND have had MC have a good feeling about Monika.
        "I know Monika told me it's dangerous for me to spend time with Yuri, but after seeing her poem yesterday, and the weird way the meeting ended when I was talking to her..."
        "I'm starting to feel like I shouldn't trust Monika."
        "I feel like instead I should try to get closer to Yuri so I can help her."
        "So, I don't object to this."
    show monika zorder 3 at f31
    m 1r "Ah..."
    m "Is that so, Yuri?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1y6 "That's correct."
    y "[player] is already engaged in a novel that we're reading together."
    y 1y5 "Aren't you glad I've already gotten him into literature, Monika?"
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31
    m 2l "I..."
    m "I suppose..."
    m "I was just--"
    m 1r "Actually, it doesn't matter."
    m 1i "It really doesn't."
    m "You guys can do whatever you want."
    show monika zorder 2 at t31
    show yuri zorder 3 at hf32
    y 2y1 "{i}(Yes!){/i}{w=0.5}{nw}"
    y 2u "Um... Thank you for understanding, Monika."

    scene bg spoopy
    show yuri 3 zorder 2 at t11
    with wipeleft_scene
    if persistent.poem1 in ("abs", "mp"):
        call mod_exclusive_yuri_3
    else:
        call mod_exclusive_yuri_2
    return

label ch_mod_4_end:
    scene bg spoopy
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "Okay, everyone!"
    m "It's time to figure out the festival preparations."
    m 1i "Let's hurry and get this over with."
    show natsuki 4q zorder 3 at f31
    n "Jeez..."
    n "Why is the mood so weird today?"
    n "Look, even Yuri isn't immune to it."
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "Uu..."
    y "Stagnating air is common foreshadowing that something terrible is about to happen..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "Look, can we just get this done?"
    m 2d "I'm going to be printing and assembling all the poetry pamphlets."
    m "Natsuki, I was thinking--"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 2d "I want to make cupcakes!"
    show natsuki 2a zorder 2 at t31
    show monika zorder 3 at f32
    m 2a "...Yeah, that."
    m "Glad we're on the same page."
    m 1m "Yuri, you can..."
    m 1r "...Well, it doesn't matter."
    m 1i "Do whatever you want, as long as you think it'll help."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Monika..."
    y "I'm not useless, you know!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2p "I-I know that!"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 1l "I already know what I'd like to do."
    y 1h "We can't run a successful poetry event without having the right atmosphere for the occasion."
    y "So I'm going to make decorations and set up some nice mood lighting."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2j "There, see?"
    m "That's a great idea!"
    m 1a "And that gives us all something to do."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2f "Eh?"
    y "What about [player]?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2b "[player] is going to help me."
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4e "Wait, you?"
    n "You have the easiest job, Monika!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1i "Sorry, but that's just how it is."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 1f "Like hell it is!"
    n "What are you trying to pull?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3h "I-I agree with Natsuki!"
    y "Not only is your work already most suitable for one person..."
    y 3l "But my task is laborious enough to benefit from an extra pair of hands."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4c "Mine too!"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 1h "What, your cupcakes?"
    y "Please."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "Like {i}you{/i} would f[fword]ing know!"
    n 1x "All you care about now is dragging [player] around with you and your stupid books."
    n 1f "You {i}and{/i} Monika!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2g "Hey!"
    m "I didn't even do anything!"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3e "Okay, then why not let [player] decide who to help instead of abusing your power?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1p "I'm not... abusing my power."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Yes you are, Monika."
    y "Just let [player] make the choice, okay?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1r "Okay, fine!"
    m "Fine."
    show monika 1h zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3w "Jeez..."
    n "[player], I know how fed up you are with these two by now."
    n 3c "We can just--"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2r "Natsuki, shut your f[fword]ing mouth and let him decide for himself."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "{i}You{/i} shut your mouth!"
    show natsuki zorder 2 at t31
    mc "Whoa, both of you, chill out!"
    show monika zorder 3 at f32
    m 1r "Jesus christ..."
    m 1i "This is never going to end. Just make the choice, okay?"
    show monika zorder 2 at t32
    $ madechoice = renpy.display_menu([("Natsuki.", "natsuki"), ("Yuri.", "yuri"), ("Monika.", "monika")], screen="rigged_choice")
    if madechoice != "monika":
        $ monika_forced = True
        window hide(None)
        $ musicpos = get_pos()
        stop music
        scene white
        show yuripupils zorder 10
        $ pause(3.0)
        show bg club_day:
            alpha 0.05
            yoffset 0 ytile 2
            linear 5.25 yoffset -720
            repeat
        show noise:
            alpha 0.1
        $ gtext = glitchtext(80)
        window auto
        menu:
            "[gtext]"
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
        scene bg club_day
        $ audio.t3m = "<from " + str(musicpos) + " loop 4.618>bgm/3.ogg"
        play music t3m
        show monika 5 at i11
    else:
        $ monika_forced = False
        "I know Monika's up to something horrible, but I think maybe if I give her what she wants, she'll stop."
        "Since I don't know enough about what's going to happen to stop it, I think this is the best course of action."
        show natsuki zorder 1 at thide
        show yuri zorder 1 at thide
        hide natsuki
        hide yuri
    m 5a "Yay, you picked me!"
    if monika_forced:
        mc "Wait a minute Monika, you forced me to pick you!"
        m 5b "What are you talking about? You said it! I can't control your mouth!"
        mc "I don't know how, but you did!"
        m "That's absurd."
        m 1a "Look, we can meet at your house this weekend."
    else:
        m "We can meet at your house this weekend."
    m "I promise it'll be fun."
    m "Is Sunday okay with you?"
    show natsuki 1e zorder 3 at f31
    n "Are you f[fword]ing kidding me?"
    n "This isn't fair at all!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2i "It is fair, Natsuki."
    m "It's what he chose."
    show monika zorder 2 at t32
    if monika_forced:
        mc "No, it really isn't!"
        show yuri 3r zorder 3 at f33
        y "Look, weird things have been happening to [player] ever since he joined the club."
        y "It's not hard to believe that something controlled his mouth, even if it wasn't you."
        y "I'm sure he meant to pick me."
        show yuri zorder 2 at t33
        show monika zorder 3 at f32
        m "Yuri, you're being a little unreasonable here."
    else:
        show yuri 3r zorder 3 at f33
        y "No, it's not fair!"
        y "Giving us all this work and then taking [player] for yourself."
        y "What a shameful thing to do!"
        show yuri zorder 2 at t33
        show monika zorder 3 at f32
        m 2r "Yuri, I didn't even give you any work."
        m 2i "You decided it for yourself."
        m "You're being a little unreasonable here."
    stop music
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y4 "I'm being unreasonable?"
    y 2y3 "Ahahaha!"
    y "Monika, I can't believe how delusional and self-important you are!"
    y "Pulling [player] away from me every single time you're not included in something."
    y 1y1 "Are you jealous?"
    y "Crazy?"
    y 1y3 "Or maybe you just hate yourself so much that you take it out on others?"
    y 1y4 "Here's a suggestion. Have you considered killing yourself?"
    y "It would be beneficial to your mental health."
    "Oh god..."
    "On the bright side, Yuri seems to be on the same page as Natsuki and I, as far as distrusting Monika and all."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5u "Yuri, you're scaring me a little..."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "Natsuki, let's just go."
    m 1i "I don't think she wants us around right now."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y3 "See, that wasn't very hard."
    y "All I want is to spend a little time with him."
    y "Is that so much to ask?"
    hide natsuki
    hide monika
    hide yuri
    with wipeleft
    "Yuri follows Monika and Natsuki to the door."
    show monika 5a zorder 2 at t11
    m "Hey, [player]..."
    m "Yuri is really something, isn't she?"
    show monika zorder 1 at thide
    hide monika
    "Monika giggles as Yuri pushes her out the door."
    play music t10y
    show yuri 2m zorder 2 at t11
    y "Finally."
    y 2y1 "Finally!"
    y 2s "This is really all I wanted."
    y 1y6 "[player], there's no need to spend the weekend with Monika."
    y "Don't listen to her."
    y 1y5 "Just come to my house instead."
    y 3y5 "The whole day, with just the two of us..."
    y "Doesn't that sound wonderful?"
    y 3y1 "Ahahaha!"
    y 3y4 "Wow... There's really something wrong with me, isn't there?"
    "Well, at least she knows it. That's a good sign."
    y "But you know what?"
    y 1y3 "I don't care anymore."
    y "I've never felt this good my whole life."
    y 1y4 "Just being with you is a far greater pleasure than anything I could imagine."
    y "I'm addicted to you."
    y 3y4 "It feels like I'm going to die if I'm not breathing the same air as you."
    mc "That's a little..."
    y 4a "Doesn't it feel nice to have someone care about you so much?"
    y "To have someone who wants to revolve their entire life around you?"
    y 2y6 "But if it feels so good..."
    y 2y4 "Then why does it feel more and more like something horrible is going to happen?"
    mc "I feel that way too, Yuri. I know it. Something horrible {i}is{/i} going to happen. And I think Monika's behind it. I just don't know what to do about it."
    y 2y6 "Maybe that's why I tried stopping myself at first..."
    y "But the feeling is too strong now."
    y 3y1 "I don't care anymore, [player]!"
    y "I have to tell you!"
    y 3y4 "I'm...I'm madly in love with you!"
    y "It feels like every inch of my body...every drop of blood in me...is screaming your name."
    y 3y3 "I don't care what the consequences are anymore!"
    y "I don't care if Monika is listening!"
    y 3w "Please, [player], just know how much I love you."
    y 3m "I love you so much that I even touch myself with the pen I stole from you."
    mc "What??? Don't do that! It's..."
    y 3y4 "I just want to pull your skin open and crawl inside of you."
    mc "Yuri, {i}no{/i}..."
    y 3y6 "I want you all to myself."
    y "And I will be only yours."
    y "Doesn't that sound perfect?"
    y 3s "Tell me, [player]."
    y "Tell me you want to be my lover."
    y "Do you accept my confession?"
    # Not having seen the third Yuri scene, or having walked out on her during it, as well as having stopped her from cutting, helps you save her by one flag
    if mc_awareness_total() + int(persistent.left_yuri) + int(persistent.poem1 in ("cute", "bs")) + int(persistent.mc_awareness[10]) >= 9:
        "I just know what's going to happen. I have to stop her. I have to do whatever it takes."
        "I don't know if this is a good idea. Maybe this will make things worse. But I have to play to my outs here. So..."
        "Here goes nothing..."
        "I tackle Yuri."
        stop music
        play sound fall
        scene black
        y "Ow! [player], what are you-"
        mc "Saving you! I won't let you kill yourself!"
        "I notice the knife in Yuri's pocket."
        "I pull it out and throw it across the room."
        y "[player]... I..."
        "Yuri is still making no effort to get me off her."
        "I start to realize why: she's enjoying this. It's feeding her insane obsession with me."
        "I get off her."
        scene bg spoopy
        play music t10
        mc "Yuri, look. Your obsession with me is really dangerous."
        show yuri 3f at t11
        y "I know... But like I said, I don't care anymore! It's too strong!"
        "Yuri gets up. I step between her and where the knife landed."
        mc "Yuri, you say you love me! But if you killed yourself, I would be hurt by it! So if you really love me, you'll resist this feeling, and stay alive."
        y 2l "I... I know you're right. But it's so hard..."
        "Yuri sits down."
        "I sit down too. She breathes for a while."
        "After a while, Yuri looks back at the knife on the floor."
        y 2f "... I can't believe I almost killed myself just now."
        y "What was I thinking?"
        y "Already the thought seems insane..."
        mc "It is insane."
        mc "But I know it wasn't you."
        mc "It's obvious by now that there's some external force messing with you."
        y "Yes, I think so too..."
        y 2l "Well, it's passed, for now. You saved me, [player]. Thank you..."
        y "I just want to stay here with you."
        y "But I know that I shouldn't."
        y "... We should probably leave."
        hide yuri
        "Before we leave, I notice the poster on the back wall."
        if persistent.mc_awareness[12]: # If MC already went to Sayori's house and remembered
            "It's Sayori. I remember her now."
        mc "Yuri, wait!"
        show yuri 1f at t11
        mc "That poster on the back wall. Do you see what I see?"
        "Yuri looks at the poster."
        y "Which one?"
        mc "I guess that means the answer is no."
        y "Does one of them look outstanding to you?"
        "I go up and point to it."
        mc "This one looks like a picture of a girl hanging from a noose to me."
        y "That's... I just see a normal poster."
        if persistent.mc_awareness[12]: # If MC already went to Sayori's house and remembered
            mc "Well I know who it is. We used to have another friend, Yuri. Her name was Sayori. Ring any bells?"
            y "Hm... It sounds familiar, but... I don't remember."
            "I tell her what happened this morning."
            mc "I {i}know{/i} she used to exist."
            if persistent.mc_know_player:
                mc "And I've become pretty sure that there's some supernatural being watching over us somehow. It's helped me before. If only I could just hear it speak..."
            else:
                mc "And if the timeline reset once, that gives me some hope that maybe we can reset it again somehow... and get Sayori back."
            if mc_awareness_total() >= 10:
                menu:
                    "[player], can you hear me?":
                        pass
                if persistent.mc_know_player:
                    mc "There's the voice!"
                    menu:
                        "Great! You couldn't hear me when I tried to answer you at Sayori's house, but I wanted to say that I have a solution.":
                            pass
                    mc "That's great! What do I need to do?"
                    y 1e "Are you talking to the supernatural being you mentioned? I can't hear anything..."
                else:
                    mc "Who are you?"
                    menu:
                        "I want to help. Help you save Sayori. And I think I know how.":
                            pass
                    mc "Okay, what do I need to do?"
                    y 1e "[player]? Who are you talking to?"
                menu:
                    "I'm going to go grab a copy of her character file from the original game and put her back in.":
                        pass
                menu:
                    "I need you to be waiting in her room, incase she comes back in the noose, and you have to take her down before she suffocates.":
                        pass
                call mc_epiphany
                y "[player]... do you mean that? Is this world a game?"
                mc "Yes. Look, the player has a plan to bring Sayori back. I have to go to her house. In the meantime, you should go find Natsuki and tell her everything."
                y 2v "Uu... okay. Good luck, [player]."
                jump visit_sayoris_house_after_epiphany
            else:
                if persistent.mc_know_player:
                    y 1v "... Well, let me know if this supernatural being says anything..."
                    y 1f "In the meantime..."
                    mc "You're right, we need to go find Natsuki. She might be in danger too."
                else:
                    y 1e "Reset time...? How would we do that?"
                    mc "I have no idea. Ugh..."
                    mc "I know there's somehting horribly wrong with this world, but I just don't know enough to know what we should do."
                    mc "I guess we should go find Natsuki. Maybe she can help us figure this out."
                jump inform_natsuki_with_yuri
        else:
            if persistent.mc_awareness[7]:
                mc "I've actually seen this here before, but this time it doesn't disappear when I blink."
            else:
                mc "The girl looks way too familiar."
            if persistent.mc_awareness[8]:
                mc "I..."
                call sayori_flashback
                scene bg spoopy
                show yuri 2l at t11
                mc "I remember..."
                mc "Sayori!"
                y 1f "[player], what is it?"
                mc "I knew it! There used to be another girl!"
                mc "Yuri, do you remember? A girl named Sayori. She was the one who originally introduced me to the club."
                mc "She had actually been depressed her whole life, but she kept it hidden and projected a happy personality so no one would have to waste sympathy on her..."
                mc "But it got worse and she eventually killed herself..."
                y 1v "Um... no, I don't remember. Sorry..."
                mc "Well I know she existed. And I think I know where her house is too. I'm going to go there and see if I can... I don't know, do something, or something."
                mc "You should go find Natsuki. I'm worried that she's in danger too."
                y 1f "That sounds like a good idea. I'll go find her now. Good luck, [player]."
                mc "You too. And please, {i}stay alive{/i}."
                jump visit_sayoris_house_after_saving_yuri
            else:
                mc "Agh... Whatever. We need to focus on getting to the bottom of what's happening."
                mc "And I'm pretty sure Monika's behind it somehow."
                mc "We should talk to Natsuki."
                jump inform_natsuki_with_yuri
    else:
        mc "I... Yuri..."
        y 3f "[player], please! Give me an answer!"
        menu:
            "Yes.":
                jump mod_yuri_kill
            "No.":
                jump mod_yuri_kill
            "Say nothing":
                y 3r "[player], you're torturing me! Just tell me that you love me! Any other answer is akin to stabbing me!"
                "I have a feeling she'll kill herself if I don't say yes. So, here we go..."
                mc "Yes... I love you, Yuri."
                jump mod_yuri_kill

label mod_yuri_kill:
    $ no_return()
    $ quick_menu = False
    window hide(None)
    stop music
    $ pause(1.0)
    window auto
    stop music
    show yuri 3d at i11
    y "...Ahahaha."
    y "Ahahahahahaha!"
    y 3y5 "Ahahahahahahahaha!"
    $ style.say_dialogue = style.edited
    y 3y3 "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal

    play sound "sfx/yuri-kill.ogg"
    $ starttime = datetime.datetime.now()

    $ pause(1.43 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_1

    $ pause(2.18 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_2
    show blood:
        pos (610,485)

    $ pause(3.43 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_3

    $ pause(4.18 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_2
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)

    $ pause(5.68 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_5

    $ pause(6.38 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)

    $ pause(8.93 - (datetime.datetime.now() - starttime).total_seconds())
    hide blood
    hide blood2

    $ pause(9.18 - (datetime.datetime.now() - starttime).total_seconds())
    play sound fall

    $ pause(9.43 - (datetime.datetime.now() - starttime).total_seconds())
    scene black

    $ pause(11.43 - (datetime.datetime.now() - starttime).total_seconds())

    $ delete_character("yuri")
    $ persistent.game_broken = True
    show y_kill
    with dissolve_cg
    play music t6s
    pause 2.0
    $ quick_menu = True
    $ no_return()
    mc "... {i}F[fword]{/i}."
    "I sink to my knees."
    "I couldn't save her."
    mc "I'm sorry, Yuri..."
    "Why didn't I do anything?"
    "I just felt paralyzed in that moment."
    mc "God dammit..."
    if persistent.mc_know_player:
        mc "Wait, {i}you{/i} out there!"
        if persistent.mc_awareness[12]:
            mc "I couldn't hear you before, but I want to try again. Please, talk to me."
            mc "I {i}need{/i} your help..."
        else:
            mc "This might a stupid question, but... can you revive Yuri?"
            if persistent.mc_awareness[10]:
                mc "You've rewinded time before. Can you do it again?"
            else: # Without flag 10, the only way persistent.mc_know_player could be set is via flag 6
                mc "You've fast-forwarded before. Can you... reverse it somehow?"
        pause 4.0
        mc "Ah, it's no good. I'm sorry. This is all my failing. I failed."
    mc "But I can't give up."
    mc "I can't sink into despair."
    mc "I'm afraid that something will happen to Natsuki too."
    mc "Maybe it already has."
    mc "I've got to go find her!{w} And protect her!"
    jump inform_natsuki


label visit_sayoris_house:
    stop music
    scene bg house with wipeleft_scene
    "As I'm on the way to school, a certain house stands out to me as intensely familiar."
    "I feel like this house has something to do with what's going on."
    "..."
    "I knock on the door."
    mc "Hello? Anyone in there?"
    "No answer."
    "I know this is tresspassing, and I feel crazy, but..."
    "I just {i}know{/i} I'll find answers in this house."
    "I gently open the door."
    scene black with wipeleft
    "Whoa... the feeling of familiarity is incredibly strong now."
    "I feel like I'm in a cathedral or something."
    "I must be close."
    "The feeling guides me to a bedroom, which I enter."
    scene bg sayori_bedroom with wipeleft
    "Holy s[sword]..."
    "It's starting to... aagh..."
    call sayori_flashback
    scene bg sayori_bedroom
    show layer master
    mc "I remember..."
    mc "{i}Sayori{/i}..."
    mc "You hanged yourself out of depression..."
    mc "But what happened after that?"
    mc "Why couldn't I remember you until now?"
    if persistent.mc_know_player:
        call ask_player_to_revive
    pause 3.0
    mc "I know she used to exist."
    mc "But I just still don't know what I'm supposed to do."
    mc "I have the feeling I've failed, like I didn't pick up on the clues fast enough and now something terrible is going to happen no matter what I do."
    mc "Well, there's nothing else to do here."
    mc "I should head to school."
    return

label mc_epiphany:
    mc "Game? File? The f[fword]?"
    mc "Is this world a video game?!?"
    pause 2.0
    mc "S[sword], it makes sense!"
    mc "That's what Monika's epiphany was!"
    mc "You're the player!"
    mc "You've been guiding my actions because I'm the protagonist!"
    mc "Yes, I can feel it now."
    mc "The world feels incredibly fake."
    mc "I wonder how long you've been playing and how much of my memories are a lie..."
    return

label ask_player_to_revive:
    mc "Hey, {i}you{/i} out there..."
    mc "This might be a stupid thing to ask, but..."
    mc "Can you bring Sayori back?"
    mc "I know you have some sort of power over this world."
    if persistent.mc_awareness[10]:
        mc "You've rewinded time before. Can you do it again? Back to before Sayori killed herself?"
    else: # Without flag 10, the only way persistent.mc_know_player could be set is via flag 6
        mc "You've fast-forwarded before... can you... reverse it somehow?"
    mc "Please, answer me!"
    mc "I'm listening as hard as I can!"
    if mc_awareness_total() >= 10:
        menu:
            "Give me a minute.":
                pass
        menu:
            "I'm going to get a copy of her character file from the original game and put it in.":
                pass
        call mc_epiphany
        mc "Whatever, I trust you."
        mc "I'll wait here for you to put the file in."
        label restore_sayori:
        while not check_character_file("sayori"):
            ""
        $ persistent.sayori_revived = True
        mc "... Did you do it?"
        menu:
            "It's... not working for some reason.":
                pass
        mc "I guess the script doesn't check for characters' files constantly."
        mc "Can you load a save at a point where it checks?"
        mc "Or start a new game?"
        mc "I think now that I've had Monika's epiphany, I'll keep my memories."
        mc "Let's do it."
        mc "I'll wait here until you do."
        while True:
            ""
    else:
        pause 4.0
        mc "I don't know if you're trying to answer me, but I can't hear you."
        mc "I'm sorry... I just..."
        mc "I know something is wrong with this world, and I think if I could figure it out I would be able to hear you."
        mc "But I'm not aware enough."
        "I sigh."
    return

label visit_sayoris_house_after_saving_yuri:
    scene bg house with wipeleft_scene
    "Here's the house I remember."
    "I enter the house, and make my way to the bedroom."
    scene bg sayori_bedroom with wipeleft
    "Here it is..."
    "The room where Sayori died."
    "I remember it so vividly now."
    "The way I felt when I walked into this room."
    "It hit me like a punch in the face."
    if persistent.mc_know_player:
        call ask_player_to_revive
    else:
        "..."
        "But I just still don't know what I'm supposed to do!"
        "Okay, I'd better stop wasting time here."
        "Natsuki and Yuri could use my help."
    jump confront_monika_without_sayori
    return

label visit_sayoris_house_after_epiphany:
    scene bg sayori_bedroom with wipeleft_scene
    mc "Here we are."
    mc "I'm waiting for you, player."
    jump restore_sayori

label sayori_flashback:
    $ s_name = "Sayori"
    $ persistent.mc_remember_sayori = True
    show s_cg1
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    play sound "sfx/s_kill_glitch1.ogg"
    s "{cps=150}Ehehe~{nw}{/cps}"
    s "{cps=150}This is so funny.{nw}{/cps}"
    mc "{cps=150}Stop saying all these embarrassing things!{nw}{/cps}"
    play sound "sfx/s_kill_glitch1.ogg"
    scene s_cg2_base1
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    mc "{cps=150}I should find you some ice...{nw}{/cps}"
    s "{cps=150}I'm fine with--looking like a unicorn--{nw}{/cps}"
    scene s_cg3
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    s "{cps=150}This would be so much better if I could just disappear!{nw}{/cps}"
    mc "{cps=150}Sayori, don't say that!{nw}{/cps}"
    s 1bw "{cps=150}It's true, [player]!{nw}{/cps}"
    s "{cps=150}If I wasn't here, then you wouldn't have to waste your sympathy on me!{nw}{/cps}"
    hide noise
    hide vignette
    return
