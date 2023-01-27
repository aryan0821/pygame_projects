import pygame
import os
import time
import random

from pygame.constants import QUIT

pygame.font.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load images
RED_SPACE_SHIP = pygame.image.load(
    "/Users/aryannair/Code/space_invaders/assets/pixel_ship_red_small.png"
)
GREEN_SPACE_SHIP = pygame.image.load(
    "/Users/aryannair/Code/space_invaders/assets/pixel_ship_green_small.png"
)
BLUE_SPACE_SHIP = pygame.image.load(
    "/Users/aryannair/Code/space_invaders/assets/pixel_ship_blue_small.png"
)

# Player player
YELLOW_SPACE_SHIP = pygame.image.load(
    "/Users/aryannair/Code/space_invaders/assets/pixel_ship_yellow.png"
)

# Lasers
RED_LASER = pygame.image.load(
    "/Users/aryannair/Code/space_invaders/assets/pixel_laser_red.png"
)
GREEN_LASER = pygame.image.load(
    "/Users/aryannair/Code/space_invaders/assets/pixel_laser_green.png"
)
BLUE_LASER = pygame.image.load(
    "/Users/aryannair/Code/space_invaders/assets/pixel_laser_blue.png"
)
YELLOW_LASER = pygame.image.load(
    "/Users/aryannair/Code/space_invaders/assets/pixel_laser_yellow.png"
)
# background
BG = pygame.transform.scale(
    pygame.image.load(
        "/Users/aryannair/Code/space_invaders/assets/background-black.png"), (WIDTH, HEIGHT)
)


class Ship:
    def __init__(self, x, y, health=100) -> None:
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))


def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont("pygame_files/font/Pixeltype.ttf", 50)
    player_vel = 5

    ship = Ship(
        300,
        650,
    )

    def redraw_window():
        WIN.blit(BG, (0, 0))

        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        ship.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and ship.x - player_vel > 0:  # left
            ship.x -= player_vel
        if keys[pygame.K_s] and ship.y + player_vel + 60 < HEIGHT:  # down
            ship.y += player_vel
        if keys[pygame.K_w] and ship.y - player_vel > 0:  # up
            ship.y -= player_vel
        if keys[pygame.K_d] and ship.x + player_vel + 50 < WIDTH:  # right
            ship.x += player_vel


main()

# def main_menu():
#     title_font = pygame.font.SysFont("pygame_files/font/Pixeltype.ttf", 70)
#     while run:
#         WIN.blit(BG, (0, 0))
#         clock.tick(60)
#         title_label = title_font.render("Press mouse to start", 1, "Light Green")
#         WIN.blit(title_label, (20, 400))
#         pygame.display.update()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 main()
#     pygame.quit()


# main_menu()
