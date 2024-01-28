import pygame as pg
from sys import exit
from random import  randint
import math

WIDTH = 1000
HEIGHT = 720

VEL = 2

class Sparks:

    pass
    """
    Change gravity, y-vel, radius, x-direction and angle movemnt to see different effects
    """
        


if __name__ == '__main__':


    pg.init()
    display = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    start = False
    
    pg.display.set_caption("Particles")

    i = 0
    while True:
        
        display.fill((0, i, i))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                start = not start
        
        i += 1
        if  i >= 255:
           i = 0
        pg.display.update()
        clock.tick(60)
