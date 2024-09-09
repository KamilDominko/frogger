import sys
import pygame as pg
from src.settings import *

pg.init()
pg.init()
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption('Frogger')
clock = pg.time.Clock()

# Pętla główna.
while True:
    # Obsługa zdarzeń.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # Klawiatura.
        if event.type == pg.KEYDOWN:
            print("asd")

    # Delta Time.
    dt = clock.tick() / 1000

    # Odśwież ekran.
    pg.display.update()
