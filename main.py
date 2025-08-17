import pygame
import player
from constants import *

def main():
    pygame.init()

    game_clock = pygame.time.Clock()
    fps = 60
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    players = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))
        players.draw(screen)
        pygame.display.flip()

        dt = 1000 / game_clock.tick(fps)

if __name__ == "__main__":
    main()
