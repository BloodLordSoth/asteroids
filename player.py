import pygame
from constants import *
from circleshape import *
from asteroid import *

class Player(CircleShape):
    def __init__(self, x, y, PLAYER_RADIUS):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self, dt):
        if self.shot_timer <= 0:
            bullet = Bullet(self.position.x, self.position.y, self.rotation, SHOT_RADIUS, PLAYER_SHOOT_SPEED)
            self.shot_timer = PLAYER_SHOOT_COOLDOWN
            print(f"Bullet created at: {bullet.position} with velocity: {bullet.velocity}")


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
         # in the player class
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        # Convert Vector2 objects to tuples
        return [(a.x, a.y), (b.x, b.y), (c.x, c.y)]
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        if self.shot_timer > 0:
            self.shot_timer -= dt