import pygame as pg
from sys import exit
from random import random, randint
import math

WIDTH = 1000
HEIGHT = 720

VEL = -4

class Particles:

    """
    Change gravity, vel, radius, x-direction and angle movemnt to see different effects
    """

    def __init__(self, radius, color) -> None:
        self.pos = list(pg.mouse.get_pos())
        self.radius = radius
        self.grav = 0.3
        self.color = color
        self.angle = 2*math.pi*random() # angle remains constant for the rest of the particle's life 
        self.vel = [randint(0, 60)/10 - 3, VEL]
        # self.vel = randint(-6, 3)


    def draw(self):
        # pg.draw.circle(display, (0, 127, 250), self.pos, self.radius, 3)
        pg.draw.circle(display, self.color, self.pos, self.radius)

    def update(self):
        
        angle = math.pi*random() # angle changes every frame
        self.pos[0] += self.vel[0]
        # self.pos[1] += self.vel[1]
        # self.pos[1] += math.cos(self.angle)+self.vel[1]
        # self.pos[0] += math.cos(self.angle)
        # self.pos[1] += self.vel
        self.pos[0] += math.cos(self.angle)*self.radius
        self.pos[1] += math.sin(self.angle)*self.radius
        self.angle += 0.08
        # self.pos[0] += math.cos(self.angle)
        # self.pos[1] += math.sin(self.angle)
        # self.angle += 0.1
        # self.pos[1] -= math.cos(self.angle)*self.radius
        # self.pos[0] += math.cos(self.angle)
        self.vel[1] += self.grav
        self.radius -= 0.1
        if self.radius <= 0:
            particles.remove(self)
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
        
        # display.fill((100, 100, 100))
        display.fill((15, 15, 15))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                start = not start

        if start:
            particles.append(Particles(randint(8, 15), (255, 128, 0)))
            particles.append(Particles(randint(8, 15), (0, 250, 250)))
            particles.append(Particles(randint(8, 15), (255, 250, 0)))
            particles.append(Particles(randint(8, 15), (150, 150, 150)))
            particles.append(Particles(randint(8, 15), (200, 200, 200)))
            particles.append(Particles(randint(8, 15), (100, 100, 100)))
            particles.append(Particles(randint(8, 15), (13, 0, 26)))

        render_particles()

        pg.display.update()
        clock.tick(60)
        
