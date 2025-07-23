from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Game
from .utils import debug
import pygame as pg
from random import choice


class Ball:

    def __init__(self, game: 'Game', pos: list[float], size: int=10):
        self.game = game
        self.pos = pg.Vector2(pos)
        self.size = size
        self.vel = pg.Vector2(choice((-1,1)), choice((-1, 1)))
        self.speed = 200
        self.speed_percent = 0

    @property
    def rect(self):
        return pg.Rect(*self.pos, self.size, self.size)

    def update(self, dt: float):
        
        # Horizontal border check
        # if self.pos.x + self.size > self.game.display.get_width()-2:
        #     self.vel.x = -self.vel.x
        
        # Vertical border check
        if self.pos.y + self.size > self.game.get_display_height()-5 or self.pos.y < 5:
            self.vel.y = -self.vel.y

        # Handle collision with player
        if abs(self.pos.x - self.game.entities[0].pos.x) < 100:
            rect = self.rect
            entity1_rect = self.game.entities[0].rect
            if rect.colliderect(entity1_rect) and self.vel.x < 0:
                if abs(self.rect.left - entity1_rect.right) < 5:
                    self.vel.x = -self.vel.x
                    mid_dist = abs((self.pos.y + self.size / 2) - (self.game.entities[0].pos.y + self.game.entities[0].size[1] / 2))
                    self.speed_percent = mid_dist / (self.game.entities[0].size[1] / 2)
                    
        
        if abs(self.pos.x - self.game.entities[1].pos.x) < 100:

            rect = self.rect
            entity2_rect = self.game.entities[1].rect
            if rect.colliderect(entity2_rect) and self.vel.x > 0:
                if abs(self.rect.right - entity2_rect.left) < 5:
                    self.vel.x = -self.vel.x
                    mid_dist = abs((self.pos.y + self.size / 2) - (self.game.entities[1].pos.y + self.game.entities[1].size[1] / 2))
                    self.speed_percent = mid_dist / (self.game.entities[0].size[1] / 2)

        self.pos.x += int(self.vel.x * self.speed * dt)
        # self.pos.y += int(self.vel.y * (self.speed + self.speed_red) * dt)
        self.pos.y += int(self.vel.y *  self.speed * (0.75 + self.speed_percent) * dt)

    def render(self):
        # pg.draw.circle(self.game.display, (100, 100, 100), self.pos, self.size)
        # pg.draw.rect(self.game.display, (100, 100, 100), (*self.pos, *self.game.assets['ball'].get_rect().size))
        self.game.display.blit(self.game.assets['ball'], self.pos)
