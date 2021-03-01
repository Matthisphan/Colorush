# Animation des monstres et du joueur
from random import randint
import pygame
#import os
#os.chdir("C:/Users/matth/Documents/Colorush")
from Colorush_settings import *
clock = pygame.time.Clock()

screen = (800, 400)
window = pygame.display.set_mode(screen)
keys = pygame.key.get_pressed()

# Animation de Mog (pnj des règles)
mog1 = pygame.image.load("Mog_Rule/wait_mog_1.png")
mog1.convert()
mog1a = pygame.image.load("Mog_Rule/wait_mog_1a.png")
mog1a.convert()
mog2 = pygame.image.load("Mog_Rule/wait_mog_2.png")
mog2.convert()
mog2a = pygame.image.load("Mog_Rule/wait_mog_2a.png")
mog2a.convert()
mog3 = pygame.image.load("Mog_Rule/wait_mog_3.png")
mog3.convert()
mog3a = pygame.image.load("Mog_Rule/wait_mog_3a.png")
mog3a.convert()
mog4 = pygame.image.load("Mog_Rule/wait_mog_4.png")
mog4.convert()
mog4a = pygame.image.load("Mog_Rule/wait_mog_4a.png")
mog4a.convert()
mog5 = pygame.image.load("Mog_Rule/wait_mog_5.png")
mog5.convert()
mog5a = pygame.image.load("Mog_Rule/wait_mog_5a.png")
mog5a.convert()
mog6 = pygame.image.load("Mog_Rule/wait_mog_6.png")
mog6.convert()
mog6a = pygame.image.load("Mog_Rule/wait_mog_6a.png")
mog6a.convert()
moglist = [mog1, mog1a, mog2, mog2a, mog3, mog3a, mog4, mog4a, mog5, mog5a, mog6, mog6a]


class Mog(object):
    def __init__(self):
        self.mog_count = 0

    def draw(self, window):
        if self.mog_count <= 11:
            window.blit(moglist[self.mog_count], [600, 228])
            self.mog_count += 1
        else:
            self.mog_count = 0
            window.blit(moglist[self.mog_count], [600, 228])
            mog_count = 1


mog = Mog()

# Animation dialogue1 règle
tchat1 = pygame.image.load("other/Dialogue1/tchat1.png")
tchat1.convert()
tchat1a = pygame.image.load("other/Dialogue1/tchat1a.png")
tchat1a.convert()
tchat1b = pygame.image.load("other/Dialogue1/tchat1b.png")
tchat1b.convert()
tchat1c = pygame.image.load("other/Dialogue1/tchat1c.png")
tchat1c.convert()
tchat1d = pygame.image.load("other/Dialogue1/tchat1d.png")
tchat1d.convert()
tchat2 = pygame.image.load("other/Dialogue1/tchat2.png")
tchat2.convert()
tchat2a = pygame.image.load("other/Dialogue1/tchat2a.png")
tchat2a.convert()
tchat2b = pygame.image.load("other/Dialogue1/tchat2b.png")
tchat2b.convert()
tchat2c = pygame.image.load("other/Dialogue1/tchat2c.png")
tchat2c.convert()
tchat2d = pygame.image.load("other/Dialogue1/tchat2d.png")
tchat2d.convert()
dialogue_1 = [tchat1, tchat1a, tchat1b, tchat1c, tchat1d, tchat2, tchat2a, tchat2b, tchat2c, tchat2d]


class Dialogue1(object):
    def __init__(self):
        self.dialogue1_count = 0

    def draw(self, window):
        if self.dialogue1_count <= 9:
            window.blit(dialogue_1[self.dialogue1_count], [50, 100])
            self.dialogue1_count += 1
        else:
            self.dialogue1_count = 0
            window.blit(dialogue_1[self.dialogue1_count], [50, 100])
            dialogue1_count = 1


dialogue1 = Dialogue1()

