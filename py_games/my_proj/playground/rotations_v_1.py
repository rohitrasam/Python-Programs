import pygame as pg
from sys import exit
import math
from numpy import array
from numpy.linalg import inv


def rotate_rect(x, y, width, height, phi):

    points = []
    points1 = array([(x, y, 1),
               (x+width, y, 1),
               (x+width, y+height, 1),
               (x, y+height, 1)])

    theta = math.atan2(height/2, width/2)

    radius = math.sqrt((height / 2)**2 + (width / 2)**2)

    thetas = [-theta, theta, -theta+math.pi, theta+math.pi]



    for theta in thetas:
        points.append((x+width/2*math.cos(theta+phi)+height/2*math.sin(theta+phi), y-width/2*math.sin(theta+phi)+height/2*math.cos(theta+phi)))
        # points.append((x+radius*math.cos(theta+phi), y-radius*math.sin(theta+phi)))

    t1 = array([[1, 0, 0],
                [0, 1, 0],
                [-(x+2*width), -(y+2*height), 1]])

    r1 = array([[math.cos(phi), math.sin(phi), 0],
               [-math.sin(phi), math.cos(phi), 0],
               [0, 0, 1]])
    
    t1_inv = inv(t1)

    pg.draw.polygon(display, "red", points)
    points1 = points1@t1@r1@t1_inv
    pg.draw.polygon(display, "green", points1[:, :-1])


if __name__ == '__main__':
    pg.init()

    display = pg.display.set_mode((1000, 1000))

    clock = pg.time.Clock()

    x = 100
    y = 50
    speed = 1
    angle = 0
    a = 100
    b = 50
    start = 500
    x_max = 0
    y_max = 0

    pg.display.set_caption("Rotations")

    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    pass
                if event.key == pg.K_r:
                    x, y = 520, 340
        angle += 0.02
        if angle > 2*math.pi:
            angle = 0   

        if y > 1000:
            y = 0
  
        # start -= 0.5
        """ Rotation around a point other than origin (perfect)"""
        # pg.draw.circle(display, (255, 255, 255), [start+a*math.cos(angle), start+b*math.sin(angle)], 3) # oval path when a != b
        # pg.draw.circle(display, (255, 0, 255), [start+a*math.cos(angle)+(b+20)*math.sin(angle), start-a*math.sin(angle)+(b+20)*math.cos(angle)], 3)
        # pg.draw.circle(display, (255, 200, 255), [start+a*math.cos(angle)+b*math.sin(angle), start-a*math.sin(angle)+b*math.cos(angle)], 3)
        # pg.draw.circle(display, (255, 0, 0), [x+500+x*math.cos(angle)-y*math.sin(angle), 360+x*math.sin(angle)+y*math.cos(angle)], 3)
        # pg.draw.circle(display, (0, 255, 0), [500+x*math.cos(angle)-y*math.sin(angle), y+360+x*math.sin(angle)+y*math.cos(angle)], 3)
        # pg.draw.circle(display, (0, 0, 255), [500+x*math.cos(angle)-y*math.sin(angle), 360+x*math.sin(angle)+y*math.cos(angle)], 3)
        """ cos func in x direction"""         # [center+ (amount in x)*x*cos(angle), y]
        # pg.draw.circle(display, (255, 255, 255), [start+2.5*x*math.cos(angle), y], 3)
        """ cos func in y direction"""
        # pg.draw.circle(display, (255, 0, 255), [y, 500+x*math.cos(angle)], 3)
        """ sin func in x direction"""
        # y += 2
        # pg.draw.circle(display, pg.Color(255, 255, 0, 255), [500+x*math.cos(angle), y], 20)
        """ sin func in y direction"""
        # pg.draw.circle(display, (0, 255, 255), [y, 500+x*math.sin(angle)], 3)
        """ Circular motion(not perfect)""" 
        # y -= math.sin(angle)
        # x += math.cos(angle) 
        # x_max = max(x_max, x)
        # y_max = max(y_max, y) 
        # print(x, y, angle)
        # pg.draw.circle(display, (255, 255, 255), [start + x*math.cos(angle), start + y*math.sin(angle)], 3)


        """ Rotating rect """
        # mx, my = pg.mouse.get_pos()
        display.fill((0, 0, 0))
        rotate_rect(250, 250, 10, 80, angle)

        pg.display.update()
        clock.tick(60)
        