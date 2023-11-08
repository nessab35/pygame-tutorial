# example 4 handling events
#import and initilaize pygame
from random import randint, choice
import random
import pygame
pygame.init()

#configure the screen
screen = pygame.display.set_mode([500, 500])
# use clock rate to get consistent frame rate
clock = pygame.time.Clock()
positions = [93, 218, 343]

class GameObject(pygame.sprite.Sprite):
    '''Parent Class'''
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))


class Apple(GameObject):
    '''Class for apple image'''
    def __init__(self):
        x = randint(50, 400)
        super(Apple, self).__init__(x, 0, 'images/apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset() # call reset here!

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # check the y position of the apple
        if self.y > 500:
            self.reset()

    # add new method
    def reset(self):
        self.x = random.choice(positions)
        self.y = -64


class StrawBerry(GameObject):
    '''Straw Berry image'''
    def __init__(self):
        y = randint(50, 400)
        super(StrawBerry, self).__init__(y, 0, 'images/strawberry.png')
        self.dy = 0
        self.dx = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # check y position of strawberry
        if self.x > 500:
            self.reset()

    def reset(self):
        self.y = random.choice(positions)
        self.x = -64

#--------------------------------------------------------------
# challenge 2, left,right,up,down in lanes using 125, difference betwen [90, 218, 343]
class Player(GameObject):
    '''Player Class'''
    def __init__(self):
        super(Player, self).__init__(0, 0, 'images/player.png')
        self.dx = 218
        self.dy = 218
        self.reset()

    def left(self):
        '''Left'''
        self.dx -= 125

    def right(self):
        '''Right'''
        self.dx += 125

    def up(self):
        '''Up'''
        self.dy -= 125

    def down(self):
        '''Down'''
        self.dy += 125

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

    def reset(self):
        self.x = 250 - 32
        self.y = 250 - 32


# creating instance
apple = Apple()
strawberry = StrawBerry()
player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # check for event in type KEYBOARD
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()

    # CHALLENGE 1
    if not (0 <= player.dx <= 500 and 0 <= player.dy <= 500):
        running = False

    # clear screen
    screen.fill((255, 255, 255))

    # draw apple/ strawberry
    apple.move()
    strawberry.move()
    apple.render(screen)
    strawberry.render(screen)

    # draw player
    player.move()
    player.render(screen)

    # update the window
    pygame.display.flip()
    # tick the clock
    clock.tick(60)
