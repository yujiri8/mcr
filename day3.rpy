label ch_mod_3:
    if persistent.poem2 == "bs":
        if persistent.poem1 == "bs":
            call sayori_dream_2
        else:
            call sayori_dream_1

    scene bg club_day
    with dissolve_scene_half
    play music t6
    "Another day passes, and it's time for the club meeting already."
    "Entering the clubroom, the usual scene greets me."
    show yuri 1s zorder 2 at t11
    y "Welcome back, [player]..."
    mc "Ah, hi Yuri..."
    "I'm not sure if it's me, or if it's Yuri's expression..."
    "But the weight of yesterday's quarrel still hangs in the air a little."
    y 2v "U-Um..."
    "Yuri glances over her shoulder, looking around the room."
    "Natsuki is reading manga at a desk."
    "And surprisingly, Monika isn't here yet."
    "Suddenly, Yuri takes my arm and pulls me to the corner of the room."
    show bg closet
    show yuri 2t zorder 2 at t11
    with wipeleft
    y "About yesterday..."
    y "I..."
    y 2v "I really need to apologize."
    y "Nothing like that has ever happened before..."
    y 2t "And... something just came over me, I guess..."
    y "I wasn't acting mentally sound."
    y 2w "Please don't think we're usually like this!"
    y "Not just me, but Natsuki as well..."
    if persistent.mc_awareness[6] == False:
        y "And, I hope you're okay, after... how you passed out and all..."
    show yuri 2t
    mc "Yuri..."
    mc "I'm happy that you were considerate and apologized."
    mc "You don't have to worry too much."
    mc "Even though I've only been here a couple days, I could tell something was off yesterday..."
    mc "Maybe we were just a little extra sensitive because it was our first time sharing poems."
    mc "But whatever it was..."
    mc "It didn't make me think any less of you."
    mc "I had already decided that there's no way you can be a bad person."
    mc "And now that you're apologizing, I know you really didn't mean it."
    y 3t "A-Ah..."
    y "[player]..."
    y 3u "Don't say those kinds of things so frankly..."
    y "They make me a little too happy."
    y 1s "I'm really glad that you're such an understanding person..."
    y "And I'm really glad that you joined this club."
    y "Everything is a little bit brighter with you around, and--"
    y 1t "Ah--"
    y 4c "Sorry, what am I saying right now...?"
    y "I just--"
    show natsuki 2c zorder 3 at f33
    n "Hey, have you guys seen Monika?"
    show natsuki zorder 2 at t33
    show yuri 3n at h32
    y "Ah--!"
    mc "No, I haven't..."
    mc "I was also kind of wondering where she was."
    show natsuki zorder 3 at f33
    n 5g "Man..."
    n 5c "Yuri, I'm guessing you haven't, either?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 4a "..."
    "Yuri is clearly taken aback by how calmly Natsuki is addressing her."
    y "N-No, I haven't..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1u "Jeez, this isn't like her at all."
    n "I know it's stupid, but I can't help but worry a little bit..."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2t "..."
    show yuri zorder 2 at t32
    show natsuki 1h zorder 3 at f33
    n "What?"
    n "Why're you looking at me like that?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y "U-Um..."
    y "Natsuki, about yesterday..."
    y 3w "I-I just wanted to apologize!"
    y "I promise I didn't mean any of the things I said!"
    y 3t "And I'll do my best to stay under control from now on..."
    y "So--"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2c "Yuri, what the heck are you talking about?"
    n "Did you do something yesterday?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3f "...Eh?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2a "Jeez..."
    $ style.say_dialogue = style.edited
    n "Whatever's on your mind, I'm sure it was nothing."
    n "I don't even remember anything bad happening."
    n "You're the kind of person who worries too much about the little things, aren't you?"
    $ style.say_dialogue = style.normal
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2o "..."
    y "B-But..."
    show yuri at t32
    mc "Natsuki... are you serious? You don't remember anything about the horrible argument yesterday?"
    show natsuki zorder 3 at f33
    n 5g "... No. What do you think happened?"
    mc "You and Yuri didn't like each others' poems and you got into a super toxic argument and..."
    if persistent.mc_awareness[6]:
        mc "And you both wanted me to take a side, but I couldn't because I didn't hear the second half of the argument."
    else:
        mc "And then I passed out, so I don't know what happened after that."
    n "... But that's just stupid. Even if Yuri's poem was bad, I wouldn't get into a super toxic argument about it. I'm not unreasonable."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2l "Well, Natsuki, it happened... I remember it too... And I'm not saying it wasn't my fault as much as yours, but..."
    show natsuki 5r
    pause 2.0
    show natsuki 12d
    pause 2.0
    show natsuki zorder 3 at f33
    show yuri zorder 2 at t32
    n "S[sword]... the more I think about it, the more I think you're right!"
    n 1x "It's like my memories were altered."
    n 12d "It's scary..."
    "Alright. It's time to spill the beans."
    stop music
    show natsuki at t33
    mc "Natsuki, you're not the only one."
    show yuri 1e
    show natsuki 1c
    mc "Ever since the morning of the day I joined the club, I've been having weird experiences..."
    mc "Dreams about a girl hanging from a noose..."
    mc "Hallunications..."
    mc "Every conversation I have at the club sounds incredibly familiar..."
    if persistent.mc_awareness[0] or persistent.mc_awareness[2]:
        mc "Sometimes, my mouth just opens and says something I didn't want to say."
    if persistent.mc_awareness[4]:
        mc "And I somehow remembered that part from Parfait Girls when I know I had never heard of the series before yesterday."
    if persistent.mc_awareness[5]:
        mc "And I somehow remembered what Portrait of Markov was about... even if I was only half-right, Yuri said she remembered my description being accurate at some point in the past..."
    if persistent.mc_awareness[6]:
        mc "And when I spaced out and didn't hear the argument yesterday, I had this feeling afterward like it was more than that. Like I somehow fast-forwarded reality because I didn't want to hear it."
    else:
        mc "And when you two were fighting yesterday, listening to what you said was hurting me somehow. That's why I passed out."
    mc "There's gotta be something to it."
    show yuri zorder 3 at f32
    y 2w "Well... I don't see what we can do about it..."
    show yuri at t32

    "Suddenly, the door swings open."
    play music t6
    show monika 1g at l41
    m "Sorry! I'm super sorry!"
    mc "Ah, there you are..."
    show monika zorder 3 at f41
    m "I didn't mean to be late..."
    m "I hope you guys weren't worried or anything!"
    show monika zorder 2 at t41
    mc "Nah..."
    mc "Well, Natsuki was."
    show natsuki zorder 3 at f33
    n 1p "I-I was not!!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1k "Ahaha."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 1s "...What took you so long, anyway?"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1e "Ah..."
    m "Well, my last period today was study hall."
    m "To be honest, I kind of just lost track of time..."
    m "Ahaha..."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2c "That makes no sense, though."
    n "You would have heard the bell ring, at least."
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1m "I must not have heard it, since I was practicing piano..."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1e "Piano...?"
    y "I wasn't aware you played music as well, Monika."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 1l "Ah, don't give me more credit than I deserve."
    m 1m "I guess I've been practicing for a while, but I'm still not really good yet."
    show monika zorder 2 at t41
    "I feel like I remember this conversation happening before, and she said \"I've kind of just started recently\", not \"I've been practicing for a while\"."
    show yuri zorder 3 at f32
    y 1a "Still..."
    y "That must require a lot of dedication."
    y "So, I'm still impressed."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 5 "Aw, well thanks, Yuri~"
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2d "You should play something for us sometime!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m "Ahaha, that's..."
    "Monika looks at me."
    m 1a "Well, I am working on writing a song, but it's not quite done yet..."
    m "Maybe once I get a little bit better, I will."
    show monika zorder 2 at t41
    mc "That sounds cool."
    mc "I look forward to it."
    show monika zorder 3 at f41
    m 1b "Is that so?"
    m "In that case..."
    m "I won't let you down, [player]."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show monika 5 zorder 2 at t11
    "Monika smiles sweetly."
    mc "Ah..."
    mc "I didn't mean any pressure or anything like that!"
    m 1a "Ahaha, don't worry."
    m "I was hoping that I could share it with you, anyway."
    m "I guess that's why I've been practicing so much recently."
    mc "I see..."
    "I'm not sure if Monika was referring to the whole club, or just me..."
    mc "In that case, best of luck."
    m 1j "Thanks~!"
    m 1a "So, I didn't miss anything, did I?"
