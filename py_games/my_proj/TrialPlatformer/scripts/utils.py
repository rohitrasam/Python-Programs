import pygame as pg
import os

BASE_PATH = "data/images/"

def load_image(path: str):
    image = pg.image.load(BASE_PATH + '/' + path)
    # image.set_colorkey((0, 0, 0))
    return image

def load_images(path: str):
    images = []
    for file in os.listdir(BASE_PATH + '/' + path):
        images.append(load_image(os.path.join(path, file)))
    
    return images

def debug(info, display: pg.Surface, x=2, y=5):
    font = pg.font.Font("data/fonts/Pixeboy.ttf")
    surf = font.render(f"{info}", False, "White")
    display.blit(surf, (x, y))