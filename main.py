# this allows us to use code from
# the open-source pygame library
# throughout this file

import sys
from constants import *
from player import *
from asteroidfield import *
from asteroids import Asteroid
import pygame


def main():
    pygame.init()
    
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")  # Should work with wildcard import
    print(f"Screen height: {SCREEN_HEIGHT}")  # Should work with wildcard import
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    #Groups
    updatable = pygame.sprite.Group()
    #drawable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    
    
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    #print(drawable.sprites())
    dt = 0
    
    
   
    
    # Add your game loop here
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        for asteroid in asteroids:
             if asteroid.collides_with(player):
                 print("Game over!")
                 sys.exit()
                 
             for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
        screen.fill("black")    
        #player.update(dt)
        
        for obj in drawable:
            obj.draw(screen)   
        
        #player.draw(screen)
        pygame.display.flip()
        

    
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

