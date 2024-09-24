from random import random
import math
from .consts import *

class Text:

    def __init__(self, font_size: int, pos: list[float], text: str, colour :list[int]=YELLOW, shadow: list[int]=ORANGE, offset=5.0, movement=True) -> None:
        self.pos = vec2(pos)
        self.font = pg.font.Font(FONT_PATH + "Pixeboy.ttf", font_size)
        self.colour = colour
        self.shadow = shadow
        self.surf = self.font.render(text, True, self.colour)
        self.surf_width , self.surf_height = self.surf.get_size()
        self.surf_rect = self.surf.get_rect(center=pos)
        self.mask = pg.mask.from_surface(self.surf)
        self.mask_surf = self.mask.to_surface()
        self.mask_surf.set_colorkey((0, 0, 0))
        self.offset = offset
        self.set_shadow()
        self.movement = movement
        self.angle = random()

    def set_shadow(self):
        for x in range(self.surf_width):
            for y in range(self.surf_height):
                if self.mask_surf.get_at((x, y))[0] != 0:
                    self.mask_surf.set_at((x, y), self.shadow)

    def update(self):
        self.pos.y += 0.4*math.sin(self.angle)
        self.angle += 0.05
        if self.angle > math.tau:
            self.angle = 0
        self.surf_rect.center = self.pos

    def render(self, display: pg.Surface):
        if self.movement:
            self.update()
        # display.blit(self.mask_surf, (self.surf_rect.x + self.offset, self.surf_rect.y + self.offset), special_flags=pg.BLEND_RGBA_ADD)
        # display.blit(self.mask_surf, (self.surf_rect.x + self.offset, self.surf_rect.y + self.offset), special_flags=pg.BLEND_RGB_ADD)
        display.blit(self.mask_surf, (self.surf_rect.x + self.offset, self.surf_rect.y + self.offset))
        display.blit(self.surf, self.surf_rect)