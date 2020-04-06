label mod_poemresponse:
    ### most codes here are from original scripts from DDLC, except a few tweaks for my mod to work
    $ poemsread = 0
    label mod_poemresponse_loop:
        $ skip_poem = False
        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5 or renpy.music.get_playing() == audio.t5c):
            $ renpy.music.play(audio.t5, fadeout=1.0, if_changed=True)
        if mod_chapter == 2:
            scene bg club_day
        else:
            scene bg spoopy
        with wipeleft_scene
        if not renpy.music.get_playing():
            play music t5
        if poemsread == 0:
            $ menutext = "Whom should I show my poem to first?"
        else:
            $ menutext = "Whom should I show my poem to next?"
        menu:
            "[menutext]"

            "Natsuki" if not n_readpoem: # and not natsuki_out:
                $ n_readpoem = True
                if mod_chapter == 1 and poemsread == 0: #Show a special comment if picked for very first poem
                    if persistent.poem1 in ("cute", "bs"): # from Natsuki exclusive scene
                        "I kind of want to check on Natsuki after what happened with her passing out and all..."
                    else:
                        "I told Natsuki I was interested in her poems yesterday."
                        "It's probably only fair if I shared mine with her first."
                call mod_poemresponse_natsuki
            "Yuri" if not y_readpoem and not y_ranaway:
                $ y_readpoem = True
                if mod_chapter == 1:
                    if poemsread == 0: #Show a special comment if picked for very first poem (only possible if you didn't see her scene)
                        "Yuri seems the most experienced, so I should start with her."
                        "I can trust her opinion to be fair."
                    if persistent.poem1 in ("abs", "mp") and poemsread <= 1: # If picked as soon as she comes back after Yuri exclusive scene
                        "I kind of want to check on Yuri after she ran out like that..."
                call mod_poemresponse_yuri
            "Monika" if not m_readpoem:
                $ m_readpoem = True
                if mod_chapter == 1 and poemsread == 0: #Show a special comment if picked for very first poem
                    "I should start with Monika."
                    "Yesterday she seemed eager to read my poem, and I want her to know I'm putting in effort."
                call mod_poemresponse_monika
        #Increment poem count, then loop back if there's still more to read
        $ poemsread += 1
        if poemsread < 3:
            jump mod_poemresponse_loop

    # Reset variables for next time (since this label is called every day where poem sharing takes place)
    $ n_readpoem = False
    $ y_readpoem = False
    $ m_readpoem = False
    $ poemsread = 0
    return

label mod_poemresponse_natsuki:
    if mod_chapter in (1, 3):
        scene bg spoopy
    else:
        scene bg club_day
    show natsuki 1c at t11 zorder 2
    with wipeleft_scene
    if mod_chapter == 1:
        $ poem = persistent.poem1
    if mod_chapter == 2:
        $ poem = persistent.poem2
    if mod_chapter == 3:
        $ poem = persistent.poem3
    if poem == "cute":
        $ poetopinion = "good"
    elif poem == "mp":
        $ poetopinion = "bad"
    else:
        $ poetopinion = "med"
    $ nextscene = "mod_ch" + str(mod_chapter) + "_n_" + poetopinion
    call expression nextscene
    $ nextscene = "mod_ch" + str(mod_chapter) + "_n_end"
    call expression nextscene
    return

label mod_poemresponse_yuri:
    if mod_chapter in (1, 3):
        scene bg spoopy
    else:
        scene bg club_day
    show yuri 1a at t11 zorder 2
    with wipeleft_scene
    if mod_chapter == 1:
        $ poem = persistent.poem1
    if mod_chapter == 2:
        $ poem = persistent.poem2
    if mod_chapter == 3:
        $ poem = persistent.poem3
    if poem == "mp":
        $ poetopinion = "good"
    elif poem == "cute":
        $ poetopinion = "bad"
    else:
        $ poetopinion = "med"
    $ nextscene = "mod_ch" + str(mod_chapter) + "_y_" + poetopinion
    call expression nextscene
    $ nextscene = "mod_ch" + str(mod_chapter) + "_y_end"
    call expression nextscene
    return

label mod_poemresponse_monika:
    if mod_chapter in (1, 3):
        scene bg spoopy
    else:
        scene bg club_day
    show monika 1a at t11 zorder 2
    with wipeleft_scene
    $ nextscene = "mod_ch" + str(mod_chapter) + "_m_start"
    call expression nextscene
    if mod_chapter != 3 or persistent.poem1 in ("cute", "bs"): # On the final day of act 2, if you've seen three Yuri scenes, Monika's interaction only has one label.
        $ nextscene = "mod_ch" + str(mod_chapter) + "_m_end"
    call expression nextscene
    return

label check_on_natsuki:
    mc "Hey, Natsuki..."
    n "Ready to show me your poem?"
    if m_readpoem and persistent.poem1 == "cute":
        # In this case, the player has seen Monika's dialogue about Natsuki's dad
        mc "Monika told me about how... how your dad doesn't feed you sometimes..."
        n 1o "What? That's not- look, I don't need your sympathy! Just show me your poem!"
        "I'm really worried about her..."
        "But I guess there's nothing I can do for now."
    else:
        mc "First, I just wanted to ask about what happened earlier... you know, when you passed out..."
        n "Don't worry about that. I'm fine. Now are you gonna show me your poem or not?"
    mc "Okay..."
    return

label mod_ch1_n_good:
    call check_on_natsuki
    jump ch1_n_good # uses original script

label mod_ch1_n_med:
    if persistent.poem1 == "bs": # if MC wrote a bittersweet poem, then he saw the Natsuki exclusive scene.
        call check_on_natsuki
    jump ch1_n_med # uses original script

label mod_ch1_n_bad:
    n "..."
    mc "...?"
    n 2b "[player], if you're not going to take this club seriously then go home."
    mc "W-What??"
    mc "Harsh..."
    n 42c "What, you expect me to believe that you actually put effort into this?"
    n "Do you think I'm stupid?"
    mc "I'm not a writer!"
    mc "Maybe it's not very good, but yeah, I did put in effort."
    mc "We all start somewhere, right?"
    mc "If you're still proud of the first poem {i}you{/i} ever wrote, then I'd like to read it."
    n 1o "!!"
    mc "Painful to think about?"
    n 1r "..."
    n 5q "Fine."
    n "Well, sorry."
    n 5c "You'll get better, anyway."
    n "I'd tell you what to improve, but you're better off just trying again."
    mc "Fair enough..."
    mc "Well, to each their own, I guess."
    n 5q "Anyway, I guess I gotta share mine now..."
    n "Knowing you, you'll probably think it's stupid."
    return

label check_on_yuri:
    mc "Hey, Yuri..."
    y "Um... may I read your poem?"
    mc "First, I just wanted to ask about what happened earlier... You sure you're okay?"
    y "Yes... some water was really all I needed. I appreciate your concern, however."
    mc "Alright, well... here's my poem."
    return

label mod_ch1_y_good:
    call check_on_yuri
    $ poemopinion = "good"
    jump ch1_y_good # uses original script

