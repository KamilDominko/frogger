import pygame as pg
from os import listdir
from random import choice


class Car(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pg.image.load(f"../graphics/cars/{choice(listdir("../graphics/cars/"))}").convert_alpha()
        self.rect = self.image.get_rect(center=pos)

        # float based movement
        self.pos = pg.math.Vector2(self.rect.center)
        if pos[0] < 200:
            self.direction = pg.math.Vector2(1, 0)
        else:
            self.direction = pg.math.Vector2(-1, 0)
            self.image = pg.transform.flip(self.image, True, False)
        self.speed = 0

    def update(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

        if not -200 < self.rect.x < 3400:
            self.kill()


if __name__ == '__main__':
    car = Car((0, 0), pg.sprite.Group())
    print(car.image)
