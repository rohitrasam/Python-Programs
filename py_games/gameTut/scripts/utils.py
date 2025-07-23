import os
import pygame as pg
# BASE_PATH = "../data/images/"
BASE_PATH = "data/images/"

def load_image(path: str) -> pg.Surface:
    img = pg.image.load(BASE_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path: str) -> list[pg.Surface]:
    images = []
    for img_name in os.listdir(BASE_PATH + path):
        images.append(load_image(os.path.join(path, img_name)))
    return images

class Animation:

    def __init__(self, images: list[pg.Surface], img_dur=5, loop=True) -> None:
        self.images = images
        self.loop = loop
        self.img_dur = img_dur
        self.done = False
        self.frame = 0
    
    def copy(self) -> 'Animation':
        return Animation(self.images, self.img_dur, self.loop)
    
    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_dur * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_dur * len(self.images) - 1)
            if self.frame >= self.img_dur * len(self.images) - 1:
                self.done = True

    def img(self) -> pg.Surface:
        return self.images[int(self.frame / self.img_dur)]