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
        print("Drawing player...")
        if hasattr(self, "triangle"):
            pygame.draw.polygon(screen, white, self.triangle(), 2)
        else:
            print("Warning: No triangle method defined!")

        
    def update(self, dt):
        # sub-classes must override
        pass