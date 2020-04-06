init 10 python:
    config.developer = "auto"

###### Custom persistent and variables ######

#############################################
default persistent.mc_awareness = [False, False, False, False, False, False, False, False, False, False, False, False, False] # These flags determine what ending you get.
    # flag 0: Refusing to check out the literature club
    # flag 1: Saying you read horror
    # flag 2: Accepting the invitation to join the literature club
    # flag 3: First poem-triggered Sayori dream
    # flag 4: Correctly remembering what Parfait Girls is about
    # flag 5: Correctly remembering what Portrait of Markov is about
    # flag 6: Skipping the fight between Yuri and Natsuki
    # flag 7: Checking the poster after day 2
    # flag 8: Second poem-triggered Sayori dream
    # flag 9: Seeing Yuri cutting in the hallway
    # flag 10: Stopping Yuri from cutting in the hallway
    # flag 11: Seeing Natsuki's neck snap
    # flag 12: Third poem-triggered Sayori dream

    # it IS possible to get all 13 of these flags, since you don't need Yuri's 3rd exclusive scene (it gives you persistent.left_yuri below)
    # max flags with Yuri's route: 10 (this means you CAN'T save Sayori on Yuri's route unless you get both the secret flags)
    # max flags before the final club meeting, including the two secret ones: 11/10 (Natsuki's/Yuri's route) - on Yuri's route day 4 doesn't contribute any of these flags
default persistent.mc_know_player = False # Whether MC has figured out that there's a being out there that's trying to guide him (but he still doesn't know he's in a game)
default persistent.sayori_revived = False
default persistent.mc_remember_sayori = False
default persistent.game_broken = False # Once a second character dies, the game becomes so broken that the new game button is disabled.
default persistent.realized_game_broken = False # Whether the player knows the game is broken
default persistent.lookup_portrait = False # Whether MC and Yuri have decided to look up the Portrait of Markov
default persistent.left_yuri = False # Whether MC walked out on Yuri during her third scene
default persistent.mod_cps = 50
#############################################
########## Curse words ############
default fword = "uck"
default fgword = "ucking"
default bword = "itch"
default aword = "sshole"
default sword = "hit"


#$ preferences.skip_unseen = False ## For future reference
# image movie_intro = Movie(play="file.ogv", pos=(0, 0), anchor=(0, 0)) ## Just incase if i need this

######################## Custom images ###############################
image splash_gl = "mod_assets/bg/splash_glitch.png"
image splash_n = "bg/splash.png"
image intro_rendered:
    "mod_assets/gl/01.png"
    pause 0.5
    "black"
    pause 1.0
    "mod_assets/gl/02.png"
    pause 0.2
    "mod_assets/gl/03.png"
    pause 0.2
    "mod_assets/gl/04.png"
    pause 0.2
    "black"
    pause 1.0
    "mod_assets/gl/05.png"
    pause 0.5
    "mod_assets/gl/06.png"
    pause 0.5
    "black"
    pause 1.0
    "mod_assets/gl/07.png"
    pause 0.3
    "mod_assets/gl/08.png"
    pause 0.3
    "mod_assets/gl/09.png"
    pause 0.5
    "mod_assets/gl/10.png"
    pause 0.2
    repeat
image bg s_hang = "mod_assets/cg/s_hang.png"
image s_alive:
    truecenter
    zoom 0.75
    "mod_assets/cg/s_alive.png"
#    subpixel True
#transform s_alive_start:
#    truecenter
#    xalign 0.3 yalign 0.25 zoom 0.8
#    linear 4 zoom 0.75 xalign 0.315 yoffset 10
image bg s_hang_glitch = "mod_assets/cg/s_hang_glitch.png"
image bg s_hang_black = "mod_assets/cg/123213.png"
image bg spoopy = "bg/club-skill.png"
image bg res_gl = "mod_assets/bg/residential_glitch.png"
image bg monika_house = "images/bg/house.jpg"
image p1 = "mod_assets/bg/p1.png"
image p1b = "mod_assets/bg/p1b.png"
image p1a = "mod_assets/bg/p1a.png"
image bg res_gl2 = "mod_assets/bg/residential_glitch2.png"
image bg cr_gl = "mod_assets/bg/class_glitch.png"
image bg cord_gl = "mod_assets/bg/corridor_glitch.png"
image s_hacker = "mod_assets/cg/s_hacker.png"
image bg club_gl = "mod_assets/bg/club_room_glitch.png"
image club_gl2 = "mod_assets/bg/club_room_glitch.png"
image mod_one_eye = "mod_assets/cg/one_eye_gl.png"
image m_smile = "mod_assets/cg/m_smile.png"
image end_credit1 = "mod_assets/cg/end_credit1.png"
image end_credit2 = "mod_assets/cg/end_credit2.png"
image natsuki gl:
    "natsuki 1w"
    0.25
    parallel:
        0.01
        "mod_assets/natsuki/1.png"
        0.01
        "mod_assets/natsuki/2.png"
        0.01
        "mod_assets/natsuki/3.png"
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
######################################################################

