import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    pygame.display.set_caption('Asteroids, I love my Philippa-kitten!')
    clock = pygame.time.Clock()
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    bullets_group = pygame.sprite.Group()
    Bullet.containers = (bullets_group, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    

    game = True
    while game:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)
        updatable.update(dt)
        # In your game loop
        for asteroid in asteroids:
            for bullet in bullets_group:
                if asteroid.collisions(bullet):
                    print("Collision detected!")
                    asteroid.split()
                    bullet.kill()
                if player.collisions(asteroid):
                    print("Game Over!")
                    import sys
                    sys.exit()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()