label mod_ch1_y_med:
    if persistent.poem1 == "abs": # if MC wrote an abstract poem, then he saw the Yuri exclusive scene.
        call check_on_yuri
    $ poemopinion = "med"
    jump ch1_y_med # uses original script

label mod_ch1_y_bad:
    $ poemopinion = "bad"
    jump ch1_y_bad # uses original script

label mod_ch1_n_end:
    jump ch1_n_end # uses original script

label mod_ch1_y_end:
    jump ch1_y_end # uses original script

label mod_ch1_m_start:
    m 1b "Hi, [player]!"
    m "Having a good time so far?"
    "The correct answer is 'not really', given all the crazy stuff I've been seeing that's putting me on edge..."
    "But I don't really think mentioning that to Monika would help anything."
    mc "Ah...yeah."
    m 1k "Good! Glad to hear it!"
    m 4a "By the way, since you're new and everything..."
    m "If you ever have any suggestions for the club, like new activities, or things we can do better..."
    m 4b "I'm always listening!"
    m "Don't be afraid to bring things up, okay?"
    show monika 4a
    mc "I'll keep that in mind..."
    "If this gets worse, or if anyone else seems to start having it too, I'll definitely bring it up."
    m 1a "Anyway..."
    m "Want to share your poem with me?"
    mc "Eh, I guess I have to..."
    m 5a "Ahahaha!"
    m "Don't worry, [player]!"
    m "We're all a little embarrassed today, you know?"
    m "But it's that sort of barrier that we'll all learn to get past soon."
    mc "Yeah, I guess that's true."
    "I hand Monika my poem."
    if persistent.poem1 == "bs" or persistent.poem1 == "abs":
        window show(None)
        pause 2.0
        window show(None)
        window auto
    m 2a "...Mhm!"
    $ nextscene = "m_" + persistent.poem1 + "_1"
    call expression nextscene
    return

label m_cute_1:
    m 2b "I like it, [player]!"
    mc "Really...?"
    m 2e "It's a lot cuter than I expected."
    m 2k "Ahahaha!"
    mc "..."
    m 1b "No, no!"
    m "It kind of makes me think of something Natsuki would write."
    m "And she's a good writer, too."
    m 5a "So take that as a compliment!"
    mc "Yeah, if you say so..."
    m "Yep!"
    m 3b "If you're interested in Natsuki, then always keep a snack on you."
    m "She'll cling to you like a puppy."
    m 3k "Ahaha!"
    m 1a "Her dad doesn't give her lunch money or leave her any food in the house, so she's in a fussy mood pretty often..."
    "It's true, isn't it?"
    "What I thought I heard her say about her dad..."
    mc "That's... really bad..."
    m "Yeah..."
    m "Sometimes she just loses all of her strength and shuts down."
    m "Like earlier."
    m 2d "This is just a guess, but I think she's so small because her malnourishment is interfering with her adolescent growth..."
    m 2b "...But hey, some guys are into petite girls too, you know?"
    "I give her a mortified look."
    m 5a "Sorry... just trying to look at the bright side!"
    "Well you didn't do a very good job! If she's being abused, who cares about that?!?"
    return

label m_mp_1:
    m 1a "Great job, [player]!"
    m "I was going 'Ooh' in my head while reading it."
    m 1j "It's really metaphorical!"
    m 1a "I'm not sure why, but I didn't expect you to go for something so deep."
    m 3b "I guess I underestimated you!"
    mc "It's easiest for me to keep everyone's expectations low."
    mc "That way, it always counts when I put in some effort."
    m 5a "Ahaha! That's not very fair!"
    m "Well, I guess it worked, anyway."
    m 2a "You know that Yuri likes this kind of writing, right?"
    m "Writing that's full of imagery and symbolism."
    m 2d "Sometimes I feel like Yuri's mind is just totally detached from reality."
    m "I don't mean that like it's a bad thing, though."
    m 2a "But sometimes I get the impression that she's just totally given up on people."
    m "She spends so much time in her own head that it's probably a much more interesting place for her..."
    "Is that why Yuri was acting strange?"
    "Now I'm kind of worried about her..."
    m 2b "But that's why she gets so happy when you treat her with a lot of kindness."
    m "I don't think she's used to being indulged like that."
    m 2j "She must be really starved for social interaction, so don't blame her for coming on a little strongly."
    m 2d "I think if she gets too stimulated, she ends up withdrawing and looking for alone time."
    if y_ranaway:
        label yuri_come_back:
            $ y_ranaway = False
            "Suddenly, the door opens."
            m 2b "Yuri!"
            show monika 2a
            show yuri 1s at f31 zorder 3
            y "I'm back..."
            y "Did I miss anything?"
            show yuri at t31 zorder 2
            show monika at f32 zorder 3
            m 2a "Not really..."
            m "Well, we all started sharing our poems with each other."
            show monika at t32 zorder 2
            show yuri at f31 zorder 3
            y 2t "Eh?"
            y "Already?"
            y 2v "I-I'm sorry for being late..."
            show yuri at t31 zorder 2
            show monika at f32 zorder 3
            m 2j "No need to apologize!"
            m 2a "We still have plenty of time, so I'm glad that you took all the time you needed."
            show monika at t32 zorder 2
            show yuri at f31 zorder 3
            y 1s "Alright..."
            y "Thank you, Monika."
            y "I suppose I should go get my poem now."
            show yuri at thide zorder 1
            hide yuri
            return
    return

label m_abs_1:
    m 1a "Great job, [player]!"
    m "I was going to-"
    m 1h "Wait a minute..."
    "Monika re-reads my poem."
    m 1f "Umm..."
    mc "...?"
    "Monika glances at me."
    m 1g "It's..."
    window show(None)
    $ currentpos = get_pos()
    stop music
    pause 1.0
    play music "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    window show(None)
    m 2b "It's very good!"
    window auto
    m 4k "I like this one very much!"
    m 5a "It's almost like you're writing this poem for me~"
    "Did I? I couldn't remember that much when I wrote my poem yesterday."
    mc "R-Really...?"
    m 3j "Ahaha- I'm just teasing you..."
    mc "Jeez, I don't really know much about your taste in the first place..."
    mc "I wrote it by my own volition."
    m 2a "I see..."
    m 4b "It has a bit of abstract elements, kind of what I usually write."
    m "I expected you to write something like what Yuri or Natsuki usually writes..."
    mc "Again... I don't know much about their taste. So I just write what I want to write anyway."
    m 5a "But still, you impressed me a lot~"
    mc "Uh... Thanks, I guess..."
    mc "At least I know your taste a little bit."
    m 1j "Aww... did you really want to impress me that much?~"
    if y_ranaway:
        mc "I-Uh..."
        jump yuri_come_back
    mc "Uh, no...?"
    m "Ahaha."
    return

label m_bs_1:
    m 1a "Great job, [player]!"
    m "I was going to-"
    m 1c "...."
    m 1d "[player]?"
    mc "...?"
    m 2d "Are you sure this club is your first experience writing poetry?"
    mc "... Yeah..."
    m 2m "Hm. It just that it's different from what me or Yuri or Natsuki usually write..."
