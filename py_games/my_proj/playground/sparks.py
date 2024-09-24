import pygame as pg
from sys import exit
from random import random, randint
from numpy import array
import math

WIDTH = 1000
HEIGHT = 720
VEL = 2



# def sparks(theta_max, theta_min, num_of_points):

    # del_theta = (theta_max - theta_min) / num_of_points
    # a = 10
    # b = 40

    # x1, y1 = a*math.cos(del_theta), b*math.sin(del_theta)
    # points =[[x1, y1]]
    # for point in range(num_of_points-1):
    #     x, y = points[point][0]*math.cos(del_theta) - (a/b)*points[point][1]*math.sin(del_theta), (b/a)*points[point][0]*math.sin(del_theta) + points[point][1]*math.cos(del_theta)
    #     points.append([x, y])
    # points = (
    #             [a*math.cos(theta+math.pi) - (a/b)*math.sin(theta+math.pi) + WIDTH/2, a*math.sin(theta+math.pi) +(b/a)*math.cos(theta+math.pi) + HEIGHT/2],
    #             [a*math.cos(phi+math.pi) - (a/b)*math.sin(phi+math.pi) + WIDTH/2, a*math.sin(phi+math.pi) + (b/a)*math.sin(phi+math.pi) + HEIGHT/2 - 0.5],
    #             [a*math.cos(theta) - (a/b)*math.sin(theta) + WIDTH/2, a*math.sin(theta) + (b/a)*math.cos(theta) + HEIGHT/2],
    #             [a*math.cos(phi) - (a/b)*math.sin(phi) + WIDTH/2, a*math.sin(phi) + (b/a)*math.cos(phi) + HEIGHT / 2], 
    #           )
    
    # points = (
    #             [x1+WIDTH/2, y1+HEIGHT/2],
    #             [x2+WIDTH/2, y2+(HEIGHT/2)],
    #             [x1*math.cos(math.pi) - y1*(a/b)*math.sin(math.pi)+ WIDTH/2, x1*(b/a)*math.sin(math.pi) + y1*math.cos(math.pi)+HEIGHT/2],
    #             [x2*math.cos(math.pi) - y2*(a/b)*math.sin(math.pi)+WIDTH/2, x2*(b/a)*math.sin(math.pi) + y2*math.cos(math.pi)+HEIGHT/2+25], 
    #           )

    # points = array(points)
    # points += [WIDTH/2, HEIGHT/2]

    
    # pg.draw.polygon(display, (50, 200, 255), points)



class Spark:

    def __init__(self, pos, colour, angle, speed) -> None:
        self.pos = pos
        self.colour = colour
        self.scale = 2
        self.minor = 1
        self.major = 1
        self.angle = angle
        self.speed = speed

    def draw(self):
        # x1, y1 = self.pos[0] + self.minor*math.cos(self.angle)*self.scale, self.pos[1] + self.major*math.sin(self.angle)*self.scale
        # x4, y4 = self.pos[0] + self.minor*math.cos(self.angle + math.pi/2)*self.scale, self.pos[1] + self.major*math.sin(self.angle + math.pi/2)*self.scale
        # x3, y3 = self.pos[0] - self.minor*math.cos(self.angle)*self.scale, self.pos[1] - self.major*math.sin(self.angle)*self.scale
        # x2, y2 = self.pos[0] + self.minor*math.cos(self.angle - math.pi/2)*self.scale, self.pos[1] - self.major*math.sin(self.angle + math.pi/2)*self.scale
        # points = [
        #         [x1, y1], 
        #         [x4, y4],
        #         [x3, y3], 
        #         [x2, y2], 
        #     ]
        points = [
                    [self.pos[0]+self.minor*math.cos(self.angle)*self.scale*self.speed, self.pos[1]+self.major*math.sin(self.angle)*self.scale*self.speed],
                    [self.pos[0]+self.minor*math.cos(self.angle+math.pi/2)*0.3*self.scale*self.speed, self.pos[1]+self.major*0.3*math.sin(self.angle+math.pi/2)*self.scale*self.speed],
                    [self.pos[0]+self.minor*3.5*math.cos(self.angle+math.pi)*self.scale*self.speed, self.pos[1]+self.major*3.5*math.sin(self.angle+math.pi)*self.scale*self.speed],
                    [self.pos[0]+self.minor*0.3*math.cos(self.angle+1.5*math.pi)*self.scale*self.speed, self.pos[1]+self.major*0.3*math.sin(self.angle+1.5*math.pi)*self.scale*self.speed],
                  ]
        # self.angle += 0.08
        self.speed -= 0.1
        # self.scale -= 0.09

        pg.draw.polygon(display, self.colour, points)

    def move(self):

        movement = [math.cos(self.angle) * self.speed, math.sin(self.angle) * self.speed]
        self.pos[0] += movement[0]
        self.pos[1] += movement[1]


if __name__ == '__main__':


    pg.init()
    display = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    sparks = []
    pg.display.set_caption("Particles")
    # spark = Spark([WIDTH/2, HEIGHT/2], (255, 150, 0), math.pi/2,5)

    while True:
        
        display.fill((20, 20, 20))
        m_pos = list(pg.mouse.get_pos())
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            # if event.type == pg.MOUSEBUTTONDOWN:
                # start = not start
                # sparks.append((Spark(m_pos, (255, 150, 0), randint(0, 360)*math.pi/180, randint(4, 6))))  # orange
        sparks.append((Spark(m_pos, (255,75, 30), randint(0, 360)*math.pi/180, randint(4, 6))))
        # for i in range(5):

        for spark in sparks:
            spark.move()
            spark.draw()
            if spark.speed <= 0:
                sparks.remove(spark)

        pg.display.update()
        clock.tick(60)
