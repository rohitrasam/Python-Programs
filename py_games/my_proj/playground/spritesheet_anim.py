import pygame as pg
from sys import exit

# 54x47
def get_image(sheet, frame, width, height, scale):
    image = pg.Surface((width, height)).convert_alpha()
    image.set_colorkey((0, 0, 0))
    image.blit(sheet, (0, 0), (frame*width, 0, width, height))
    image = pg.transform.scale(image, (width*scale, height*scale))
    return image


image_path = "D:\Python Programs\py_games\FREE_Samurai 2D Pixel Art\FREE_Samurai 2D Pixel Art\Sprites\ATTACK 1\sprite_0.png"

pg.init()

display = pg.display.set_mode((480, 480))
pg.display.set_caption("Spritesheets")

clock = pg.Clock()
sprite_sheet_image = pg.image.load(image_path).convert_alpha()

frame0 = get_image(sprite_sheet_image, 0, 54, 47, 3)

while True:

    display.fill((80, 80, 80))

    # display.blit(sprite_sheet_image, (10, 240))
    for i in range(14):
        frame = get_image(sprite_sheet_image, i, 54, 47, 3)
        display.blit(frame, (180, 180))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    pg.display.update()
    clock.tick(7)