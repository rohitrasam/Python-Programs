from sys import exit
import pygame as pg
import math


k = 0.012
pg.init()
display = pg.display.set_mode((600, 480))

clock = pg.time.Clock()

vel = 0
# force = 0
pos = [300, 400] 
height = pos[1]
target_height = pos[1]-50

k = 0.015
d = 0.04

def water_update(spring_const, damp):

    global vel
    height = pos[1]
    
    loss = -damp * vel
    x = height - target_height

    force = -spring_const * x

    vel += force + loss

    pos[1] += vel

while True:

    display.fill((0,)*3)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit("Thanks!!")


    key = pg.mouse.get_pressed()[0]
    if key:
        pos[1] = pg.mouse.get_pos()[1]

    water_update(k, d)
    pg.draw.circle(display, (255, 255, 100), pos, 5)

    clock.tick(60)
    pg.display.update()



# print(sorted(enumerate([4, 2, 1, 3]), reverse=True))
# print(list(enumerate(sorted([4, 2, 1, 3], reverse=True))))

