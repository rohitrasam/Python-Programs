import pygame as pg

BASE = "data/images/"

def load_image(path: str):
    img = pg.image.load(BASE + path)
    return img.convert_alpha()

def debug(info, display: pg.Surface, x=2, y=5):
    font = pg.font.Font("data/fonts/Pixeboy.ttf")
    surf = font.render(f"{info}", False, "White")
    display.blit(surf, (x, y))