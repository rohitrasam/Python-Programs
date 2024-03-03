import pygame as pg
from sys import exit
from random import  randint
import math

WIDTH = 1000
HEIGHT = 720

if __name__ == '__main__':


    pg.init()
    display = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    start = False
    base_font = pg.font.Font(None, 50)

    temp_text = ""
    
    pg.display.set_caption("Particles")


    while True:
        
        display.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            # if event.type == pg.MOUSEBUTTONDOWN:
            #     start = not start
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    temp_text = temp_text[:-1]
                else:
                    temp_text += event.unicode

        text_surf = base_font.render(temp_text, True, (0, 200, 200))
        
        display.blit(text_surf, (WIDTH/2, HEIGHT/2))
        pg.display.update()
        clock.tick(60)
