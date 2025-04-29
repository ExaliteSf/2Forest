import pygame
from scripts.settings import BLEU_JOUEUR, JOUEUR_VITESSE

class Player:
    def __init__(self):
        self.rect = pygame.Rect(400, 300, 50, 50)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= JOUEUR_VITESSE
        if keys[pygame.K_RIGHT]:
            self.rect.x += JOUEUR_VITESSE
        if keys[pygame.K_UP]:
            self.rect.y -= JOUEUR_VITESSE
        if keys[pygame.K_DOWN]:
            self.rect.y += JOUEUR_VITESSE

    def draw(self, surface):
        pygame.draw.rect(surface, BLEU_JOUEUR, self.rect)
