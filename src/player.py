import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pg.Surface((50, 50))
        self.image.fill("red")
        self.rect = self.image.get_rect(center=pos)

    def input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.rect.x += 1
        if keys[pg.K_LEFT]:
            self.rect.x -= 1
        if keys[pg.K_UP]:
            self.rect.y -= 1
        if keys[pg.K_DOWN]:
            self.rect.y += 1

    def update(self):
        self.input()