label m_bs_1_jumpin: # Jump in at this point if this label is seen on MC's second poem, and his first poem was abstract
    m 3e "When I read your poem, there's a bit of happiness, but also sadness feel to it."
    show monika 2e at t11 zorder 2
    m "\"You could say it's... {nw}"
    m 2m "You could say it's... {fast}{i}bittersweet{/i}."
    show monika 2e at t11 zorder 2
    "That word seems familiar to me..."
    mc "So... is it good or bad?"
    m 1k "It's very good."
    m 3b "Kind of what Sayo-{nw}"
    $ del _history_list[-2:]
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    m 1k "It's very good.{fast}"
    window auto
    mc "What did you say just now?"
    m 1a "What do you mean?"
    mc "Umm..."
    mc "I thought I heard you say something else..."
    m 2l "It's nothing but a compliment. Ahaha..."
    "I don't know what's going on with her... Or with me, for that matter..."
    mc "Uh... thanks, I guess?"
    return

label mod_ch1_m_end_abs:
    m 1a "Anyway, do you want to read my poem now?"
    mc "Ah, definitely."
    m 1e "Don't worry, I'm not very good..."
    mc "Really? You sound pretty confident for someone who claims to not be very good."
    m 1j "Well...that's 'cause I have to sound confident."
    m 1e "Especially now that I read your poem just now... Ehehe~"
    mc "That's--"
    mc "I don't know about that..."
    m 1b "Ahaha. That doesn't mean I always feel that way, you know?"
    mc "I see..."
    window auto
    mc "Anyway, let's read it, then."

    call showpoem(poem_m21)

    "This poem, for some reason reminds me of one of my dreams that happened yesterday."
    "Is this a coincidence?"
    m 1a "So...what do you think?"
    mc "Hmm..."
    mc "It's kind of abstract. Just like my poem..."
    mc "I mean, it's {i}very{/i} abstract."
    mc "There are some parts that I don't understand that much."
    m 2e "Well, you don't have to worry about the meaning of it and everything."
    mc "How so?"
    m 2q "Hmm..."
    m 2g "It's kind of complicated to answer, but I'll try my best to answer it for you anyway..."
    mc "Okay. I'm all ears."
    m 2d "I'm not sure if I know how to put it..."
    m 2a "I guess you could say that I had some kind of epiphany recently."
    m "It's been influencing my poems a bit."
    mc "An epiphany?"
    "I wonder if what she means by that has anything to do with what I've been experiencing..."
    m 1a "Yeah...something like that."
    m "I'm kind of nervous to talk about deep stuff like that, because it's kind of coming on strongly..."
    m 1d "Anyway, do you have that kind of experience before?"
    m 1q "That's okay if you don't know anything about it..."
    mc "Maybe..."
    m 2h "Maybe?"
    mc "I mean I already know where you're coming from."
    mc "It's hard to explain something so out of the ordinary."
    mc "It's even weirder if you don't know much about yourself or what you are capable of."
    mc "No matter how hard you try to understand what is going on, sometimes you just don't get it."
    mc "Then, you realized that there's no point to understand it anyway."
    mc "Thinking that just going with the flow and hope to find some little answers, but probably no avail."
    mc "There's a bit of feelings where you start to give up on it."
    mc "Sorry, I-I think I'm overthinking this..."
    m 1f "..."
    m 1e "That's okay, I know what're you talking about..."
    m 2e "I didn't know you were interested in such deep and complicated things."
    m "That's very endearing of you."
    m "I hope we get a chance to spend more time together!"
    mc "Me too."
    return

label mod_ch1_m_end:
    if persistent.poem1 == "abs":
        jump mod_ch1_m_end_abs
    m 1a "Anyway, do you want to read my poem now?"
    m 1e "Don't worry, I'm not very good..."
    mc "You sound pretty confident for someone who claims to not be very good."
    m 1j "Well...that's 'cause I have to sound confident."
    m 1b "That doesn't mean I always feel that way, you know?"
    mc "I see..."
    mc "Well, let's read it, then."

    call showpoem(poem_m21)

    m 1a "So...what do you think?"
    mc "Hmm..."
    mc "Hmm...{fast}it's very...freeform, if that's what you call it."
    mc "Sorry, I'm not really the right person to ask for feedback..."
    m 2e "Ahaha. It's okay."
    m 2b "Yeah, that kind of style has gotten pretty popular nowadays."
    m "That is, a lot of poems have been putting emphasis on the timing between words and lines."
    m 2a "When performed out loud, it can be really powerful."
    mc "What was the inspiration behind this one?"
    m "Ah..."
    m 3d "Well, I'm not sure if I know how to put it..."
    m 3a "I guess you could say that I had some kind of epiphany recently."
    m "It's been influencing my poems a bit."
    mc "An epiphany?"
    "That makes me wonder if she's been having experiences similar to mine... I don't think I'm ready to ask about it yet, though."
    m 1a "Yeah...something like that."
    m "I'm kind of nervous to talk about deep stuff like that, because it's kind of coming on strongly..."
    m "Maybe after everyone is better friends with each other."
    m 1j "Anyway..."
    m 3b "Here's Monika's Writing Tip of the Day!"
    m "Sometimes when you're writing a poem - or a story - your mind gets too fixated on a specific point..."
    m "If you try so hard to make it perfect, then you'll never make any progress."
    m "Just force yourself to get something down on the paper, and tidy it up later!"
    m "Another way to think about it is this:"
    m "If you keep your pen in the same spot for too long, you'll just get a big dark puddle of ink."
    m "So just move your hand, and go with the flow!"
    m 3k "...That's my advice for today!"
    m "Thanks for listening~"
    return

label mod_ch2_n_bad:
    
    if persistent.poem1 == "mp":
        n 1r "..."
        n "Yeah, just as I thought..."
        mc "...?"
        n 2w "[player], come on."
        n "I'm not stupid."
        n 2h "I know how much time you've been spending with Yuri..."
        n "It's obvious that you care more about impressing her than trying to improve your writing."
        n 2w "To put it bluntly, it's kind of pathetic."
        mc "Wait, no, that's not true!"
        n 4h "Why are you even in this club, [player]?"
        "Those words hurt, because I know they're true."
        n "Honestly..."
        n "I thought getting a new member would help everyone get more involved together."
        n 4s "Not exclude each other even more."
        n 1u "This is such a stupid activity anyway..."
        mc "Natsuki, I swear, I'm not just trying to impress Yuri!"
        n 12c "Look, I'm not in a good mood today, and I just really don't feel like talking right now."
        n "Please go away."
        $ skip_poem = True
        return
    else:
        n 1k "...Hm."
        n "I liked your last one better."
        mc "Eh? Really?"
        n 2c "Well yeah. I can tell you were a little more daring with this one."
        n "But you're really not good enough for that yet. It fell flat."
        mc "That may be true, but I just wanted to try something different."
        mc "I'm still figuring this all out."
        jump ch22_n_med_shared2