# Animation dialogue2 règle
Tchat1 = pygame.image.load("other/Dialogue2/tchat1.png")
Tchat1.convert()
Tchat1a = pygame.image.load("other/Dialogue2/tchat1a.png")
Tchat1a.convert()
Tchat1b = pygame.image.load("other/Dialogue2/tchat1b.png")
Tchat1b.convert()
Tchat1c = pygame.image.load("other/Dialogue2/tchat1c.png")
Tchat1c.convert()
Tchat1d = pygame.image.load("other/Dialogue2/tchat1d.png")
Tchat1d.convert()
Tchat2 = pygame.image.load("other/Dialogue2/tchat2.png")
Tchat2.convert()
Tchat2a = pygame.image.load("other/Dialogue2/tchat2a.png")
Tchat2a.convert()
Tchat2b = pygame.image.load("other/Dialogue2/tchat2b.png")
Tchat2b.convert()
Tchat2c = pygame.image.load("other/Dialogue2/tchat2c.png")
Tchat2c.convert()
Tchat2d = pygame.image.load("other/Dialogue2/tchat2d.png")
Tchat2d.convert()
dialogue_2 = [Tchat1, Tchat1a, Tchat1b, Tchat1c, Tchat1d, Tchat2, Tchat2a, Tchat2b, Tchat2c, Tchat2d]


class Dialogue2(object):
    def __init__(self):
        self.dialogue2_count = 0

    def draw(self, window):
        if self.dialogue2_count <= 9:
            window.blit(dialogue_2[self.dialogue2_count], [50, 100])
            self.dialogue2_count += 1
        else:
            self.dialogue2_count = 0
            window.blit(dialogue_2[self.dialogue2_count], [50, 100])
            dialogue2_count = 1


dialogue2 = Dialogue2()

# Animation dialogue3 règle
Tchaat1 = pygame.image.load("other/Dialogue3/tchat1.png")
Tchaat1.convert()
Tchaat2 = pygame.image.load("other/Dialogue3/tchat2.png")
Tchaat2.convert()
Tchat3 = pygame.image.load("other/Dialogue3/tchat3.png")
Tchat3.convert()
Tchat4 = pygame.image.load("other/Dialogue3/tchat4.png")
Tchat4.convert()
Tchat5 = pygame.image.load("other/Dialogue3/tchat5.png")
Tchat5.convert()
Tchat6 = pygame.image.load("other/Dialogue3/tchat6.png")
Tchat6.convert()
Tchat7 = pygame.image.load("other/Dialogue3/tchat7.png")
Tchat7.convert()
Tchat8 = pygame.image.load("other/Dialogue3/tchat8.png")
Tchat8.convert()
Tchat9 = pygame.image.load("other/Dialogue3/tchat9.png")
Tchat9.convert()
Tchat10 = pygame.image.load("other/Dialogue3/tchat10.png")
Tchat10.convert()
Tchat11 = pygame.image.load("other/Dialogue3/tchat11.png")
Tchat11.convert()
dialogue_3 = [Tchaat1, Tchaat2, Tchat3, Tchat4, Tchat5, Tchat6, Tchat7, Tchat8, Tchat9, Tchat10, Tchat11]


class Dialogue3(object):
    def __init__(self):
        self.dialogue3_count = 0

    def draw(self, window):
        if self.dialogue3_count <= 9:
            window.blit(dialogue_3[self.dialogue3_count], [50, 100])
            self.dialogue3_count += 1
        else:
            self.dialogue3_count = 0
            window.blit(dialogue_3[self.dialogue3_count], [50, 100])
            dialogue3_count = 1


dialogue3 = Dialogue3()

# Animation titre colorush
title0 = pygame.image.load("background/Menu/Colorush_animation/Colorush_title0.png")
title0.convert()
title1 = pygame.image.load("background/Menu/Colorush_animation/Colorush_title1.png")
title1.convert()
title2 = pygame.image.load("background/Menu/Colorush_animation/Colorush_title2.png")
title2.convert()
title3 = pygame.image.load("background/Menu/Colorush_animation/Colorush_title3.png")
title3.convert()
title4 = pygame.image.load("background/Menu/Colorush_animation/Colorush_title4.png")
title4.convert()
title5 = pygame.image.load("background/Menu/Colorush_animation/Colorush_title5.png")
title5.convert()
title6 = pygame.image.load("background/Menu/Colorush_animation/Colorush_title6.png")
title6.convert()
title7 = pygame.image.load("background/Menu/Colorush_animation/Colorush_title7.png")
title7.convert()
title8 = pygame.image.load("background/Menu/Colorush_animation/Colorush_title8.png")
title8.convert()
title9 = pygame.image.load("background/Menu/Colorush_animation/Colorush_title9.png")
title9.convert()
titlecolorush = [title0, title1, title2, title3, title4, title5, title6, title7, title8, title9]


