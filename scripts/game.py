import pygame
import sys
from scripts.settings import SCREEN_WIDTH, SCREEN_HEIGHT, VERT_FORET
from scripts.player import Player
from scripts.tiled_loader import TiledMap

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Survie dans la Forêt")
        self.clock = pygame.time.Clock()
        self.player = Player()

        # Chargement de la carte depuis Tiled
        self.map = TiledMap("assets/maps/map.tmx")


    def run(self):
        running = True
        while running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.player.update()

            self.screen.fill(VERT_FORET)
            self.map.draw(self.screen)
            self.player.draw(self.screen)

            pygame.display.flip()

        pygame.quit()
        sys.exit()
