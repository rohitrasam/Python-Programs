import pygame as pg
from typing import TYPE_CHECKING

from scripts.utils import debug
if TYPE_CHECKING:
    from ..main import Game
    from .tileset import TileSet

class Player:
    
    def __init__(self, game: 'Game', pos: list[int], size: list[int]) -> None:
        self.game = game
        self.size = size
        self.pos = pg.Vector2(pos)
        self.offset_pos = self.pos.copy()
        self.size = size
        self.vel = pg.Vector2(0)
        self.speed = 5
        self.air_time = 0 
        self.jumps = 2
        self.flip = False
        self.frame = 0
        self.action = 'idle'
        self.imgs = self.game.assets['player/' + self.action]
        self.dur = 0
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}

    @property
    def rect(self) -> pg.Rect:
        return pg.Rect(self.pos, self.size)

    def handle_input(self) -> None:
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.vel.x = -2
            self.flip = True
        if keys[pg.K_d]:
            self.vel.x = 2
            self.flip = False

    def update(self, tilesets: list['TileSet']) -> None:
        self.collisions = {'up': False, 'down': False, 'left': False, 'right': False}

        self.vel = pg.Vector2(0, self.vel.y)
        self.handle_input()

        if self.pos.x > self.game.screen.get_width() - 2:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = self.game.screen.get_width()

        # collsion detection
        self.pos.x += self.vel.x
        player_rect = self.rect
        for idx, tileset in enumerate(tilesets):
            for tile_rect in tileset.tile_collisions():
                if player_rect.colliderect(tile_rect):
                    if self.vel.x > 0:
                        player_rect.right = tile_rect.left
                    if self.vel.x < 0:
                        player_rect.left = tile_rect.right
                    self.pos.x = player_rect.x

        self.pos.y += self.vel.y
        player_rect = self.rect
        for idx, tileset in enumerate(tilesets):
            for tile_rect in tileset.tile_collisions():
                if player_rect.colliderect(tile_rect):
                    if self.vel.y > 0:
                        player_rect.bottom = tile_rect.top
                        self.collisions['down'] = True
                        self.jumps = 2
                    if self.vel.y < 0:
                        player_rect.top = tile_rect.bottom
                        self.collisions['up'] = True
                    self.pos.y = player_rect.y
        
        self.vel.y = min(self.vel.y + 0.1, 5)

        if self.collisions['up'] or self.collisions['down']:
            self.vel.y = 0  

    def jump(self):
        if self.jumps:
            self.vel.y = -3
            self.jumps -= 1

    def render(self, offset: list=[0, 0]) -> None:
        self.offset_pos = pg.Vector2(self.pos[0] - offset[0], self.pos[1] - offset[1])
        self.animation()
        self.frame = (self.frame + self.dur) % (len(self.imgs))
        # pg.draw.rect(self.game.screen, (0, 255, 255), self.rect)
        debug(self.rect.y, self.game.screen, y=40)
        debug(f"vel: {int(self.vel.y)}", self.game.screen, y=60)
        self.game.screen.blit(pg.transform.flip(self.imgs[int(self.frame)], self.flip, False), self.offset_pos)

    def animation(self):
        self.air_time += 1
        
        if self.collisions['down']:
            self.air_time = 0

        if self.air_time > 4:
            self.set_action('jump')
            self.dur = 0
        elif self.vel.x == 0:
            self.set_action('idle')
            self.dur = 0.1
        else:
            self.set_action('run')
            self.dur = 0.2
        
    def set_action(self, action: str):
        if action != self.action:
            self.action = action
            self.imgs = self.game.assets['player/' + self.action]