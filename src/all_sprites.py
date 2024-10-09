import pygame as pg
from settings import *


class AllSprites(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pg.math.Vector2()
        self.bg = pg.image.load("../graphics/main/map.png").convert_alpha()
        self.fg = pg.image.load("../graphics/main/overlay.png").convert_alpha()

    def customize_draw(self, surface, player):
        self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2

        surface.blit(self.bg, -self.offset)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            surface.blit(sprite.image, offset_pos)

        surface.blit(self.fg, -self.offset)
