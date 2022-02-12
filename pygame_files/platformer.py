import pygame
from sys import exit

from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION
from pygame.image import get_sdl_image_version


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("pygame_files/font/Pixeltype.ttf", 50)
game_active = True
start_time = 0

sky_surf = pygame.image.load("pygame_files/graphics/Sky.png").convert()
ground_surf = pygame.image.load("pygame_files/graphics/ground.png").convert()
# score_surf = test_font.render("My game", False, "Black")
# score_rect = score_surf.get_rect(center=(400, 50))

snail_surf = pygame.image.load("pygame_files/graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load(
    "pygame_files/graphics/Player/player_walk_1.png"
).convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

player_stand = pygame.image.load(
    "pygame_files/graphics/Player/player_stand.png"
).convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_start_surf = test_font.render("Runner Game", False, (111, 196, 169))
game_start_rect = game_start_surf.get_rect(center=(400, 75))

game_inst = test_font.render("Press Space to jump", False, (111, 196, 169))
game_inst_rect = game_inst.get_rect(center=(400, 325))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
                snail_rect.left = 800

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        # pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
        # pygame.draw.rect(screen, "#c0e8ec", score_rect)
        # screen.blit(score_surf, score_rect)
        score = display_score()

        snail_rect.left -= 5
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)

        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_start_surf, game_start_rect)

        if score == 0:
            screen.blit(game_inst, game_inst_rect)
        else:
            screen.blit()
        # if player_rect.colliderect(snail_rect):
        #     print('collision')

        # mouse_position = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_position):
        #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)
