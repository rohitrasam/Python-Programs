import pygame as pg
from sys import exit
from random import randint
from numpy import array
from numpy.linalg import norm

class Player:
    
    def __init__(self) -> None:
        self.pos = array((240,)*2, dtype=float)
        self.surf = pg.Surface((25, 25))
        self.surf.fill((0, 100, 255))
        self.rect = self.surf.get_rect(center=self.pos)
        self.vel = array([0, 0], dtype=float)

    def move(self):
        self.vel = array([0, 0])

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.vel[1] = -1
        if keys[pg.K_s]:
            self.vel[1] = 1
        if keys[pg.K_a]:
            self.vel[0] = -1
        if keys[pg.K_d]:
            self.vel[0] = 1

        if self.vel.all() != 0:
            self.pos += self.vel / norm(self.vel)*5
        else:
            self.pos += self.vel*5
        
        self.rect.center = self.pos

    def render(self, screen, offset):
        screen.blit(self.surf, self.rect.center - offset)


class Obstacles:

    def __init__(self, pos) -> None:
        self.pos = array(pos)
        self.surf = pg.Surface((50, 50))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=self.pos)
    
    def render(self, screen, offset):
        self.rect.center = offset
        screen.blit(self.surf, self.rect)

class Camera:

    def __init__(self) -> None:
        
        self.offset = array((0, )*2)
        self.half_w, self.half_h = (240,)*2

    def center_target(self, target: Player):
        self.offset[0] = target.pos[0] - self.half_w # - self.offset[0]
        self.offset[1] = target.pos[1] - self.half_h # - self.offset[1]

    def draw(self, obs: list[Obstacles], player: Player, screen):

        self.center_target(player)

        for ob in obs:
            offset_pos = ob.pos - self.offset
            ob.render(screen, offset_pos)


class Game:

    def __init__(self) -> None:
        
        pg.init()
        self.size = (480,)*2
        self.display = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()
        self.player = Player()
        pg.display.set_caption("Camera Movement")
        self.obs = [Obstacles((randint(0, 429),randint(0, 429))) for _ in range(0, 5)]
        self.camera = Camera()

    def main_loop(self):

        while True:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
            
            self.display.fill((0, 0, 0))

            self.camera.draw(self.obs, self.player, self.display)
            self.player.move()
            self.player.render(self.display, self.camera.offset)

            pg.display.update()
            self.clock.tick(60)


if __name__ == '__main__':

    Game().main_loop()