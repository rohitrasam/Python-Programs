from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Game
    from scripts.tilemap import Tilemap
from scripts.tilemap import Tilemap
import pygame as pg
class PhysicsEntity:

    def __init__(self, game: Game, entity_type: str, pos: list[float], size: list[int]):
        self.game = game
        self.type = entity_type
        self.pos = pg.Vector2(pos)
        self.size = size
        self.vel = pg.Vector2(0)
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        self.action = ''
        self.anim_offset = (-3, -3)
        self.flip = False
        self.set_action('idle')

    def rect(self) -> pg.Rect:
        return pg.Rect(self.pos, self.size)

    def set_action(self, action: str):
        if action != self.action:
            self.action = action
            self.animation = self.game.assests[self.type + '/' + self.action].copy()

    def update(self, tilemap: Tilemap, movement=[0, 0]):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        frame_movement = (movement[0] + self.vel.x, movement[1] + self.vel.y)
        
        self.pos.x += frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos.x = entity_rect.x

        self.pos.y += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos.y = entity_rect.y

        if movement[0] > 0:
            self.flip = False
        elif movement[0] < 0:
            self.flip = True

        self.vel.y = min(self.vel.y + 0.1, 5)

        if self.collisions['down'] or self.collisions['up']:
            self.vel.y = 0

        self.animation.update()

    def render(self, surf: pg.Surface, offset=(0, 0)):
        surf.blit(pg.transform.flip(self.animation.img(), self.flip, False), (self.pos.x - offset[0] + self.anim_offset[0], self.pos.y - offset[1] + self.anim_offset[1]))
        # surf.blit(self.game.assests['player'], (self.pos.x - offset[0], self.pos.y - offset[1] ))


class Player(PhysicsEntity):
    
    def __init__(self, game: Game, pos: list[float], size: list[int]):
        super().__init__(game, 'player', pos, size)
        self.air_time = 0

    def update(self, tilemap: Tilemap, movement=[0, 0]):
        super().update(tilemap, movement)

        self.air_time += 1
        if self.collisions['down']:
            self.air_time = 0

        if self.air_time > 4:
            self.set_action('jump')
        elif movement[0] != 0:
            self.set_action('run')
        else:
            self.set_action('idle')