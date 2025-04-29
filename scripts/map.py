import pygame

# === CONFIGURATION ===
TAILLE_TUILE = 22       # Taille native d'une tuile dans le spritesheet
ZOOM = 3                # Facteur d'agrandissement
TAILLE_TUILE_AFFICHEE = TAILLE_TUILE * ZOOM

# Taille de la fenêtre adaptée automatiquement
NB_COLONNES = 12
NB_LIGNES = 9
SCREEN_WIDTH = NB_COLONNES * TAILLE_TUILE_AFFICHEE
SCREEN_HEIGHT = NB_LIGNES * TAILLE_TUILE_AFFICHEE

# === DONNÉES DE LA MAP ===
map_data = [
    [110, 15, 2, 15, 15, 48, 17, 19, 47, 33, 45, 1],
    [15, 35, 34, 50, 34, 15, 34, 5, 32, 19, 48, 45],
    [31, 4, 31, 15, 15, 31, 4, 50, 16, 15, 31, 47],
    [2, 45, 47, 18, 18, 65, 4, 20, 32, 50, 19, 32],
    [61, 1, 62, 33, 78, 49, 45, 34, 34, 17, 61, 50],
    [34, 30, 4, 47, 4, 110, 110, 62, 61, 52, 61, 61],
    [64, 60, 34, 45, 16, 33, 60, 48, 5, 108, 91, 78],
    [45, 45, 45, 45, 40, 78, 47, 101, 67, 108, 78, 87],
    [61, 67, 110, 110, 108, 91, 83, 87, 101, 36, 45, 45]
]

# === FONCTION POUR EXTRAIRE ET REDIMENSIONNER LES TUILES ===
def charger_tuiles(image_path):
    sheet = pygame.image.load(image_path).convert_alpha()
    sheet_width, sheet_height = sheet.get_size()
    tiles = []

    for y in range(0, sheet_height, TAILLE_TUILE):
        for x in range(0, sheet_width, TAILLE_TUILE):
            rect = pygame.Rect(x, y, TAILLE_TUILE, TAILLE_TUILE)
            tile = sheet.subsurface(rect)
            tile = pygame.transform.scale(tile, (TAILLE_TUILE_AFFICHEE, TAILLE_TUILE_AFFICHEE))
            tiles.append(tile)

    return tiles

# === INITIALISATION PYGAME ===
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Survie dans la Forêt")

# === CHARGER LES TUILES ===
tiles = charger_tuiles("assets/map.png")

# === BOUCLE PRINCIPALE ===
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))

    # Afficher la map
    for ligne_idx, ligne in enumerate(map_data):
        for col_idx, tile_idx in enumerate(ligne):
            if tile_idx < len(tiles):
                x = col_idx * TAILLE_TUILE_AFFICHEE
                y = ligne_idx * TAILLE_TUILE_AFFICHEE
                screen.blit(tiles[tile_idx], (x, y))

    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mettre à jour l'écran
    pygame.display.flip()
    clock.tick(60)

# === FERMETURE PYGAME ===
pygame.quit()
