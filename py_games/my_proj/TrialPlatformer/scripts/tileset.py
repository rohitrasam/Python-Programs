from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Game
import pygame as pg


class TileSet:
    """
        Platform will contain many tiles.

        `example`: 1,2,2,2,1 is one platform of 1 and 2 type of tiles
    """
    def __init__(self, game: Game, pos: list[int], platform_size: int, tile_size: int=16) -> None:
        self.game = game
        self.tile_size = tile_size
        self.pos = pos
        self.tiles = [{
            'type': 1, 'pos': (self.pos[0]+i, self.pos[1])
            } for i in range(platform_size)]
        self.tiles[0]['type'] = 0
        self.tiles[-1]['type'] = 2
        
    def tile_collisions(self):
        return [pg.Rect(tile['pos'][0]*self.tile_size, tile['pos'][1]*self.tile_size, *(self.tile_size,)*2) for tile in self.tiles]

    def render(self, offset: list[int]=[0, 0]):
        for tile in self.tiles:
            # for rec in self.tile_collisions():
            #     pg.draw.rect(self.game.screen, (255, 0, 0), rec)
            self.game.screen.blit(self.game.assets['tiles'][tile['type']], (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1]*self.tile_size - offset[1]))
