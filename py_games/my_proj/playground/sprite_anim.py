import pygame as pg
from sys import exit
import os

image_path = "D:/Python Programs/py_games/FREE_Samurai 2D Pixel Art/FREE_Samurai 2D Pixel Art/Sprites/RUN/"

class Player:

    def __init__(self) -> None:
        self.sprites = []
        self.load_images()
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.is_animating = False

    def load_images(self):
        for file in os.listdir(image_path):
            self.sprites.append(pg.image.load(image_path + file))

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.is_animating = False
                self.current_sprite = 0
            self.image = self.sprites[int(self.current_sprite)]
        screen.blit(self.image, (50, 50))

pg.init()

display = pg.display.set_mode((480, 480))
screen = pg.Surface((250, 250))
pg.display.set_caption("Spritesheets")

clock = pg.Clock()

player = Player()

while True:

    # display.fill((80, 80, 80))
    screen.fill((80, 80, 80))
    player.update()
    display.blit(pg.transform.scale(screen, display.get_size()), (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            player.animate()

    pg.display.update()
    clock.tick(60)