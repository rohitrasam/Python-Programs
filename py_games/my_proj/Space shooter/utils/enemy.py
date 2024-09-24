from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Game
import math
from random import randint, random
from .consts import *
from .entity import Entity
from .bullet import Bullet
from .particles import Smoke

class Enemy(Entity):

    def __init__(self, game: Game, img: pg.Surface) -> None:
        super().__init__()
        self.game = game
        self.pos = vec2(WIDTH + randint(25, 75), HEIGHT * random())
        self.surf = img
        self.surf_copy =self.surf
        self.rect = self.surf_copy.get_rect(center=self.pos)
        self.mask = pg.mask.from_surface(self.surf_copy)
        self.vel = vec2(0, 0)
        self.max_hp = 5
        self.hp = self.max_hp
        self.angle = 0
        self.drag = randint(3, 5) / 10

    def update(self):
        self.angle = Entity.get_angle(self.pos, self.game.player.pos)
        self.surf_copy = pg.transform.rotate(self.surf, self.angle - 90)
        self.mask = pg.mask.from_surface(self.surf_copy)
        self.rect = self.surf_copy.get_rect(center=self.pos)
        
        dist = math.hypot(self.game.player.pos.x - self.pos.x, self.game.player.pos.y - self.pos.y)
        self.vel.x = self.game.player.pos.x - self.pos.x
        self.vel.y = self.game.player.pos.y - self.pos.y

    
        self.pos += (self.vel / dist) * VEL * self.drag/1.2
        self.rect.center = self.pos
    
    def shoot(self):
        self.gunshot.play().set_volume(0.1)
        return Bullet(self.game, (20, 10), self.rect.center, self.game.player.rect.center, self.game.assets["bullet"], ENEMY, self.angle)
    
    def render(self):
        self.game.display.blit(self.surf_copy, self.rect)
        self.update()
        self.health()
    
    def health(self):
        ratio = self.hp / self.max_hp
        if ratio <= 0.3:
            for _ in range(7):
                self.game.smoke.append(Smoke(self.game, randint(MIN_RAD, MAX_RAD), self.pos)) 
        if self.hp <= 0:
            self.explosion.play().set_volume(0.5)
            self.game.enemies.remove(self)
        

