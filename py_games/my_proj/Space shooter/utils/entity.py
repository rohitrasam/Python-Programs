import math
from .consts import *
from abc import abstractmethod


class Entity:


    def __init__(self) -> None:
        self.gunshot = pg.mixer.Sound(SFX_PATH + "shoot.wav")
        self.explosion = pg.mixer.Sound(SFX_PATH + "explode.wav")

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def shoot(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def health(self):
        pass

    @staticmethod
    def get_angle(pos, dest_pos=None):
        mx, my = pg.mouse.get_pos() if not dest_pos else dest_pos
        dy = pos.y - my
        dx = mx - pos.x
        angle = math.atan2(dy, dx)
        return math.degrees(angle)  # angle * 180 / math.pi -> rads to deg