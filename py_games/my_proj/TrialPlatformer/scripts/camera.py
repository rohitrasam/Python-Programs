from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Game
import pygame as pg
from .player import Player
from .utils import debug

class Camera:

    def __init__(self, game: 'Game') -> None:
        self.offset = pg.Vector2(0)
        self.game = game
        self.half_w, self.half_h = self.game.screen.get_width() // 2, 50
        self.border = 0

    def center_target(self, target: Player):
        # self.offset.x += int((target.rect.centerx - self.half_w - self.offset.x) / 2)
        self.offset.y += int((target.rect.centery - self.half_h - self.offset.y) / 15)  # Dafluffly potato/ CD Codes method
        # self.offset.y = int(target.rect.centery - self.half_h) # Clear code method
        debug(f"border={self.border}, y={self.offset.y}", self.game.screen, y=20)
        self.offset.y = min(self.border, self.offset.y) # CD codes method

    def update(self, target: Player):
        self.center_target(target)

    def update_border(self):
        self.border += int(self.game.player.vel.y)