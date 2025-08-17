import pygame
import player
from constants import *

def main():
    
    pygame.init()

    # defines groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # adds all Player method's to the updateable and drawable groups
    player.Player.containers = (updateable, drawable)

    # has player start in the center of the screen
    player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    game_clock = pygame.time.Clock()
    fps = 60
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # updates everything in updateable group
        updateable.update(dt)

        # draws a black screen
        screen.fill((0, 0, 0))
        
        # draws all objects in drawable group
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()

        dt = game_clock.tick(fps) / 1000

if __name__ == "__main__":
    main()
