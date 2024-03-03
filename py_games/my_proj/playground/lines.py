import pygame as pg
import math
from sys import exit
from numpy import linspace


WIDTH = 1000
HEIGHT = 720
VEL = 2


if __name__ == '__main__':


    pg.init()
    display = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    start = None
    end = None
    points = None
    flag = True
    lines =[]
    # y = ((y2-y1)*(x-x1)/(x2-x1)) - y1
    # spark = Sparks()
    pg.display.set_caption("Particles")

    while True:
        
        display.fill((20, 20, 20))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

            if flag and event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[0]:
                start = pg.mouse.get_pos()
                end = None
                flag = not flag
            elif not flag and event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[0]:
                end = pg.mouse.get_pos()
                flag = not flag
                lines.append((start, end))
                # dist = math.hypot(start[0]-end[0], start[1] - end[1])
                # points = linspace(start[0], end[0], int(dist*100))   

        # pg.draw.lines(display, (255, 255, 255), lines, 1)
        for line in lines:
            
            pg.draw.circle(display, (0, 255, 255), line[0], 5)
            pg.draw.circle(display, (255, 0, 0), line[1], 5)
            pg.draw.line(display, (255, 255, 255), line[0], line[1], 4)

        if start:
            pg.draw.circle(display, (0, 255, 255), (start[0], start[1]), 5)
            if not flag:
                pg.draw.line(display, (255, 255, 255), start, pg.mouse.get_pos(), 4)
        if end:
            pg.draw.circle(display, (255, 0, 0), (end[0], end[1]), 5)


        #     for x in points:
        #         y = ((end[1]-start[1])*(x-start[0])/(end[0]-start[0])) + start[1]
        #         # y = x**2
        #         pg.draw.circle(display, (255, 255, 255), (x, y), 1)

        pg.display.update()
        clock.tick(60)
