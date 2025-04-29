import pygame
import sys
from scripts.settings import SCREEN_WIDTH, SCREEN_HEIGHT, VERT_FORET
from scripts.player import Player
from scripts.map import Map


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Survie dans la Forêt")
        self.clock = pygame.time.Clock()
        self.player = Player()

        map_data = [
            [0, 1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10, 11],
            [12, 13, 14, 15, 16, 17],
        ]

        self.map = Map("assets/map.png", map_data)



    def run(self):
        running = True
        while running:
            self.clock.tick(60)  # 60 FPS

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.player.update()

            self.screen.fill(VERT_FORET)  # au cas où la map n’occupe pas tout l’écran
            self.map.draw(self.screen)
            self.player.draw(self.screen)


        pygame.quit()
        sys.exit()
