import pygame
from scripts.settings import JOUEUR_VITESSE

class Player:
    def __init__(self):
        self.spritesheet = pygame.image.load("assets/characters/player.png").convert_alpha()

        self.frame_width = 24
        self.frame_height = 28

        self.centers_x = [24 + i * 48 for i in range(6)]

        # === FRAMES PAR DIRECTION ===
        self.frames_idle_down = [self.get_frame(x, 34) for x in self.centers_x]
        self.frames_walk_down = [self.get_frame(x, 178) for x in self.centers_x]

        self.frames_idle_right = [self.get_frame(x, 82) for x in self.centers_x]
        self.frames_walk_right = [self.get_frame(x, 225) for x in self.centers_x]

        self.frames_idle_up = [self.get_frame(x, 130) for x in self.centers_x]
        self.frames_walk_up = [self.get_frame(x, 273) for x in self.centers_x]

        # === GAUCHE = FLIP DES SPRITES DROITE ===
        self.frames_idle_left = [pygame.transform.flip(img, True, False) for img in self.frames_idle_right]
        self.frames_walk_left = [pygame.transform.flip(img, True, False) for img in self.frames_walk_right]

        # === ÉTAT ACTUEL ===
        self.direction = "down"
        self.moving = False
        self.current_frame = 0
        self.image = self.frames_idle_down[0]
        self.rect = self.image.get_rect(center=(400, 300))

        self.last_switch = pygame.time.get_ticks()
        self.switch_delay = 100

    def get_frame(self, cx, cy):
        x = cx - self.frame_width // 2
        y = cy - self.frame_height // 2
        return self.spritesheet.subsurface(pygame.Rect(x, y, self.frame_width, self.frame_height)).copy()

    def update(self):
        keys = pygame.key.get_pressed()
        self.moving = False

        if keys[pygame.K_DOWN]:
            self.rect.y += JOUEUR_VITESSE
            self.direction = "down"
            self.moving = True
        elif keys[pygame.K_RIGHT]:
            self.rect.x += JOUEUR_VITESSE
            self.direction = "right"
            self.moving = True
        elif keys[pygame.K_UP]:
            self.rect.y -= JOUEUR_VITESSE
            self.direction = "up"
            self.moving = True
        elif keys[pygame.K_LEFT]:
            self.rect.x -= JOUEUR_VITESSE
            self.direction = "left"
            self.moving = True

        now = pygame.time.get_ticks()
        if now - self.last_switch >= self.switch_delay:
            self.last_switch = now
            self.current_frame = (self.current_frame + 1) % 6

        # Choix des frames
        if self.direction == "down":
            self.image = self.frames_walk_down[self.current_frame] if self.moving else self.frames_idle_down[self.current_frame]
        elif self.direction == "right":
            self.image = self.frames_walk_right[self.current_frame] if self.moving else self.frames_idle_right[self.current_frame]
        elif self.direction == "left":
            self.image = self.frames_walk_left[self.current_frame] if self.moving else self.frames_idle_left[self.current_frame]
        elif self.direction == "up":
            self.image = self.frames_walk_up[self.current_frame] if self.moving else self.frames_idle_up[self.current_frame]

    def draw(self, surface):
        surface.blit(self.image, self.rect)
