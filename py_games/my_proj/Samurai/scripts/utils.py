import pygame as pg
import os

BASE_PATH = "data/images/"

def load_image(path: str) -> pg.Surface:
    image = pg.image.load(BASE_PATH + path).convert_alpha()
    image.set_colorkey((0, 0, 0))
    return image

def load_images(path: str):
    images = []
    for image_name in os.listdir(BASE_PATH + path):
        images.append(load_image(os.path.join(path, image_name)))

    return images
