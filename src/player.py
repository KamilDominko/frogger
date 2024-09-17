import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.import_assets()
        self.frame_index = 0
        self.image = self.animation[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        # Float based movement
        self.pos = pg.math.Vector2(self.rect.center)
        self.direction = pg.math.Vector2()
        self.speed = 200

    def import_assets(self):
        path = "../graphics/player/right/"
        self.animation = [pg.image.load(f'{path}{frame}.png').convert_alpha() for frame in range(4)]
        # for frame in range(4):
        #     surf = pg.image.load(f'{path}{frame}.png').convert_alpha()
        #     self.animation.append(surf)
        print(self.animation)

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
        elif keys[pg.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pg.K_UP]:
            self.direction.y = -1
        elif keys[pg.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.animation):
            self.frame_index = 0
        self.image = self.animation[int(self.frame_index)]

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)
