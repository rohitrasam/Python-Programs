import pygame as pg
from sys import exit
from random import random, randint
import math

WIDTH = 1000
HEIGHT = 720

VEL = 2

class Particles:

    """
    Change gravity, y-vel, radius, x-direction and angle movemnt to see different effects
    """

    def __init__(self, radius) -> None:
        self.pos = list(pg.mouse.get_pos())
        self.radius = radius
        self.grav = 0.3
        self.vel = [randint(0, 20)/10 -1, -7]


    def draw(self):
        pg.draw.circle(display, (0, 127, 250), self.pos, self.radius)

    def update(self):

        self.pos[1] += self.vel[1]

        angle = 3*random()
        self.pos[0] += math.cos(angle)*self.radius 
        # self.pos[0] += self.vel[0]
        self.radius -= 0.1
        if self.radius <= 0:
            particles.remove(self)
        # self.vel[1] += self.grav
        self.draw()


def render_particles():
    for particle in particles:
        particle.update()

if __name__ == '__main__':


    pg.init()
    display = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    start = False

    particles = []   
    
    pg.display.set_caption("Particles")

    while True:
        
        display.fill((20, 20, 20))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                start = not start

        print(len(particles))
        if start:
            particles.append(Particles(randint(4, 8)))

        render_particles()

        pg.display.update()
        clock.tick(60)
        
