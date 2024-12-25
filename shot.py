from circleshape import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 1)

    def update(self, dt):
        self.move(self.velocity * dt)

    def move(self, dt):
        self.position += dt