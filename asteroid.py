import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = new_velocity1 * 1.2
            new_asteroid2.velocity = new_velocity2 * 1.2

            

        
    def draw(self, screen):
        pygame.draw.circle(screen, white, self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += (self.velocity * dt)

class Bullet(CircleShape):
    def __init__(self, x, y, rotation, SHOT_RADIUS, PLAYER_SHOOT_SPEED):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED
          
    def draw(self, screen):
        pygame.draw.circle(screen, white, self.position, self.radius, 2)
        
    # In your Bullet class update method
    def update(self, dt):
    # Update position based on velocity and direction
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt    
    # Print position for debugging
        #print(f"Bullet position: {self.position}")
