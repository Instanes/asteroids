import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2 )
        

    def update(self, dt):
        # sub-classes must override
        pass
    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius
    
   # def draw(self, screen):
   #     points = self.triangle()
   #     print("Triangle points:", points)
   #     pygame.draw.polygon(screen, (255, 255, 255), points, 2)

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
        
    def update(self, dt):
        self.position += self.velocity * dt