from constants import *
from circleshape import CircleShape
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            velocity_asteroid1 = self.velocity.rotate(angle)
            velocity_asteroid2 = self.velocity.rotate(-angle)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, split_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, split_radius)
            asteroid1.velocity = velocity_asteroid1 * 1.2
            asteroid2.velocity = velocity_asteroid2 * 1.2