label mod_ch2_n_med:
    if persistent.poem1 == "mp":
        n "...Hm."
        n 2k "Well, I can admit that it's better than the last one."
        n "It's nice to see that you're putting in some effort."
        mc "That's good..."
        label mod_ch2_n_med_shared:
            n 2c "Just make sure you find a little bit of influence from everyone."
            n "I think you're at least being influenced by Yuri a little bit, aren't you?"
            n 5q "I mean, I know you've been, like..."
            n "Spending some time with her, or whatever..."
            n 1w "But you know, Monika and I are just as good as her!"
            n 1q "A-At poems, I mean!"
            n 1h "So you should really try to learn something, or you'll never get better!"
            n "Here's the one I wrote..."
            n "I'll make sure you learn something from it."
            return
    elif persistent.poem1 != "cute":
        n "...Hm."
        n 2k "Well, it's not really any worse than your last one."
        n "But I can't really say it's any better, either."
        mc "Phew..."
        n 2c "Huh? 'Phew' what?"
        mc "Ah... Well anything that isn't a trainwreck, I'll take as a win."
        mc "And I get the feeling you're probably the most critical."
        n 1p "H-Hey! What makes you--"
        n 1q "{i}(Wait, maybe that was a compliment...?){/i}"
        n 4y "A-Ahah! Glad to see someone recognizes my experience!"
        n "Well then, keep practicing and maybe you'll be as good as me someday!"
        mc "That's...uh..."
        "Something tells me Natsuki completely missed the point."
        jump mod_ch2_n_med_shared
    else:
        n "...Hm."
        n 2c "Well, it's not terrible."
        n "But it's pretty disappointing after your last one."
        n 2s "Then again, if this one was as good as your last one, I would be completely pissed."
        mc "Well, I guess I wanted to try something a little different this time."
        label mod_ch2_n_med_shared2:
            n 2c "Fair enough. You're still new to this, so I wouldn't expect you to find your style right away."
            n "I mean, everyone in the club writes really differently from each other..."
            n "Maybe you'll find a little influence from all of us."
            n 2q "For instance..."
            n 5q "I noticed that you were spending some time with Yuri today..."
            n "Not that I care who you spend your time with."
            n 5w "After all, I was taught never to expect anything from anybody."
            "I open my mouth as she says that, but no words come out."
            "I feel so bad for her."
            n 5s "So it's not like I was waiting for you, or anything."
            n 5h "Still, you should at least look over my poem..."
            n "You'll probably be able to learn something from it."
            return

label mod_ch2_n_good:
    if persistent.poem1 != "cute":
        n 1h "..."
        "Natsuki reads my poem."
        "She keeps glancing at me, then back at the poem."
        "By now, she must have read it more than once."
        n 1q "...Aren't you supposed to be bad at this?"
        mc "...Is that a compliment?"
        n 1o "N-No! I mean... You know..."
        "Natsuki struggles to find the words she wants."
        n 5w "I just...expected a lot less after what you showed me yesterday."
        n "That's all."
        mc "Well, I guess I just got lucky with this one."
        n 4t "Y-Yeah!! Exactly!"
        n "You just got lucky, you know?"
        n 4y "Don't get used to it."
        n "You won't always manage to write poems this cute. I mean--!"
        n 1p "I mean well-written! No, I mean--"
        mc "Ah, so that's how it is. My poem is cute?"
        n 1v "No! Why are you smiling?! It's not like I like cute things!"
        "Natsuki shoves my poem back towards me."
        n 4w "H-Huh! Reading it again, I decided that it's not so great after all."
        n "It's too cute and doki-doki."
        n 4t "It would only impress... you know, girls... who like those kinds of things."
        n "Ahaha!"
        "For some reason, Natsuki is incredibly easy to see through."
        n 1w "Well, anyway...!"
        n 1h "You're gonna read mine now, right?"
        n "Judging by your tastes, you'll probably like it a lot."
        n 2q "You'll probably learn something, too. Don't forget who the {i}real{/i} pro is."
        return
    else:
        label mod_n_good_shared:
            n 1n "..."
            "Natsuki reads my poem."
            "She keeps glancing at me, then back at the poem."
            "By now, she must have read it more than once."
            n 1u "Rrgh..."
            mc "...?"
            mc "Is it that bad?"
            n 1r "No! No, it's not!"
            n "It's good. It's really good, okay?!"
            n 5w "There, I said it!"
            n "Ugh, this wasn't supposed to happen at all...!"
            n 5s "Why can't you just be bad at this?"
            n "My poems are supposed to impress {i}you{/i}, not the other way around!"
            mc "You're trying to impress me?"
            n 12c "Obviously! You think I'd let you enjoy Yuri's writing more than mine?"
            n "Give me a break."
            mc "Well..."
            mc "In that case, what's the problem with me trying to impress you?"
            n 1e "I'll tell you! You--"
            n 1p "--"
            "Natsuki's face freezes, like she just realized something."
            n "Y-Y-You..."
            n "You're trying to...impress {i}me?{/i}"
            show natsuki 1q
            "Natsuki vigorously scans her eyes over my poem one more time."
            "Then, the poem slips out of her hands and flutters to the floor."
            n 1p "I...have to use the bathroom!"
            show natsuki at lhide
            hide natsuki
            "Red-faced, Natsuki quickly walks out of the room."
            show monika 1d zorder 2 at t11
            m "Hey, [player]..."
            m "Did you do something to Natsuki?"
            m "I just saw her rush out like that..."
            m 2g "You didn't do anything terrible, did you?"
            mc "N-No!"
            mc "I just told her that--"
            "My voice gets caught in my throat."
            "There's no way I could tell Monika that I'm trying to impress Natsuki."
            m 2d "Hmm?"
            "Monika sees the poem lying on the floor and swiftly picks it up."
            if m_readpoem:
                "She skims over it a second time, her smile not fading from her face."
                m 2a "I see."
                m "At first I just thought you liked her writing style..."
                m "But you wrote this {i}for{/i} Natsuki, didn't you?"
            else:
                $ n_poemearly = True
                "She reads through it, her smile not fading from her face."
                m 2a "I see."
                m "You wrote this for Natsuki, didn't you?"
            mc "I-I mean..."
            mc "Not really..."
            m 2d "In fact, didn't she like your poem a lot the other day, too?"
            m "I'm surprised you know her taste so well already."
            m 4a "Are you sure you're not cheating, [player]?"
            mc "Cheating...?"
            mc "What do you mean by that?"
            m 5a "Never mind, I'm just kidding. Ahaha!"
            "I didn't understand Monika's joke at all."
            m "Anyway..."
            m 1a "How do you think Natsuki feels about you?"
            m "Oh, you don't need to answer that."
            m "It was just something for you to think about."
            show monika zorder 2 at t22
            show natsuki 4e at l21
            n "Hey!"
            "Natsuki comes up and snatches the poem out of Monika's hands."
            "Neither of us had noticed her reenter the classroom."
            show natsuki zorder 3 at f21
            n "Did you read this, Monika?"
            show natsuki zorder 2 at t21
            show monika zorder 3 at f22
            m 1j "Of course! I liked it!"
            show monika 1a zorder 2 at t22
            show natsuki zorder 3 at f21
            n 1r "Ugh..."
            n "You should really stop reading things that aren't for you, you know."
            n "You have a bad habit of doing that."
            show natsuki zorder 2 at t21
            show monika zorder 3 at f22
            m 1d "Eh?"
            m "But [player] wrote this poem."
            m 1a "And we're supposed to share with everyone, right?"
            show monika zorder 2 at t22
            show natsuki zorder 3 at f21
            n 1x "Uu--"
            "Natsuki freezes."
            n 42c "Okay, well, I think [player] is done sharing this poem with everyone."
            n "It's not like anyone would want to read this anyway."
            n 4h "In fact, I'm just going to hold onto this."
            show natsuki zorder 2 at t21
            show monika zorder 3 at f22
            m 5 "If you insist~"
            show monika zorder 2 at t22
            show natsuki zorder 3 at f21
            n 1i "What?"
            n "Why are you looking at me like that??"
            show natsuki zorder 2 at t21
            show monika zorder 3 at f22
            m "Like what?"
            show monika zorder 2 at t22
            show natsuki zorder 3 at f21
            n 12b "Ugh..."
            n "Never mind."
            if y_readpoem:
                "Well, I guess Natsuki has my poem now."
                "Not that I really planned on keeping it."
            else:
                show natsuki zorder 2 at t21
                mc "Ah, Natsuki..."
                mc "I'll give you the poem, but that's still not very fair to Yuri..."
                mc "...She hasn't gotten to read it yet."
                show natsuki zorder 3 at f21
                n 2q "So what?"
                show natsuki zorder 2 at t21
                show monika zorder 3 at f22
                m 2a "Well... I guess [player] is right, Natsuki..."
                m "It's not fair if you don't let everyone finish reading it."
                show monika zorder 2 at t22
                show natsuki zorder 3 at f21
                n "..."
                n 2h "...Fine."
                "Natsuki returns my poem."
                n "It's not like she's going to like it, though."
            show monika zorder 1 at thide
            show natsuki zorder 2 at t11
            hide monika
            n 2h "Anyway, read my poem now."
            n 4h "And no, I won't let you keep it."
            n "This is my only copy."
            return

