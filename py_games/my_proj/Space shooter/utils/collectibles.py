from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Game
import math
from .consts import *
from random import randint

class Collectibles:

    def __init__(self, game: Game, img: pg.Surface) -> None:
        self.game = game
        self.star_pos = self.pos = vec2(WIDTH + 50, (randint(3, 5) / 10)*HEIGHT)
        self.vel = vec2(randint(2, 5), randint(4, 8))
        self.surf = img
        self.rect = self.surf.get_rect(center=self.pos)
        self.angle = 0
        # reset to original position
        self.reset = False    

    def update(self):
        self.pos.x -= self.vel.x
        self.pos.y += self.vel.y*math.sin(self.angle)
        self.angle += 0.04
        self.rect.center = self.pos
        if self.reset:
            self.pos = self.star_pos
    
    def render(self):
        self.game.display.blit(self.surf, self.rect)
        self.update()

class HealthPack(Collectibles):

    def __init__(self, game: Game, img: pg.Surface) -> None:
        super().__init__(game, img)

class MissilePack(Collectibles):
    
    def __init__(self, game: Game, img: pg.Surface) -> None:
        super().__init__(game, img)
