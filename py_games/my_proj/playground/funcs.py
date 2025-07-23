import pygame as pg
from sys import exit
import math
from numpy import array
from numpy.linalg import inv



if __name__ == '__main__':
    pg.init()

    display = pg.display.set_mode((1000, 1000))

    clock = pg.time.Clock()
    pg.display.set_caption("Funcs")

    x, y = (0, 500)
    phi = 0

    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        
        pg.draw.circle(display, (255,)*3, (x, y), 1)

        phi += 0.001
        y += math.log(phi)
        x += 1
        # display.fill((0, 0, 0))
        
        pg.display.update()
        clock.tick(60)
        