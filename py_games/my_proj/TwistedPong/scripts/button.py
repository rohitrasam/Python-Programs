import math
from typing import TYPE_CHECKING

from scripts.utils import debug
if TYPE_CHECKING:
    from ..main import Game
import pygame as pg

class Button:

    def __init__(self, game: 'Game', text: str, pos: list[int], size=[77, 20]):
        self.game = game
        self.pos = pg.Vector2(pos)
        self.size = size
        # self.color = color
        self.text = text
        self.hover = False
        self.angle = 0
        # self.font = pg.font.Font("data/fonts/Pixeboy.ttf", size=self.size)
        # self.surf = self.font.render(self.text, False, self.color)

    @property
    def rect(self):
        return pg.Rect(self.pos.x-self.size[0] // 2, self.pos.y-self.size[1] // 2, *self.size)

    def update(self, dt: float):
        self.pos.y += math.sin(self.angle*5) * dt * 20
        self.angle = (self.angle + 0.015) % math.tau


    def render(self):
        self.game.display.blit(self.game.assets[self.text], [self.pos.x-self.size[0] // 2, self.pos.y-self.size[1] // 2])