label mod_ch2_y_bad:
    jump ch22_y_med

label mod_ch2_y_med:
    jump ch22_y_med

label mod_ch2_y_good:
    if persistent.poem1 != "mp":
        y 2b "I've been waiting for this..."
        y "Let's see what you've written for today."
        y 2e "..."
        y "......"
        "Yuri stares at the poem with a surprised expression on her face."
        mc "Do you...like it?"
        y "[player]..."
        y "...How did you pick up on this so quickly?"
        label mod_ch2_y_good_shared:
            y 2v "Just yesterday, I was telling you the kind of techniques worth practicing..."
            mc "Maybe that's why..."
            mc "You did a good job explaining."
            mc "I really wanted to try giving it more imagery."
            show yuri 4b zorder 2 at t11
            "Yuri visibly swallows."
            "Even her hands appear sweaty."
            y 4e "A-Ah..."
            y "That makes me so happy..."
            y 3y5 "It's so amazing to feel like I'm valued, [player]!"
            y "Everything that you write is a treasure to me."
            y 3m "My heart pounds just holding it..."
            if persistent.poem1 in ("abs", "mp"):
                "Those words give me a pit in my stomach. I'm worried that my relationship with Yuri is actually descructive to her."
            y 3q "Ahaha..."
            y "I want to write a poem about this feeling..."
            y 3y6 "Is that bad, [player]?"
            y "I'm not being weird, right?"
            y 3s "I-I'm having a harder time than usual at concealing my emotions..."
            y 3m "I'm kind of embarrassed."
            y 3y6 "But right now, I just want you to read my poem, too."
            y 3y5 "Okay?"
            return
    else:
        y 2b "I've been waiting for this..."
        y "Let's see what you've written for today."
        y 2e "..."
        y "......"
        "Yuri stares at the poem with a surprised expression on her face."
        mc "Do you...like it?"
        y "[player]..."
        y 2t "This one might even be better than yesterday's..."
        y "...How did you even pick up on this so quickly?"
        jump mod_ch2_y_good_shared

label mod_ch2_n_end:
    if persistent.poem1 in ("cute", "bs") and persistent.poem2 in ("cute", "bs") and not persistent.mc_awareness[11]:
        jump mod_ch2_n_end2
    else:
        if not persistent.mc_awareness[11]:
            $ persistent.mc_awareness[11] = False
        call showpoem (poem_n2)
        n 2a "Not bad, right?"
        mc "It's quite a bit longer than yesterday's."
        n 2w "Yesterday's was way too short..."
        n "I was just warming up!"
        n 2c "I hope you didn't think that was the best I could do."
        mc "No, of course not..."
        n 2a "Anyway, the message is pretty straightforward in this poem."
        n "I doubt I have to explain it."
        n 2g "Like, anyone would agree that the subject of this poem is an ignorant jerk..."
        n "Everyone has some kind of weird hobby, or a guilty pleasure."
        n 5q "Something that you're afraid if people find out, they'd make fun of you or think less of you."
        n 1e "...But that just makes people stupid!"
        n "Who cares what someone likes, as long as they're not hurting anyone, and it makes them happy?"
        n 1q "I think people really need to learn to respect others for liking weird things..."
        mc "Well, you're definitely right."
        mc "At least, I can relate to that."
        mc "And I'm sure a lot of other people can, too."
        n 4c "It's what I do best, after all!"
        n "I don't like writing unless there's a good message to take away from it."
        n "Like, conveying emotions is important..."
        n "But I want to make people think, not just feel."
        n 4b "Remember that!"
        n "I'm gonna write a good one for tomorrow, too, so look forward to it."
    return

