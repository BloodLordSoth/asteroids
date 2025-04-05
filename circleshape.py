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

        
    def collisions(self, other_circle):
    # Make sure other_circle is also a CircleShape with position and radius
        if not hasattr(other_circle, 'position') or not hasattr(other_circle, 'radius'):
            return False
    # Calculate distance between centers
        distance = self.position.distance_to(other_circle.position)
    # Check if distance is less than sum of radii
        return distance < (self.radius + other_circle.radius)


    def draw(self, screen):
        if hasattr(self, "triangle"):
            pygame.draw.polygon(screen, white, self.triangle(), 2)
        else:
            print("Warning: No triangle method defined!")

        
    def update(self, dt):
        # sub-classes must override
        pass