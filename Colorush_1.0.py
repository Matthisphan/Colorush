# coding:utf-8
import pygame
#import os
#os.chdir("C:/Users/matth/Documents/Colorush")
from Colorush_sprites import*
from Colorush_settings import*

pygame.init()
screen = (height, width)
pygame.display.set_caption("ColoRush")
window = pygame.display.set_mode(screen)
clock = pygame.time.Clock()


# choisir un chiffre pour faire apparaître un monstre
chiffre = randint(0, 2)
# Ces trois variables permettent de créer les images des monstres morts sans
# qu'ils ne se répètent et pour plus tard arrêter les animations des morts
# des monstres
d_greenmonster = 0
d_redmonster = 0
d_purplemonster = 0
# Ces trois variables mis ici permettent que lorsqu'on démarre le jeu
# après l'avoir fermé, les animations de mort des monstres se réinitialisent
greenmonster.monster_dead_count = 0
redmonster.monster_dead_count = 0
purplemonster.monster_dead_count = 0

# image menu
fleche_retour = pygame.image.load("background/flèche_retour2.png")
# image de la flèche retour dans les règles
x_fleche = 1000
y_fleche = 0
lim_x_fleche = 1040
lim_y_fleche = 40
# coordonnées de l'image de la flèche
play_image = pygame.image.load("background/Menu/play1_buton.png")
play_image.convert()
play2_image = pygame.image.load("background/Menu/play2_buton.png")
play2_image.convert()
# images du boutton "play"
x_play = 330
y_play = 180
lim_x_play = 420
lim_y_play = 219
# coordonnées du boutton play
regles_image = pygame.image.load("background/Menu/regles1_buton.png")
regles_image.convert()
regles2_image = pygame.image.load("background/Menu/regles2_buton.png")
regles2_image.convert()
# images du boutton règle

x_regles = 315
y_regles = 220
lim_x_regles = 445
lim_y_regles = 264
# coordonnées du boutton règle

quit_image = pygame.image.load("background/Menu/quitter1_buton.png")
quit_image.convert()
quit2_image = pygame.image.load("background/Menu/quitter2_buton.png")
quit2_image.convert()
# images du boutton quitter

x_quit = 312
x_quit2 = 311
y_quit = 265
lim_x_quit = 450
lim_y_quit = 292
# coordonnées du boutton quitter

# image fond de ColoRush
x_sol1 = 0
x_sol2 = 800
x_sol3 = 0
# coordonnées de 3 sol (on en utilise 2 qui se déplacent de droite à gauche et
# 1 qui reste à la même place
sol_image = pygame.image.load("background/Monosol_ColoRush.png")
sol_image.convert()
sol2_image = pygame.image.load("background/Monosol_ColoRush.png")
sol2_image.convert()
sol3_image = pygame.image.load("background/Monosol_ColoRush.png")
sol3_image.convert()
# images du sol répété trois fois dans 3 variables différentes

background = pygame.image.load("background/fond_colorush.png")
background.convert()
# image du fond d'écran
# image Game Over
game_over_image = pygame.image.load("background/game_over.png")
game_over_image.convert()

# creer un message


def creer_message(font, message, message_rectangle, couleur):

    if font == 'petite':
        font = pygame.font.SysFont('unispacebold', 15, False)
    elif font == 'moyenne':
        font = pygame.font.SysFont('unispacebold', 20, False)
    elif font == 'grande':
        font = pygame.font.SysFont('unispacebold', 30, False)

    message = font.render(message, True, couleur)
    window.blit(message, message_rectangle)


def menu_window():
    window.blit(background, [0, 0])
    window.blit(sol3_image, [x_sol3, 0])
    window.blit(sol_image, [x_sol1, 0])
    window.blit(sol2_image, [x_sol2, 0])
    window.blit(play_image, [x_play, y_play])
    window.blit(regles_image, [x_regles, y_regles])
    window.blit(quit_image, [x_quit, y_quit])
# création du fond, sol,boutton play,regles et image

    # Animation bouton play
    if x_souris >= x_play and x_souris <= lim_x_play:
        if y_souris >= y_play and y_souris <= lim_y_play:
            window.blit(play2_image, [x_play, y_play])

    # Animation bouton regles
    if x_souris >= x_regles and x_souris <= lim_x_regles:
        if y_souris >= y_regles and y_souris <= lim_y_regles:
            window.blit(regles2_image, [x_regles, y_regles])

    # Animation bouton quitter
    if x_souris >= x_quit and x_souris <= lim_x_quit:
        if y_souris >= y_quit and y_souris <= lim_y_quit:
            window.blit(quit2_image, [x_quit2, y_quit])
    Colorush_title.draw(window)
    link.draw(window)
    pygame.display.update()


