import pygame as pg
from os import walk


class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.import_assets()
        self.frame_index = 0
        self.status = "down"
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        # Float based movement
        self.pos = pg.math.Vector2(self.rect.center)
        self.direction = pg.math.Vector2()
        self.speed = 200

    def import_assets(self):
        self.animations = dict()
        for index, folder in enumerate(walk("../graphics/player")):
            if index == 0:
                for name in folder[1]:
                    self.animations[name] = []
            else:
                for image in folder[2]:
                    path = str(folder[0]).replace("\\", "/") + "/" + image
                    img = pg.image.load(path).convert_alpha()
                    key = folder[0].split("\\")[1]
                    self.animations[key].append(img)

    def move(self, dt):
        # Znormalizuj wektor, jeżeli jego długość nie równa zero.
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        else:
            self.direction.x = 0
        if keys[pg.K_UP]:
            self.direction.y = -1
            self.status = "up"
        elif keys[pg.K_DOWN]:
            self.direction.y = 1
            self.status = "down"
        else:
            self.direction.y = 0

    def animate(self, dt):
        current_animation = self.animations[self.status]
        if self.direction.magnitude() != 0:
            self.frame_index += 10 * dt
            if self.frame_index >= len(current_animation):
                self.frame_index = 0
        else:
            self.frame_index = 0
        self.image = current_animation[int(self.frame_index)]

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)
