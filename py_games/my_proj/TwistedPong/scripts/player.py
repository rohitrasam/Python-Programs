from __future__ import annotations
import pygame as pg
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Game


class Player:

    def __init__(self, game: 'Game', pos: list[float], size: list[float], player_type: str):
        self.game = game
        self.pos = pg.Vector2(pos)
        self.size = size
        self.vel = pg.Vector2()
        self.speed = 300
        self.player_type = player_type

    @property
    def rect(self) -> pg.Rect:
        return pg.Rect(*self.pos, *self.size)

    def update(self, dt: float):
        self.vel = pg.Vector2()
        keys = pg.key.get_pressed()
        if self.player_type == "P1":
            if keys[pg.K_w]:
                self.vel.y = -self.speed
            if keys[pg.K_s]:
                self.vel.y = self.speed

        if self.player_type == "P2":
            if keys[pg.K_UP]:
                self.vel.y = -self.speed
            if keys[pg.K_DOWN]:
                self.vel.y = self.speed
            
        if self.pos.y <= 0 and self.vel.y < 0:
            self.pos.y = 0
            self.vel.y = 0
        if self.pos.y + self.size[1] >= self.game.get_display_height() and self.vel.y > 0:
            self.pos.y = self.game.get_display_height() - self.size[1]
            self.vel.y = 0

        self.pos.y += int(self.vel.y * dt)

    def render(self):
        self.game.display.blit(self.game.assets['player'], self.pos)

