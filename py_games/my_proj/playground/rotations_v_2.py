import pygame as pg
import math
from sys import exit



def coord_axis():
    pg.draw.circle(display, "red", (origin_x, origin_y), 3)
    pg.draw.line(display, "red", (0, origin_y), (SIZE, origin_y), 1)
    pg.draw.line(display, "red", (origin_x, 0), (origin_x, SIZE), 1)

SIZE = 800
origin_x = origin_y  = SIZE / 2 # = 400, 400
phi = 0

if __name__ == '__main__':
    pg.init()

    display = pg.display.set_mode((SIZE,)*2)
    clock = pg.time.Clock()

    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            

        phi += 0.05
        if phi >= 2*math.pi:
            phi = 0

        radius = math.sqrt(20**2+20**2)

        display.fill((10, 10, 10))
        coord_axis()



        pg.display.update()
        fps = clock.tick(60)


        


