import pygame as pg
from sys import exit
import math

WIDTH = 1000
HEIGHT = 720

gravity = 0.98
bounce_stop = 1

class Ball:
    
    def __init__(self, pos, radius, color, mass, retention, speed, _id) -> None:
        self.pos = pos
        self.radius = radius
        self.color = color
        # self.mass = mass
        self.retention = retention
        self.speed = speed
        # self.id = _id


    def update(self):
        self.move()
        self.speed[1] = self.check_gravity()
        pg.draw.circle(display, self.color, self.pos, self.radius)

    def check_gravity(self):

        if self.pos[1] < HEIGHT-self.radius:
            self.speed[1] += gravity
        else:
            if self.speed[1] > bounce_stop:
                self.speed[1] = (-1)*self.speed[1]*self.retention # (-1) flips y speed and decreases it by the retention value
            else:
                if abs(self.speed[1]) <= bounce_stop:
                    self.speed[1] = 0
        return self.speed[1]

    def move(self):
        self.pos[1] += self.speed[1]
        

if __name__ == '__main__':


    pg.init()
    display = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    ball1 = Ball([WIDTH/2, 100], 50, (255, 255, 255), 100, 0.9, [0, 0], 1)
    ball2 = Ball([WIDTH/3, 100], 50, (20, 200, 255), 300, 0.6, [0, 0], 2)

    
    pg.display.set_caption("Gravity")

    while True:
        
        display.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

    
        ball1.update()
        ball2.update()
        pg.display.update()
        clock.tick(60)
        