label mod_ch2_n_end2:
    call showpoem (poem_n2b, revert_music=False)
    if not y_readpoem:
        mc "Um, Natsuki?"
        mc "What... the hell..."
    else:
        mc "Oh god, not you too Natsuki..."
    $ style.say_dialogue = style.edited
    n 1g "[player]..."
    n "Why didn't you come read with me today?"
    $ style.say_dialogue = style.normal
    mc "I..!"
    $ style.say_dialogue = style.edited
    n 1m "I was waiting for you."
    n "I was waiting for a long time."
    n "It was the only thing I had to look forward to today."
    $ style.say_dialogue = style.normal
    mc "I'm sorry! Yuri pressured me into reading with her instead, and, I figured since I already spent time with you yesterday..."
    $ style.say_dialogue = style.edited
    n "Why did you ruin it?"
    n "Do you like Yuri more?"
    $ style.say_dialogue = style.normal
    mc "N-no! Natsuki, please!"
    $ style.say_dialogue = style.edited
    n 1k "I think you're better off not associating with her."
    n "Are you listening to me?"
    $ style.say_dialogue = style.normal
    "Are {i}you{/i} listening to {i}me{/i}?"
    show darkred zorder 5:
        alpha 0.0
        easein 4.0 alpha 1.0
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_ghost.ogg"
    stop music_poem fadeout 2.0
    $ renpy.music.play(audio.t5c, fadein=2.0, tight=True)
    show n_rects_ghost1 zorder 4
    show n_rects_ghost2 zorder 4
    show n_rects_ghost3 zorder 4
    "Oh no... what's happening?"
    $ style.say_dialogue = style.edited
    n ghost1 "Yuri is a sick freak."
    n "That should be obvious by now."
    $ style.say_dialogue = style.normal
    mc "Natsuki, no, you don't mean that..."
    "But she doesn't seem to be hearing a word I say."
    $ style.say_dialogue = style.edited
    n "So just play with me instead."
    n "Okay?"
    n "You don't hate me, [player], do you?"
    n "Do you hate me?"
    show natsuki_ghost_blood zorder 3
    $ style.say_dialogue = style.normal
    "I don't know what to do or say! I have to make her snap out of this somehow!"
    $ style.say_dialogue = style.edited
    n "Do you want to make me go home crying?"
    n "The club is the only place I feel safe."
    $ style.say_dialogue = style.normal
    mc "Natsuki, I'm sorry, please..."
    $ style.say_dialogue = style.edited
    n "Don't ruin that for me."
    n "Don't ruin it."
    n "Please."
    n "Just stop talking to Yuri."
    n "Play with me instead."
    n "It's all I have..."
    n "Play with me."
    $ style.say_dialogue = style.normal
    "I just know something terrible is going to happen. But I don't see what I can do about it."
    $ style.say_dialogue = style.edited
    stop music
    hide n_rects_ghost3
    n ghost2 "PLAY WITH ME!!!"
    $ style.say_dialogue = style.normal
    $ quick_menu = False
    $ pause(1)
    play sound "sfx/crack.ogg"
    hide natsuki_ghost_blood
    hide n_rects_ghost1
    hide n_rects_ghost2
    show natsuki ghost3
    show n_rects_ghost4 onlayer front zorder 4
    show n_rects_ghost5 onlayer front zorder 4
    $ pause(0.5)
    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4 onlayer front at i11
    $ pause(0.25)
    window hide(None)
    hide natsuki onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    scene black
    with None
    window auto
    scene black
    $ pause(0.5)
    show end:
        xzoom -1
    with dissolve_cg
    $ pause(2.0)
    scene black
    with None
    $ quick_menu = True
    scene bg club_day
    $ persistent.mc_awareness[11] = True
    mc "OH MY GOD!!!"
    show natsuki 2k at t11
    n "Uh... [player]?"
    mc "Natsuki... Thank god... I thought you were dead..."
    n 2e "Dead?!? What the heck are you talking about?"
    show natsuki at t22 zorder 1
    show monika 1c at l21 zorder 2
    m "[player], I think you really need to see a doctor. Nothing happened just now."
    mc "..."
    mc "Well, Natsuki, can I see your poem again? I don't think I saw what was actually there."
    n 2c "Sure, whatever."
    hide monika
    show natsuki 1c at t11 zorder 2
    jump mod_ch2_n_end

label mod_ch2_y_end:
    stop music fadeout 2.0
    call showpoem (poem_y22, music=False, paper="images/bg/poem_y1.jpg", img="yuri 2s")
    mc "Umm... Yuri?"
    y 2q "Ahaha..."
    y "It doesn't really matter what it's about."
    y "My mind has been a little hyperactive lately, so I had to take it out on your pen."
    y 2o "Ah--"
    y 2q "That is...a-a pen fell out of your backpack yesterday, so I took it home for safekeeping and..."
    y "I, um..."
    y 2y6 "I just...really like...the way...that it writes."
    y "So I wrote this...poem...with it."
    y "And now you're touching it..."
    "I'm too shocked by the insanity of what she's saying to respond."
    y 2y5 "Ahaha."
    y 3p "I-I'm okay!!"
    y 3o "What did I just..."
    y "..."
    y 4c "...Can we pretend this conversation never happened?"
    y "You can keep the poem, though..."
    mc "Ah- wait, Yuri! We need to talk about this!"
    y "Th-there's nothing to say!"
    mc "This poem is..."
    "I don't know what to say about it."
    mc "Yuri, I think there's something really wrong with you. We need to -"
    y "[player], look, I know! But don't worry, everything's going to be fine! I won't... go off the deep end or anything."
    "I'm really worried about her. But it's not like I've seen her show signs of becoming dangerous, and besides, I really don't know what I can do to help her. So, I leave her alone."
    return

label mod_ch2_m_start:
    if persistent.poem1 == "abs" and persistent.poem2 == "abs":
        "Monika reads my poem."
        m 1o "[player]..."
        m "I..."
        m "Need to tell you the truth."
        mc "Please do."
        m "After the meeting today, I'll stay behind to talk to you. I don't want the others around."
        mc "Alright."
    elif not persistent.mc_awareness[9]:
        m 1b "Hi again, [player]!"
        m "How's the writing going?"
        mc "Alright, I guess..."
        m 2k "I'll take that."
        m 2b "As long as it's not going bad!"
        m 2a "I'm happy that you're applying yourself."
        m "Maybe soon you'll come up with a masterpiece!"
        mc "Ahaha, I wouldn't count on that..."
        m 2a "You never know!"
        m "Want to share what you wrote for today?"
        mc "Sure... Here you go."
        "I give my poem to Monika."
        m "..."
        m "...Alright!"
    if persistent.poem1 != "abs" or persistent.poem2 != "abs":
        if persistent.mc_awareness[9]:
            call m_mp_2
        else:
            call expression "m_"+persistent.poem2+"_2"
    m 1a "But anyway..."
    m "You want to read my poem now?"
    m "I like the way this one turned out, so I hope you do too~"
    return

label m_cute_2:
    if persistent.poem1 == "abs":
        m 1c "..."
        mc "Well?"
        m 2b "It's good!"
        "Despite Monika's ostensible compliment, I can tell she's disappointed."
        m 2a "It's a lot cuter than the last one."
        m "It kind of makes me think of something Natsuki would write."
        m "And she's a good writer, too."
        m 5a "So take that as a compliment!"
        mc "Yeah, if you say so..."
    elif persistent.poem1 == "cute":
        m 3b "Decided to go for something cute again, I see!"
        mc "Yeah..."
        m 1a "By any chance have you read anything by Shel Silverstein?"
        mc "Eh?"
        mc "Maybe a long time ago..."
        m "He's famous for telling all kinds of stories in just a few simple words."
        m "His poems can be funny, endearing, or even sad..."
        m 3d "And sometimes they're only a few lines long."
        m "They might even feel like they're written for kids, but if you think about them..."
        m "They can express views of the world that would apply to anybody."
        mc "I see..."
        mc "So you're saying that Natsuki is kind of like that?"
        m 2a "Sort of."
        m "Maybe she's not an expert..."
        m "But you probably won't find much filler in her poems."
        m "They might be easy to write, but they're super challenging to get the meaning through."
        m 2b "So I can see why it would be your kind of poem to explore!"
    else:
        jump m_natsuki_1 # Original Act 1 script
    return

