﻿# This is used for top-level game strucutre.
# Should not include any actual events or scripting; only logic and calling other labels.
# define config.developer = True
label start:

    # Set the ID of this playthrough
    $ anticheat = persistent.anticheat

    # We'll keep track of the chapter we're on for poem response logic and other stuff
    $ chapter = 0

    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    $ _dismiss_pause = config.developer

    # Each of the girls' names before the MC learns their name throughout ch0.
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ config.main_menu_music = audio.t1
    $ allow_skipping = True
    $ config.allow_skipping = True

    if persistent.playthrough == 0:
        #Intro
        call ch_mod_intro
    
    elif persistent.playthrough == 1:
        # Day 1
        call ch_mod_1a
        jump mod_continue

    elif persistent.playthrough == 2:
        # Day 1 if you reload, skips the glitched Sayori part
        call ch_mod_1b
        label mod_continue:
            $ mod_chapter = 0

            # Poem choice
            if not persistent.poem1:
                call mod_poem_game
            else:
                call ch_mod_p1_reload

            # Day 2
            $ mod_chapter = 1
            call ch_mod_2
            call mod_poemresponse
            call ch_mod_2_end

            if not persistent.poem2:
                call mod_poem_game
            else:
                call ch_mod_p2_reload

            # Day 3
            $ mod_chapter = 2
            call ch_mod_3
            call mod_poemresponse
            call ch_mod_3_end

            if not persistent.poem3:
                call mod_poem_game
            else:
                call ch_mod_p3_reload

            # Day 4
            $ mod_chapter = 3
            call ch_mod_4
            call mod_poemresponse
            call ch_mod_4_end
            # Endings are called from within ch_mod_4_end

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
