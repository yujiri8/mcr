screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.8
        spacing gui.navigation_spacing

        #if not persistent.autoload or not main_menu:

        if main_menu:
            if not persistent.game_broken:
                textbutton _("New Game") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
            else:
                $ gtext = glitchtext(20)
                $ gtext2 = glitchtext(60)
                textbutton _(gtext) action Show(screen="dialog", message=gtext2, ok_action=Function(realize_game_broken))
        else:
            textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]
            textbutton _("Save Game") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]
        textbutton _("Load Game") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]
        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()
        else:
            textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]
        if renpy.variant("pc"):
            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action Help("README.html")
            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("Quit") action Quit(confirm=not main_menu)

screen main_menu():
    # This ensures that any other menu screen is replaced.
    tag menu
    style_prefix "main_menu"
    add "menu_bg"
    add "menu_art_y"
    add "menu_art_n"
    if not persistent.sayori_revived:
        add "menu_art_s_glitch"
    else:
        add "menu_art_s"
    add "menu_art_m"
    frame:
        pass

## The use statement includes another screen inside this one. The actual
## contents of the main menu are in the navigation screen.
    use navigation
    
    add "menu_particles"
    add "menu_particles"
    add "menu_particles"
    add "menu_particles"
    add "menu_fade"
    add "menu_logo_mod"

    if gui.show_name:
        vbox:
            if persistent.playthrough > 0:
                text "[config.name!t]":
                    style "main_menu_title"
                text "v[config.version], by Yujiri":
                    style "main_menu_version"

    key "K_ESCAPE" action Quit(confirm=False)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

style main_menu_frame:
    xsize 310
    yfill True

    background "menu_nav"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size

############################### Confirmation Box #################################

#image confirm_glitch:
#    "gui/overlay/confirm_glitch.png"
#    pause 0.02
#    "gui/overlay/confirm_glitch2.png"
#    pause 0.02
#    repeat

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    #key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")
