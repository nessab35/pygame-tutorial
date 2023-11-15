import pygame

# Game Object
class GameObject(pygame.sprite.Sprite):
    '''Parent Class'''
    def __init__(self, x, y, image):
        super().__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect()

    def render(self,screen):
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.surf, (self.x, self.y))
