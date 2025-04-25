# this allows us to use code from
# the open-source pygame library
# throughout this file


from constants import *
import pygame


def main():
    pygame.init()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")  # Should work with wildcard import
    print(f"Screen height: {SCREEN_HEIGHT}")  # Should work with wildcard import
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    # Add your game loop here
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
    screen.fill("black")

if __name__ == "__main__":
    main()

