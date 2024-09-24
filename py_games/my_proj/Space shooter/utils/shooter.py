from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Game
from random import randint
from .consts import *
from .entity import Entity
from .bullet import Bullet
from.particles import Smoke, Spark

class Shooter(Entity):
    
    def __init__(self, game: Game, pos: list[float], img: pg.Surface) -> None:
        super().__init__()
        self.game = game
        self.pos = vec2(pos)
        self.surf = img 
        self.surf_copy = self.surf
        self.rect = self.surf_copy.get_rect(center=self.pos)
        self.mask = pg.mask.from_surface(self.surf_copy)
        self.vel = vec2(0, 0)
        self.max_hp = 100
        self.hp = self.max_hp
        self.angle = 0
        self.is_visible = True
        
    def update(self):
        self.angle = Entity.get_angle(self.pos)
        self.surf_copy = pg.transform.rotate(self.surf, self.angle - 90)
        self.mask = pg.mask.from_surface(self.surf_copy)
        self.rect = self.surf_copy.get_rect(center=self.pos)

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.vel.y = -VEL
        if keys[pg.K_s]:
            self.vel.y = VEL    
        if keys[pg.K_a] and self.rect.left >= 0:
            self.vel.x = -VEL
        if keys[pg.K_d]:
            self.vel.x = VEL

        # TODO: implement after Enemy class and shoot method
        if self.hp <= 0:
            self.explosion.play()
            self.game.player = None
        
        
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel = self.vel.normalize() * VEL

        self.pos += self.vel

        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        
        # self.rect.center = self.pos no need to assign rect to pos again
        self.vel = vec2(0, 0)

    def render(self):
        hp_ratio = self.hp/self.max_hp
        pg.draw.rect(self.game.display, "red", (75, 18, 300, 20))
        pg.draw.rect(self.game.display, "lightgreen", (75, 18, 300*hp_ratio, 20))
        self.game.display.blit(self.surf_copy, self.rect)
        self.update()
        # self.health()

    def shoot(self):
        self.gunshot.play().set_volume(0.1)
        mx, my = pg.mouse.get_pos()
        return Bullet(self.game, (20, 10), self.rect.center, (mx, my), self.game.assets["bullet"], SHOOTER, self.angle)

    def health(self):
        ratio = self.hp / self.max_hp
        if ratio <= 0.3:
            for _ in range(7):
                self.game.smoke.append(Smoke(self.game, randint(MIN_RAD, MAX_RAD), self.pos))

        
    # def __del__(self):
    #     pass