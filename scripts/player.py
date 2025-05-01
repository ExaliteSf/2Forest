import pygame
from scripts.settings import JOUEUR_VITESSE

class Player:
    def __init__(self):
        self.spritesheet = pygame.image.load("assets/characters/player.png").convert_alpha()

        self.frame_width = 36
        self.frame_height = 36

        self.centers_x = [24 + i * 48 for i in range(6)]

        # === FRAMES PAR DIRECTION ===
        self.frames_idle_down = [self.get_frame(x, 34) for x in self.centers_x]
        self.frames_walk_down = [self.get_frame(x, 178) for x in self.centers_x]

        self.frames_idle_right = [self.get_frame(x, 82) for x in self.centers_x]
        self.frames_walk_right = [self.get_frame(x, 225) for x in self.centers_x]

        self.frames_idle_up = [self.get_frame(x, 130) for x in self.centers_x]
        self.frames_walk_up = [self.get_frame(x, 273) for x in self.centers_x]

        # Gauche = flip des frames droite
        self.frames_idle_left = [pygame.transform.flip(img, True, False) for img in self.frames_idle_right]
        self.frames_walk_left = [pygame.transform.flip(img, True, False) for img in self.frames_walk_right]

        # === ATTACK FRAMES (4 par direction) ===
        self.frames_attack_down = [self.get_frame(x, 323) for x in self.centers_x[:4]]
        self.frames_attack_right = [self.get_frame(x, 371) for x in self.centers_x[:4]]
        self.frames_attack_up = [self.get_frame(x, 418) for x in self.centers_x[:4]]
        self.frames_attack_left = [pygame.transform.flip(img, True, False) for img in self.frames_attack_right]

        # === ÉTAT ACTUEL ===
        self.direction = "down"
        self.moving = False
        self.current_frame = 0
        self.image = self.frames_idle_down[0]
        self.rect = self.image.get_rect(center=(400, 300))

        # Animation générale
        self.last_switch = pygame.time.get_ticks()
        self.switch_delay = 100

        # Attaque
        self.attacking = False
        self.attack_frame = 0
        self.attack_start_time = 0
        self.attack_delay = 1000      # Délai entre attaques
        self.attack_frame_duration = 100  # Durée d'une frame d'attaque

    def get_frame(self, cx, cy):
        x = cx - self.frame_width // 2
        y = cy - self.frame_height // 2
        return self.spritesheet.subsurface(pygame.Rect(x, y, self.frame_width, self.frame_height)).copy()

    def get_attack_frame(self):
        if self.direction == "down":
            return self.frames_attack_down[self.attack_frame]
        elif self.direction == "right":
            return self.frames_attack_right[self.attack_frame]
        elif self.direction == "left":
            return self.frames_attack_left[self.attack_frame]
        elif self.direction == "up":
            return self.frames_attack_up[self.attack_frame]

    def update(self):
        keys = pygame.key.get_pressed()

        now = pygame.time.get_ticks()

        # Déclenchement de l’attaque
        if keys[pygame.K_e] and not self.attacking:
            if now - self.attack_start_time >= self.attack_delay:
                self.attacking = True
                self.attack_start_time = now
                self.attack_frame = 0
                self.last_switch = now

        # === Si en pleine attaque ===
        if self.attacking:
            if now - self.last_switch >= self.attack_frame_duration:
                self.last_switch = now
                self.attack_frame += 1
                if self.attack_frame >= 4:
                    self.attack_frame = 0
                    self.attacking = False
                else:
                    self.image = self.get_attack_frame()
            else:
                self.image = self.get_attack_frame()
            return  # ne rien faire d’autre pendant l’attaque

        # === Déplacement normal ===
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

        # Animation standard
        if now - self.last_switch >= self.switch_delay:
            self.last_switch = now
            self.current_frame = (self.current_frame + 1) % 6

        # Choix des frames classiques
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
