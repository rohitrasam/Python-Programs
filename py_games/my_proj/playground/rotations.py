import pygame as pg
from sys import exit
import math



if __name__ == '__main__':
    pg.init()

    display = pg.display.set_mode((1000, 1000))

    clock = pg.time.Clock()

    x = 50
    y = 50
    speed = 1
    angle = 0
    a = 50
    b = 50
    start = 500
    x_max = 0
    y_max = 0

    pg.display.set_caption("Rotations")

    while True:
        
        # display.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    pass
                if event.key == pg.K_r:
                    x, y = 520, 340
        angle += 0.03
        if angle > 2*math.pi:
            angle = 0   

        # if y > 1000:
        #     y = 20
  
        # start -= 0.5
        """ Rotation around a point other than origin (perfect)"""
        # pg.draw.circle(display, (255, 255, 255), [start+a*math.cos(angle), start+b*math.sin(angle)], 3)
        # pg.draw.circle(display, (255, 0, 255), [start+a*math.cos(angle)+(b+20)*math.sin(angle),  start-a*math.sin(angle)+(b+20)*math.cos(angle)], 3)
        # pg.draw.circle(display, (255, 200, 255), [start+a*math.cos(angle)+b*math.sin(angle),  start-a*math.sin(angle)+b*math.cos(angle)], 3)
        # pg.draw.circle(display, (255, 0, 0), [x+500+x*math.cos(angle)-y*math.sin(angle),  360+x*math.sin(angle)+y*math.cos(angle)], 3)
        # pg.draw.circle(display, (0, 255, 0), [500+x*math.cos(angle)-y*math.sin(angle),  y+360+x*math.sin(angle)+y*math.cos(angle)], 3)
        # pg.draw.circle(display, (0, 0, 255), [500+x*math.cos(angle)-y*math.sin(angle),  360+x*math.sin(angle)+y*math.cos(angle)], 3)
        """ cos func in x direction"""         # [center+ (amount in x)*x*cos(angle), y]
        # pg.draw.circle(display, (255, 255, 255), [start+2.5*x*math.cos(angle), y], 3)
        """ cos func in y direction"""
        # pg.draw.circle(display, (255, 0, 255), [y, 500+x*math.cos(angle)], 3)
        """ sin func in x direction"""
        # pg.draw.circle(display, (255, 255, 0), [500+x*math.sin(3*angle), y], 3)
        """ sin func in y direction"""
        # pg.draw.circle(display, (0, 255, 255), [y, 500+x*math.sin(angle)], 3)
        """ Circular motion(not perfect)""" 
        # y -= math.sin(angle)
        # x += math.cos(angle) 
        # x_max = max(x_max, x)
        # y_max = max(y_max, y) 
        print(x, y, angle)
        # pg.draw.circle(display, (255, 255, 255), [x, y], 3)

        pg.display.update()
        clock.tick(60)
        
