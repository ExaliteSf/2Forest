import pygame

class Camera:
    def __init__(self, screen_size, map_size, zoom=1):
        self.screen_width, self.screen_height = screen_size
        self.map_width, self.map_height = map_size
        self.zoom = zoom

        self.offset_x = 0  # <- nécessaire
        self.offset_y = 0  # <- nécessaire

        self.render_surface = pygame.Surface(
            (self.screen_width // self.zoom, self.screen_height // self.zoom)
        )

    def apply(self, target_rect):
        """Décale une position selon la caméra"""
        return target_rect.move(-self.offset_x, -self.offset_y)

    def center_on(self, target_rect):
        """Centre la caméra sur le joueur"""
        self.offset_x = max(0, min(
            target_rect.centerx - self.render_surface.get_width() // 2,
            self.map_width - self.render_surface.get_width()
        ))

        self.offset_y = max(0, min(
            target_rect.centery - self.render_surface.get_height() // 2,
            self.map_height - self.render_surface.get_height()
        ))

    def draw_to_screen(self, screen):
        """Dessine la surface zoomée sur l'écran"""
        scaled = pygame.transform.scale(self.render_surface, (self.screen_width, self.screen_height))
        screen.blit(scaled, (0, 0))



