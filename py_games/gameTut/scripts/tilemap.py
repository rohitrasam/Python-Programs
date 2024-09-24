import pygame as pg

NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)] # all  permutations of -1, 0, 1 for 2 places = 3 x 3
PHYSICS_TILES = {'grass', 'stone'} # looking for value in set more efficient than in a list

class TileMap:
    
    def __init__(self, game, tile_size: int) -> None:
        
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tile = []

        for i in range(10):
            self.tilemap[str(3+i)+", 10"] = {'type': 'grass', 'variant': 1, 'pos' : (3+i, 10)} # can implement it as a Tile object
            self.tilemap["10, "+str(5+i)] = {'type': 'stone', 'variant': 1, 'pos' : (10, 5+i)} # can implement it as a Tile object

    # this func converts pixel position into a grid position
    def tiles_around(self, pix_pos: list):
        tiles = []
        tile_loc = (int(pix_pos[0] // self.tile_size), int(pix_pos[1] // self.tile_size)) # convert pixel position in to grid position
        for offset in NEIGHBOR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ", " + str(tile_loc[1] + offset[1]) 
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        
        return tiles
        

    def physics_rects_around(self, pos: list):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pg.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        
        return rects

        
    def render(self, surf: pg.Surface):

        for tile in self.offgrid_tile:
            surf.blit(self.game.assests[tile['type']][tile['variant']], tile['pos'])

        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(self.game.assests[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))

            # print("line 26 ", self.game.assests[tile['variant']])