class Title(object):
    def __init__(self):
        self.title_count = 0

    def draw(self, window):
        if self.title_count <= 9:
            window.blit(titlecolorush[self.title_count], [200, 50])
            self.title_count += 1
        else:
            self.title_count = 0
            window.blit(titlecolorush[self.title_count], [200, 50])
            title_count = 1


Colorush_title = Title()


# Animation marche link vert
walk_gl1 = pygame.image.load("Green_Link/marche/walk_green_link1.png")
walk_gl1.convert()
walk_gl2 = pygame.image.load("Green_Link/marche/walk_green_link2.png")
walk_gl2.convert()
walk_gl3 = pygame.image.load("Green_Link/marche/walk_green_link3.png")
walk_gl3.convert()
walk_gl4 = pygame.image.load("Green_Link/marche/walk_green_link4.png")
walk_gl4.convert()
walk_gl5 = pygame.image.load("Green_Link/marche/walk_green_link5.png")
walk_gl5.convert()
walk_gl6 = pygame.image.load("Green_Link/marche/walk_green_link6.png")
walk_gl6.convert()
walk_gl7 = pygame.image.load("Green_Link/marche/walk_green_link7.png")
walk_gl7.convert()
walk_gl8 = pygame.image.load("Green_Link/marche/walk_green_link8.png")
walk_gl8.convert()
walk_gl9 = pygame.image.load("Green_Link/marche/walk_green_link9.png")
walk_gl9.convert()
walk_gl10 = pygame.image.load("Green_Link/marche/walk_green_link10.png")
walk_gl10.convert()
walkgreenlink = [walk_gl10, walk_gl9, walk_gl8, walk_gl7, walk_gl6, walk_gl5, walk_gl4, walk_gl3, walk_gl2, walk_gl1]
    # Animation mort link vert
dead_gl1 = pygame.image.load("Green_Link/mort/dead_green_link1.png")
dead_gl1.convert()
dead_gl2 = pygame.image.load("Green_Link/mort/dead_green_link2.png")
dead_gl2.convert()
dead_gl3 = pygame.image.load("Green_Link/mort/dead_green_link3.png")
dead_gl3.convert()
dead_gl4 = pygame.image.load("Green_Link/mort/dead_green_link4.png")
dead_gl4.convert()
dead_gl5 = pygame.image.load("Green_Link/mort/dead_green_link5.png")
dead_gl5.convert()
dead_gl6 = pygame.image.load("Green_Link/mort/dead_green_link6.png")
dead_gl6.convert()
dead_gl7 = pygame.image.load("Green_Link/mort/dead_green_link7.png")
dead_gl7.convert()
dead_gl8 = pygame.image.load("Green_Link/mort/dead_green_link8.png")
dead_gl8.convert()
dead_gl9 = pygame.image.load("Green_Link/mort/dead_green_link9.png")
dead_gl9.convert()
deadgreenlink = [dead_gl1, dead_gl2, dead_gl3, dead_gl4, dead_gl5, dead_gl6, dead_gl7, dead_gl8, dead_gl9]
reglesgreenlink = [dead_gl1, dead_gl1, dead_gl1, dead_gl1, dead_gl1, dead_gl3, dead_gl3, dead_gl3, dead_gl3, dead_gl3]


class Greenplayer(object):
    def __init__(self):
        self.link_walk_count = 0
        self.link_dead_count = 0
        self.link_regles_count = 0

    def draw(self, window):
        if self.link_walk_count <= 9:
            window.blit(walkgreenlink[self.link_walk_count], [10, 278])
            self.link_walk_count += 1
        else:
            self.link_walk_count = 0
            window.blit(walkgreenlink[self.link_walk_count], [10, 278])
            link_walk_count = 1

    def mort(self, window):
        if self.link_dead_count < 9:
            window.blit(deadgreenlink[self.link_dead_count], [10, 278])
            self.link_dead_count += 1

    def regles(self, window):
        if self.link_regles_count <= 9:
            window.blit(reglesgreenlink[self.link_regles_count], [10, 278])
            self.link_regles_count += 1
        else:
            self.link_regles_count = 0
            window.blit(reglesgreenlink[self.link_regles_count], [10, 278])


greenlink = Greenplayer()


