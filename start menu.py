# import pygame
# import time
# import random
#
# pygame.init()
#
# display_width = 800
# display_height = 600
#
# black = (0,0,0)
# white = (255,255,255)
# red = (255,0,0)
#
# block_color = (53,115,255)
#
# car_width = 73
#
# gameDisplay = pygame.display.set_mode((display_width,display_height))
# pygame.display.set_caption('A bit Racey')
# clock = pygame.time.Clock()
#
# carImg = pygame.image.load('titlescreen.png')
#
#
# def things_dodged(count):
#     font = pygame.font.SysFont(None, 25)
#     text = font.render("Dodged: "+str(count), True, black)
#     gameDisplay.blit(text,(0,0))
#
# def things(thingx, thingy, thingw, thingh, color):
#     pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
#
# def car(x,y):
#     gameDisplay.blit(carImg,(x,y))
#
# def text_objects(text, font):
#     textSurface = font.render(text, True, black)
#     return textSurface, textSurface.get_rect()
#
# def message_display(text):
#     largeText = pygame.font.Font('freesansbold.ttf',115)
#     TextSurf, TextRect = text_objects(text, largeText)
#     TextRect.center = ((display_width/2),(display_height/2))
#     gameDisplay.blit(TextSurf, TextRect)
#
#     pygame.display.update()
#
#     time.sleep(2)
#
#     game_loop()
#
#
#
# def crash():
#     message_display('You Crashed')
#
# def game_intro():
#
#     intro = True
#
#     while intro:
#         for event in pygame.event.get():
#             print(event)
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
#         gameDisplay.fill(white)
#         largeText = pygame.font.Font('freesansbold.ttf',115)
#         TextSurf, TextRect = text_objects("A bit Racey", largeText)
#         TextRect.center = ((display_width/2),(display_height/2))
#         gameDisplay.blit(TextSurf, TextRect)
#         pygame.display.update()
#         clock.tick(15)
#
#
#
#
#
#
# def game_loop():
#     x = (display_width * 0.45)
#     y = (display_height * 0.8)
#
#     x_change = 0
#
#     thing_startx = random.randrange(0, display_width)
#     thing_starty = -600
#     thing_speed = 4
#     thing_width = 100
#     thing_height = 100
#
#     thingCount = 1
#
#     dodged = 0
#
#     gameExit = False
#
#     while not gameExit:
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x_change = -5
#                 if event.key == pygame.K_RIGHT:
#                     x_change = 5
#
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                     x_change = 0
#
#         x += x_change
#         gameDisplay.fill(white)
#
#         things(thing_startx, thing_starty, thing_width, thing_height, block_color)
#
#
#
#         thing_starty += thing_speed
#         car(x,y)
#         things_dodged(dodged)
#
#         if x > display_width - car_width or x < 0:
#             crash()
#
#         if thing_starty > display_height:
#             thing_starty = 0 - thing_height
#             thing_startx = random.randrange(0,display_width)
#             dodged += 1
#             thing_speed += 1
#             thing_width += (dodged * 1.2)
#
#         if y < thing_starty+thing_height:
#             print('y crossover')
#
#             if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
#                 print('x crossover')
#                 crash()
#
#         pygame.display.update()
#         clock.tick(60)
#
# game_intro()
# game_loop()
# pygame.quit()
# quit()

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)


class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """

    def __init__(self, x, y, width, height, color):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """

    # Set speed vector
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        """ Find a new position for the player """

        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Room(object):
    """ Base class for all rooms. """

    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


class Room1(Room):
    """This creates all the walls in room 1"""
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [390, 50, 20, 500, BLUE]
                ]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room2(Room):
    """This creates all the walls in room 2"""
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [190, 50, 20, 500, GREEN],
                 [590, 50, 20, 500, GREEN]
                ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room3(Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, PURPLE],
                 [0, 350, 20, 250, PURPLE],
                 [780, 0, 20, 250, PURPLE],
                 [780, 350, 20, 250, PURPLE],
                 [20, 0, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE]
                ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, RED)
                self.wall_list.add(wall)

        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)


def main():
    """ Main Program """

    # Call this function so the Pygame library can initialize itself
    pygame.init()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])

    # Set the title of the window
    pygame.display.set_caption('Maze Runner')

    # Create the player paddle object
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    clock = pygame.time.Clock()

    done = False

    while not done:

        # --- Event Processing ---

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)

        # --- Game Logic ---

        player.move(current_room.wall_list)

        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790

        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0

        # --- Drawing ---
        screen.fill(BLACK)

        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