def regles_window():
    window.blit(background, [0, 0])
    window.blit(fleche_retour, [x_fleche, 0])
    window.blit(sol3_image, [x_sol3, 0])
    window.blit(sol_image, [x_sol1, 0])
    window.blit(sol2_image, [x_sol2, 0])
    window.blit(play_image, [x_play, y_play])
    window.blit(regles_image, [x_regles, y_regles])
    window.blit(quit_image, [x_quit, y_quit])
# création du fond, de la flèche,des sols et du boutton play,règle,quitter qui
# partent à droit
    if dialogue_count == 0:
        dialogue1.draw(window)
    elif dialogue_count == 1:
        dialogue2.draw(window)
    else:
        dialogue3.draw(window)
# les dialogues du personnage qui explique les règles
    if link.link_player == 0:
        greenlink.regles(window)
    if link.link_player == 1:
        redlink.regles(window)
    if link.link_player == 2:
        purplelink.regles(window)
# Selon la couleur de link, le personnage regarde
    mog.draw(window)
# apparition du personnage qui explique les règles
    pygame.display.update()


def game_window(dead_greenmonster, dead_redmonster, dead_purplemonster):
    window.blit(background, [0, 0])
    window.blit(sol3_image, [x_sol3, 0])
    window.blit(sol_image, [x_sol1, 0])
    window.blit(sol2_image, [x_sol2, 0])
    window.blit(play_image, [x_play, y_play])
    window.blit(regles_image, [x_regles, y_regles])
    window.blit(quit_image, [x_quit, y_quit])
# création du fond, des sols et du boutton play,règles et quitter
    monster.draw(window, chiffre, x_greenmonster, x_redmonster, x_purplemonster)
# apparition du monstre
    creer_message('moyenne', 'Score:{}'.format(str(score)), (0, 0), (0, 0, 0))
    creer_message('petite', 'Highscore:{}'.format(str(high_score)), (0, 25), (0, 0, 0), )
# appelle à la fonction qui écrie les messages
    link.draw(window)
# création du link
    if dead_greenmonster == True:
        greenmonster.mort(window)
# Si le monstre vert est mort on affiche son animation de mort
    if dead_redmonster == True:
        redmonster.mort(window)
# Si le monstre rouge est mort on affiche son animation de mort
    if dead_purplemonster == True:
        purplemonster.mort(window)
# Si le monstre violet est mort on affiche son animation de mort
    pygame.display.update()


def dead_window():
    window.blit(game_over_image, [0, 0])
# création de l'image gameover
    if link.link_player == 0:
        greenlink.mort(window)
# si link est vert, il meurt avec son animation vert
    if link.link_player == 1:
        redlink.mort(window)
# si link est rouge, il meurt avec son animation rouge
    if link.link_player == 2:
        purplelink.mort(window)
# si link est violet, il meurt avec son animation violet
    pygame.display.update()