################ Custom Transformations and Styles ###################
style window_lq is window:
    background Image("mod_assets/textbox_lq.png", xalign=0.5, yalign=1.0)

style window_ghost is window:
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0, alpha=0.5)

style jp is default:
    font "mod_assets/gui/MSGOTHIC.ttf"
    #kerning 8
    outlines [(10, "#000", 0, 0)]
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

transform m_pos:
    xpos 320
    ypos 500

### f21(400) and t22(880) | f32(640) and f33(1040); refer to day2.rpy
transform mod_pos_gl(x=540, alt_x=640, z=0.80):
    yanchor 1.0 ypos 1.03 subpixel True
    block:
        xcenter alt_x zoom z*1.05
        alpha 1.00
        parallel:
            easein .3 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset 0
        repeat
    time 1.5
    xcenter x

transform mod_finstant(x=400, z=0.80): # special finstant for yuri; refer to day2.rpy
        xcenter x yoffset 0 zoom z*1.05 alpha 1.00 yanchor 1.0 ypos 1.03

transform mod_malpha(a=1.00):
    i31
    alpha a
######################################################################

####################### Custom audio #################################
define audio.t1g = "mod_assets/sfx/1g.ogg"
define audio.spoopy = "<loop 105.51>mod_assets/sfx/spoopy_glitch.ogg"
define audio.aglitch1 = "mod_assets/sfx/glitch1.ogg"
define audio.t3l = "<loop 4.618>mod_assets/sfx/3l.ogg"
define audio.ap1 = "mod_assets/sfx/p1.ogg"
define audio.aglitch2 = "<loop 0>mod_assets/sfx/glitch2.ogg"
define audio.t2l = "<loop 4.499>mod_assets/sfx/2l.ogg"
define audio.t2o = "<loop 4.492>mod_assets/sfx/2o.ogg"
define audio.gb_gl = "mod_assets/sfx/gb_gl.ogg"
define audio.throw = "mod_assets/sfx/whoosh.ogg" # I know this isn't realistic ffs
define audio.sgl = "mod_assets/sfx/select_gl.ogg"
define audio.t2gl = "<loop 4.492>mod_assets/sfx/2gl.ogg"
define audio.t9gl = "<loop 3.172>mod_assets/sfx/9gl.ogg"
define audio.t666 = "<loop 10.893>mod_assets/sfx/666.ogg"
define audio.ggg = "mod_assets/sfx/ggg.ogg"
define audio.s_gl = "mod_assets/sfx/s_gl.ogg"
define audio.fall_gl = "mod_assets/sfx/fall_gl.ogg"
define audio.gl = "mod_assets/sfx/gl.ogg"
define audio.tgl3 = "<loop 4.444>mod_assets/sfx/glitch3.ogg"
define audio.tpj = "<loop 0>mod_assets/sfx/pj.ogg"
define audio.t7fast = "<loop 31.880>bgm/7g.ogg"
define audio.start_gl = "<loop 0>mod_assets/sfx/start_gl.ogg"
define audio.t8g = "<loop 9.938>mod_assets/sfx/8g.ogg"
define audio.t8g2 = "mod_assets/sfx/8g2.ogg"
define audio.dhglitch = "mod_assets/sfx/dhg.ogg"
define audio.dhglitch2 = "<loop 6.424>mod_assets/sfx/dhg2.ogg"
define audio.t99 = "<loop 3.172>mod_assets/sfx/monika_r_u_ok.ogg"
define audio.endc = "<loop 3.172>mod_assets/sfx/end_credit.ogg"
define audio.ngl = "mod_assets/sfx/ngl.ogg"
define audio.end7 = "mod_assets/sfx/7end.ogg"
define audio.punch = "mod_assets/sfx/punch.ogg"
define audio.confront = "<to 67 loop 0.7>mod_assets/sfx/ourreality2.ogg"
define audio.hurry = "<to 91>mod_assets/sfx/hurry.ogg"
define audio.secondbest = "<loop 0>mod_assets/sfx/festival.ogg"
######################################################################

