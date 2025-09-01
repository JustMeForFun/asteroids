import pygame
from circleshape import CircleShape
from constants import PLAYER_SPEED

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)