# musique et bruitage
music_menu = pygame.mixer.music.load("musique_menu.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(-1)

music_in_game = pygame.mixer.Sound("Musique_in_game.wav")

quit_sound = pygame.mixer.Sound("sound_quit.wav")

select_sound = pygame.mixer.Sound("sound_select.wav")

game_over_sound = pygame.mixer.Sound("game_over_sound.wav")

dialogue1_sound = pygame.mixer.Sound("dialogue1.wav")
dialogue2_sound = pygame.mixer.Sound("dialogue2.wav")
dialogue3_sound = pygame.mixer.Sound("dialogue3.wav")

lvl_up_sound = pygame.mixer.Sound("lvl_up.wav")

kill_monster_sound = pygame.mixer.Sound("kill_monster_sound.wav")

hightscore_sound = pygame.mixer.Sound("hightscore_sound.wav")

# son du personnage dans les règles


def random_voice_mog():
    chiffre = randint(0, 2)
    if chiffre == 0:
        dialogue1_sound.play()
    if chiffre == 1:
        dialogue2_sound.play()
    if chiffre == 2:
        dialogue3_sound.play()


# souris
x_souris = 0
y_souris = 0

# différent état
dead_greenmonster = False
dead_redmonster = False
dead_purplemonster = False
menu = True
game = False
regles = False
launched = True
mort = False

while launched:
    clock.tick(fps)
    for event in pygame.event.get():
        # curseur de la souris
        if event.type == pygame.MOUSEMOTION:
            x_souris, y_souris = event.pos
        # Bouton regles
        if event.type == pygame.MOUSEBUTTONDOWN and x_souris >= x_regles:
            if x_souris <= lim_x_regles and y_souris >= y_regles:
                if y_souris <= lim_y_regles:
                    select_sound.play()
                    random_voice_mog()
                    x_fleche = 1000
                    y_fleche = 0
                    lim_x_fleche = 1040
                    lim_y_fleche = 40
                    menu = False
                    game = False
                    regles = True
        # button dialogue
        if event.type == pygame.MOUSEBUTTONDOWN and x_souris >= 70:
            if x_souris <= 787 and y_souris >= 140 and y_souris <= 262:
                if regles == True:
                    random_voice_mog()
                    dialogue_count += 1
                    if dialogue_count >= 4:
                        dialogue_count = 0
        # Buton retour
        if event.type == pygame.MOUSEBUTTONDOWN and x_souris >= x_fleche:
            if x_souris <= lim_x_fleche and y_souris >= y_fleche:
                if y_souris <= lim_y_fleche:
                    select_sound.play()
                    x_play = 330
                    y_play = 180
                    lim_x_play = 420
                    lim_y_play = 219
                    x_regles = 315
                    y_regles = 220
                    lim_x_regles = 445
                    lim_y_regles = 264
                    x_quit = 312
                    x_quit2 = 311
                    y_quit = 265
                    lim_x_quit = 450
                    lim_y_quit = 292
                    menu = True
                    regles = False
        # Bouton quitter
        if event.type == pygame.MOUSEBUTTONDOWN and x_souris >= x_quit:
            if x_souris <= lim_x_quit and y_souris >= y_quit:
                if y_souris <= lim_y_quit:
                    quit_sound.play()
                    pygame.time.wait(1500)
                    launched = False
        # quitter avec la croix
        if event.type == pygame.QUIT:
            quit_sound.play()
            pygame.time.wait(1500)
            launched = False
        # button game over
        if event.type == pygame.MOUSEBUTTONDOWN and x_souris >= 343:
            if x_souris <= 375 and y_souris >= 285 and y_souris <= 297:
                if mort == True:
                    select_sound.play()
                    music_in_game.play(-1)
                    game = True
                    mort = False
        if event.type == pygame.MOUSEBUTTONDOWN and x_souris >= 432:
            if x_souris <= 458 and y_souris >= 283 and y_souris <= 297:
                if mort == True:
                    select_sound.play()
                    music_menu = pygame.mixer.music.load("musique_menu.mp3")
                    pygame.mixer.music.play(-1)
                    menu = True
                    mort = False
                    x_play = 330
                    y_play = 180
                    lim_x_play = 420
                    lim_y_play = 219
                    x_regles = 315
                    y_regles = 220
                    lim_x_regles = 445
                    lim_y_regles = 264
                    x_quit = 312
                    x_quit2 = 311
                    y_quit = 265
                    lim_x_quit = 450
                    lim_y_quit = 292
        # Bouton play
        if event.type == pygame.MOUSEBUTTONDOWN and x_souris >= x_play:
            if x_souris <= lim_x_play and y_souris >= y_play:
                if y_souris <= lim_y_play:
                    select_sound.play()
                    music_in_game.play()
                    pygame.mixer.music.stop()
                    menu = False
                    regle = False
                    game = True
        # Contrôle du joueur
        if event.type == pygame.KEYDOWN and game == True:
            if event.key == pygame.K_w:
                if link.link_player == 2:
                    link.link_player = 0
                else:
                    link.link_player += 1
            if event.key == pygame.K_q:
                if link.link_player == 0:
                    link.link_player = 2
                else:
                    link.link_player -= 1
    # Dans le menu
    if menu == True:
        x_sol1 -= 5
        x_sol2 -= 5
        if x_sol1 <=- 800:
            x_sol1 = 800
        if x_sol2 <=- 800:
            x_sol2 = 800
        menu_window()
    # Dans les règles
    if regles == True:
    # mise en place du sol
        x_sol1 =0
        x_sol2 =800
    # nous bougeons la flèche à gauche
        if x_fleche == 0:
            pass
        else:
            x_fleche -= 50
            lim_x_fleche -= 50
    # nous bougeons les boutons play,règles et quitter à gauche
        if x_play and lim_x_play and x_regles and lim_x_regles and x_quit and x_quit2 and lim_x_quit <= -100:
            pass
        else:
            x_play -= 50
            lim_x_play -= 50
            x_regles -= 50
            lim_x_regles -= 50
            x_quit -= 50
            x_quit2 -= 50
            lim_x_quit -= 50
        regles_window()

    # Dans le jeu
    if game == True:
    # nous augmentons le score à chaque boucle
        score += 1
    # si le joueur atteint le highscore, un son se produit
        if high_score != 0:
            if score == high_score:
                hightscore_sound.play()
    # les sols bougent à gauche par rapport à la vitesse des monstres
        x_sol1 -= v_monster
        x_sol2 -= v_monster
        if x_sol1 <=- 800:
            x_sol1 = 800
        if x_sol2 <=- 800:
            x_sol2 = 800
    # nous mettons les variables des morts à 0 au cas où le joueur recommance
    # une partie
        purplelink.link_dead_count = 0
        greenlink.link_dead_count = 0
        redlink.link_dead_count = 0
    # nous bougeons les bouttons play,règle et quitter à gauche
        if x_play and lim_x_play and x_regles and lim_x_regles and x_quit and x_quit2 and lim_x_quit <= -100:
            pass
        else:
            x_play -= 50
            lim_x_play -= 50
            x_regles -= 50
            lim_x_regles -= 50
            x_quit -= 50
            x_quit2 -= 50
            lim_x_quit -= 50
    # si le score atteint 500,1000,1500... la vitesse des monstres augmentent
        if score == score_palier+500:
            lvl_up_sound.play()
            score_palier += 500
            v_monster += 5
            if fps <= 29:
                fps += 1
    # si le chiffre est 0 nous mettons en place le monstre vert
        if chiffre == 0:
            if x_greenmonster > 10:
    # on réduit sa vitesse
                x_greenmonster -= v_monster
            else:
    # si le joueur a la même couleur que le monstre le monstre meurt
                if link.link_player == 0:
                    kill_monster_sound.play()
                    x_greenmonster = 805
                    dead_greenmonster = True
                    chiffre = randint(0, 2)
                else:
    # Mais si le joueur n'a pas la couleur, le jeu s'arrête en vérifiant si le
    # score est le nouveau high score et cela arrête le jeu pour mettre en place
    # l'état mort
                    pygame.mixer.stop()
                    if score > high_score:
                        high_score = score
                        score = 0
                    else:
                        score = 0
                    game = False
                    mort = True
                    game_over_sound.play()
                    x_greenmonster = 805
                    chiffre = randint(0, 2)
    # si le chiffre est 1 nous mettons en place le monstre rouge
        if chiffre == 1:
            if x_redmonster > 25:
    # on réduit sa vitesse
                x_redmonster -= v_monster
            else:
                if link.link_player == 1:
                    kill_monster_sound.play()
                    x_redmonster = 805
                    dead_redmonster = True
                    chiffre = randint(0, 2)
                else:
    # Mais si le joueur n'a pas la couleur, le jeu s'arrête en vérifiant si le
    # score est le nouveau high score et cela arrête le jeu pour mettre en place
    # l'état mort
                    pygame.mixer.stop()
                    if score > high_score:
                        high_score = score
                        score = 0
                    else:
                        score = 0
                    game = False
                    mort = True
                    game_over_sound.play()
                    x_redmonster = 805
                    chiffre = randint(0, 2)
    # si le chiffre est 2 nous mettons en place le monstre violet
        if chiffre == 2:
            if x_purplemonster > 30:
    # on réduit sa vitesse
                x_purplemonster -= v_monster
            else:
                if link.link_player == 2:
                    kill_monster_sound.play()
                    x_purplemonster = 805
                    dead_purplemonster = True
                    chiffre = randint(0, 2)
                else:
    # Mais si le joueur n'a pas la couleur, le jeu s'arrête en vérifiant si le
    # score est le nouveau high score et cela arrête le jeu pour mettre en place
    # l'état mort
                    pygame.mixer.stop()
                    if score > high_score:
                        high_score = score
                        score = 0
                    else:
                        score = 0
                    game = False
                    mort = True
                    game_over_sound.play()
                    x_purplemonster = 805
                    chiffre = randint(0, 2)
    # nous utilisons la fonction permettant de créent les images et les persos
        game_window(dead_greenmonster, dead_redmonster, dead_purplemonster)
    # nous ajoutons les variables pour afficher chaque images de l'animation de
    # mort des monstres
        if dead_greenmonster == True:
            d_greenmonster += 1
            if d_greenmonster == 11:
                d_greenmonster = 0
                dead_greenmonster = False
        if dead_redmonster == True:
            d_redmonster += 1
            if d_redmonster == 11:
                d_redmonster = 0
                dead_redmonster = False
        if dead_purplemonster == True:
            d_purplemonster += 1
            if d_purplemonster == 9:
                d_purplemonster = 0
                dead_purplemonster = False
    # Dans le gameover
    if mort == True:
        x_sol1 = 0
        x_sol2 = 800
        score_palier = 0
        v_monster = 5
        fps = 20
    # on utilise la fonction pour animer la mort de link et afficher l'image
        dead_window()

pygame.quit()
