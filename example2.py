# example2 
# Import and initialize pygame
import pygame
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.surf, (self.x, self.y))

# create instance of Game Object
apple = GameObject(120, 300, 'images/apple.png')

#------------------------------------------------------------
# CHALLENGE 1
strawberry = GameObject(200, 300, 'images/strawberry.png')
#------------------------------------------------------------

#------------------------------------------------------------
# CHALLENGE 2
strawberry1 = GameObject(210, 40, 'images/strawberry.png') # top-middle
strawberry2 = GameObject(210, 400, 'images/strawberry.png') # middle - left
strawberry3 = GameObject(50, 200, 'images/strawberry.png') # bottom middle
strawberry4 = GameObject(380, 200, 'images/strawberry.png') # middle right

apple1 = GameObject(50, 400, 'images/apple.png') # bottom left
apple2 = GameObject(50, 45, 'images/apple.png') # top left
apple3 = GameObject(375, 45, 'images/apple.png') # top right
apple4 = GameObject(375, 400, 'images/apple.png') # bottome right
apple5 = GameObject(210, 200, 'images/apple.png') # middle
#------------------------------------------------------------
# Create the game loop
running = True
while running:
    # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw a circle
    screen.fill((255, 255, 255))
    # draw the surface
    apple.render(screen)
#------------------------------------
    # CHALLENGE 1
    strawberry.render(screen)
#-------------------------------------
    # CHALLENGE 2
    strawberry1.render(screen)
    strawberry2.render(screen)
    strawberry3.render(screen)
    strawberry4.render(screen)

    apple1.render(screen)
    apple2.render(screen)
    apple3.render(screen)
    apple4.render(screen)
    apple5.render(screen)
    # Update the window
    pygame.display.flip()
