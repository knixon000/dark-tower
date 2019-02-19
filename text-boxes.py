
import pygame, sys
from pygame.locals import *

pygame.init()


pygame.display.set_caption('font test')
display_width = 640
display_height = 480
screen = pygame.display.set_mode((display_width, display_height))

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

clock = pygame.time.Clock()


font = pygame.font.SysFont(None, 25)
'''
Hey, this is going to be the dialog for the game. You should thank Carlos for this.
  
'''
def dialog_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [display_width/7, display_height/1.2])

dialog_to_screen("Hero, you have awakened Hero. Your name is Thesus.", white)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(20)

