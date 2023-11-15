# example 3 making things move
#import and initilaize pygame
from random import randint
import random
import pygame
pygame.init()

#configure the screen
screen = pygame.display.set_mode([500, 500])

# use clock rate to get consistent frame rate
clock = pygame.time.Clock()
positions = [93, 218, 343]


#----------------------------------------------------------------
# Game Object
class GameObject(pygame.sprite.Sprite):
    '''Parent Class'''
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))


#----------------------------------------------------------------
# Apple
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


#--------------------------------------------------------------
# Challenge 2
class StrawBerry(GameObject):
    '''class for starwberry image'''
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


# create instance of GameObject class
apple = Apple()
strawberry = StrawBerry()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clear screen
    screen.fill((255, 255, 255))

    # draw apple
    apple.move()
    strawberry.move()
    apple.render(screen)
    strawberry.render(screen)

    # update the window
    pygame.display.flip()
    # tick the clock
    clock.tick(60)
