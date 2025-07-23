import pygame as pg
from sys import exit




if __name__ == '__main__':
    pg.init()

    display = pg.display.set_mode((400, 400))
    clock = pg.time.Clock()

    light_surf = pg.Surface((200, 200))
    light_surf.set_colorkey((0, 0, 0))
    light_rect = light_surf.get_rect(center=(200, 200))

    while True:

        display.fill((0, 0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                exit()
        
        light_rect.center = pg.mouse.get_pos()

        pg.draw.rect(display, (12, 0, 80), (25, 25, 200, 100))
        pg.draw.rect(display, (80, 0, 12), (175, 275, 200, 100))

        for i in range(5):
            pg.draw.circle(light_surf, (120/(6-i), 120/(6-i), 120/(6-i)), (100, 100), 10*(6-i)+(i*2))

        display.blit(light_surf, light_rect, special_flags=pg.BLEND_RGB_ADD)


        pg.display.update()
        clock.tick(60)
        