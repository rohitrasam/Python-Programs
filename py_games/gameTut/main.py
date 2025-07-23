import sys, pygame as pg
from scripts.utils import load_image, load_images, Animation
from scripts.entities import PhysicsEntity, Player
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds
class Game:

    WIDTH = 1000
    HEIGHT = 720

    def __init__(self) -> None:
        
        pg.init()
        pg.display.set_caption("Game")

        self.screen = pg.display.set_mode((self.WIDTH,self.HEIGHT)) # main surface
        self.display = pg.Surface((self.WIDTH/2, self.HEIGHT/2))
        self.clock = pg.time.Clock()
        self.assests: dict[str, list[pg.Surface] | pg.Surface | Animation] = {
            'decor': load_images("tiles/decor"),
            'grass': load_images("tiles/grass"),
            'large_decor': load_images("tiles/large_decor"),
            'stone': load_images("tiles/stone"),
            'player': load_image('entities/player.png'),
            'background': pg.transform.scale(load_image('background.png'), self.display.get_size()),
            'clouds': load_images('clouds'),
            'player/idle': Animation(load_images('entities/player/idle'), img_dur=6),
            'player/jump': Animation(load_images('entities/player/jump'), img_dur=6),
            'player/run': Animation(load_images('entities/player/run'), img_dur=4),
            'player/slide': Animation(load_images('entities/player/slide')),
            'player/wall_slide': Animation(load_images('entities/player/wall_slide')),
        }

        self.movement = [False, False]
        self.clouds = Clouds(self.assests['clouds'])
        self.player = Player(self, (50, 50), (8, 15))
        self.tilemap = Tilemap(self, tile_size=16)
        self.scroll = [0, 0]
        self.tilemap.load('map.json')

    def run(self):
        while True:
            
            # self.display.fill((10, 150, 255))
            self.display.blit(self.assests['background'], (0, 0))

            # casting to int() eliminates the jittering issue
            self.scroll[0] += int((self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30)
            self.scroll[1] += int((self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30)


            self.clouds.update()
            self.clouds.render(self.display, self.scroll)
            self.tilemap.render(self.display, offset=self.scroll)
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=self.scroll)


            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        self.movement[0] = True
                    if event.key == pg.K_d:
                        self.movement[1] = True
                    if event.key == pg.K_w:
                        self.player.vel.y = -3
                if event.type == pg.KEYUP:
                    if event.key == pg.K_a:
                        self.movement[0] = False
                    if event.key == pg.K_d:
                        self.movement[1] = False
            
            self.screen.blit(pg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pg.display.update()
            self.clock.tick(60)


if __name__ == '__main__':

    game = Game()
    game.run()