import pygame

class Player:
    def __init__(self, x, y):
        y = y -120
        self.position = [x, y]
        self.speed = 5
        self.jump_velocity = 0
        self.is_jumping = False
        self.gravity = 0.5
        self.ground_level = y

    def handle_input(self, keys):
        if keys[pygame.K_LEFT] and self.position[0] > 10:
            self.position[0] -= self.speed
        if keys[pygame.K_RIGHT] and self.position[0] < 1270:
            self.position[0] += self.speed
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.jump_velocity = -10
            self.is_jumping = True

    def update(self):
        if self.is_jumping:
            self.position[1] += self.jump_velocity
            self.jump_velocity += self.gravity
            if self.position[1] >= self.ground_level:
                self.position[1] = self.ground_level
                self.is_jumping = False

    def draw(self, screen):
        pygame.draw.ellipse(screen, "white", (self.position[0] - 25, self.position[1] + 25, 50, 100))  # Body
        pygame.draw.circle(screen, "white", (self.position[0], self.position[1]), 30)  # Head
        pygame.draw.circle(screen, "black", (self.position[0], self.position[1]), 26)  # Head
