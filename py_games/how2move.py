# import pygame as pg


# pg.init()

# screen = pg.display.set_mode((600, 400))

# img = pg.image.load("py_games\Free 3 Cyberpunk Sprites Pixel Art\\1 Biker\Biker_hurt.png").convert_alpha()
# rect_1 = pg.Rect(200, 100, 150, 100)
# # rect_1.width = 400
# # rect_1.height = 150
# rect_2 = img.get_rect(topright=(200, 200))

# clock = pg.time.Clock()
# run = True
# while run:

#     screen.fill((255, 255, 255))
#     pg.draw.rect(screen, (255, 0, 255), rect_1)
#     pg.draw.rect(screen, (0, 150, 255), rect_2)
#     screen.blit(img, rect_2)

#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             run = False

#     pg.display.flip()
#     pg.display.update()

#     clock.tick(60)
from random import randint


if randint(0, 1):
     print(1)
else:
     print(0)