label ch_mod_intro:
    $ delete_character("sayori")
    $ quick_menu = False
    $ config.allow_skipping = False
    $ config.keymap['dismiss'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    stop music
    play music g2
    window hide(None)
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 3.0
    hide screen tear
    stop music
    scene white
    play music t1g
    show intro with Dissolve(0.5, alpha=True)
    #pause 2.5
    pause 2.0
    hide intro
    show splash_gl
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    hide splash_gl
    show splash_n
    pause 0.25
    hide splash_n with Dissolve(0.5, alpha=True)
    show splash_warning "WARNING: Flashing colours after you dismiss the error dialog!\n-firelightning13" with Dissolve(0.5, alpha=True)
    pause 1.0
    hide splash_warning
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    stop music
    scene black with trueblack
    window auto
    $ config.keymap['dismiss'] = dismiss_keys
    $ renpy.display.behavior.clear_keymap_cache()

    $ renpy.call_screen("dialog", "Error: Script file is missing or corrupt.\nPlease reinstall the game.", ok_action=Return())
    scene black with trueblack
    pause 1.0
    show intro_rendered
    play music spoopy
    $ config.keymap['dismiss'] = []
    $ renpy.display.behavior.clear_keymap_cache()

    $ gtext = glitchtext(renpy.random.randint(12, 80))
    mc "[gtext]{nw}"
    $ consolehistory = []

    pause 0.5
    "Initiating \"DDLC: MC's Revenge\" mod{w=0.5}{nw}"
    "Initiating \"DDLC: MC's Revenge\" mod{fast}.{w=0.5}{nw}"
    "Initiating \"DDLC: MC's Revenge\" mod.{fast}.{w=0.5}{nw}"
    "Initiating \"DDLC: MC's Revenge\" mod..{fast}.{w=0.5}{nw}"
    "Initiating \"DDLC: MC's Revenge\" mod{fast}{w=0.5}{nw}"
    "Initiating \"DDLC: MC's Revenge\" mod{fast}.{w=0.5}{nw}"
    "Initiating \"DDLC: MC's Revenge\" mod.{fast}.{w=0.5}{nw}"
    call hideconsole
    $ config.keymap['dismiss'] = dismiss_keys
    $ renpy.display.behavior.clear_keymap_cache()

    $ currentpos = get_pos()
    stop music
    window hide(None)
    hide intro_rendered
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    play music g2
    pause 3.0
    hide screen tear
    stop music
    $ audio.spoopy = "<from " + str(currentpos) + " loop 105.51>mod_assets/sfx/spoopy_glitch.ogg"
    play music spoopy

    mc "Argh...."
    mc "What's this?"
    "I glance around."
    "I can't see anything."
    mc "Where am I?"
    "Where are these noises coming from?!"
    "Ah-"
    mc "What is happening to me...?"
    show intro_rendered
    $ gtext = glitchtext(renpy.random.randint(12, 80))
    mc "{cps=*0.5}Hell{/cps}{nw}"
    $ style.say_dialogue = style.edited
    mc "{cps=*2}Hell{fast}l111o000o who[gtext]{/cps}{nw}"

    play sound "sfx/s_kill_glitch1.ogg"
    hide intro_rendered
    scene bg sayori_bedroom
    window hide(None)
    pause 0.25
    scene black
    pause 0.75
    scene bg s_hang
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/glitch3.ogg"
    pause 0.25
    stop sound
    hide screen tear
    scene black
    pause 1.5
    play sound "sfx/s_kill_glitch1.ogg"
    scene bg s_hang_glitch
    pause 0.2
    stop sound
    scene black
    window show(None)
    $ style.say_dialogue = style.normal

    mc "What... {w}the heck?!"
    mc "What is this?!"
    "My head is spinning like crazy."
    mc "Arghh....!{nw}"
    mc "Why are you showing me that?!{nw}"
    mc "Who's that girl?!{nw}"
    mc "Who are you!?{nw}"
    pause 3.0

    stop music fadeout 2.0
    $ renpy.music.play(audio.ghostmenu, channel="trans", fadein=2.0, tight=True)
    show noise at noisefade(2) zorder 3
    "This room..."
    "It's getting closer..."
    "I can't move."
    "I can't go anywhere..."
    "Please help me..."
    "Help me, [player]..."
    $ renpy.call_screen("dialog", "Please help me.", ok_action=Return())

    $ renpy.music.stop(channel='trans', fadeout=None)
    play music g2
    window hide(None)
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    $ persistent.playthrough = 1
    $ renpy.utter_restart()
    return
