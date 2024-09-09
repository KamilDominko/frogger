import sys
import pygame as pg
from settings import *
from player import Player

pg.init()
pg.init()
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption('Frogger')
clock = pg.time.Clock()

# Grupy.
all_sprites = pg.sprite.Group()

# Sprite'y.
player = Player((600, 400), all_sprites)

# Pętla główna.
while True:
    # Obsługa zdarzeń.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # Klawiatura.
        # if event.type == pg.KEYDOWN:
        #     print("key pressed")

    # Delta Time.
    dt = clock.tick() / 1000

    # Update.
    all_sprites.update(dt)

    # Rysowanie.
    display_surface.fill('black')
    all_sprites.draw(display_surface)

    # Odśwież ekran.
    pg.display.update()
