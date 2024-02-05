import pygame as pg
from sys import exit
from random import random, randint
from numpy import array
import math

WIDTH = 1000
HEIGHT = 720
VEL = 2

class Sparks:

    """
    Change gravity, y-vel, radius, x-direction and angle movemnt to see different effects
    """
    def __init__(self) -> None:
        # self.pos = array(pg.mouse.get_pos())
        self.scale = 2
        self.pos = array(pg.mouse.get_pos(), dtype=float)
        
        # self.vel = array([random()*2*math.pi, -4])
        self.vel = randint(3, 6)
        self.angle = random() * math.pi*2
        self.center = array([[WIDTH/2, HEIGHT/2]])
        self.alive = True


    def update(self):
        self.pos += array([math.cos(self.angle)*self.vel, math.sin(self.angle)*self.vel])
        # self.angle += 0.1
        self.vel -= 0.1
        if self.vel <= 0:
            self.alive = False
        self.draw()


    def draw(self):
        if self.alive:
            updated_pos = [[self.pos[0] + math.cos(self.angle)*self.scale*self.vel, self.pos[1] + math.sin(self.angle)*self.scale*self.vel],
                           [self.pos[0] + math.cos(self.angle+math.pi*0.5)*self.scale*self.vel*0.3, self.pos[1] + math.sin(self.angle+math.pi*0.5)*self.scale*self.vel*0.3],
                           [self.pos[0] - math.cos(self.angle)*self.scale*self.vel*3.5, self.pos[1] - math.sin(self.angle)*self.scale*self.vel*3.5],
                           [self.pos[0] + math.cos(self.angle-math.pi*0.5)*self.scale*self.vel*0.3, self.pos[1] - math.sin(self.angle+math.pi*0.5)*self.scale*self.vel*0.3],]
            pg.draw.polygon(display, (220, 20, 60), updated_pos)
        



def render_sparks():
    for i, spark in sorted(enumerate(sparks), reverse=True):
        spark.update()
        if not spark.alive:
            sparks.pop(i)

if __name__ == '__main__':


    pg.init()
    display = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    start = False
    sparks = []  
    
    # spark = Sparks()
    pg.display.set_caption("Particles")

    while True:
        
        display.fill((20, 20, 20))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                start = not start

        if start:
            for _ in range(10):
                sparks.append(Sparks())
        
        render_sparks()
    
        # for spark in sparks:
        pg.display.update()
        clock.tick(60)
