import pygame
from player import Player
from level import Level
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_LEVEL

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Initialize game components
player = Player(640, GROUND_LEVEL)
level = Level(GROUND_LEVEL)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input
    keys = pygame.key.get_pressed()
    player.handle_input(keys)

    # Update game state
    player.update()

    # Draw everything
    screen.fill("black")
    level.draw(screen)
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
