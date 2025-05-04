import pygame
from scripts.settings import JOUEUR_VITESSE

class Enemy:
    def __init__(self, position):
        self.spritesheet = pygame.image.load("assets/characters/skeleton.png").convert_alpha()

        self.frame_width = 36
        self.frame_height = 36
        self.centers_x = [24 + i * 48 for i in range(6)]

        self.frames_walk = [self.get_frame(x, 178) for x in self.centers_x]
        self.current_frame = 0
        self.image = self.frames_walk[0]
        self.rect = self.image.get_rect(center=position)

        self.last_switch = pygame.time.get_ticks()
        self.switch_delay = 150

        # IA : patrouille horizontale
        self.direction = 1
        self.patrol_distance = 100
        self.start_x = position[0]

    def get_frame(self, cx, cy):
        x = cx - self.frame_width // 2
        y = cy - self.frame_height // 2
        return self.spritesheet.subsurface(pygame.Rect(x, y, self.frame_width, self.frame_height)).copy()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_switch >= self.switch_delay:
            self.last_switch = now
            self.current_frame = (self.current_frame + 1) % len(self.frames_walk)

        # Patrouille simple gauche/droite
        self.rect.x += self.direction * JOUEUR_VITESSE
        if abs(self.rect.x - self.start_x) > self.patrol_distance:
            self.direction *= -1  # demi-tour

        self.image = self.frames_walk[self.current_frame]

    def draw(self, surface, camera):
        surface.blit(self.image, camera.apply(self.rect))