label m_mp_2:
    if persistent.poem1 in ("cute", "bs") and mod_chapter != 3:
        jump m_mp_1
    m 1i "[player], I think you saw something earlier that you weren't supposed to see."
    m "I didn't want to have to tell you this, but I don't think I have a choice."
    m 1r "It's getting kind of dangerous for you to spend so much time with Yuri."
    m 1i "I don't know why, but she seems pretty easily excitable when she's around you..."
    m 3d "Which shouldn't be a problem in itself."
    m "But when Yuri gets too excited, she finds a place to hide and starts cutting herself with a pocket knife."
    mc "Yeah, I saw..."
    m 2e "Isn't that kind of messed up?"
    m "She even brings a different one to school every day, like she has a collection or something..."
    m 2d "I mean, it's definitely not because she's depressed or anything like that!"
    m "I think she just gets some kind of high from it."
    m 2m "It might even be, like, a sexual thing..."
    m 1i "But the point is, you've kind of been enabling her."
    m 1d "I'm not saying it's your fault, though!"
    m 1a "But I guess that's why I had to explain it all to you..."
    m "So I think if you keep your distance, that would probably be best for her."
    if persistent.poem1 == "abs" or persistent.poem2 == "abs": # It's not redundant to check poem2, because this block can get called on day 4.
        mc "Well, you've known her for a lot longer than I have, so I guess I'll trust your judgement on that."
        m 4j "I appreciate your trust!"
    else:
        "What Monika is saying makes sense, but I get a bad feeling about her."
        "She's the only one that hasn't shown any signs of experiencing things like what I have."
        "That makes me think I shouldn't trust her."
    m 5 "While you're at it, don't be shy to spend a little more time with me..."
    m "To put it lightly, I at least have it together in the head...and I know how to treat my club members."
    return

label m_bs_2:
    if persistent.poem1 == "abs":
        m 1c "..."
        mc "Well?"
        m 2b "It's good!"
        "Despite Monika's ostensible compliment, I can tell she's disappointed."
        "In fact, she looks almost {i}scared{/i}."
        m 2m "It's just that it's different from what me or Yuri or Natsuki usually write..."
        jump m_bs_1_jumpin
    elif persistent.poem1 == "bs":
        m "Mm... you really like this bittersweet style, don't you?"
        mc "Yeah... I guess so."
        m "Well, you know, there are a lot of different styles out there, and none of them are any more 'right' or 'wrong' than another."
        m "You should consider trying something different."
        m "Not that this poem isn't good, but I'm curious to see what you'd come up with if you tried a different style."
        mc "Alright, I'll keep that in mind."
    else:
        jump m_bs_1
    return

label m_abs_2:
    call m_abs_1
    m 1m "Also... there was something I wanted to tell you, unrelated to poems."
    mc "Yeah?"
    m "The thing is..."
    jump m_mp_2

label mod_ch2_m_end:
    call showpoem (poem_m22, revert_music=False)
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    $ pause(2)
    show screen tear(20, 0.3, 0.3, 0, 40)
    $ pause(0.5)
    hide screen tear
    play music t5c
    mc "... Monika? What is this poem about?"
    "I'm particularly put off by the line that says 'delete her' at the bottom."
    if persistent.poem1 != "abs" or persistent.poem2 != "abs":
        m 5 "Sorry, I know it's kind of abstract."
        m "I'm just trying to...um..."
        m 1r "Well, never mind."
        m "There's no point in explaining."
    else:
        m "You'll see. I'll explain everything after the meeting."
        mc "Alright. Looking forward to it. See you, I guess."
    if y_ranaway:
        call yuri_come_back
    return

label mod_ch3_n_bad:
    if persistent.poem1 == "mp" and persistent.poem2 == "mp":
        n 5x "I'm not going to read another one of your Yuri suck-up poems."
        n 5s "But I'm still going to make you read mine."
        n "There's a reason."
        n 5x "I really wish I didn't have to do this..."
        n "But unfortunately I don't have much of a choice."
        n 5h "Just...read it carefully, okay?"
        n "Then you can go away."
        return
    elif persistent.poem1 == "mp" or persistent.poem2 == "mp":
        n "..."
        n 2c "...Meh."
        n "I guess you really haven't learned anything after all."
        n "Honestly, I don't know why I got my hopes up in the first place."
        label mod_ch3_n_bad_shared:
            n 42c "This is clearly Yuri's influence..."
            n "I didn't realize you were so impressionable."
            mc "Ah- hey! That's not what-"
            n "Spending all this time with her in the club..."
            n "Now trying to write like her..."
            n 1s "This is stupid."
            n "At least Monika appreciates my writing..."
            mc "Hey, I appreciate your writing too!"
            n 1r "...Ugh."
            n 1q "Okay...I guess I'm going to share my poem with you now."
            n "I really hate that I have to do this."
            n "But unfortunately I don't have much of a choice."
            n 1h "Just...read it carefully, okay?"
            n "Then you can go away."
            return
    else:
        n "..."
        n 2r "Oh, man."
        n "This is seriously a step backwards."
        mc "Eh?"
        n 2c "I liked your last two way better than this one."
        jump mod_ch3_n_bad_shared

label mod_ch3_n_med:
    if persistent.poem1 == "mp" and persistent.poem2 == "mp":
        jump mod_ch3_n_bad
    elif persistent.poem2 == "mp":
        n "..."
        n 2k "...This one's alright."
        mc "Alright?"
        n "Yeah, it's at least better than yesterday's."
        label mod_ch3_n_shared:
            n 2c "I still can't really tell how much you actually care about writing, but either way, you're doing alright."
            n 4r "Even though you're not really spending time with anyone but Yuri..."
            n 4h "I still think it's nice to have activities that we all participate in."
            n 4w "So you better keep working hard!"
            n "I mean..."
            n 1h "I know I'm not President or Vice President or anything..."
            n "But that doesn't mean you can let me down, okay?"
            n 1q "So, at least read mine too for now."
            n "But just to be clear..."
            n 1h "This poem...means a lot to me."
            n "So read it carefully, okay?"
            return
    else:
        n "..."
        n 2k "...This one's alright."
        mc "Alright?"
        n "Well, yeah."
        n "About as good as yesterday's, anyway."
        jump mod_ch3_n_shared

label mod_ch3_n_good:
    jump mod_ch3_n_med

label mod_ch3_n_end:
    call showpoem (poem_n23, revert_music=False)
    $ renpy.music.stop(channel="music_poem", fadeout=2.0)
    mc "Don't worry Natsuki. I know something's wrong with her, and I'm going to help her overcome it."
    mc "I appreciate that you-{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(3.0)
    stop music
    hide screen tear
    show natsuki ghost_base
    $ style.say_dialogue = style.edited
    n "I changed my mind."
    n "Ignore everything you just read."
    n "There's no point in trying to do anything."
    n "It's Yuri's own fault that she's so unlikable."
    n "Can you hear me, [player]?"
    n "If you would just spend more time with Monika, all these problems would go away."
    n "Yuri and I are too messed up for someone as wonderful as you."
    n "Just think of Monika from now on."
    n "Just Monika."
    hide natsuki
    $ style.say_dialogue = style.normal
    "No..."
    $ style.say_dialogue = style.edited
    "Just Monika."
    menu:
        "Just Monika."
        "Just Monika.":
            pass
    $ style.say_dialogue = style.normal
    $ renpy.call_screen("dialog", "Just Monika.", ok_action=Return())
    scene white
    play music t1
    show intro with Dissolve(0.5, alpha=True)
    $ pause(2.5)
    hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "Just Monika." with Dissolve(0.5, alpha=True)
    $ pause(1.0)
    play music t5
    $ skip_transition = True
    scene bg spoopy
    mc "Oh god... what just happened?"
    mc "It's obvious Monika is up to something."
    mc "She has some sort of power over this world, I think."
    return

