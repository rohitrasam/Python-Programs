import sys, pygame as pg
from scripts.utils import load_images
from scripts.tilemap import Tilemap

RENDER_SCALE = 2.0

class Editor:

    WIDTH = 1000
    HEIGHT = 720

    def __init__(self) -> None:
        
        pg.init()
        pg.display.set_caption("Editor")

        self.screen = pg.display.set_mode((self.WIDTH,self.HEIGHT)) # main surface
        self.display = pg.Surface((self.WIDTH/2, self.HEIGHT/2))
        self.clock = pg.time.Clock()
        self.assests: dict[str, list[pg.Surface] | pg.Surface] = {
            'decor': load_images("tiles/decor"),
            'grass': load_images("tiles/grass"),
            'large_decor': load_images("tiles/large_decor"),
            'stone': load_images("tiles/stone"),
        }

        self.tile_list = list(self.assests)
        self.tile_group = 0
        self.tile_variant = 0

        self.movement = [False, False, False, False]
        self.tilemap = Tilemap(self, tile_size=16)

        try:
            self.tilemap.load("../map.json")
        except FileNotFoundError:
            pass

        self.scroll = [0, 0]
        self.clicking = False
        self.right_clicking = False
        self.shift = False
        self.ongrid = True

    def run(self):
        while True:
            
            # self.display.fill((10, 150, 255))
            self.display.fill((0, 0, 0))

            self.scroll[0] += (self.movement[1] - self.movement[0])*2
            self.scroll[1] += (self.movement[3] - self.movement[2])*2

            render_scroll = int(self.scroll[0]), int (self.scroll[1])
            self.tilemap.render(self.display, offset=render_scroll)

            curr_tile_img = self.assests[self.tile_list[self.tile_group]][self.tile_variant].copy()
            curr_tile_img.set_alpha(180)

            mpos = pg.mouse.get_pos()
            mx, my = mpos[0] / RENDER_SCALE, mpos[1] / RENDER_SCALE,  
            # gives coords of mouse in terms of tile system
            tile_pos = (int((mx + self.scroll[0]) // self.tilemap.tile_size), int((my + self.scroll[1]) // self.tilemap.tile_size))

            if self.ongrid:
                self.display.blit(curr_tile_img, (tile_pos[0] * self.tilemap.tile_size - self.scroll[0], tile_pos[1] * self.tilemap.tile_size - self.scroll[1]))
            else:
                self.display.blit(curr_tile_img, (mx, my))
                

            if self.clicking and self.ongrid:
                self.tilemap.tilemap[f"{tile_pos[0]}:{tile_pos[1]}"] = {'type': self.tile_list[self.tile_group], 'variant': self.tile_variant, 'pos': tile_pos}
            if self.right_clicking:
                tile_loc = f"{tile_pos[0]}:{tile_pos[1]}"
                if tile_loc in self.tilemap.tilemap:
                    del self.tilemap.tilemap[tile_loc]
                for tile in self.tilemap.offgrid_tiles.copy():
                    tile_img = self.assests[tile['type']][tile['variant']]
                    tile_r = pg.Rect(tile['pos'][0] - self.scroll[0], tile['pos'][1] - self.scroll[1], tile_img.get_width(), tile_img.get_height())
                    if tile_r.collidepoint(mx, my):
                        self.tilemap.offgrid_tiles.remove(tile)

            self.display.blit(curr_tile_img, (5, 5))

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicking = True
                        if not self.ongrid:
                            self.tilemap.offgrid_tiles.append({'type': self.tile_list[self.tile_group], 'variant': self.tile_variant, 'pos': (mx + self.scroll[0], my + self.scroll[1])})
                    if event.button == 3:
                        self.right_clicking = True
                    if self.shift:
                        if event.button == 4:
                            self.tile_variant = (self.tile_variant - 1) % len(self.assests[self.tile_list[self.tile_group]])
                        if event.button == 5:
                            self.tile_variant = (self.tile_variant + 1) % len(self.assests[self.tile_list[self.tile_group]])
                    else:
                        if event.button == 4:
                            self.tile_group = (self.tile_group - 1) % len(self.tile_list)
                            self.tile_variant = 0
                        if event.button == 5:
                            self.tile_group = (self.tile_group + 1) % len(self.tile_list)
                            self.tile_variant = 0
                if event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.clicking = False
                    if event.button == 3:
                        self.right_clicking = False


                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        self.movement[0] = True
                    if event.key == pg.K_d:
                        self.movement[1] = True
                    if event.key == pg.K_w:
                        self.movement[2] = True
                    if event.key == pg.K_s:
                        self.movement[3] = True
                    if event.key == pg.K_g:
                        self.ongrid = not self.ongrid
                    if event.key == pg.K_t:
                        self.tilemap.autotile()
                    if event.key == pg.K_o:
                        self.tilemap.save('../map.json')
                    if event.key == pg.K_LSHIFT:
                        self.shift = True
                if event.type == pg.KEYUP:
                    if event.key == pg.K_a:
                        self.movement[0] = False
                    if event.key == pg.K_d:
                        self.movement[1] = False
                    if event.key == pg.K_w:
                        self.movement[2] = False
                    if event.key == pg.K_s:
                        self.movement[3] = False
                    if event.key == pg.K_LSHIFT:
                        self.shift = False
            
            self.screen.blit(pg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pg.display.update()
            self.clock.tick(60)


if __name__ == '__main__':

    editor = Editor()
    editor.run()