# Animation marche monstre vert
walk_gm1 = pygame.image.load("Green_Monster/marche/walk_green_monster1.png")
walk_gm1.convert()
walk_gm2 = pygame.image.load("Green_Monster/marche/walk_green_monster2.png")
walk_gm2.convert()
walk_gm3 = pygame.image.load("Green_Monster/marche/walk_green_monster3.png")
walk_gm3.convert()
walk_gm4 = pygame.image.load("Green_Monster/marche/walk_green_monster4.png")
walk_gm4.convert()
walk_gm5 = pygame.image.load("Green_Monster/marche/walk_green_monster5.png")
walk_gm5.convert()
walk_gm6 = pygame.image.load("Green_Monster/marche/walk_green_monster6.png")
walk_gm6.convert()
walkgreenmonster = [walk_gm1, walk_gm2, walk_gm3, walk_gm4, walk_gm5, walk_gm6]
    # Animation mort monstre vert
dead_gm1 = pygame.image.load("Green_Monster/mort/dead_green_monster1.png")
dead_gm1.convert()
dead_gm2 = pygame.image.load("Green_Monster/mort/dead_green_monster2.png")
dead_gm2.convert()
dead_gm3 = pygame.image.load("Green_Monster/mort/dead_green_monster3.png")
dead_gm3.convert()
dead_gm4 = pygame.image.load("Green_Monster/mort/dead_green_monster4.png")
dead_gm4.convert()
dead_gm5 = pygame.image.load("Green_Monster/mort/dead_green_monster5.png")
dead_gm5.convert()
dead_gm6 = pygame.image.load("Green_Monster/mort/dead_green_monster6.png")
dead_gm6.convert()
dead_gm7 = pygame.image.load("Green_Monster/mort/dead_green_monster7.png")
dead_gm7.convert()
dead_gm8 = pygame.image.load("Green_Monster/mort/dead_green_monster8.png")
dead_gm8.convert()
dead_gm9 = pygame.image.load("Green_Monster/mort/dead_green_monster9.png")
dead_gm9.convert()
dead_gm10 = pygame.image.load("Green_Monster/mort/dead_green_monster10.png")
dead_gm10.convert()
deadgreenmonster = [dead_gm1, dead_gm2, dead_gm3, dead_gm4, dead_gm5, dead_gm6, dead_gm7, dead_gm8, dead_gm9, dead_gm10]


class GreenMonster(object):
    def __init__(self):
        self.monster_walk_count = 0
        self.monster_dead_count = 0

    def draw(self, window, x_greenmonster):
        if self.monster_walk_count <= 5:
            window.blit(walkgreenmonster[self.monster_walk_count], [x_greenmonster, 220])
            self.monster_walk_count += 1
        else:
            self.monster_walk_count = 0
            window.blit(walkgreenmonster[self.monster_walk_count], [x_greenmonster, 220])
            monster_walk_count = 1

    def mort(self, window):
        if self.monster_dead_count <= 9:
            window.blit(deadgreenmonster[self.monster_dead_count], [10, 220])
            self.monster_dead_count += 1
        else:
            self.monster_dead_count = 0


greenmonster = GreenMonster()

# Animation marche link violet
walk_pl1 = pygame.image.load("Purple_Link/marche/walk_purple_link1.png")
walk_pl1.convert()
walk_pl2 = pygame.image.load("Purple_Link/marche/walk_purple_link2.png")
walk_pl2.convert()
walk_pl3 = pygame.image.load("Purple_Link/marche/walk_purple_link3.png")
walk_pl3.convert()
walk_pl4 = pygame.image.load("Purple_Link/marche/walk_purple_link4.png")
walk_pl4.convert()
walk_pl5 = pygame.image.load("Purple_Link/marche/walk_purple_link5.png")
walk_pl5.convert()
walk_pl6 = pygame.image.load("Purple_Link/marche/walk_purple_link6.png")
walk_pl6.convert()
walk_pl7 = pygame.image.load("Purple_Link/marche/walk_purple_link7.png")
walk_pl7.convert()
walk_pl8 = pygame.image.load("Purple_Link/marche/walk_purple_link8.png")
walk_pl8.convert()
walk_pl9 = pygame.image.load("Purple_Link/marche/walk_purple_link9.png")
walk_pl9.convert()
walk_pl10 = pygame.image.load("Purple_Link/marche/walk_purple_link10.png")
walk_pl10.convert()
walkpurplelink = [walk_pl10, walk_pl9, walk_pl8, walk_pl7, walk_pl6, walk_pl5, walk_pl4, walk_pl3, walk_pl2, walk_pl1]
    # Animation mort link violet