####################### Sayori pajama sprites ########################
image sayori 1ca = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1cb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1cc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1cd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1ce = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1cf = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1cg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1ch = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1ci = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1cj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1ck = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1cl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1cm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1cn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1co = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1cp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1cq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1cr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1cs = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1ct = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1cu = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1cv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1cw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1cx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1cy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2ca = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2cb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2cc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2cd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2ce = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2cf = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2cg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2ch = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2ci = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2cj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2ck = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2cl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2cm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2cn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2co = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2cp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2cq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2cr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2cs = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2ct = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2cu = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2cv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2cw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2cx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2cy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/1l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3ca = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3cb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3cc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3cd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3ce = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3cf = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3cg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3ch = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3ci = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3cj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3ck = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3cl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3cm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3cn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3co = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3cp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3cq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3cr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3cs = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3ct = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3cu = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3cv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3cw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3cx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3cy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4ca = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4cb = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4cc = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4cd = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4ce = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4cf = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4cg = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4ch = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4ci = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4cj = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4ck = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4cl = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4cm = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4cn = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4co = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4cp = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4cq = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4cr = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4cs = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4ct = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4cu = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4cv = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4cw = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4cx = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4cy = im.Composite((960, 960), (0, 0), "mod_assets/sayori/2l.png", (0, 0), "mod_assets/sayori/2r.png", (0, 0), "sayori/y.png")
######################################################################
####################### Monika crying sprites ########################
image monika cry1 = im.Composite((960, 960), (0, 0), "mod_assets/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/monika/2_face/base.png", (0, 0), "mod_assets/monika/2_face/1_mouth/3.png", (0, 0), "mod_assets/monika/2_face/2_nose/1.png", (0, 0), "mod_assets/monika/2_face/3_eyes/g.png", (0, 0), "mod_assets/monika/2_face/4_eyebrows/4.png")
image monika cry2 = im.Composite((960, 960), (0, 0), "mod_assets/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/monika/2_face/base.png", (0, 0), "mod_assets/monika/2_face/1_mouth/4.png", (0, 0), "mod_assets/monika/2_face/2_nose/1.png", (0, 0), "mod_assets/monika/2_face/3_eyes/i.png", (0, 0), "mod_assets/monika/2_face/4_eyebrows/4.png")
image monika cry3 = im.Composite((960, 960), (0, 0), "mod_assets/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/monika/2_face/base.png", (0, 0), "mod_assets/monika/2_face/1_mouth/4.png", (0, 0), "mod_assets/monika/2_face/2_nose/1.png", (0, 0), "mod_assets/monika/2_face/3_eyes/i.png", (0, 0), "mod_assets/monika/2_face/4_eyebrows/2.png")
#image monika cry4 = im.Composite((960, 960), (0, 0), "mod_assets/monika/1_uniform/1_body_left/1.png", (0, 0), "mod_assets/monika/1_uniform/2_body_right/1.png", (0, 0), "mod_assets/monika/2_face/base.png", (0, 0), "mod_assets/monika/2_face/1_mouth/4.png", (0, 0), "mod_assets/monika/2_face/2_nose/3.png", (0, 0), "mod_assets/monika/2_face/3_eyes/2.png", (0, 0), "mod_assets/monika/2_face/4_eyebrows/2.png")
######################################################################
### And single MC sprite :)
image mc = im.Composite((960, 960), (0, 0), "mod_assets/mc_body.png", (0, 0), "mod_assets/mc_head.png")

###################### Custom Functions ############################
init python:
    def ModWarningSave():
            if not player: return
            persistent.playername = player
            renpy.hide_screen("confirm")
            renpy.jump_out_of_context("start")

    def monika_showed_up(event, interact=True, **kwargs):
        if event == "begin":
            config.keymap['dismiss'] = []
            renpy.display.behavior.clear_keymap_cache()
        elif event == "slow_done":
            config.keymap['dismiss'] = dismiss_keys
            renpy.display.behavior.clear_keymap_cache()

    def check_character_file(name):
        try: renpy.file("../characters/"+name+".chr")
        except: return False
        return True

    def mc_awareness_total():
        i = 0
        for flag in persistent.mc_awareness:
            if flag: i += 1
        return i

    def realize_game_broken():
        persistent.realized_game_broken = True
        renpy.hide_screen("dialog")
   
    def full_reset():
        renpy.music.stop()
        delete_all_saves()
        renpy.loadsave.location.unlink_persistent()
        renpy.persistent.should_save_persistent = False
        renpy.utter_restart()

    def no_return():
        delete_all_saves()
        renpy.take_screenshot()
        renpy.save("1-1", "autosave")

    renpy.music.register_channel("trans", mixer="music", tight=True)
