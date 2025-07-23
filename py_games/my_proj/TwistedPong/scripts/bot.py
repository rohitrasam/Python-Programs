from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Game
from scripts.utils import debug
import pygame as pg


class Bot:

    def __init__(self, game: 'Game', pos: list[int], size: list[int], level: int=1):
        self.game = game
        self.pos = pg.Vector2(pos)
        self.vel = pg.Vector2(1)
        self.size = size
        self.level = level
        self.speed = [400, 425, 450, 475, 500]
        self.trigger =  0.5
    
    @property
    def rect(self) -> pg.Rect:
        return pg.Rect(*self.pos, *self.size)

    def update(self, dt: float):
        if self.pos.x - self.game.ball.pos.x < self.game.get_display_width() * self.trigger:
            dist = pg.Vector2.distance_to(self.pos, self.game.ball.pos)
            self.vel.y = (self.game.ball.pos.y - self.pos.y) / dist
        else:
            self.vel.y = 0

        if self.pos.y <= 0 and self.vel.y < 0:
            self.pos.y = 0
            self.vel.y = 0
        if self.pos.y + self.size[1] >= self.game.get_display_height() and self.vel.y > 0:
            self.pos.y = self.game.get_display_height() - self.size[1]
            self.vel.y = 0

        self.pos.y += int(self.vel.y * self.speed[self.level-1] * dt)

    def render(self):
        self.game.display.blit(self.game.assets['player'], self.pos)