dead_pl1 = pygame.image.load("Purple_Link/mort/dead_purple_link1.png")
dead_pl1.convert()
dead_pl2 = pygame.image.load("Purple_Link/mort/dead_purple_link2.png")
dead_pl2.convert()
dead_pl3 = pygame.image.load("Purple_Link/mort/dead_purple_link3.png")
dead_pl3.convert()
dead_pl4 = pygame.image.load("Purple_Link/mort/dead_purple_link4.png")
dead_pl4.convert()
dead_pl5 = pygame.image.load("Purple_Link/mort/dead_purple_link5.png")
dead_pl5.convert()
dead_pl6 = pygame.image.load("Purple_Link/mort/dead_purple_link6.png")
dead_pl6.convert()
dead_pl7 = pygame.image.load("Purple_Link/mort/dead_purple_link7.png")
dead_pl7.convert()
dead_pl8 = pygame.image.load("Purple_Link/mort/dead_purple_link8.png")
dead_pl8.convert()
dead_pl9 = pygame.image.load("Purple_Link/mort/dead_purple_link9.png")
dead_pl9.convert()
deadpurplelink = [dead_pl1, dead_pl2, dead_pl3, dead_pl4, dead_pl5, dead_pl6, dead_pl7, dead_pl8, dead_pl9]
reglespurplelink = [dead_pl1, dead_pl1, dead_pl1, dead_pl1, dead_pl1, dead_pl3, dead_pl3, dead_pl3, dead_pl3, dead_pl3]


class Purpleplayer(object):
    def __init__(self):
        self.link_walk_count = 0
        self.link_dead_count = 0
        self.link_regles_count = 0

    def draw(self, window):
        if self.link_walk_count <= 9:
            window.blit(walkpurplelink[self.link_walk_count], [10, 278])
            self.link_walk_count += 1
        else:
            self.link_walk_count = 0
            window.blit(walkpurplelink[self.link_walk_count], [10, 278])
            link_walk_count = 1

    def mort(self, window):
        if self.link_dead_count < 9:
            window.blit(deadpurplelink[self.link_dead_count], [10, 278])
            self.link_dead_count += 1

    def regles(self, window):
        if self.link_regles_count <= 9:
            window.blit(reglespurplelink[self.link_regles_count], [10, 278])
            self.link_regles_count += 1
        else:
            self.link_regles_count = 0
            window.blit(reglespurplelink[self.link_regles_count], [10, 278])


purplelink = Purpleplayer()


# Animation marche monstre violet
walk_pm1 = pygame.image.load("Purple_Monster/marche/walk_purple_monster1.png")
walk_pm1.convert()
walk_pm2 = pygame.image.load("Purple_Monster/marche/walk_purple_monster2.png")
walk_pm2.convert()
walk_pm3 = pygame.image.load("Purple_Monster/marche/walk_purple_monster3.png")
walk_pm3.convert()
walk_pm4 = pygame.image.load("Purple_Monster/marche/walk_purple_monster4.png")
walk_pm4.convert()
walkpurplemonster = [walk_pm1, walk_pm2, walk_pm3, walk_pm4]
    # Animation mort monstre violet
dead_pm1 = pygame.image.load("Purple_Monster/mort/dead_purple_monster1.png")
dead_pm1.convert()
dead_pm2 = pygame.image.load("Purple_Monster/mort/dead_purple_monster2.png")
dead_pm2.convert()
dead_pm3 = pygame.image.load("Purple_Monster/mort/dead_purple_monster3.png")
dead_pm3.convert()
dead_pm4 = pygame.image.load("Purple_Monster/mort/dead_purple_monster4.png")
dead_pm4.convert()
dead_pm5 = pygame.image.load("Purple_Monster/mort/dead_purple_monster5.png")
dead_pm5.convert()
dead_pm6 = pygame.image.load("Purple_Monster/mort/dead_purple_monster6.png")
dead_pm6.convert()
dead_pm7 = pygame.image.load("Purple_Monster/mort/dead_purple_monster7.png")
dead_pm7.convert()
dead_pm8 = pygame.image.load("Purple_Monster/mort/dead_purple_monster8.png")
dead_pm8.convert()
deadpurplemonster = [dead_pm1, dead_pm2, dead_pm3, dead_pm4, dead_pm5, dead_pm6, dead_pm7, dead_pm8]


