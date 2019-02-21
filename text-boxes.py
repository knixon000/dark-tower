
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

dialog_to_screen("???: Hero, you have awakened Hero. Your name is Thesus.", white)
dialog_to_screen("???: A wanderer that stumbled into my tower.", white)
dialog_to_screen("???: You need to escape the tower at all cost.", white)
dialog_to_screen("Thesus: Who are you?", white)
dialog_to_screen("???: That isn't important right now.", white)
dialog_to_screen("???: You must find your way out before its too late.", white)
dialog_to_screen("Thesus: My legs feel numb I cant move.", white)
dialog_to_screen("???: You have been out for a while.", white)
dialog_to_screen("???: Your recollection of memories are jumbled as well.", white)
dialog_to_screen("???: Get moving hero, your life depends on it.", white)
##level 2
dialog_to_screen("???: Oh no!!!", white)
dialog_to_screen("Thesus: What is it? Who's blood is that??", white)
dialog_to_screen("???: The blood of a hero who killed the monster.", white)
dialog_to_screen("???: At the cost of his own life.", white)
dialog_to_screen("Thesus: Monster? What monster?", white)
dialog_to_screen("???: A beast that's part man and part bull known as the Minotaur.", white)
dialog_to_screen("Thesus: I see...", white)
dialog_to_screen("???: Ignore it for now. You must escape the tower.", white)
##Level 3
dialog_to_screen("Thesus: May I ask who you are?", white)
dialog_to_screen("???: My name is Viridi also known as the Goddess of Death.", white)
dialog_to_screen("Thesus: Goddess of Death I see...", white)
dialog_to_screen("Viridi: It is my responsibility to ensure you leave this maze.", white)
dialog_to_screen("Thesus: Thank You!!! Now I'll keep pushing on.", white)
##Level 4
dialog_to_screen("Thesus: Why do I feel so much pain in my chest?", white)
dialog_to_screen("Viridi: You're starting to remember Thesus.", white)
dialog_to_screen("Viridi: You'll find your answers soon.. I promise.", white)
dialog_to_screen("Thesus: I vaguely remember fighting something and the pain.", white)
dialog_to_screen("Viridi: Good let those memories flow Thesus... find the truth.", white)
dialog_to_screen("Thesus: I can see the trail ending as well as a bright light.", white)
dialog_to_screen("Viridi: You're near the end... Keep going!", white)
##Level 5
dialog_to_screen("Thesus: Omg is that the Minotaur??", white)
dialog_to_screen("Viridi: Yes!! Do you remember Thesus?", white)
dialog_to_screen("Thesus: I've been here before...I fought that beast...", white)
dialog_to_screen("Thesus: .....", white)
dialog_to_screen("Thesus: I..I..I killed that beast...", white)
dialog_to_screen("Thesus: That beast killed me...", white)
dialog_to_screen("Viridi: Yes Thesus.. this maze is your purgatory", white)
dialog_to_screen("Viridi: Now step into the light it's time to move on...", white)
dialog_to_screen("Viridi: *Evil Grin* Into Hell!!!", white)
dialog_to_screen("TO BE CONTINUED.......", white)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(20)

