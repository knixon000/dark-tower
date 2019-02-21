
from pygame.locals import *
import pygame
pygame.init()

running = True

screen = pygame.display.set_mode((1050, 600 ))
pygame.display.set_caption('Dark Tower')
black = 0,0,0

hits = 0


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

class Player():
    x =410
    y = 0
    speed = 1

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed
        #collision attempt
    def get_rect(self):
        self.rect = self.get_rect()

        pygame.draw.rect(screen,black,rect, 2)

        self.rect.inflate_ip(-10,-10)
        # return pygame.Rect(self.x, self.y, 0.5, 0.5)


    def update(self, maze):
        self.rect.x += self.change_x

        hits = pygame.sprite.collide_rect(self,maze, False)


        for hit in hits:
            if self.change_x >0:
                self.rect.right == maze.rect.left
            else:
                self.rect.left == maze.rect.right


        self.rect.y += self.change_y
        for hit in hits:
            if self.change_y >0:
                self.rect.bottom == maze.rect.top
            else:
                self.rect.top == maze.rect.bottom





class Maze:

    def __init__(self):

         self.M = 32
         self.N = 25
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
                       1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,
                       1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1,0,1,0,0,0,1,0,1,0,1,
                       1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1,0,1,
                       1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,
                       1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,
                       1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,
                       1,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
                       1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,
                       1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,
                       1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,
                       1,0,1,1,1,0,1,0,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,
                       1,0,1,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,
                       1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,
                       1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,
                       1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,]

    def draw(self,display_surf,image_surf):
       bx = 0
       by = 0
       for i in range(0,self.M*self.N):
           if self.maze[ bx + (by*self.M) ] == 1:
               display_surf.blit(image_surf,( bx * 30 , by * 30))

           elif self.maze[ bx + (by*self.M) ] == 0:
                hits == False

               # #collision attempt
               # rect = pygame.Rect(bx * 25, by * 25, 25, 25)
               #
               # if player.rect.collidepoint(event.pos):
               #     pass  # Collision!

           bx = bx + 1
           if bx > self.M-1:
               bx = 0
               by = by + 1

    def get_rect(self):
        self.rect = self.get_rect()
        return pygame.Rect(self.x, self.y, 0.5, 0.5)

class App:

    windowWidth = 1050
    windowHeight = 660
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.player = Player()
        self.maze = Maze()

    #     ## check if the player is still in the maze##
    #     if self.player.get_rect().collide_rect(self.maze.rect):
    #         hit = True
    #     else:
    #         hit = False
    # ##reverse player's movement if they hit the wall##
    #     if hit == True:
    #         self.x = -1
    #         self.y *= -1

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Dark Tower')
        self._running = True
        # self._image_surf = pygame.image.load("Cloak-Test.gif").convert()
        # self._image_surf = pygame.transform.scale(self._image_surf, (70,50))
        self._block_surf = pygame.image.load("tiles.png").convert()
        self._block_surf = pygame.transform.scale(self._block_surf , (30,30))
        # self._block_surf = pygame.Surface.get_rect(center=(100,100))
        self._image_surf = pygame.image.load("Cloak-Test.gif").convert()
        self._image_surf = pygame.transform.scale(self._image_surf, (50,30))
        # self._image_surf = pygame.Surface.get_rect(center=(100,100))
        # self.rect = self._image_surf.get_rect()


    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
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
        #
        #     # new_rect = self.rect.move(self.player.x, self.player.y)
        #     # if self.rect.collide_rect(self.maze.rect):
        #     # if self.rect.collide_rect(self.maze.rect):
        #         # self.player.rect = new_rect
        #     #     print("Collision!")
        #     # else:
        #     keys = pygame.key.get_pressed()
        #
        #     if (keys[K_RIGHT]):
        #         self.player.moveRight()
        #
        #     if (keys[K_LEFT]):
        #         self.player.moveLeft()
        #
        #     if (keys[K_UP]):
        #         self.player.moveUp()
        #
        #     if (keys[K_DOWN]):
        #         self.player.moveDown()
        #
        #     if (keys[K_ESCAPE]):
        #         self._running = False
        #



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
