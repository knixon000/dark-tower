

import pygame
import time
import random
import sys
import keyboard  # using module keyboard
from pygame import K_SPACE, K_w, K_a, K_s, K_d, K_DOWN, K_UP, K_0, K_1
from pygame.locals import *
pygame.init()
pygame.font.init()
pygame.mixer.init()







keys = pygame.key.get_focused()
keys == True
pressed = pygame.key.get_pressed()

white= (255,255,255)

gameDisplay = pygame.display.set_mode((1050,600))



event = pygame.event.wait()

spacebar_was_pressed = pygame.K_SPACE #pygame.key.get_pressed()[pygame.K_SPACE] #pygame.K_SPACE #keyboard.is_pressed("SPACE") #

def main ():
    running = True

    if event.type == pygame.QUIT:
        running = False # break the loop
        quit_game()
    else:
        titlescreen()


def quit_game():
    running = False # break the loop
    print("Goodbye!")
    pygame.quit()
    sys.exit()


#-----------------------------------------------------------------------------
#titlescreen of game code
def titlescreen():
    running = True
    #play titlescreen music
    pygame.mixer.music.load('Darkpg Test I.wav')
    pygame.mixer.music.play(-1)

    keys == True
    # while running == True:
    width=1050;
    height=600

    screen = pygame.display.set_mode((width, height ))

    # #display titlescreen image
    # pygame.display.set_caption('Dark Tower')
    # titlescreen = pygame.image.load("titlescreen.png").convert()
    # titlescreen = pygame.transform.scale(titlescreen, (1000, 600))
    # x = 20; # x coordnate of image
    # y = 30; # y coordinate of image
    # screen.blit(titlescreen, ( x,y)) # paint image to screen


    #display logo
    logo = pygame.image.load("logo.png").convert()
    logo = pygame.transform.scale(logo, (1050, 600))
    x = 0; # x coordnate of image
    y = 0; # y coordinate of image
    screen.blit(logo, ( x,y)) # paint image to screen


    #display text
    red = (128, 0, 0)
    myfont = pygame.font.SysFont('Garamond', 34)
    textsurface = myfont.render('press spacebar to continue', True, (red))
    screen.blit(textsurface,(350,500))

    # #play titlescreen music
    # pygame.mixer.music.load('Darkpg Test I.wav')
    # pygame.mixer.music.play(-1)

    pygame.display.flip() # paint screen one time

    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if spacebar_was_pressed: #and event.type == KEYDOWN:
                    print("The spacebar was pressed.")
                    intro()


            elif event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    quit_game()

#-----------------------------------------------------------------
#intro is the text box screens
def intro():
    running = True
    print("Intro is running.")
    event = pygame.event.wait()
    #play titlescreen music
    # pygame.mixer.music.load('Darkpg Test I.wav')
    # pygame.mixer.music.play(-1)
    while running == True:
        screen = pygame.display.set_mode((1000, 600))

        display_width = 7
        display_height = 1.2

        #display titlescreen image
        pygame.display.set_caption('Dark Tower')
        titlescreen = pygame.image.load("titlescreen.png").convert()
        titlescreen = pygame.transform.scale(titlescreen, (1050, 600))
        x = 0; # x coordnate of image
        y = 0; # y coordinate of image
        screen.blit(titlescreen, ( x,y)) # paint image to screen

        font = pygame.font.SysFont(None, 25)
        '''
        virdi_dialog_1 = "Hero, you have awakened Hero. Your name is Theseus."
                             "A wanderer that stumbled into my tower."
                             "You need to escape the tower at all cost."
        '''
        def dialog_to_screen(msg, color):
            screen_text = font.render(msg, True, color)
            # screen.blit(screen_text, [display_width/7, display_height/1.2])
            screen.blit(screen_text,(260,500))


        dialog_to_screen("Hero, you have awakened Hero. Your name is Theseus.", white)

        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if spacebar_was_pressed: #and event.type == KEYDOWN:
                    pygame.mixer.fadeout(1)
                    pygame.mixer.music.stop()
                    print("The spacebar was pressed.")
                    levelOne()


            elif event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    quit_game()






#-----------------------------------------------------------------------------

#first level code
def levelOne():
    running = True
    print("Level One has started!")
    screen = pygame.display.set_mode((1000, 600))
    # screen.blit(1000,600)
    screen.fill(white)
    pygame.display.update()



    running = True # our variable to control the loop.
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # break the loop
                quit_game()
                pygame.quit()
                sys.exit()
                quit()




#-----------------------------------------------------------------------------
#second level code
def levelTwo():
    print("Level two has started!")
    running = True

    event = pygame.event.wait()


    running = True # our variable to control the loop.
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # break the loop
                quit_game()
                pygame.quit()
                sys.exit()
                quit()
#-----------------------------------------------------------------------------
#third level code
def levelThree():
    running = True
    event = pygame.event.wait()
    print("Level three has started!")



    running = True # our variable to control the loop.
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # break the loop
                quit_game()
                pygame.quit()
                sys.exit()
                quit()
#-----------------------------------------------------------------------------
#forth level code
def levelFour():
    running = True
    event = pygame.event.wait()
    print("Level four has started!")



    running = True # our variable to control the loop.
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # break the loop
                quit_game()
                pygame.quit()
                sys.exit()
                quit()

#-----------------------------------------------------------------------------
#fifth level code
def levelFive():
    running = True
    event = pygame.event.wait()
    print("Level five has started!")



    running = True # our variable to control the loop.
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # break the loop
                quit_game()
                pygame.quit()
                sys.exit()
                quit()
#--------------------------------------------------------------------------
#call and QUIT

main()

quit_game()
pygame.quit()
titlescreen()









# pygame.quit()
