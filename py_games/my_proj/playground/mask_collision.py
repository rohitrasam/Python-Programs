import pygame as pg
from sys import exit
import math

SIZE = 800

class Mouse:

    def __init__(self) -> None:
        self.size = 10
        self.surf = pg.Surface((self.size, )*2)
        self.surf.fill((20, 100, 255))
        self.rect = self.surf.get_rect(center=(SIZE/2,)*2)
        self.mask = pg.mask.from_surface(self.surf)
    
    def update(self, display):
        self.rect.center = pg.mouse.get_pos()
        display.blit(self.surf, self.rect)

class Image:

    def __init__(self) -> None:
        self.surf = pg.image.load("Space shooter/data/imgs/tiny-spaceships/4X/tiny_ship9.png") .convert_alpha()
        self.rect = self.surf.get_rect(center=(SIZE/3,)*2)
        self.mask = pg.mask.from_surface(self.surf)

    def update(self, display):
        display.blit(self.surf, self.rect)

class Game:

    def __init__(self) -> None:
        self.screen = pg.display.set_mode((SIZE,)*2)
        pg.display.set_caption("Mask collision")
        self.clock = pg.time.Clock()
        self.running = True
        self.mouse = Mouse()
        self.img = Image()
        self.main()


    def main(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            self.img.update(self.screen)
            self.mouse.update(self.screen)
            
            offset_x, offset_y = self.img.rect.left - self.mouse.rect.left, self.img.rect.top - self.mouse.rect.top

            """ top-left of other mask should align with th top-left of the 1st mask """
            if self.mouse.mask.overlap(self.img.mask, (offset_x, offset_y)):
                print((offset_x, offset_y), self.mouse.mask.overlap(self.img.mask, (offset_x, offset_y)))
            # if self.mouse.mask.overlap_area(self.img.mask, (offset_x, offset_y)) >= 50:
            #     print((offset_x, offset_y), self.mouse.mask.overlap_area(self.img.mask, (offset_x, offset_y)))

            pg.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()