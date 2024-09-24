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
        self.grav = 0.25
        self.color = list(color)
        self.angle = 2*math.pi*random() # angle remains constant for the rest of the particle's life 
        # self.vel = [VEL, VEL]
        self.vel = [randint(0, 60)/10 - 3, VEL]
        # self.vel = randint(-6, 3)
        # self.r = 255
        # self.g = 150
        # self.surf = pg.Surface((self.radius*4,self.radius*4))

    def draw(self):
        # pg.draw.circle(display, (0, 127, 250), self.pos, self.radius, 3)
        self.update()
        pg.draw.circle(display, self.color, self.pos, self.radius)
        rad = self.radius * 2
        # light(rad, (20, 10, 0))
        # pg.draw.circle(self.surf, (250, 100, 20), (self.radius*4,)*2, self.radius*4)
        # self.surf.set_colorkey((0, 0, 0))
        display.blit(light(rad, (30, 20, 0)), (self.pos[0]-self.radius*2, self.pos[1]-self.radius*2), special_flags=pg.BLEND_RGB_ADD)

    def update(self):
        
        angle = math.pi*random() # angle changes every frame
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        # self.pos[1] += math.cos(self.angle)+self.vel[1]
        # self.pos[0] += math.cos(self.angle)
        # self.pos[1] += self.vel[1]
        # self.pos[0] += math.cos(self.angle)*4
        # self.pos[1] += math.sin(self.angle)*4
        # self.angle += 0.08
        # self.pos[0] += math.cos(self.angle)
        # self.pos[1] += math.sin(self.angle)
        # self.angle += 0.1
        # self.pos[1] -= math.cos(self.angle)*self.radius
        # self.pos[0] += math.cos(self.angle)
        self.vel[1] += self.grav
        # self.pos[1] += self.vel[1]
        self.color[0] -= 2.35
        self.color[1] -= 1.38
        if self.color[0] <= 0 or self.color[1] <= 0:
            self.color[0] = 25
            self.color[1] = 15
        # self.color = (self.r, self.g, 0)
        # self.color = (self.r, self.g, 0)
        self.radius -= 0.1
        if self.radius <= 0:
            particles.remove(self)

def light(radius, color):
    surf = pg.Surface((radius*2, radius*2))
    pg.draw.circle(surf, color, (radius, radius), radius)
    # surf.set_colorkey((0, 0, 0))
    return surf

def render_particles():
    for particle in particles:
        particle.draw()

if __name__ == '__main__':


    pg.init()
    display = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    start = False
    font = pg.font.Font("Space shooter/data/fonts/Pixeboy.ttf", 50)

    particles = []   
    
    pg.display.set_caption("Particles")
    while True:
        
        fps = clock.tick(60)
        display.fill((0, 0, 0))
        # display.fill((15, 15, 15))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                start = not start

        if start:
            # particles.append(Particles(randint(8, 15), (255, 128, 0)))
            # particles.append(Particles(randint(8, 15), (200, 100, 0)))
            # particles.append(Particles(randint(8, 15), (150, 75, 0)))
            # particles.append(Particles(randint(8, 15), (100, 50, 0)))
            # particles.append(Particles(randint(8, 15), (0, 250, 250)))
            # particles.append(Particles(randint(8, 15), (255, 250, 0)))
            # particles.append(Particles(randint(8, 15), (150, 150, 150)))
            # particles.append(Particles(randint(8, 15), (200, 200, 200)))
            # particles.append(Particles(randint(8, 15), (100, 100, 100)))
            particles.append(Particles(randint(8, 15), (255, 150, 0)))

        render_particles()
        display.blit(font.render(f"FPS: {int(1000/fps)}", True, (255, 0, 0)), (10, 10))

        pg.display.update()
        
