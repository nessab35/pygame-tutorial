# example 3
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


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))


class Apple(GameObject):
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
        self.x = random.choice(positions) # CHALLENGE 2
        self.y = -64


# CHALLENGE 1
class StrawBerry(GameObject):
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
        self.y = random.choice(positions) # CHALLENGE 2
        self.x = -64


# create instance of GameObject class
apple = Apple()
strawberry = StrawBerry()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
