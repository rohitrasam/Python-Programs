from numpy import array
from numpy.linalg import inv
import pygame as pg
import math
from sys import exit


def coord_axis():
    pg.draw.circle(display, "red", (origin_x, origin_y), 3)
    pg.draw.line(display, "red", (0, origin_y), (SIZE, origin_y), 1)
    pg.draw.line(display, "red", (origin_x, 0), (origin_x, SIZE), 1)

def revs(x, y, width, height, alpha, beta, center, color):
    points = array([[x, y, 1],
                    [x+width, y, 1],
                    [x+width, y+height, 1],
                    [x, y+height, 1]])
    t1 = array([[1, 0, 0],
                [0, 1, 0],
                [-(x+width/2), -(y+height/2), 1]])
    t1_inv = inv(t1)

    rot1 = array([[ math.cos(alpha), math.sin(alpha), 0],
                  [-math.sin(alpha), math.cos(alpha), 0],
                  [               0,               0, 1]])

    t2 = array([[         1,          0, 0],
                [         0,          1, 0],
                [-center[0], -center[1], 1]])
    t2_inv = inv(t2)    
    
    rot2 = array([[ math.cos(beta), math.sin(beta), 0],
                  [-math.sin(beta), math.cos(beta), 0],
                  [              0,              0, 1]])
 
    points = points@t1@rot1@t1_inv@t2@rot2@t2_inv
    pg.draw.polygon(display, color, points[:, :2])




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
        # if phi >= 4*math.pi:
        #     phi = 0

        radius = math.sqrt(20**2+20**2)

        display.fill((10, 10, 10))
        coord_axis()
        revs(600, 700, 10, 50, phi, phi/2, [origin_x, origin_y], (10, 150, 255))
        revs(500, 600, 10, 50, phi, phi/2, [origin_x-50, origin_y], (150, 10, 255))
        revs(401, 700, 10, 50, phi, phi/2, [origin_x+50, origin_y], (150, 255, 10))

        pg.display.update()
        fps = clock.tick(60)


        


