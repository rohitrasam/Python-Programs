import pygame as pg
import math
from numpy import array

def coord_axis():
    # pg.draw.circle(display, "red", (origin_x, origin_y), 3)
    pg.draw.line(display, "red", (0, origin_y), (SIZE, origin_y), 1)
    pg.draw.line(display, "red", (origin_x, 0), (origin_x, SIZE), 1)


def ellipse(center, mjr, mnr, phi):

    point = array([[mjr*math.cos(phi)/2, mnr*math.sin(phi)/2, 1]])

    rot = array([[math.cos(phi), mnr*math.sin(phi)/mjr, 0],
                 [-mjr*math.sin(phi)/mnr, math.cos(phi), 0],
                 [0, 0, 1]])

    t = array([[1, 0, 0],
               [0, 1, 0],
               [center[0], center[1], 1]])

    point = point@rot@t

    pg.draw.circle(display, (50, 150, 255), point[0, :2], 1)


SIZE = 800
origin_x = origin_y  = SIZE / 2 # = 400, 400
angle = 0


if __name__ == '__main__':
    pg.init()

    display = pg.display.set_mode((SIZE,)*2)
    clock = pg.time.Clock()

    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        # display.fill((10, 10, 10))
        coord_axis()
        ellipse((origin_x, origin_y), 500, 250, angle)
        angle += 0.01
        fps = clock.tick(60)
        pg.display.update()
