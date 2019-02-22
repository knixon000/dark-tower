

import pygame
import os
import time
import random
import sys
import keyboard  # using module keyboard
from pygame import K_SPACE, K_w, K_a, K_s, K_d, K_DOWN, K_UP, K_0, K_1
from pygame.locals import *
flags = FULLSCREEN | DOUBLEBUF
import pygame.surfarray
import numpy
import collision
pygame.init()
pygame.font.init()
pygame.mixer.init()







keys = pygame.key.get_focused()
keys == True
pressed = pygame.key.get_pressed()

white= (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((1050,600))



event = pygame.event.wait()

spacebar_was_pressed = pygame.K_SPACE




def main ():
    running = True

    if event.type == pygame.QUIT:
        running = False # break the loop
        quit_game()
    else:
        titlescreen()



#-----------------------------------------------------------------------------------

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
    pygame.display.set_caption('Dark Tower')

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
        screen = pygame.display.set_mode((1050, 600))

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


        dialog_to_screen("Hero, you have awakened. Your name is Theseus.", white)

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
    event = pygame.event.wait()
    pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
    screen = pygame.display.set_mode((1050, 600))
    screen.fill(white)
    screen.set_alpha(None)

    font = pygame.font.SysFont(None, 120)
    def level_to_screen(msg, color):
        screen_text = font.render(msg, True, color)
        screen.blit(screen_text,(400,250))

    level_to_screen("Level 1", red)

    pygame.display.update()

    display_width = 300
    display_height = 250


    class Player:
        x = 44
        y = 44
<<<<<<< HEAD
        speed = 1

=======
        speed = 0.5
            
>>>>>>> 5aa9f07552802139a4466125bd4a12d31c4dbf96
        def moveRight(self):
            self.x = self.x + self.speed

        def moveLeft(self):
            self.x = self.x - self.speed

        def moveUp(self):
            self.y = self.y - self.speed

        def moveDown(self):
            self.y = self.y + self.speed


    class Maze:
        def __init__(self):
             self.M = 32
             self.N = 21
             self.maze = [ 1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                           1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                           1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
                           1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                           1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,
                           1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,
                           1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,
                           1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,
                           1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,
                           1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,
                           1,0,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,
                           1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,
                           1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,
                           1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,
                           1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,
                           1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,
                           1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,
                           1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                           1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,
                           1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,
                           1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1]

        def draw(self,display_surf,image_surf):
           bx = 0
           by = 0
           for i in range(0,self.M*self.N):
               if self.maze[ bx + (by*self.M) ] == 1:
                   display_surf.blit(image_surf,( bx * 30 , by * 30))

               bx = bx + 1
               if bx > self.M-1:
                   bx = 0
                   by = by + 1


    class App:

        windowWidth = 960
        windowHeight = 630
        player = 0

        def __init__(self):
            self._running = True
            self._display_surf = None
            self._image_surf = None
            self._block_surf = None
            self.player = Player()
            self.maze = Maze()

        def on_init(self):
            pygame.init()
            self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

            pygame.display.set_caption('Pygame pythonspot.com example')
            self._running = True
            # self._image_surf = pygame.image.load("Cloak-Test.gif").convert()
            # self._image_surf = pygame.transform.scale(self._image_surf, (70,50))
            self._block_surf = pygame.image.load("tiles.png").convert()
            self._block_surf = pygame.transform.scale(self._block_surf , (30,30))
            self._image_surf = pygame.image.load("Cloak-Test.gif").convert()
            self._image_surf = pygame.transform.scale(self._image_surf, (65,45))


        def on_event(self, event):
            if event.type == QUIT:
                self._running = False

        def on_loop(self):
            pass

        def on_render(self):
            self._display_surf.fill((30,30,30))
            # self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
            self.maze.draw(self._display_surf, self._block_surf)
            self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
            pygame.display.flip()

        def on_cleanup(self):
            pygame.quit()

        def on_execute(self):
            if self.on_init() == False:
                self._running = False

            while( self._running ):
                pygame.event.pump()
                keys = pygame.key.get_pressed()

                if (keys[K_RIGHT]):
                    self.player.moveRight()

                if (keys[K_LEFT]):
                    self.player.moveLeft()

                if (keys[K_UP]):
                    self.player.moveUp()

                if (keys[K_DOWN]):
                    self.player.moveDown()

                if (keys[K_ESCAPE]):
                    self._running = False



                self.on_loop()
                self.on_render()
            self.on_cleanup()

    if __name__ == "__main__" :
        theApp = App()
        theApp.on_execute()

    event = pygame.event.wait()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # break the loop
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


def __init__(self):
    self.rect = pygame.Rect(32, 32, 16, 16)

def move(self, dx, dy):

    # Move each axis separately. Note that this checks for collisions both times.
    if dx != 0:
        self.move_single_axis(dx, 0)
    if dy != 0:
        self.move_single_axis(0, dy)

def move_single_axis(self, dx, dy):

    # Move the rect
    self.rect.x += dx
    self.rect.y += dy

    # If you collide with a wall, move out based on velocity
    for wall in walls:
        if self.rect.colliderect(wall.rect):
            if dx > 0: # Moving right; Hit the left side of the wall
                self.rect.right = wall.rect.left
            if dx < 0: # Moving left; Hit the right side of the wall
                self.rect.left = wall.rect.right
            if dy > 0: # Moving down; Hit the top side of the wall
                self.rect.bottom = wall.rect.top
            if dy < 0: # Moving up; Hit the bottom side of the wall
                self.rect.top = wall.rect.bottom







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
