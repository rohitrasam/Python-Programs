import pygame as pg
import os

BASE_IMG_PATH = "data/images/"

def load_image(path):

    # always use .convert() for fastest blitting format
    img = pg.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img


def load_images(path):
    images =[]
    for img in os.listdir(BASE_IMG_PATH + path):
        images.append(load_image(path + '/' + img))

    return images
