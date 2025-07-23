import pygame as pg
import numpy as np
from random import randint
from sys import exit

SIZE = (480,)*2
FPS = 60
Vec2 = pg.Vector2
acc = 20
grav = 20
vel = 40
fric = -2

class Entity:

    def __init__(self, pos: list[float], size: tuple[float], color: list[float], speed: float, accl: float) -> None:
        self.pos = Vec2(pos)
        self.size = size
        self.color = color
        self.speed = speed
        self.accl = accl
        self.vel = Vec2(self.speed, self.speed)
        self.acc = Vec2(0, grav)
        self.surf = pg.Surface(self.size)
        self.rect = self.surf.get_rect(center=self.pos)
        self.surf.fill(self.color)
        self.zero_grav = False
    
    def update(self, dt: float):

        keys = pg.key.get_just_pressed()
        if keys[pg.K_SPACE]:
            self.zero_grav = not self.zero_grav
            print(self.zero_grav)

        if self.zero_grav:
            self.acc.y = 0
        else:
            self.acc.y = grav

        if self.pos.y > SIZE[1]-2:
            self.vel.y = -self.vel.y
        if self.pos.y-self.size[1] < 0:
            self.vel.y = -self.vel.y

        if self.pos.x + self.size[0]/2 > SIZE[0]-2:
            self.vel.x = -self.vel.x
        if self.pos.x-self.size[0]/2 < 0:
            self.vel.x = -self.vel.x 
        
        self.vel += self.acc * dt
        self.pos += self.vel * dt
        self.rect.midbottom = self.pos

    def render(self, screen: pg.Surface):
        screen.blit(self.surf, self.rect)
        # pg.draw.circle(screen, self.color, self.pos, self.size[0]/2)

# def spawn_area() -> list[int]:
#     return (randint(30, SIZE[0]-30), randint(30, SIZE[1]-30))
spawn_area = lambda: (randint(30, SIZE[0]-30), randint(30, SIZE[1]-30))

# def color() -> int:
#     return randint(0, 255)
color = lambda: randint(0, 255)

if __name__ == '__main__':

    pg.init()
    display = pg.display.set_mode(SIZE)
    clock = pg.time.Clock()
    running = True

    entities: list[Entity] = []
    # entityA = Entity(spawn_area, (30, 30), (255, 0, 0), vel, acc)
    # entityB = Entity(spawn_area, (30, 30), (0, 150, 255), vel+10, acc-20)
    for i in range(1, 20):
        entities.append(Entity(spawn_area(), (5, 5), (color(), color(), color()), vel, acc))


    while running:

        dt = 1/clock.tick(FPS)
        pg.display.set_caption(f"Physics room {round(dt*1000, 2)}")
        display.fill((0, 0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_just_pressed()[0]:
                for _ in range(10):
                    entities.append(Entity(spawn_area(), (5, 5), (color(), color(), color()), vel, acc))

        for entity in entities:
            entity.render(display)
            entity.update(dt)

        pg.display.update()
          
