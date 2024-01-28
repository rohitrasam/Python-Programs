from sys import exit
import math
import pygame as pg




if __name__ == '__main__':

    pg.init()  

    ship_original = pg.image.load("Space shooter/imgs/tiny-spaceships/2X/tiny_ship15.png")

    screen = pg.display.set_mode([800]*2)
    clock = pg.time.Clock()
    run = True
    bas_font = pg.font.Font(None, 30)
    x = y = 400

    while run:
        mx, my = pg.mouse.get_pos()
        fps = clock.tick(60)/1000
        text_render = bas_font.render(f"FPS: {str(round(1/fps))}", True, (0, 127, 250))
        screen.fill("white")
        screen.blit(text_render, (0, 0))
        dx = mx - x
        dy = y - my
        angle = math.atan2(dy, dx) * 180 / math.pi
        ship = pg.transform.rotate(ship_original, angle - 90)
        ship_rect = ship.get_rect(center=(x, y))
        screen.blit(ship, ship_rect) 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            y -= 5
        if keys[pg.K_s]:
            y += 5
        if keys[pg.K_a]:
            x -= 5
        if keys[pg.K_d]:
            x += 5
        
        pg.display.update()
