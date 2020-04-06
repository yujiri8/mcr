label sayori_dream_1:
    with wipeleft_scene
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
    pause 1.0
    scene bg bedroom
    $ persistent.mc_awareness[3] = True
    "Argh..."
    "I had a bad dream..."
    if mod_chapter == 1:
        "...Wait, didn't I have that same dream yesterday?"
    else:
        "...Wait, didn't I have that same dream the day I started going to the literature club?"
    "I sit up."
    "And the girl looked eerily familiar, too..."
    "Ah, whatever. It was just a dream."
    "It's pretty late right now. I'd better get to school!"
    return

label sayori_dream_2:
    scene s_hacker
    play sound dhglitch
    $ s_name = "S" + glitchtext(1) + "a" + glitchtext(1) + "y" + glitchtext(1) + "o" + glitchtext(1) + "r" + glitchtext(1) + "i"
    s "[player] help me!!{w=1.5}{nw}"
    pause 1.5
    $ s_name = "Sayori"
    scene bg s_hang
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    scene bg bedroom
    $ persistent.mc_awareness[8] = True
    "I wake up breathing hard."
    "Another dream..."
    "Was it the same girl?"
    "Just who {i}is{/i} she?"
    "It's driving me insane..."
    "Oh well. Better get to school."
    return

label sayori_dream_3:
    scene bg s_hang_black
    play sound s_gl
    mc "No, no no no...{w=1}{nw}"
    scene m_smile
    play sound aglitch2
    pause 1.0
    scene bg s_hang
    play music td
    mc "NOOOO!!{w=2}{nw}"
    stop music
    scene bg bedroom
    "I wake up again."
    "S[sword]... it felt so real that time..."
    "I just {i}know{/i} that girl is someone I know! Or someone I used to know..."
    $ persistent.mc_awareness[12] = True
    "{i}Sayori{/i}."
    "That was her name."
    "But what in the hell happened to her?"
    "Something that made me forget about her..."
    "Did I lose my memories, like Natsuki?"
    "God, everything is so f[fword]ed up ever since the day I joined this club..."
    "But I have to stay."
    "I think I'm going to get to the bottom of this soon."
    return