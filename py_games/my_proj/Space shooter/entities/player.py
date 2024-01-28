import pygame as pg
from scripts.conts import *

class Player:
        
        def __init__(self, _type) -> None:
            self.gunshot = pg.mixer.Sound("Space Shooter/sfx/shoot.wav")
            self.explosion = pg.mixer.Sound("Space Shooter/sfx/explode.wav")
            self.vel = 6
            self.type = _type

        def update(self):
              pass
              
        def health(self):
              pass
        
        def shoot(self):
              pass