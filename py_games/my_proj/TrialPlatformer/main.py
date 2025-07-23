import pygame as pg
from sys import exit
import random
# from perlin_noise import PerlinNoise
from scripts.player import Player
from scripts.tileset import TileSet
from scripts.utils import load_image, load_images
from scripts.utils import debug
from scripts.camera import Camera

# TODO: Improve camera system -> Done
# TODO: Collision check boundaries -> Done
# TODO: Add sprites -> Done
    # TODO: Animate sprites -> Done
# TODO: Resolve Player speed error(Not able to jump whn speed < 20) -> Done
# TODO: Double jump logic -> Done
# TODO: Platform placement: width and height between each platform -> In Progress
# TODO: Adding platforms
    # TODO: Refactor platorm code (use Perlin noise? or random())
# TODO: Set and update player boundary -> Done

class Game:

    WIDTH, HEIGHT = 480, 640

    def __init__(self) -> None:
        pg.init()
        self.fps = 60
        pg.display.set_caption("Jump'n")
        self.display = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen = pg.Surface((self.WIDTH // 2, self.HEIGHT // 2))
        self.clock = pg.Clock()
        # self.noise = PerlinNoise(10, 500)
        self.assets = {
                'player': load_image('player/idle/0.png'),
                'player/idle': load_images('player/idle'),
                'player/run': load_images('player/run'),
                'player/jump': load_images('player/jump/'),
                'background': load_image('background.png'),
                'tiles': load_images('tiles')
            }
        self.player = Player(self, (self.screen.get_width() // 2, self.screen.get_height() - 20), (9, 28))
        # self.tilesets = [TileSet(self, (3+33*self.noise(i*2/50), i*4), random.randint(3, 4)) for i in range(-4, 5)]    # self.screen.get_width() // tile_size = 14
        self.tilesets = [TileSet(self, (random.randint(0, 11), i*4), random.randint(3, 4)) for i in range(-4, 5)]    # self.screen.get_width() // tile_size = 14
        self.tilesets.insert(0, TileSet(self, (0, 19), 15))
        self.tilesets1 = [(tile.pos[0], tile.pos[1]) for tile in self.tilesets]
        self.camera = Camera(self)


    def run(self):
        while True:

            self.screen.blit(self.assets['background'], (0, 0))

            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    exit()
                if event.type == pg.KEYDOWN and event.key == pg.K_w:
                    self.player.jump()
            
            for idx, tile in enumerate(self.tilesets1):
                pg.draw.rect(self.screen, (255, 0, 0), (tile[0]*16, tile[1]*16-self.camera.offset.y, 16, 16))
                debug(idx, self.screen, tile[0]*16, tile[1]*16-self.camera.offset.y)

            self.camera.update(self.player) 
            self.player.update(self.tilesets)
            self.player.render(self.camera.offset)
            for idx, tileset in enumerate(self.tilesets):
                tileset.render(self.camera.offset)
                debug(tileset.pos[1], self.screen, tileset.pos[0]*16 - self.camera.offset.x, tileset.pos[1]*16 - self.camera.offset.y)
                if tileset.pos[1]*tileset.tile_size - self.camera.offset.y > self.screen.get_height():
                    self.tilesets.pop(idx)

            # update camera border
            if self.player.offset_pos[1] <= self.camera.half_h and self.player.vel.y < 0:
                self.camera.update_border()

            # add platforms
            if len(self.tilesets) < 7:
                self.add_platforms()

            self.display.blit(pg.transform.scale(self.screen, self.display.get_size()), (0, 0))
            pg.display.update()
            self.clock.tick(self.fps)

    def add_platforms(self):
        tileset = TileSet(self, [random.randint(0, 11), self.tilesets[0].pos[1] - 4], random.randint(3, 4))
        self.tilesets.insert(0, tileset)

    
if __name__ == '__main__':
    Game().run()