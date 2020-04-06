label mod_exclusive_cute_1:
    scene bg spoopy
    with wipeleft_scene
    n "Ugh...!"
    "I hear Natsuki utter an exasperated sigh from within the closet."
    "She seems to be annoyed by something."
    "I approach her, in case she needs a hand."
    if renpy.music.get_playing() == audio.t2gl: # stops the music abruptly
        stop music
        play music t6
    else:
        play music t6 fadeout 1.0
    scene bg closet
    show natsuki 4r at t11 zorder 2
    with wipeleft_scene
    window auto
    mc "Natsuki, are you looking for something in there?"
    $ style.say_dialogue = style.edited
    n 4x "f[fgword] monikammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
    $ _history_list[-1].what = "Freaking Monika..."
    $ style.say_dialogue = style.normal
    "That's pretty extreme..."
    n "She never puts my stuff back in the right spot!"
    n "What's the point in keeping your collection organized if someone else is just gonna mess it up?"
    "Natsuki slides a bunch of stacked books and boxes across the shelf."
    mc "Manga..."
    n 2c "You read manga, right?"
    mc "Ah--"
    mc "...Sometimes..."
    "Manga is one of those things where you can't admit you're really into it until you figure out where the other person stands."
    mc "...How did you know, anyway?"
    n 2k "I heard you bring it up at some point."
    n "Besides, it's kind of written on your face."
    "What's that supposed to mean...?"
    mc "I-I see..."
    "There's a lone volume of manga amidst a stack of various books on the side of one of the shelves."
    "Curious, I pull it out of the stack."
    n 1b "{i}There{/i} it is!"
    "Natsuki snatches it out of my hand."
    "She then turns to a box of manga and slips the volume right into the middle of the rest."
    n 4d "Aah, much better!"
    n "Seeing a box set with one book missing is probably the most irritating sight in the world."
    mc "I know that feel..."
    "I get a closer look at the box set she's admiring."
    mc "Parfait Girls...?"
    menu:
        "It sounds vaguely familiar..."
        "Is that that series about a group of girls who get obsessed with some guy at an ice cream shop?":
            $ no_return()
            n "Have you read this before?"
            mc "No, but I've-"
            "Wait, no I haven't..."
            $ persistent.mc_awareness[4] = True
            mc "Uh... to be honest, I don't know how I knew that."
            mc "I can't remember ever hearing about this series before."
            n 2e "Whatever. Don't make it sound bad, though! It might be a silly chapter, but it's good!"
            jump read_parfait
        "Is that that series about a group of girls who work at an ice cream shop and get obsessed with a guy who frequents it?":
            $ no_return()
            $ persistent.mc_awareness[4] = False
            n 2c "No... you must be thinking of a different series."
        #"It's a series I've never heard of in my life."
        #"That probably means it's either way out of my demographic, or it's simply terrible."
        #n 5g "If you're gonna judge, you can go do it through the glass on that door."
        #"She points to the classroom door."
        #mc "H-Hey, I wasn't judging anything...!"
        #mc "I didn't even say anything."
        #n 5c "It was the tone of your voice."
    n "But I'll tell you one thing, [player]."
    n 4l "Consider this a lesson straight from the Literature Club:{nw}"
    $ _history_list[-1].what = "Consider this a lesson straight from the Literature Club: Don't judge a book by its cover!"
    $ style.say_dialogue = style.edited
    n "don't judge a bookkkkkkkkkkkkkkkkk kkkkk kk{space=20}k{space=40}k{space=120}k{space=160}k{space=200}k"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()