class PurpleMonster(object):
    def __init__(self):
        self.monster_walk_count = 0
        self.monster_dead_count = 0

    def draw(self, window, x_purplemonster):
        if self.monster_walk_count <= 3:
            window.blit(walkpurplemonster[self.monster_walk_count], [x_purplemonster, 227])
            self.monster_walk_count += 1
        else:
            self.monster_walk_count = 0
            window.blit(walkpurplemonster[self.monster_walk_count], [x_purplemonster, 227])
            monster_walk_count = 1

    def mort(self, window):
        if self.monster_dead_count <= 7:
            window.blit(deadpurplemonster[self.monster_dead_count], [30, 227])
            self.monster_dead_count += 1
        else:
            self.monster_dead_count = 0


purplemonster = PurpleMonster()

# Animation marche link rouge
walk_r1 = pygame.image.load("Red_Link/marche/walk_red_link1.png")
walk_r1.convert()
walk_r2 = pygame.image.load("Red_Link/marche/walk_red_link2.png")
walk_r2.convert()
walk_r3 = pygame.image.load("Red_Link/marche/walk_red_link3.png")
walk_r3.convert()
walk_r4 = pygame.image.load("Red_Link/marche/walk_red_link4.png")
walk_r4.convert()
walk_r5 = pygame.image.load("Red_Link/marche/walk_red_link5.png")
walk_r5.convert()
walk_r6 = pygame.image.load("Red_Link/marche/walk_red_link6.png")
walk_r6.convert()
walk_r7 = pygame.image.load("Red_Link/marche/walk_red_link7.png")
walk_r7.convert()
walk_r8 = pygame.image.load("Red_Link/marche/walk_red_link8.png")
walk_r8.convert()
walk_r9 = pygame.image.load("Red_Link/marche/walk_red_link9.png")
walk_r9.convert()
walk_r10 = pygame.image.load("Red_Link/marche/walk_red_link10.png")
walk_r10.convert()
walkredlink = [walk_r10, walk_r9, walk_r8, walk_r7, walk_r6, walk_r5, walk_r4, walk_r3, walk_r2, walk_r1]
    # Animation mort link rouge
dead_r1 = pygame.image.load("Red_Link/mort/dead_red_link1.png")
dead_r1.convert()
dead_r2 = pygame.image.load("Red_Link/mort/dead_red_link2.png")
dead_r2.convert()
dead_r3 = pygame.image.load("Red_Link/mort/dead_red_link3.png")
dead_r3.convert()
dead_r4 = pygame.image.load("Red_Link/mort/dead_red_link4.png")
dead_r4.convert()
dead_r5 = pygame.image.load("Red_Link/mort/dead_red_link5.png")
dead_r5.convert()
dead_r6 = pygame.image.load("Red_Link/mort/dead_red_link6.png")
dead_r6.convert()
dead_r7 = pygame.image.load("Red_Link/mort/dead_red_link7.png")
dead_r7.convert()
dead_r8 = pygame.image.load("Red_Link/mort/dead_red_link8.png")
dead_r8.convert()
dead_r9 = pygame.image.load("Red_Link/mort/dead_red_link9.png")
dead_r9.convert()
deadredlink = [dead_r1, dead_r2, dead_r3, dead_r4, dead_r5, dead_r6, dead_r7, dead_r8, dead_r9]
reglesredlink = [dead_r1, dead_r1, dead_r1, dead_r1, dead_r1, dead_r3, dead_r3, dead_r3, dead_r3, dead_r3]


class Redplayer(object):
    def __init__(self):
        self.link_walk_count = 0
        self.link_dead_count = 0
        self.link_regles_count = 0

    def draw(self, window):
        if self.link_walk_count <= 9:
            window.blit(walkredlink[self.link_walk_count], [10, 278])
            self.link_walk_count += 1
        else:
            self.link_walk_count = 0
            window.blit(walkredlink[self.link_walk_count], [10, 278])
            link_walk_count = 1

    def mort(self, window):
        if self.link_dead_count < 9:
            window.blit(deadredlink[self.link_dead_count], [10, 278])
            self.link_dead_count += 1

    def regles(self, window):
        if self.link_regles_count <= 9:
            window.blit(reglesredlink[self.link_regles_count], [10, 278])
            self.link_regles_count += 1
        else:
            self.link_regles_count = 0
            window.blit(reglesredlink[self.link_regles_count], [10, 278])


