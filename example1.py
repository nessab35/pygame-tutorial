# challenge 1
import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

radius = 50


# create the game loop
running  = True
while running:
    # looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    colors = {
        'red' : (235, 52, 67),
        'orange' : (235, 147, 52),
        'yellow' : (235, 210, 52),
        'green' : (15, 191, 59),
        'blue' : (5, 145, 245),
        'white' : (255, 255, 255),}

    positions = {
        'position1' : (250, 250), # yellow
        'position2' : (75, 100), # red
        'position3' : (425, 100), # ornage
        'position4' : (75, 400), # green
        'position5' : (425, 400),} #blue

    # clear the screen
    screen.fill((colors['white']))
    # draw a circle
    # colored 5 circles
    pygame.draw.circle(screen, colors['yellow'], positions['position1'], radius)
    pygame.draw.circle(screen, colors['red'], positions['position2'], radius)
    pygame.draw.circle(screen, colors['orange'], positions['position3'], radius)
    pygame.draw.circle(screen, colors['green'], positions['position4'], radius)
    pygame.draw.circle(screen, colors['blue'], positions['position5'], radius)

    # update display
    pygame.display.flip()

# challenge 2
import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

# color
colors = {
    'white' : (255, 255, 255),
    'dark grey' : (50, 50, 50),}

# circle
radius = 50


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

    # clear screen
    screen.fill(colors['white'])

    # drawing here


    # update display
    pygame.display.flip()