# example 2

#import and initilaize pygamne
import pygame
pygame.init()

#configure the screen
screen = pygame.display.set_mode([500, 500])

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))

# create instance of GameObject class
apple = GameObject(120, 300, 'images/apple.png')
strawberry = GameObject(200, 300, 'images/strawberry.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    apple.render(screen)
    strawberry.render(screen)

    pygame.display.flip()
