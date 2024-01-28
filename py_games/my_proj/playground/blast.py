import pygame as pg
from sys import exit
from random import  randint, random
import math

WIDTH = 1000
HEIGHT = 720

VEL = 2

class Blast:

    def __init__(self, pos) -> None:

        self.pos = pos
        self.colours = {0: (100, 100, 100), 1: (150, 150, 150), 2:(200, 200, 200)}
        self.curr_color = self.colours[randint(0, 2)]

        self.radius = 1
        self.kill = False
    
    def update(self):
        
        if self.radius >= 60:
            self.kill = True

        if self.kill:
            self.radius -= random()
        else:
            self.radius += randint(1, 4)

        pg.draw.circle(display, self.curr_color, self.pos, self.radius)

                

def render_blast():
    for i, blast in sorted(enumerate(blasts), reverse=True):
        blast.update()
        if blast.radius <= 0:
            blasts.pop(i)
    
blasts = []

if __name__ == '__main__':

    pg.init()
    display = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    start = False
    pg.display.set_caption("Blast")

    while True:
        
        display.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                start = not start
        if start:
            blasts.append(Blast((WIDTH/2+randint(60, 150), HEIGHT/2+randint(60, 150))))
        render_blast()
    
        pg.display.update()
        clock.tick(60)
