from pygame.locals import *
import pygame


running = True


class Player:
    x = 44
    y = 44
    speed = 0.5

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
         self.N = 24
         self.maze = [ 1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
                       1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,
                       1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,
                       1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,0,1,0,0,0,0,0,0,1,
                       1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,1,1,0,0,1,
                       1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,
                       1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1,
                       1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,
                       1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,
                       1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,
                       1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,
                       1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,1,0,1,
                       1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,
                       1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,1,1,1,0,1,
                       1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,0,1,0,1,
                       1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,
                       1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,1,0,1,0,1,
                       1,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,
                       1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,
                       1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,
                       1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,0,0,0,1,0,0,1,1,1,1,1,0,1,
                       1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,0,0,0,1,0,1,
                       1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,
                       1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]


    def draw(self,display_surf,image_surf):
       bx = 0
       by = 0
       for i in range(0,self.M*self.N):
           if self.maze[ bx + (by*self.M) ] == 1:
               display_surf.blit(image_surf,( bx * 30 , by * 28))

           bx = bx + 1
           if bx > self.M-1:
               bx = 0
               by = by + 1


class App:

    windowWidth = 960
    windowHeight = 670
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
        self._block_surf = pygame.image.load("dirt.png").convert()
        self._block_surf = pygame.transform.scale(self._block_surf , (30,30))
        self._image_surf = pygame.image.load("Cloak-Test.gif").convert()
        self._image_surf = pygame.transform.scale(self._image_surf, (60,40))


    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((94,38,18))
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
