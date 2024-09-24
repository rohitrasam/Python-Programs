from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..main import Game
import math
from random import randint, random
from .consts import *


class Smoke:

    def __init__(self, game: 'Game', radius: float, pos: list[float]) -> None:
        self.game = game
        self.radius = radius
        self.pos = vec2(pos)
        self.color = list(FIRE)
        self.angle = randint(0, 360) * math.pi / 180

    def update(self):
        self.pos.x += math.cos(self.angle)
        self.pos.y += math.sin(self.angle)

        self.color[0] -= 2.35*2
        self.color[1] -= 1.38*2
        if self.color[0] <= 0 or self.color[1] <= 0:
            self.color[0] = 2
            self.color[1] = 1
        self.radius -= 0.07

    def render(self):
        pg.draw.circle(self.game.display, self.color, self.pos, self.radius)
        self.update()


class Spark:

    def __init__(self, game: 'Game', color: list, angle: float, pos: list[float], speed: float) -> None:
        self.game = game
        self.color =color
        self.angle = angle
        self.pos = vec2(pos)
        self.speed = speed
        self.scale = 1

    def update(self):
        self.pos[0] += self.speed * math.cos(self.angle)
        self.pos[1] += self.speed * math.sin(self.angle)
        self.speed -= 0.3


    def render(self):
        points = [[self.pos[0] + math.cos(self.angle)*self.scale*self.speed, self.pos[1] + math.sin(self.angle)*self.scale*self.speed],
                  [self.pos[0] + math.cos(self.angle+math.pi/2)*self.scale*self.speed*0.3, self.pos[1] + math.sin(self.angle+math.pi/2)*self.scale*self.speed*0.3],
                  [self.pos[0] + math.cos(self.angle+math.pi)*self.scale*self.speed*3.5, self.pos[1] + math.sin(self.angle+math.pi)*self.scale*self.speed*3.5],
                  [self.pos[0] + math.cos(self.angle+1.5*math.pi)*self.scale*self.speed*0.3, self.pos[1] + math.sin(self.angle+1.5*math.pi)*self.scale*self.speed*0.3],]
        pg.draw.polygon(self.game.display, self.color, points)
        self.update()


class Explosion:
    pass