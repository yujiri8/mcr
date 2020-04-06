label mod_poem_game:
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $ config.keymap['dismiss'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    scene black
    pause 1.0
    show p1 zorder 1
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    play music ap1
    pause 0.33
    hide p1
    show p1a zorder 1
    pause 0.4
    hide p1a
    show p1b zorder 1
    show m_sticker at m_pos zorder 2
    pause 2.58
    show screen tear(20, 0.1, 0.1, 0, 40)
    pause 0.59
    #3.9
    hide screen tear
    hide p1b
    show p1 zorder 1
    pause 1.55
    show m_sticker hop
    pause 0.04
    hide m_sticker
    hide m_sticker hop
    hide pl
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 2.0
    hide screen tear
    stop music
    scene black with trueblack
    scene bg notebook
    show screen quick_menu
    show n_sticker at sticker_mid
    show y_sticker at sticker_right
    with dissolve_scene_full
    play music t4
    stop music
    hide screen quick_menu
    hide n_sticker
    hide y_sticker
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    play music aglitch2
    pause 2.0
    stop music
    hide screen tear
    scene white
    pause 2.0
    show noise:
        alpha 0.1
    $ config.keymap['dismiss'] = dismiss_keys
    $ renpy.display.behavior.clear_keymap_cache()
    $ gtext = glitchtext(80)
    "[gtext]"
    if mod_chapter == 0:
        menu:
            "ŴHaŧ ĸIñd øF ¶o3m shoųlÐ ¡ mÆke¿"
            "Something cute":
                $ persistent.poem1 = "cute"
            "Something bittersweet":
                $ persistent.poem1 = "bs" # lol
            "Something metaphorical":
                $ persistent.poem1 = "mp"
            "Something abstract":
                $ persistent.poem1 = "abs"
    elif mod_chapter == 1:
        menu:
            "ŴHaŧ shoųlÐ ¡ Ŵrlŧ3 Æbøųŧ¿"
            "Insecurity":
                $ persistent.poem2 = "cute"
            "Guilt":
                $ persistent.poem2 = "bs"
            "Lust":
                $ persistent.poem2 = "mp"
            "Imprisonment":
                $ persistent.poem2 = "abs"
    else:
        $ gtext = glitchtext(50)
        $ gtext2 = glitchtext(10)
        menu:
            "[gtext]"
            "Literature":
                $ persistent.poem3 = "cute"
            "Suicide":
                $ persistent.poem3 = "bs"
            "Love":
                $ persistent.poem3 = "mp"
            "[gtext2]":
                $ persistent.poem3 = "abs"

    hide noise
    scene black
    $ quick_menu = True
    $ config.allow_skipping = True
    $ allow_skipping = True
    return

label ch_mod_p1_reload:
    if persistent.poem1 == "cute":
        scene black
        "I decide to write a cute poem."
    elif persistent.poem1 == "bs":
        scene black
        "I decide to write a bittersweet poem."
    elif persistent.poem1 == "mp":
        scene black
        "I decide to write a metaphorical poem."
    elif persistent.poem1 == "abs":
        scene black
        "I decide to write an abstract poem."
    else:
        $ renpy.error("persistent.poem1 should have been set to one of the four options for this block to be called, but it is "+persistent.poem1)
    return



label ch_mod_p2_reload:
    if persistent.poem2 == "cute":
        scene black
        "I decide to write a poem about insecurity."
    elif persistent.poem2 == "bs":
        scene black
        "I decide to write a poem about guilt."
    elif persistent.poem2 == "mp":
        scene black
        "I decide to write a poem about lust."
    elif persistent.poem2 == "abs":
        scene black
        "I decide to write a poem about imprisonment."
    else:
        $ renpy.error("persistent.poem2 should have been set to one of the four options for this block to be called, but it is "+persistent.poem2)
    return



label ch_mod_p3_reload:
    if persistent.poem3 == "cute":
        scene black
        "I decide to write a poem about literature."
    elif persistent.poem3 == "bs":
        scene black
        "I decide to write a poem about suicide."
    elif persistent.poem3 == "mp":
        scene black
        "I decide to write a poem about love."
    elif persistent.poem3 == "abs":
        scene black
        "I decide to write a poem."
    else:
        $ renpy.error("persistent.poem3 should have been set to one of the four options for this block to be called, but it is "+persistent.poem3)
    return
