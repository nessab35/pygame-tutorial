import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

# colors
yellow = (235, 210, 52)
red = (235, 52, 67)
orange = (235, 147, 52)
green = (15, 191, 59)
blue = (5, 145, 245)
dark_grey = (50, 50, 50)

circle_size = 50

# positions
position1 = (250, 250)# yellow
position2 = (75, 100) # red
position3 = (425, 100) # ornage
position4 = (75, 400) # green
position5 = (425, 400) # blue

# create the game loop
running  = True
while running:
    # looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clear the screen
    screen.fill((255, 255, 255))
    # draw a circle
    # colored 5 circles
    pygame.draw.circle(screen, yellow, position1, circle size)
    pygame.draw.circle(screen, red, position2, circle size)
    pygame.draw.circle(screen, orange, position3, circle size)
    pygame.draw.circle(screen, green, position4, circle size)
    pygame.draw.circle(screen, blue, position5, circle size)

    # dark grey 9 circles
    #for row in range():

    # update display
    pygame.display.flip()