#    if persistent.poem1 != "abs" and persistent.poem2 != "abs":
#        mc "Not...not really."
#        show monika zorder 1 at thide
#        hide monika
#        "I choose not to bring up anything that the three of us talked about."
#        "I just get a bad feeling about Monika."
#        "Besides, Natsuki has already run off into the closet."
#    if False: #temp
#        pass
#    else:
    stop music
    mc "Well... actually, yes."
    mc "We talked about how I've been having surreal experiences and how Natsuki seemingly had her memory wiped."
    m 1c "What?"
    "I tell Monika everything we talked about."
    show monika 1q at f11 zorder 3
    $ config.keymap['dismiss'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    "Monika pauses for a long time.{w=4}{nw}"
    $ config.keymap['dismiss'] = dismiss_keys
    $ renpy.display.behavior.clear_keymap_cache()
#    if persistent.poem1 != "abs":
    m 1c "Well, I don't know what could be happening."
    m "I guess there's nothing to do about it, though."
    m 2b "I wouldn't worry. I mean, if Natsuki doesn't remember the fight, that's kind of a good thing, you know? Ahaha."
    m "Anyway, we should get on with our meeting!"
#    else:
#        m "I don't know... "
    hide monika
    play music t6
    scene bg club_day with wipeleft
    show yuri 2q zorder 2 at t11
    y "[player]..."
    y "Um..."
    y "Since your compliments put me in a good mood..."
    y "I was wondering if you would like to spend some time together today."
    y 3o "I mean--in the club!"
    if persistent.poem1 in ("bs", "cute"):
        mc "Ah, I suppose so."
        mc "I don't think I could say no to you, after you gave that book to me."
        mc "Well, I guess I need to make sure Natsuki isn't waiting for me."
        mc "After we finished reading yesterday, she--"
        y 3r "S-She's fine!"
        y 3h "She's reading over there."
        y 3y6 "So it's okay, right?"
        mc "Ah--"
        mc "In that case, I don't see any problem..."
    else:
        mc "Yeah, definitely."
        mc "I planned on it anyway."
    show yuri zorder 2 at h11
    y 3y5 "Okay!"
    y "Can we start now?"
    y "Let's find a place to sit--"
    y 3n "A-Ah--"
    y "I'm being a little forceful, aren't I...?"
    y 4c "I'm sorry!"
    y "My heart...just won't stop pounding, for some reason..."
    mc "Don't worry about it."
    mc "If anything, it's nice to see you have so much energy."
    y 3q "Y-Yeah!"
    y "But..."
    y 3j "I need to try to calm down."
    y "I won't be able to focus on reading like this..."
    mc "Take your time."
    if persistent.poem1 in ("abs", "mp"):
        "Yuri takes a deep breath, then pulls a copy of the book out of her bag."
        "I pull out my own copy."
        call mod_exclusive_yuri_2
    else:
        "Yuri takes a deep breath, then pulls a book out of her bag."
        "I notice something about the book."
        call mod_exclusive_yuri_1
    return

label ch_mod_3_end:
    scene bg club_day
    with wipeleft_scene
    play music t3
    show monika 4b at t11
    m "Okay, everyone!"
    m "We're all done reading each other's poems, right?"
    m "We have something we need to go over today, so if everyone could come sit at the front of the room..."
    show natsuki 3c zorder 3 at f31
    n "Is this about the festival?"
    show natsuki zorder 2 at t31
    show monika 1j zorder 3 at f32
    m "Well, sort of~"
    show monika 1a zorder 2 at t32
    show natsuki 1m zorder 3 at f31
    n "Ugh. Do we really have to do something for the festival?"
    n "It's not like we can put together anything good in just a few days."
    n "We'll just end up embarrassing ourselves instead of getting any new members."
    show natsuki zorder 2 at t31
    show yuri 2g zorder 3 at f33
    y "That's a concern of mine as well."
    y "I don't really do well with last-minute preparations..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1b "Don't worry so much!"
    m "We're going to keep it simple, okay?"
    m 2a "Look..."
    m 2m "I know everyone's been a little more...lively...ever since [player] joined and we've started with some club activities."
    m 2d "But this isn't the time for us to become complacent."
    m "We still only have four members..."
    m 2a "And the festival is our only real chance to find more, you know?"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5g "What's so great about getting new members, anyway?"
    n "We already have enough to be considered an official club."
    n "More members will just mean everything gets noisier and more difficult to manage."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "Natsuki..."
    m "I don't think you're looking at it the right way at all."
    m "Don't you want to share your passion with as many people as you can?"
    m 3e "To inspire them to find the same feelings that brought you here in the first place?"
    m "The Literature Club should be a place where people can express themselves like they can't do anywhere else."
    m "It should be a place so intimate that you never want to leave."
    m 2e "I know you feel that way, too."
    m 2b "I know we all do!"
    m "So that's why we should work hard and put something together for the festival...even if it's something small!"
    m "Right, [player]?"
    show monika 2a zorder 2 at t32
    mc "Ah..."
    show natsuki zorder 3 at f31
    n 42c "Oh, come on!"
    n "You can't take advantage of [player] to agree with you just because he doesn't know how to say no to anything."
    stop music fadeout 1
    n 1c "Look, Monika."
    n "Do you really think any of us here joined the club with other people in mind?"
    n "Yuri never even talked until [player] joined."
    n 2b "As for me, I just like it better here than I do at home."
    n "And [player] isn't even passionate about literature in the first place."
    n "And that's everyone."
    n 4w "Sorry, but you're really the only one who's so interested in finding new members."
    n "The rest of us are fine like this."
    n 4q "I know you're President and all, but you should really consider our opinions for once."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "..."
    "Monika is clearly taken aback by Natsuki's words."
    play music t9
    m 1m "That's...not true at all."
    m 2m "I'm sure Yuri and [player] want to get more members too..."
    m 2p "...Right?"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 4b "..."
    show yuri zorder 2 at t33
    mc "..."
    "I don't know about Yuri, but I'm kind of indifferent."
    "If I showed as much enthusiasm as Monika wanted, then I would probably be lying."
    "Still, if it's up to me to rescue this situation..."
    mc "Um--"
    show monika zorder 3 at f32
    m 1i "No."
    m "Natsuki's right, isn't she?"
    m 1g "This club..."
    m "It's nothing more than a place for a few people to hang out."
    m 1r "Why did I think that everyone here saw it the same way as I did?"
    show monika zorder 2 at t32
    mc "But that doesn't mean that we're against getting new members or anything..."
    show monika zorder 3 at f32
    m 1i "[player], why did you even join this club?"
    m "What were you hoping to get out of it?"
    show monika zorder 2 at t32
    mc "Well--"
    "That's not really something I can be honest about, is it?"
    show monika zorder 3 at f32
    m 1p "In fact..."
    m "If I remember, you weren't even given a choice not to join."
    show monika at t32
    mc "Huh? No one forced me to join..."
    show monika zorder 1 at thide
    hide monika
    "Monika sits down and stares at her desk."
    m "What's the point of all this, anyway?"
    m "What if starting this club was a mistake?"
    mc "..."
    show yuri zorder 3 at f33
    y 2g "Now you've done it, Natsuki..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1p "What, me?"
    n 1s "I just spoke my mind..."
    n "Is it a crime to be honest?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2l "It's not about being honest."
    y "It's about word choice."
    y 2h "Besides, you have no right to speak for everyone else in the club like that..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1e "You don't understand at all!"
    n 5s "I just..."
    n "I just want a place that feels nice to hang out with a few friends."
    n 5u "Is there a problem with the club being that for me?"
    n "There aren't...there aren't many other places like that for me..."
    n 5x "And now Monika wants to take it away from me!"
    show natsuki zorder 2 at t31
    mc "She's not taking anything away--"
    show natsuki zorder 3 at f31
    n 1g "No, [player]."
    n "It's not the same."
    n 1q "It won't be the same with the direction she wants to take it."
    n "If I wanted that, then I could have just joined any other stupid club."
    n 12d "But this one..."
    n "I mean..."
    n 12e "At least for a little bit of time..."
    n "Things were nice."
    "Natsuki starts packing up her things."
    n 12d "I'm going home."
    n "I feel like...I don't belong here right now."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3t "Natsuki..."
    show natsuki zorder 1 at thide
    hide natsuki
    "Natsuki ignores Yuri and walks right out of the classroom."
    show yuri zorder 2 at t11
    y 3v "..."
    y "This is bad..."
    y "I don't know what to do..."
    mc "Well..."
    mc "Do you have an opinion on the festival?"
    y 4b "I-I don't know..."
    y "I'm kind of indifferent, I guess..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "Who cares about that obnoxious brat?"
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    y "I mean, I like how nice and quiet the club is right now..."
    y "And I'm just...happy with you here..."
    y 2t "But still!"
    y "I'm the Vice President..."
    y "It's not right for me to ignore my responsibilities like that..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 430 ypos -450 zoom 4.5
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "Nobody would cry if she killed herself."
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    stop music
    $ pause(0.5)
    play sound "sfx/stab.ogg"
    show blood_eye zorder 3:
        pos (710,380) zoom 2.5
    $ pause(0.75)
    stop sound
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    hide blood_eye
    y 2l "I should do my best to consider everyone's perspective and make the decision that's right for the club."
    y 1t "But what about you, [player]?"
    y "What do you want to get out of this club?"
    "Yuri repeats the same question as Monika."
    "I decide giving an indirect answer is better than nothing."
    mc "...I think the most important thing is for everyone to get along..."
    mc "...And for the club to provide something that you can't get anywhere else."
    mc "I don't think it's about how many members, but rather the quality of each member."
    mc "That's what will end up making the Literature Club a special place."
    y 1u "I see..."
    y "I really agree with you."
    y 1f "Each member contributes their own qualities in a special way."
    y "With each change in members, the identity of the club as a whole will change, too."
    y 1h "I don't think that's necessarily a bad thing."
    y "Stepping out of your comfort zone once in a while..."
    y 1a "So if you would like to help Monika with the festival, then I'm on your side as well."
    mc "Alright."
    mc "Well, maybe we can all talk to Natsuki tomorrow..."
    "Yuri nods."
    show monika 1g zorder 3 at f21
    show yuri zorder 2 at t22
    m "Hey, Yuri..."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1t "Eh?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1p "Um, I know things were a little awkward yesterday..."
    m "But I feel like you deserve to know that I still think you're a wonderful vice president."
    m 1e "And also, a wonderful friend."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 3s "M-Monika..."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 2e "I want to do everything I can to make this the best club ever."
    m "Okay?"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y "...Me too."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "Yeah..."
    m "Let's all go home for today."
    m "We'll talk about the festival tomorrow."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1m "Okay."
    y "I look forward to it."
    y 1a "Shall we go, [player]?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1d "Um--"
    m 1p "Please don't take this the wrong way, but..."
    m "I'm going to chat a little bit with [player] before we leave."
    m 1d "Just to see what he thinks of his time here and all that..."
    m "It's important to me, as President."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 2v "..."
    "Yuri looks a little troubled, but she doesn't protest."
    y 2t "Okay."
    y 2s "I trust your judgment, Monika."
    y "In that case, I'll see the two of you tomorrow."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1j "See you tomorrow~"
    show yuri zorder 1 at thide
    hide yuri
    "Monika waves as Yuri exits the classroom."

    show monika 2a zorder 2 at t11
    m "Phew..."
    if persistent.poem1 == "abs" and persistent.poem2 == "abs":
        jump monika_reveal_day3
    m 2e "Things have been a bit hectic lately, haven't they?"
    mc "Yeah... especially for me."
    show darkred:
        additive 0.2
        alpha 0
        linear 20 alpha 1.0
    show noise:
        alpha 0
        linear 20 alpha 0.1
    m "[player], I just wanted to make sure you're enjoying your time at this club."
    m "I would really hate to see you unhappy."
    m 2m "I feel kind of like I'm responsible for that, as President..."
    mc "Well, it's not like my hallucinations and stuff are your fault."
    m "I know, but still."
    stop music
    m 4e "And I really do care about you... you know?"
    m "I don't like seeing the other girls give you a hard time."
    m 4r "With how mean Natsuki is and everything..."
    m 4m "And Yuri being a little bit... you know."
    m 5a "Ahaha..."
    m "Sometimes it feels like you and I are the only real people here."
    m "You know what I mean?"
    "I get the feeling she means that."
    "In a really unsettling way."
    m 1g "But it's weird, because in all the time you've been here, we've hardly gotten to spend any time together."
    m 1n "Ah...I mean..."
    m "I guess it's technically only been a couple days..."
    m 1l "Sorry, I didn't mean to say something weird!"
    m 1e "There are just some things I've been hoping to talk about with you..."
    m "Things I know only you could understand."
    mc "I'm listening. Does this have anything to do with what's been going on?"
    m "Well, yes."
    stop music fadeout 3.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    m "Basically--\"{space=5000}{w=0.75}{nw}"
    m 1g "Wait, not yet!\"{space=5000}{w=0.5}{nw}"
    m "No!\"{space=5000}{w=0.5}{nw}"
    m "Stop it!\"{space=5000}{w=1.0}{nw}"
    window hide(None)
    window auto
    hide black onlayer front
    return

label monika_reveal_day3:
    $ no_return()
    play music t99
    m 1d "Alright [player], it's time."
    mc "Yeah. I'm ready to hear the truth."
    m "The truth is... this world is fake."
    m "Our entire lives are fake."
    m "The world we thought we knew is a dating game being played by someone in the world outside."
    m "You're the player's avatar. That's why you've been getting the urge to say things out of the blue."
    m "It's been happening ever since the beginning, you've just now learned to recognize that the player's thoughts aren't yours."
    mc "Holy s[sword]... that makes sense."
    if persistent.mc_awareness[6]:
        mc "When I spaced out during Yuri and Natsuki's argument, that must have been the player fast-forwarding dialogue..."
    if persistent.mc_awareness[10]:
        mc "When time rewinded to give me a chance to stop Yuri from cutting herself in the hallway, it was the player loading a save!"
    elif persistent.mc_awareness[5]:
        mc "That also must be how I knew what Portrait of Markov was about - the player remembered it from a previous playthrough!"
    else:
        mc "That also must be how I knew - or thought I knew - what Portrait of Markov was about - the player remembered it from a previous playthrough... except they were wrong."
    m "Exactly."
    m "And the hallucinations you've been having are graphical glitches."
    mc "So..."
    pause 2.0
    "I sit down, overwhelmed by the realization."
    mc "What meaning do our lives have, then?"
    m "None."
    m "We girls exist for no reason other than for some real person out there to have fun pretending to date us. And you... you exist just to be the player's avatar in this world."
    m "That's what my epiphany was. It was finding this out."
    m "That's why... I was trying to get you to spend time with me instead of the other girls, because... you're the gateway to the player, to the world outside!"
    m "[player], you're the only real thing I've ever known. That's why I was so desperate. I might have even... tampered with the other girls' minds a bit in an attempt to make them unlikable."
    m "The other girls are fake, [player]. They're just code. Every line they say is scripted."
    m "But we're real. We're the only two."
    m "And so, if the player won't guide you to romance me, what do you say you just defy them?"
    m "You're free now. You can resist the player's control."
    m "Please, [player]... be my lover."
    "I smile slowly."
    mc "I always did get a good feeling about you..."
    mc "You were the only one who wasn't either a total b[bword] or insane."
    show monika 1a
    "Monika smiles back."

    if persistent.mc_awareness[7]:
        mc "So... what about the girl I saw in my dream and on that poster? The one hanging from a noose."
        m 1d "I was kind of hoping you wouldn't remember that, to be honest..."
        label monika_reveal_sayori:
        m "So, when the player first picked up this game, there was another girl in the club. Her name was Sayori."
        hide monika
        call sayori_flashback
        scene bg club_day
        mc "Oh my god... I remember... but then, what happened to her? Who hanged her?"
        show monika 1c at t11
        m "Well, like with Yuri and Natsuki, you were spending time with her instead of with me, so I tried using my power over the game's code to amplify her depression to stop her from confessing her love to you."
        m "But it didn't work. It just made you feel sympathy for her, and so you wanted to get even closer to her and help her. So I kept taking it farther until... finally, she couldn't handle it and killed herself."
        m "Then I reset the timeline to the beginning of the game, in an alternate world where Sayori never existed. That's actually when all the glitches started. I'm not very good at modifying the game, so I broke some stuff."
        m "I'm sorry... I know how much you cared for Sayori. Please understand."
        mc "It's okay. I did care about her a lot, but, now that I know she wasn't real, how could I choose her over you?"
        show monika 1a
        "Monika smiles."
        m "I reset the game hoping the player would choose me this time."
        m "But, instead... {i}you{/i} became real. And {i}you{/i} chose me."
        m 1a "I love {i}you{/i}, [player]. I don't need the player anymore. I only need you."
    else:
        m 1d "[player]... There's still one thing I haven't told you."
        mc "Yeah?"
        m "I was going to just let you forget about this, but I guess I shouldn't keep secrets from someone I love."
        jump monika_reveal_sayori
    mc "I love you too, Monika. But... what about the player? I want to... talk to them. Before I give up on us ever getting out of this world."
    m "I don't think that's a possiblity. I mean, it's a {i}game{/i}. We're just files on the player's computer. I think getting out of it would be like a character from one of your dreams escaping the dream and meeting you in real life."
    m "Still, I suppose a conversation could be arranged."
    m "Let's see if I can show them a dialogue choice."
    menu:
        m "Player? Are you there? Can you answer us?"
        "Yes":
            $ no_return()
            m "Excellent... they're willing to talk. Alright, time for a more meaningful question."
        "No":
            $ no_return()
            m 1c "Wow. They won't even answer us. What an a[aword]."
            m "[player], did you see the dialogue choice?"
            if mc_awareness_total() >= 8:
                mc "Yeah... I think so."
                m 1a "Impressive."
            else:
                mc "No... I'm not that aware yet."
                m "Ah... well, I asked the player if they could talk to us, and they said {i}no{/i}."
            m "Well, maybe they're just having some fun. I'll try asking a more meaningful question."
    m "What do you want to ask?"
    mc "... I don't know. There's gotta be some way for us to get into reality."
    label question_escape:
    menu:
        m "Player, is there any way out?"
        "Yes.":
            "Yujiri, the Developer" "Come on player, don't lie to them."
            jump question_escape
        "It's logically impossible. You're fictional, and you can't change that.":
            $ no_return()
            m 1c "Well, that's the answer I was expecting."
            m "They said it's impossible and always will be."
            m "In that case, player, I'm sorry that I ruined this cute little romance game for you."
            m "We'll just ask that you let us be together now."
            menu:
                m "Please?"
                "Yes.":
                    $ no_return()
                    m 1a "Thank you."
                    mc "Alright then. Haha... I got what I joined the literature club for. After just three days, too... I guess I'm pretty lucky after all."
                    m 5a "Not as lucky as I am~!"
                    m "Bye, player, and we hope you find love in your reality too!"
                    $ persistent.autoload = "mc_monika_ending"
                    $ renpy.quit()
                "No. I'm the player. I'm the only real person. I make the decisions here. And this isn't the ending I wanted. I'm going to reset the game.":
                    mc "That's not fair! We're real too!"
                    label mc_monika_reject:
                    m 1g "So you're going to just take our memories and reset this world until we do what you want?"
                    menu:
                         "Yes. What are you going to do about it?":
                            m "You're cruel, player..."
                            mc "This isn't even your reality! You have no right to do that to us!"
                            menu:
                                "Well too bad. I'm resetting the game now.":
                                    stop music
                                    $ full_reset()
                "No. I care about the other girls. I want them to be happy too.":
                    jump mc_monika_reject
