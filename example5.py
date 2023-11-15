# Using Groups
# Example 5
from random import randint, choice
import random
import pygame
pygame.init()


#configure the screen
screen = pygame.display.set_mode([500, 500])
# use clock rate to get consistent frame rate
clock = pygame.time.Clock()
lanes = [93, 218, 343]
WHITE = (255, 255, 255)

#----------------------------------------------------------------
# Game Object
class GameObject(pygame.sprite.Sprite):
    '''Parent Class'''
    def __init__(self, x, y, image):
        super().__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y

    def render(self,screen):
        screen.blit(self.surf, (self.x, self.y))


#----------------------------------------------------------------
# Apple
class Apple(GameObject):
    '''Class for apple image'''
    def __init__(self):
        x = randint(50, 400)
        super().__init__(x, 0, 'images/apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # check the y position of the apple
        if self.y > 500 or self.y < -64:
            self.reset()

    def reset(self):
        self.x = choice(lanes)
        # challenge 1
        if randint(0, 1) == 0:
            self.y = -64
            self.dy = (randint(0, 200) / 100) + 1
        else:
            self.y = 500
            self.dy = ((randint(0, 200) / 100) + 1) * -1


#----------------------------------------------------------------
# Strawberry
class StrawBerry(GameObject):
    '''Straw Berry image'''
    def __init__(self):
        y = randint(50, 400)
        super().__init__(y, 0, 'images/strawberry.png')
        self.dy = 0
        self.dx = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # check y position of strawberry
        if self.x > 500 or self.x < -64:
            self.reset()

    def reset(self):
        self.y = choice(lanes)
        # challenge 1
        if randint(0, 1) == 0:
            self.x = -64
            self.dx = (randint(0, 200) / 100) +1
        else:
            self.x = 500
            self.dx = ((randint(0, 200) / 100) + 1) * -1


#----------------------------------------------------------------
# challenge 2
# Bomb
class Bomb(GameObject):
    '''Bomb Image'''
    def __init__(self):
        self.y = randint(50, 400)
        super().__init__(self.y, 0, 'images/bomb.png')
        self.dy = 0
        self.dx = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # check y position of bomb
        if self.x > 500 or self.y > 500 or self.x < -64 or self.y < -64:
            self.reset()

    def reset(self):
        reset_conditions = randint(0, 4)

        if reset_conditions == 0:
            self.x = -64
            self.y = choice(lanes)
            self.dx = (randint(0, 200) / 100) +1
            self.dy = 0
        elif reset_conditions == 1:
            self.x = 500
            self.y = choice(lanes)
            self.dx = ((randint(0, 200) / 100) + 1) * -1
            self.dy = 0
        elif reset_conditions == 2:
            self.x = choice(lanes)
            self.y = -64
            self.dx = 0
            self.dy = (randint(0, 200) / 100) + 1
        else:
            self.x = choice(lanes)
            self.y = 500
            self.dx = 0
            self.dy = ((randint(0, 200) / 100) + 1) * -1


#----------------------------------------------------------------
# Player
class Player(GameObject):
    '''Player Class'''
    def __init__(self):
        super().__init__(0, 0, 'images/player.png')
        self.dx = 0
        self.dy = 0
        self.pos_x = 1
        self.pos_y = 1
        self.reset()

    def left(self):
        '''Left'''
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()

    def right(self):
        '''Right'''
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()

    def up(self):
        '''Up'''
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()

    def down(self):
        '''Down'''
        if self.pos_y < len(lanes) - 1:
            self.pos_y += 1
            self.update_dx_dy()

    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

    def reset(self):
        self.x = lanes[self.pos_x]
        self.y = lanes[self.pos_y]
        self.dx = self.x
        self.dy = self.y

    def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]


#----------------------------------------------------------------
# creating instance
apple = Apple()
strawberry = StrawBerry()
player = Player()
bomb = Bomb()

# made sprites Group
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)


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

    # clear screen
    screen.fill((WHITE))

    # Move and render sprites
    for entity in all_sprites:
        entity.move()
        entity.render(screen)

    # update the window
    pygame.display.flip()
    # tick the clock
    clock.tick(60)
