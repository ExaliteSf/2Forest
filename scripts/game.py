import pygame
import sys
from scripts.settings import SCREEN_WIDTH, SCREEN_HEIGHT, VERT_FORET
from scripts.player import Player
from scripts.tiled_loader import TiledMap
from scripts.camera import Camera
from scripts.enemy import Enemy


class Game:
    def __init__(self):
        # Initialisation pygame
        pygame.init()

        # Musique
        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/music/forest.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        # Fenêtre
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Survie dans la Forêt")
        self.clock = pygame.time.Clock()

        # Map et caméra
        self.map = TiledMap("assets/maps/map.tmx")
        self.camera = Camera(
            screen_size=(SCREEN_WIDTH, SCREEN_HEIGHT),
            map_size=(self.map.width, self.map.height),
            zoom=3
        )

        # Joueur et ennemi
        center_x = self.map.width // 2
        center_y = self.map.height // 2
        self.player = Player((center_x, center_y))
        self.enemy = Enemy((center_x, center_y - 100))  # l’ennemi est juste au-dessus du joueur

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Mise à jour
            self.player.update(self.map.collision_rects)
            self.enemy.update()
            self.camera.center_on(self.player.rect)

            # Dessin
            self.camera.render_surface.fill(VERT_FORET)
            self.map.draw(self.camera.render_surface, self.camera)

            # Dessiner l’ennemi et son contour rouge
            self.enemy.draw(self.camera.render_surface, self.camera)
            pygame.draw.rect(
                self.camera.render_surface,
                (255, 0, 0),
                self.camera.apply(self.enemy.rect),
                2  # épaisseur du contour
            )

            self.player.draw(self.camera.render_surface, self.camera)

            self.camera.draw_to_screen(self.screen)
            pygame.display.flip()

        pygame.quit()
        sys.exit()