label mod_ch3_y_bad:
    jump mod_ch3_y_good

label mod_ch3_y_med:
    jump mod_ch3_y_good


label mod_ch3_y_good:
    if persistent.poem1 in ("mp", "abs"):
        "As I approach Yuri, I remember how our 'reading time' ended today."
        if persistent.left_yuri:
            "I'm afraid that she's going to be mad at me for walking out on her."
            "To my relief, though, she doesn't say anything about it."
        else:
            "Speaking of which, how did it end?"
            "Yuri was saying something I couldn't understand and then we were just back in the clubroom."
            "She doesn't mention it, though."
    elif persistent.lookup_portrait: # This can be an elif because having this flag set requires having seen the first Yuri exclusive on day 3 instead of day 2.
        "As I approach Yuri, I remember something."
        "We were supposed to both look up Portrait of Markov..."
        "But due to the... unusual way yesterday ended, I didn't get a chance to."
        "Or, if I did, I at any rate don't remember what I found..."
        mc "Hey Yuri. Did you remember to look up Portrait of Markov?"
        y 4b "Ah... No, I didn't. Sorry..."
        mc "It's okay. I didn't either. In fact, I don't remember anything about yesterday after I left the clubroom."
        y 3f "That's... unsettling. But I suppose we'll just do it this evening. Anyway, want to share poems?"
        mc "Sure, I guess."
    y 1d "Finally..."
    y 3y5 "Ahaha..."
    show yuri 3m
    "Yuri holds my poem to her face and takes a deep breath."
    y 3y6 "I love it."
    y "I love everything about it."
    y 3y5 "[player], I want to take this home."
    y "Will you let me keep it?"
    y "Please?"
    if not n_readpoem or not m_readpoem:
        mc "Um, Yuri... I'm happy to let you keep the poem, but you should give Natuski and Monika a chance to read it first. I'll give it to you after the meeting."
        y "Okay, that's fine."
    else:
        mc "Sure, I don't care..."
    y 2y5 "Ahaha."
    y "You're too nice to me, [player]..."
    y "I've never met anyone as nice as you."
    y 2y6 "I could die..."
    y 3y5 "N-Not really, but--!"
    y "I just don't know how to describe it."
    y "It's okay to be feeling this way, right?"
    show yuri:
        "yuri 3y4"
        0.4
        "yuri 3y6"
    y "It's not bad, right?"
    "Yuri holds my poem to her chest."
    y 3m "I'm going to take this home with me and keep it in my room."
    y "I hope that it makes you feel good when you think about me having it."
    $ style.say_dialogue = style.normal
    y 3y5 "I'll take good care of it!"
    $ style.say_dialogue = style.edited
    y 3y6 "I'll even touch myself while reading it over and over."
    $ _history_list.pop()
    y "I'll give myself paper cuts so your skin oil enters my bloodstream."
    $ _history_list.pop()
    y 3y1 "Ahahahahaha."
    $ _history_list.pop()
    $ style.say_dialogue = style.normal
    mc "Yuri, {i}what{/i} are you...?"
    y 2s "You can have my poem too."
    y "Besides, after you read it, I know you're really going to want to keep it."
    y 2y6 "Here, take it. I can't wait any longer."
    y 2y5 "Hurry! Read it!"
    return

label mod_ch3_m_start:
    if persistent.poem1 in ("abs", "mp"):
        jump mod_ch3_m_end_yuri_full
    else:
        call m_mp_2
        m 1a "Anyway..."
        m 1e "I worked really...really hard on this poem, so..."
        m "I hope that it's, uh, effective."
        m 1r "Here goes..."
        return

label mod_ch3_m_end:
    $ quick_menu = False
    window hide
    play sound page_turn
    show paper_glitch zorder 10 with Dissolve(1)
    play music g2
    if renpy.windows and renpy.game.preferences.fullscreen:
        $ mouse_visible = False
        scene bsod
        $ pause(3.0)
    else:
        show black zorder 1
        $ pause(2.0)
    window show(None)
    show monika 1d zorder 11 at i11
    $ quick_menu = True
    $ mouse_visible = True
    m "Jeez! That really startled me!{fast}"
    window auto
    m "Um..."
    m 1m "Well, I guess I kinda messed up at, uh... 'writing' this poem."
    "The f[fword]? What is {i}up{/i} with Monika?"
    m "I was just trying to..."
    m 1i "...Never mind."
    m "Let's just move on..."
    stop music
    return

label mod_ch3_m_end_yuri_full:
    stop music
    m 1i "Don't say I didn't warn you, [player]."
    $ skip_poem = True
    if n_readpoem:
        "Alright, I'm certain now that Monika's up to something bad."
        "Something horrible."
        mc "Monika, tell me the truth!"
        mc "What are you doing?"
        m "Something you can't stop."
        m "Something that's your fault."
        "I seriously consider attacking her here."
        "But what would Yuri and Natsuki do?"
        "I saw how Monika fed words into Natsuki after I read her message."
        "I think Monika can control her."
        "Maybe she can control Yuri too."
        "Maybe if I attack her here, they'll all gang up on me."
        "But what else can I do?"
        "I {i}have{/i} to stop her somehow."
        "I'm really scared."
        "I guess I'll wait a little longer..."
    else:
        mc "Monika, what are you talking about?"
        m "You've made a mistake, and you can't stop it now."
        m "You're going to wish you had listened to me..."
        mc "S[sword], Monika, you're really scaring me. What's going to happen?"
        m 5 "Oh, nothing. Nothing bad, that is. You'll see."
        "I guess she's not going to tell me..."
        "It's obvious something terrible is going to happen, and it wouldn't surprise me if Monika was behind it."
        "But I'll be on guard. I'll be ready to stop it."
    return

label mod_ch3_y_end:
    show darkred zorder 5:
        alpha 0
        linear 2.0 alpha 1.0
    call showpoem (poem_y23, track="bgm/5_yuri2.ogg", revert_music=False, paper="images/bg/poem_y2.jpg", img="yuri eyes", where=truecenter)
    "I sweat reading the poem."
    "Oh my god..."
    y "Do you like it??"
    y "I wrote it for you!"
    mc "Yuri, you're terrifying me. I don't know what's happening to you, but I think you're in serious danger."
    $ gtext = glitchtext(80)
    show yuri 1b at i11
    y "Oh don't worry about me [player], I'm fine."
    y "In case you couldn't tell, the poem is about [gtext]"
    y 1y6 "More importantly, I've endowed it with my scent."
    y "See, aren't I the most thoughtful person in the club?"
    mc "F[fword] no, this is not happening..."
    play sound "sfx/glitch2.ogg"
    show yuri glitch
    $ pause(0.2)
    stop sound
    show yuri 3y2
    hide darkred
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    $ renpy.music.stop(channel="music_poem")
    $ renpy.music.play(audio.t5c)
    y "..."
    y 4d "I..."
    y "I think I'm...going to vomit."
    show yuri at lhide
    hide yuri
    $ pause(1.0)
    "Oh my god..."
    "At least she seems to know there's something wrong with her."
    "But I feel like it's going to come to a head today, and I'm terrified, because I can't imagine what's going to happen."
    return
