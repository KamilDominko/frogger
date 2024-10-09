import sys
import pygame as pg
from random import choice, randint
from settings import *
from player import Player
from car import Car
from all_sprites import AllSprites

pg.init()
pg.init()
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption('Frogger')
clock = pg.time.Clock()

# Grupy.
# all_sprites = pg.sprite.Group()
all_sprites = AllSprites()

# Sprite'y.
# car1 = Car((1000, 200), all_sprites)
# car2 = Car((100, 200), all_sprites)
# car3 = Car((600, 200), all_sprites)
player = Player((600, 400), all_sprites)

# Timery.
car_timer = pg.event.custom_type()
pg.time.set_timer(car_timer, 50)

pos_list = list()

# Pętla główna.
while True:
    # Obsługa zdarzeń.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == car_timer:
            random_pos = choice(CAR_START_POSITIONS)
            if random_pos not in pos_list:
                pos_list.append(random_pos)
                pos = (random_pos[0], random_pos[1] + randint(-10, 10))
                Car(pos, all_sprites)
            if len(pos_list) > 5:
                del pos_list[0]

    # Delta Time.
    dt = clock.tick() / 1000

    # Update.
    all_sprites.update(dt)

    # Rysowanie.
    display_surface.fill('black')
    # all_sprites.draw(display_surface)
    all_sprites.customize_draw(display_surface, player)

    # Odśwież ekran.
    pg.display.update()