redlink = Redplayer()


# Animation marche monstre rouge
walk_rm1 = pygame.image.load("Red_monster/marche/walk_red_monster1.png")
walk_rm1.convert()
walk_rm2 = pygame.image.load("Red_monster/marche/walk_red_monster2.png")
walk_rm2.convert()
walk_rm3 = pygame.image.load("Red_monster/marche/walk_red_monster3.png")
walk_rm3.convert()
walk_rm4 = pygame.image.load("Red_monster/marche/walk_red_monster4.png")
walk_rm4.convert()
walk_rm5 = pygame.image.load("Red_monster/marche/walk_red_monster5.png")
walk_rm5.convert()
walk_rm6 = pygame.image.load("Red_monster/marche/walk_red_monster6.png")
walk_rm6.convert()
walkredmonster = [walk_rm1, walk_rm2, walk_rm3, walk_rm4, walk_rm5, walk_rm6]
    # Animation mort monstre rouge
dead_rm1 = pygame.image.load("Red_Monster/mort/dead_red_monster1.png")
dead_rm1.convert()
dead_rm2 = pygame.image.load("Red_Monster/mort/dead_red_monster2.png")
dead_rm2.convert()
dead_rm3 = pygame.image.load("Red_Monster/mort/dead_red_monster3.png")
dead_rm3.convert()
dead_rm4 = pygame.image.load("Red_Monster/mort/dead_red_monster4.png")
dead_rm4.convert()
dead_rm5 = pygame.image.load("Red_Monster/mort/dead_red_monster5.png")
dead_rm5.convert()
dead_rm6 = pygame.image.load("Red_Monster/mort/dead_red_monster6.png")
dead_rm6.convert()
dead_rm7 = pygame.image.load("Red_Monster/mort/dead_red_monster7.png")
dead_rm7.convert()
dead_rm8 = pygame.image.load("Red_Monster/mort/dead_red_monster8.png")
dead_rm8.convert()
dead_rm9 = pygame.image.load("Red_Monster/mort/dead_red_monster9.png")
dead_rm9.convert()
dead_rm10 = pygame.image.load("Red_Monster/mort/dead_red_monster10.png")
dead_rm10.convert()
deadredmonster = [dead_rm1, dead_rm2, dead_rm3, dead_rm4, dead_rm5, dead_rm6, dead_rm7, dead_rm8, dead_rm9, dead_rm10]


class RedMonster(object):
    def __init__(self):
        self.monster_walk_count = 0
        self.monster_dead_count = 0

    def draw(self, window, x_redmonster,):
        if self.monster_walk_count <= 5:
            window.blit(walkredmonster[self.monster_walk_count], [x_redmonster, 227])
            self.monster_walk_count += 1
        else:
            self.monster_walk_count = 0
            window.blit(walkredmonster[self.monster_walk_count], [x_redmonster, 227])
            monster_walk_count = 1

    def mort(self, window):
        if self.monster_dead_count <= 9:
            window.blit(deadredmonster[self.monster_dead_count], [25, 227])
            self.monster_dead_count += 1
        else:
            self.monster_dead_count = 0


redmonster = RedMonster()


class Player(object):
    def __init__(self):
        self.link_walk_count = 0
        self.link_player = 0

    def draw(self, window):
        if self.link_player == 0:
            greenlink.draw(window)
        if self.link_player == 1:
            redlink.draw(window)
        if self.link_player == 2:
            purplelink.draw(window)


link = Player()

class Monster(object):
    def __init__(self):
        self.monster_walk_count = 0

    def draw(self, window, chiffre, x_greenmonster, x_redmonster, x_purplemonster):
        if chiffre == 0:
            greenmonster.draw(window, x_greenmonster)
        if chiffre == 1:
            redmonster.draw(window, x_redmonster)
        if chiffre == 2:
            purplemonster.draw(window, x_purplemonster)
monster = Monster()
