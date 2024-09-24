import pygame as pg
from sys import exit
import math

SIZE = 800

class Image:

    def __init__(self) -> None:
        self.surf = pg.image.load("Space shooter/data/imgs/tiny-spaceships/4X/tiny_ship9.png") .convert_alpha()
        self.rect = self.surf.get_rect(center=(SIZE/3,)*2)
        self.mask = pg.mask.from_surface(self.surf)

        """ mask -> surface """
        self.new_surf = self.mask.to_surface()
        self.new_surf.set_colorkey((0, 0, 0))   # removing the black bg color

        """ filling in the surface with a color """
        self.surf_w, self.surf_h = self.new_surf.get_size()
        for x in range(self.surf_w):
            for y in range(self.surf_h):
                if self.new_surf.get_at((x, y))[0] != 0:    # checks if the pixel colour is white or not
                    self.new_surf.set_at((x, y), (15, 0, 0))   # sets the pixel colour to red


    def update(self, display):

        """ Outline """
        for point in self.mask.outline():
            x = self.rect.left + point[0]
            y = self.rect.top + point[1]
        #     # pg.draw.rect(display, "black", (x-2, y-2, 1, 1))    # gives a central shadow effect
        #     # pg.draw.rect(display, "black", (x-2, y-2, 2, 2))    # gives a left shadow effect
        #     # pg.draw.rect(display, "black", (x, y, 4, 4))    # gives a right shadow effect
            pg.draw.circle(display, "red", (x, y), 2)  # outline effect
        # display.blit(self.new_surf, self.rect)
        # display.blit(self.surf, self.rect)
    

class Game:

    def __init__(self) -> None:
        self.screen = pg.display.set_mode((SIZE,)*2)
        pg.display.set_caption("Mask collision")
        self.clock = pg.time.Clock()
        self.img = Image()
        self.main()


    def main(self):
        while True:
            self.screen.fill((100, 100, 100))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

            self.img.update(self.screen)
        
            pg.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()