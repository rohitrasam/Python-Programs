from __future__ import annotations
import pygame as pg
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Game


class Entity:

    def __init__(self, game: 'Game', type: str, size: list[int], pos: list[int]) -> None:
        self.game = game
        self.size = list(size)
        self.pos = pg.Vector2(pos)
        self.vel = pg.Vector2(0)

    def update(self):

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.vel.y = -2
        if keys[pg.K_s]:
            self.vel.y = 2
        if keys[pg.K_a]:
            self.vel.x = -2
        if keys[pg.K_d]:
            self.vel.x = 2

        # self.vel.y = min(self.vel.y + 0.5, 10)

        self.pos += self.vel
        self.vel = pg.Vector2(0)

    def render(self):
        self.game.display.blit(self.game.sprites['player'], self.pos)