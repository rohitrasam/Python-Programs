# from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Game
import math
from random import random, randint
from .consts import *
from .particles import Spark

class Bullet:

    ammo = []

    def __init__(self, game: 'Game', size: list[float], pos: list[float], dest: list[float], img: pg.Surface, _type: str, angle: float) -> None:
        self.game = game
        self.pos = vec2(pos)
        self.size = size
        self.angle = angle
        self.type = _type
        self.surf = pg.transform.scale(img, self.size)
        self.surf_copy = pg.transform.rotate(self.surf, self.angle)
        self.rect = self.surf_copy.get_rect(center=pos)
        self.mask = pg.mask.from_surface(self.surf_copy)
        self.dest = vec2(dest)
        self.dir = vec2(self.dest.x - self.pos.x, self.dest.y - self.pos.y)
        self.dist = ((self.dir.x)**2 + (self.dir.y)**2)**0.5
        self.vel = vec2(0, 0)
        # self.bounces = 1
    
    def update(self):
        if self.dist > 0:
            self.vel.x = (self.dir.x / self.dist)* BULLET_VEL
            self.vel.y = (self.dir.y / self.dist)* BULLET_VEL
        
        self.pos += self.vel
        self.rect.center = self.pos

        if self.rect.centerx > WIDTH + 40 or self.rect.centerx < -40 or self.rect.centery >  HEIGHT + 40 or self.rect.centery < -40:
            Bullet.ammo.remove(self)

        """Collision detection"""
        enemy_idx = self.rect.collidelist(self.game.enemies)

        if self.rect.colliderect(self.game.player.rect) and self.type == ENEMY:
            offset = (self.game.player.rect.x - self.rect.x, self.game.player.rect.y - self.rect.y)
            if self.mask.overlap(self.game.player.mask, offset):
                for _ in range(15):
                    self.game.sparks.append(Spark(self.game, WHITE, random()*math.tau, self.pos, randint(MIN_SPEED, MAX_SPEED)))
                self.game.player.hp -= 1
                Bullet.ammo.remove(self)
        
        if enemy_idx > -1 and self.type == SHOOTER:
            enemy = self.game.enemies[enemy_idx]
            offset = (enemy.rect.x - self.rect.x, enemy.rect.y - self.rect.y)
            if self.mask.overlap(enemy.mask, offset):
                for _ in range(10):
                    self.game.sparks.append(Spark(self.game, WHITE, random()*math.tau, self.pos, randint(MIN_SPEED, MAX_SPEED)))
                enemy.hp -= 1
                # self.game.enemies[enemy_idx].hp -= 1
                Bullet.ammo.remove(self)


    def render(self):
        self.game.display.blit(self.surf_copy, self.rect)
        self.update()