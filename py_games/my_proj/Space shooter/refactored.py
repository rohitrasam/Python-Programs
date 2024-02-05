import pygame as pg
import math
from sys import exit
from random import random, randint
import os
from entities.enemy import Enemy
from scripts.consts import *

class Game:


    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption("Space Jam")
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.imgs = {
            "bg": self.load_images("space_background_pack"),
            "player": self.load_image("tiny-spaceships/2X/tiny_ship15.png"),
            "enemy": self.load_image("tiny-spaceships/2X/tiny_ship9.png"),
            "projectile": self.load_image("projectile.png"),
            "explosions": self.load_images("/Explosion")
            }
        # self.player = [Shooter()]
        self.enemies = []
        self.smoke_particles = []
        # self.enemies.append(Enemy())
        self.explosions = []

    def render_bg(self, str_scroll, str_width, str_height):
            self.screen.blit(pg.transform.smoothscale(self.imgs["bg"][0], self.screen.get_size()), (0, 0))
            for i in range(6):
                for j in range(5):
                    self.screen.blit(self.imgs["bg"][1], (i*str_width+str_scroll, j*str_height))

            # self.screen.blit(self.imgs["bg"][2], (WIDTH+10+plt_scroll, HEIGHT/4))
            # self.screen.blit(self.imgs["bg"][3], (WIDTH+60+plt_scroll,  HEIGHT/2))
            # self.screen.blit(self.imgs["bg"][4], (WIDTH+plt_scroll, HEIGHT/2+HEIGHT/4))

    
    def run(self):
        str_scroll = 0

        star_width, star_height = self.imgs["bg"][1].get_size()
        while True:
            self.render_bg(str_scroll, star_width, star_height)

            str_scroll -= 1
            
            if abs(str_scroll) > star_width:
                str_scroll = 0

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
            
            pg.display.update()
            self.clock.tick(60)

    
    def load_image(self, path):

        return pg.image.load(f"{BASE_PATH}{path}").convert_alpha()
    
    def load_images(self, path) -> list[pg.Surface]:
        imgs = []
        for file in os.listdir(BASE_PATH + path):
            imgs.append(self.load_image(f"{path}/{file}"))
        return imgs



if __name__ == '__main__':

    Game().run()