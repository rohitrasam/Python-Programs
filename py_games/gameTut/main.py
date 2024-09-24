import sys, pygame as pg
from  scripts.entities import PhysicsEntity
from scripts.utils import load_image, load_images
from scripts.tilemap import TileMap

class Game:

    WIDTH = 1000
    HEIGHT = 720

    def __init__(self) -> None:
        
        pg.init()

        self.screen = pg.display.set_mode((self.WIDTH,self.HEIGHT)) # main surface
        self.display = pg.Surface((self.WIDTH/2, self.HEIGHT/2)) # 2nd surface to render on
        
        pg.display.set_caption("Game")

        self.clock = pg.time.Clock()
        self.assests = {
            "player": load_image('entities/player.png'),
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
        }

        # self.img = pg.image.load("py_games\gameTut\data\images\clouds\cloud_1.png")
        # self.img.set_colorkey((0, 0, 0))
        # self.img_pos = [self.WIDTH/2, self.HEIGHT/2]
                       # -x,   +x,    -y,    +y
        self.movement = [False, False]
        # self.collision_area = pg.Rect(50, 50, 300, 50)

        self.player = PhysicsEntity(self, 'Player', (self.WIDTH/8, self.HEIGHT/8), (8, 15))
        self.tilemap = TileMap(self, tile_size=16)

        self.run()

    def run(self):
        while True:
            # since we are rendering on the 2nd surface we use display
            self.display.fill((14, 200, 248))
            self.tilemap.render(self.display)
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)
            # print(self.tilemap.tiles_around(self.player.pos))
            # updates the position of the cloud
            # for eg. if self.img_pos = [360, 500]
            # self.movement = [False, False, False, False]
            # if UP key is pressed self.movement =  [True, False, False, False]
            # and self.img_pos[1] will become 500 + (0 - 1)*5 = 495
            # and our img will move upwards.
            # If RIGHT key is pressed self.movement = [False, False, True, False]
            # and self.img_pos[0] will become 320 + (1 - 0) * 5 = 325
            # self.img_pos[0] += (self.movement[3] - self.movement[2]) * 5
            # self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5

            # img_rect = pg.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())

            # if img_rect.colliderect(self.collision_area):
            #     pg.draw.rect(self.screen, (100, 10, 15), self.collision_area)
            # else:
            #     pg.draw.rect(self.screen, (0, 50, 155), self.collision_area)
                # IMP to seperate updates and renders for your objects

            # cloud img rendered, passes above the rect and not below the rect
            # if we paste code on line 41 above the code for `img_rect` then the 
            # our cloud will pass under the rect
            # self.screen.blit(self.img, self.img_pos)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = True
                    if event.key == pg.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pg.K_UP:
                        self.player.velocity[1] = -3
                    #     self.movement[2] = True
                    # if event.key == pg.K_DOWN:
                    #     self.movement[3] = True
                if event.type == pg.KEYUP:
                    if event.key == pg.K_LEFT:
                        self.movement[0] = False
                    if event.key == pg.K_RIGHT:
                        self.movement[1] = False
                    # if event.key == pg.K_UP:
                    #     self.movement[2] = False
                    # if event.key == pg.K_DOWN:
                    #     self.movement[3] = False
            
            self.screen.blit(pg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pg.display.update()
            self.clock.tick(60)


Game()