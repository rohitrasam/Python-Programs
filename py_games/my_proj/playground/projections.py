from numpy import array
from numpy.linalg import inv
import pygame as pg
import math
from sys import exit


def coord_axis():
    # pg.draw.circle(display, "red", (origin_x, origin_y), 3)
    pg.draw.line(display, "red", (0, origin_y), (SIZE, origin_y), 1)
    pg.draw.line(display, "red", (origin_x, 0), (origin_x, SIZE), 1)

def proj(angle):
    points = array([
            [-1, -1, -1, 1],
            [1, -1, -1, 1],
            [1, 1, -1, 1],
            [-1, 1, -1, 1],
            [-1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, -1, 1, 1],
            [-1, -1, 1, 1],
        ]) * scale
        
    Pz = array([[1, 0, 0,  0],
                [0, 1, 0,  0],
                [0, 0, 1, -6],
                [0, 0, 0,  1]])
    
    Rz = array([
                [math.cos(angle), math.sin(angle), 0, 0],
                [-math.sin(angle), math.cos(angle), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])

    Ry = array([
                [math.cos(angle), 0, -math.sin(angle), 0],
                [0, 1, 0, 0],
                [math.sin(angle), 0, math.cos(angle), 0],
                [0, 0, 0, 1]
            ])
                  
    Rx = array([
                [1, 0, 0, 0],
                [0, math.cos(angle), math.sin(angle), 0],
                [0, -math.sin(angle), math.cos(angle), 0],
                [0, 0, 0, 1]
                  ])
                  

    points = points@Rx@Ry@Pz
    for point in points[:, :2]:
        
        pg.draw.circle(display, (255, 255, 255), point+[origin_x, origin_y], 4)
    
    for point in range(4):
        connect_points(points[point], points[(point+1)%4])
        connect_points(points[point+4], points[((point+1)%4)+4])
        connect_points(points[point], points[len(points)-point-1])

    # connect_points(points[0], points[1])
    # connect_points(points[1], points[2])
    # connect_points(points[2], points[3])
    # connect_points(points[3], points[0])

    # connect_points(points[4], points[5])
    # connect_points(points[5], points[6])
    # connect_points(points[6], points[7])
    # connect_points(points[7], points[4])

    # connect_points(points[0], points[7])
    # connect_points(points[1], points[6])
    # connect_points(points[2], points[5])
    # connect_points(points[3], points[4])

        
        
def connect_points(start, end):
    pg.draw.line(display, (255,)*3, start[:2]+[origin_x, origin_y], end[:2]+[origin_x, origin_y], 1)


SIZE = 800
origin_x = origin_y  = SIZE / 2 # = 400, 400
scale = 80
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

        phi += 0.01
        display.fill((10, 10, 10))
        coord_axis()
        proj(phi)
        fps = clock.tick(60)
        pg.display.update()


        


