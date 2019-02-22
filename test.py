
from pygame.locals import *
import pygame
pygame.init()

running = True

screen = pygame.display.set_mode((1050, 600 ))
pygame.display.set_caption('Dark Tower')
black = 0,0,0

# hits = pygame.sprite.collide_rect(player,maze, False)


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

# for hit in hits:
#     if self.change_x >0:
#         self.rect.right == maze.rect.left
#     else:
#         self.rect.left == maze.rect.right
#
#
# self.rect.y += self.change_y
# for hit in hits:
#     if self.change_y >0:
#         self.rect.bottom == maze.rect.top
#     else:
#         self.rect.top == maze.rect.bottom


class Player():
    x =410
    y = 0
    speed = 1


    def __init__(self, image, x, y):
        self.image = image
        self.width = image.get_width()
        self.height = image.get_height()
        self.rect = pygame.Rect(x, y, 30, 10)
        self.screen = screen

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed


        self.rect.inflate_ip(-1,-1)
        self.screen_rect = screen.get_rect()

        pygame.draw.rect(self.screen,black,rect, 2)






class Maze(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load("Cloak-Test.gif").convert()
        x = 0
        y = 0
        self.image = pygame.image.load("tiles.png").convert()
        self.width = image.get_width()
        self.height = image.get_height()
        self.rect = pygame.Rect(x, y, 30, 30)
        self.screen = screen
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

           bx = bx + 1
           if bx > self.M-1:
               bx = 0
               by = by + 1

    # def get_rect(self):
    #     return pygame.Rect(self.x, self.y, 0.5, 0.5)

class App:

    windowWidth = 1050
    windowHeight = 660
    player = 0

    def __init__(self):
        image = pygame.image.load("Cloak-Test.gif").convert()
        x =410
        y = 0



        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.player = Player(image,x,y)
        self.maze = Maze(x,y)



    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Dark Tower')
        self._running = True


        self._block_surf = pygame.image.load("tiles.png").convert()
        self._block_surf = pygame.transform.scale(self._block_surf , (30,30))


        self._image_surf = pygame.image.load("Cloak-Test.gif").convert()
        self._image_surf = pygame.transform.scale(self._image_surf, (50,30))







    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))


        self.maze.draw(self._display_surf, self._block_surf)
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))


        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            # hits = pygame.sprite.collide_rect(self.player,self.maze)

            # hits = self.player.get_rect().collidepoint(event.pos)

            # hits = pygame.sprite.collide_rect(self._image_surf, self._block_surf)


            sprite_group = pygame.sprite.Group()
            sprite_group.add(self.player)
            sprite_group.add(self.maze)

            hits = pygame.sprite.spritecollide(self.player, self.maze, True)

            while hits == False:
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

            while hits == True:
                def update(self, maze):
                    pygame.event.pump()

                    self.rect.x += self.change_x

                    # hits = pygame.sprite.collide_rect(player,maze, False)


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
