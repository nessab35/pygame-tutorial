import pygame
pygame.font.init()

lanes = [93, 218, 343]
PINK = (199, 70, 177)
BLACK = (0, 0, 0)
fruit_captured = 0
score_increase = 100
my_font = pygame.font.SysFont('timesnewroman', 20, True)
my_font_scoreboard = pygame.font.SysFont('timesnewroman', 38, True)
screen = pygame.display.set_mode([500, 500])
