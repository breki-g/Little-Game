import pygame

class Level:
    def __init__(self, ground_level):
        self.ground_level = ground_level

    def draw(self, screen):
        pygame.draw.line(screen, "white", (0, self.ground_level), (1280, self.ground_level), 5)
