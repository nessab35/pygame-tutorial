import pygame
from pygame.locals import *
from apple import Apple
from strawberry import StrawBerry
from player import Player
from bomb import Bomb
from alian import Alian1, Alian2
from cloud import Cloud1
from bird import Bird
from constants import PINK, BLACK, fruit_captured
pygame.font.init()

screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

apple = Apple()
strawberry = StrawBerry()
player = Player()
bomb = Bomb()
alian_one = Alian1()
alian_two = Alian2()
cloud_one = Cloud1()
cloud_two = Cloud1()
cloud_three = Cloud1()
bird_ = Bird()

# made sprites Group
fruit_sprites = pygame.sprite.Group()
fruit_sprites.add(apple)
fruit_sprites.add(strawberry)

alian_sprites = pygame.sprite.Group()
alian_sprites.add(alian_one)
alian_sprites.add(alian_two)

bomb_sprites = pygame.sprite.Group()
bomb_sprites.add(bomb)


all_sprites = pygame.sprite.Group()
sprites_to_add = [player, apple, strawberry, bomb, alian_one, alian_two, cloud_one, cloud_two, cloud_three, bird_]
for sprite in sprites_to_add:
    all_sprites.add(sprite)


pygame.display.set_caption("Alian VS. Fruit- Nessa Begay")
pygame.mixer.init()


def play_background_music():
    pygame.mixer.music.load("sounds/background.mp3")
    pygame.mixer.music.play()


def play_sound(sound):
    sound = pygame.mixer.Sound(f"sounds/{sound}.wav")
    pygame.mixer.Sound.play(sound)
    return sound


def show_game_over():
    screen.fill((BLACK))
    my_font = pygame.font.SysFont('timesnewroman', 20)
    line_1 = my_font.render("Game Over! Your score is ____", True, (PINK))
    screen.blit(line_1, (65, 150))
    line_2 = my_font.render("To play again, press ENTER. To exit, press ESC!", True, (PINK))
    screen.blit(line_2, (70, 200))

    pygame.display.flip()

    pygame.mixer.music.pause()


running = True
game_over = False


pygame.display.set_caption("Alian VS. Fruit- Nessa Begay")
play_background_music()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # check for event in type KEYBOARD
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN and game_over:
                pygame.mixer.music.unpause()
                game_over = False
                fruits_captured = 0
                player.reset()
                bomb.reset()
                strawberry.reset()
                apple.reset()
                alian_one.reset()
                alian_two.reset()
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()

    # clear screen
    screen.fill((PINK))

    # Move and render sprites
    for entity in all_sprites:
        entity.move()
        entity.render(screen)
        fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
        alian = pygame.sprite.spritecollideany(player, alian_sprites)
        if fruit:
            play_sound("eating_fruit")
            fruit_captured += 0.3
            fruit.reset()

        if alian:
            play_sound("explosion")
            alian_one.reset()
            alian_two.reset()
            game_over = True

        if pygame.sprite.collide_rect(player, bomb):
            play_sound("explosion")
            game_over = True

    if game_over:
        show_game_over()

    # update the window
    pygame.display.flip()
    # tick the clock
    clock.tick(60)
