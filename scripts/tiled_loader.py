import pygame
import pytmx

class TiledMap:
    def __init__(self, filename):
        self.tmx_data = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = self.tmx_data.width * self.tmx_data.tilewidth
        self.height = self.tmx_data.height * self.tmx_data.tileheight
        self.collision_rects = self.get_collision_rects("water")  # Nom du calque de collision

    def draw(self, surface, camera):
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    if gid == 0:
                        continue  # Aucun tile à cet endroit
                    tile = self.tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        tile_rect = pygame.Rect(
                            x * self.tmx_data.tilewidth,
                            y * self.tmx_data.tileheight,
                            self.tmx_data.tilewidth,
                            self.tmx_data.tileheight
                        )
                        surface.blit(tile, camera.apply(tile_rect))

    def get_collision_rects(self, layer_name):
        rects = []
        layer = self.tmx_data.get_layer_by_name(layer_name)
        for x, y, gid in layer:
            if gid != 0:
                rect = pygame.Rect(
                    x * self.tmx_data.tilewidth,
                    y * self.tmx_data.tileheight,
                    self.tmx_data.tilewidth,
                    self.tmx_data.tileheight
                )
                rects.append(rect)
        return rects