label read_parfait:
    n 4l "In fact--"
    "Natsuki pulls out the first volume of Parfait Girls from the box."
    n "I'm gonna show you exactly why!"
    "She shoves the book right into my hands."
    mc "Ah..."
    "I stare at the cover."
    "It features four girls in colorful attire striking animated feminine poses."
    "It's... exceedingly \"moe\"."
    n 4b "Don't just stand there!"
    mc "Uwa--"
    show natsuki zorder 1 at thide
    hide natsuki
    "Natsuki grabs my arm and pulls me out of the closet."
    "She then takes a seat against the wall, beneath the windowsills."
    "She pats on the ground next to her, signaling me to sit there."
    show bg spoopy
    show natsuki 2a zorder 2 at t11
    with wipeleft
    mc "Wouldn't chairs be more comfortable...?"
    "I take my seat."
    n 2k "Chairs wouldn't work."
    n "We can't read at the same time like that."
    mc "Eh? Why's that?"
    mc "Ah...I guess it's easier to be close together like this..."
    n 2o "--!"
    n 5r "D-Don't just say that!"
    n "You'll make me feel weird about it!"
    "Natsuki crosses her arms and scootches an inch away from me."
    mc "Sorry..."
    show natsuki 5g
    "I didn't exactly expect to be sitting this close to her, either..."
    "Not that I can say it's a particularly bad thing."
    "I open the book."
    "It's only a few seconds before Natsuki once again inches closer, reclaiming the additional space while she hopes I won't notice."
    "I can feel her peering over my shoulder, much more eager to begin reading than I am."
    n 1k "Wow, how long has it been since I read the beginning...?"
    mc "Hm?"
    mc "You don't go back and flip through the older volumes every now and then?"
    n 2k "Not really."
    n "Maybe sometimes after I've already finished the series."
    n 2c "Hey, are you paying attention?"
    mc "Uh..."
    "I am, but nothing's really happened yet, so I can talk at the same time."
    "It looks like it's about a bunch of friends in high school."
    "Typical slice-of-life affair."
    "I kind of grew out of these, since it's rare for the writing to be entertaining enough to make up for the lack of plot."
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    mc "...Are you sure this isn't boring for you?"
    n "It's not!"
    mc "Even though you're just watching me read?"
    n "Well...!"
    n "I'm...fine with that."
    mc "If you say so..."
    mc "...I guess it's fun sharing something you like with someone else."
    mc "I always get excited when I convince any of my friends to pick up a series I enjoy."
    mc "You know what I mean?"
    n "...?"
    mc "Hm?"
    mc "You don't?"
    show n_cg1_exp2 at cgfade
    n "Um..."
    n "That's not..."
    n "Well, I wouldn't really know."
    mc "...What do you mean?"
    mc "Don't you share your manga with your friends?"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Could you not rub it in?"
    n "Jeez..."
    mc "Ah... Sorry..."
    n "Hmph."
    n "Like I could ever get my friends to read this..."
    n "They just think manga is for kids."
    n "I can't even bring it up without them being all like..."
    n "'Eh? You still haven't grown out of that yet?'"
    n "Makes me want to punch them in the face..."
    mc "Urgh, I know those kinds of people..."
    mc "Honestly, it takes a lot of effort to find friends who don't judge, much less friends who are also into it..."
    mc "I'm already kind of a loser, so I guess I gravitated toward the other losers over time."
    mc "But it's probably harder for someone like you..."
    hide n_cg1_exp3
    n "Hm."
    n "Yeah, that's pretty accurate."
    "{i}...Wait, which part??{/i}"
    n "I mean, I feel like I can't even keep it in my own room..."
    $ style.say_dialogue = style.edited
    n "My dad would beat the s[sword] out of me if he found this."
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "I don't even know what my dad would do if he found this."
    mc "Your dad would do {i}what{/i}?"
    n "I just said I don't know what he'd do. He'd be very angry though."
    "Weird... maybe she didn't say what I thought?"
    n "At least it's safe here in the clubroom."
    show n_cg1_exp3 at cgfade
    n "'Cept Monika's kind of a jerk about it..."
    n "Ugh! I just can't win, can I?"
    mc "Well, it paid off in the end, didn't it?"
    mc "I mean, here I am, reading it."
    n "Well, it's not like that solves any of my problems."
    mc "Maybe..."
    mc "But at least you're enjoying yourself, right?"
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "--"
    n "..."
    n "...So?"
    mc "Ahaha."
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Jeez, that's enough!"
    n "Are you gonna keep reading, or what?"
    mc "Yeah, yeah..."
    "I flip the page."
    show black with dissolve_cg
    "..."
    "..."
    "....."
    "......."
    "........."
    "Time passes."
    hide n_cg1_exp3
    show n_cg1_exp4 behind black at cgfade
    "Natsuki is strangely quiet now."
    "I glance over at her."
    hide black with dissolve_cg
    "It looks like she's started to fall asleep."
    mc "Hey, Natsuki..."
    hide n_cg1_exp4
    show n_cg1_exp5 at cgfade
    n "Y-Yeah...?"
    "Suddenly, Natsuki collapses straight into me."
    play sound fall
    mc "H-Hey--"
    show n_cg1_exp5
    hide n_cg1_exp5
    show n_cg1b
    hide n_cg1_base
    $ currentpos = get_pos()
    $ audio.t6g = "<from " + str(currentpos) + " loop 10.893>bgm/6g.ogg"
    play music t6g
    $ ntext = glitchtext(96)
    $ style.say_dialogue = style.edited
    n "{color=#000}[ntext]{/color}"
    $ style.say_dialogue = style.normal
    "What the f[fword] is-"
    $ style.say_dialogue = style.edited
    $ ntext = glitchtext(96)
    n "{color=#000}[ntext]{/color}"
    $ style.say_dialogue = style.normal
    stop music
    window hide(None)
    window auto
    scene bg spoopy
    show monika 1r zorder 2 at t11
    m "Oh jeez..."
    m 1d "Natsuki, are you okay?"
    show monika zorder 2 at t21
    show natsuki 12b zorder 3 at f22
    n "..."
    show natsuki zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "Here..."
    show monika zorder 2 at t21
    "Monika reaches into her bag and pulls out some kind of protein bar."
    "She throws it in Natsuki's direction."
    "Natsuki's eyes suddenly light up again."
    "She snatches the bar from the floor and immediately tears off the wrapper."
    show natsuki zorder 3 at f22
    n 1s "I told you not to give mmph..."
    show natsuki zorder 2 at t22
    "She doesn't even finish her sentence before stuffing it into her mouth."
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 3b zorder 2 at t11
    m "Don't worry, [player]."
    m "She's fine."
    m "It just happens every now and then."
    m 1a "That's why I always keep a snack in my bag for her."
    m 5a "Anyway...!"
    m "Why don't we all share poems now?"
    return