from perlin_noise import PerlinNoise
import pygame as pg
from sys import exit

noise = PerlinNoise(10, 500)


if __name__ == '__main__':
    pg.init()

    display = pg.display.set_mode((640, 480))

    clock = pg.time.Clock()
    pg.display.set_caption("Noise")

    x, y = (0, 0)
    counter = {}

    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                print(counter)
                pg.quit()
                exit()
        print(x)
        y = 100*noise(x/25) + 240
        counter[(x, y)] = counter.get((x, y), 0) + 1

        pg.draw.rect(display, (255,)*3, (x*10, y, 10, 10))

        x = (x + 1) % 640
        
        pg.display.update()
        clock.tick(60)
