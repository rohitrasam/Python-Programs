import pygame as pg
from sys import exit
import math

SIZE = 800

class Mouse:

    def __init__(self) -> None:
        self.size = 50
        self.surf = pg.Surface((self.size, )*2)
        self.surf.fill((20, 100, 255))
        self.rect = self.surf.get_rect(center=(SIZE/2,)*2)
        self.mask = pg.mask.from_surface(self.surf)
    
    def update(self, display):
        self.rect.center = pg.mouse.get_pos()
        display.blit(self.surf, self.rect)

class Image:

    def __init__(self) -> None:
        self.surf = pg.image.load("Space shooter\imgs\collectibles\health32x32.png").convert_alpha()
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

            offset = (self.img.rect.left - self.mouse.rect.left, self.img.rect.top - self.mouse.rect.top)
            if self.mouse.mask.overlap(self.img.mask, offset):
                new_mask = self.mouse.mask.overlap_mask(self.img.mask, offset)
                new_surf = new_mask.to_surface()
                new_surf.set_colorkey((0, 0, 0))
                for x in range(new_surf.get_width()):
                    for y in range(new_surf.get_height()):
                        if new_surf.get_at((x, y))[0] != 0:
                            new_surf.set_at((x, y), (255, 150, 150))
                self.screen.blit(new_surf, self.mouse.rect)

            pg.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()