

import pygame
import time
import random
import keyboard  # using module keyboard
from pygame import K_SPACE
pygame.font.init()
pygame.init()
#
# win = pygame.display.set_mode((1000, 620))
# pygame.display.set_caption("Dark Tower")
#
#
#
# def crash():
#     message_display('You Crashed')
#
# def game_intro():
#     titlescreenImg= pygame.image.load("titlescreen.png").convert()
#     titlescreen = pygame.display.set_mode((1000,620))
#     intro = True
#
#     while intro:
#         for event in pygame.event.get():
#             print(event)
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
#
#         win.fill((0,0,0))  # Fills the screen with black
#         titlescreenImg.blit("titlescreen.png", (20,20))
#         pygame.display.update()
#         clock.tick(15)
#
# x = 50
# y = 50
# width = 40
# height = 60
# vel = 5
#
# maze = pygame.image.load("maze1.png")
# playerController = pygame.image.load('cloak-test.gif')
#
# run = True
#
# while run:
#     pygame.time.delay(100)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#     keys = pygame.key.get_pressed()
#
#     if keys[pygame.K_LEFT]:
#         x -= vel
#
#     if keys[pygame.K_RIGHT]:
#         x += vel
#
#     if keys[pygame.K_UP]:
#         y -= vel
#
#     if keys[pygame.K_DOWN]:
#         y += vel


# game_intro()

keys = pygame.key.get_pressed()

def titlescreen():

    running = True

    while running == True:
        width=1050;
        height=600

        screen = pygame.display.set_mode((width, height ))



        #display titlescreen image
        pygame.display.set_caption('Dark Tower')
        titlescreen = pygame.image.load("titlescreen.png").convert()
        titlescreen = pygame.transform.scale(titlescreen, (1000, 600))
        x = 20; # x coordnate of image
        y = 30; # y coordinate of image
        screen.blit(titlescreen, ( x,y)) # paint image to screen


        #play titlescreen music
        pygame.mixer.music.load('Darkpg Test I.wav')
        pygame.mixer.music.play(-1)


        #display text
        red = (128, 0, 0)
        myfont = pygame.font.SysFont('Garamond', 72)
        textsurface = myfont.render('Press Spacebar to Continue', True, (red))
        screen.blit(textsurface,(150,500))



        spacebar_was_pressed = pygame.key.get_pressed()[pygame.K_SPACE]

        for event in pygame.event.get():
            if spacebar_was_pressed:
                pygame.mixer.music.stop()
                gameDisplay.fill(0,0,0)
                print("The spacebar was pressed.")
            else:
                pygame.mixer.music.play(-1)



        pygame.display.flip() # paint screen one time

        running = True
        while (running): # loop listening for end of game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        while running == True:  # making a loop

            try:  # used try so that if user pressed other than the given key error will not be shown

                if keyboard.is_pressed('K_SPACE'):  # if spacebar is pressed
                    print('You Pressed The Spacebar')
                    gameDisplay.fill(white)
                    # largeText = pygame.font.Font('freesansbold.ttf',75)
                    # TextSurf, TextRect = text_objects("Press Spacebar to continue", largeText)
                    # TextRect.center = ((display_width/2),(display_height/2))
                    # gameDisplay.blit(TextSurf, TextRect)
                    # pygame.display.update()
                    # clock.tick(15)
                    break  # finishing the loop
                else:
                    pass
                    print("That didn't work.")
            except:
                break  # if user pressed a key other than the given key the loop will break

                sceneOne()



# when spacebar was pressed start code of scene one

def sceneOne():
    print("Scene One has started!")





titlescreen()

pygame.quit()

pygame.display.update()

pygame.quit()
