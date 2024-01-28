import math
from sys import exit
from random import randint
import pygame as pg

size = 800


screen = pg.display.set_mode([size]*2)

player = pg.Rect((randint(0, size-50), randint(0, size-50)), (50, 50))
obj1 = pg.Rect((randint(0, size-50), randint(0, size-50)), (50, 50))
obj2 = pg.Rect((randint(0, size-50), randint(0, size-50)), (50, 50))

clock = pg.time.Clock()

start = False
run = True

def move():
    dist1 = ((player.centerx-obj1.centerx)**2 + (player.centery-obj1.centery)**2)**0.5
    dist2 = ((player.centerx-obj2.centerx)**2 + (player.centery-obj2.centery)**2)**0.5

    if dist1 < dist2 and dist1 != 0:
        player.centerx += (-player.centerx+obj1.centerx)/dist1*5
        player.centery += (-player.centery+obj1.centery)/dist1*5
    elif dist2 != 0:
        player.centerx += (-player.centerx+obj2.centerx)/dist2*5
        player.centery += (-player.centery+obj2.centery)/dist2*5


def draw():

    pg.draw.rect(screen, "green", obj1)
    pg.draw.rect(screen, "blue", obj2)
    pg.draw.rect(screen, "red", player)




while run:

    screen.fill((0, 0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_s:
                start = not start
    draw()
    if start:
        move()

    pg.display.update()
    clock.tick(60)