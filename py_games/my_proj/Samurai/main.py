import pygame as pg
from sys import exit
from scripts.entities import Entity
from scripts.utils import load_image, load_images

class Game:

    WIDTH = 1000
    HEIGHT = 720

    def __init__(self) -> None:
        pg.init()

        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.display = pg.Surface((self.WIDTH // 2, self.HEIGHT // 2))
        self.clock = pg.Clock()
        self.sprites = {
            'player/idle': load_images('player/idle'),
            'player': load_image('player/idle/0.png')
        }
        self.player = Entity(self, 'player', (20, 34), (0, 0))

    def run(self):

        while True:
            

            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    exit()
            
            self.display.fill((10, 20, 50))
            self.player.update()
            self.player.render()

            self.screen.blit(pg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pg.display.update()
            self.clock.tick(60)

if __name__ == '__main__':

    Game().run()