import pygame as pg
from sys import exit


def bouncing_rect():
    global other_speed
    moving_rect.x += moving_speed[0]
    moving_rect.y += moving_speed[1]

    # collision with screen borders
    if moving_rect.right >= width or moving_rect.left <= 0:
        moving_speed[0] *= -1
    if moving_rect.bottom >= height or moving_rect.top <= 0:
        moving_speed[1] *= -1

    other_rect.y += other_speed
    if other_rect.bottom >= height or other_rect.top <= 0:
        other_speed *= -1


    if moving_rect.colliderect(other_rect):
        if abs(other_rect.top - moving_rect.bottom) < 10 and moving_speed[1] > 0:
            moving_speed[1] *= -1
        if abs(other_rect.bottom - moving_rect.top) < 10 and moving_speed[1] < 0:
            moving_speed[1] *= -1
        if abs(other_rect.left - moving_rect.right) < 10 and moving_speed[0] > 0:
            moving_speed[0] *= -1
        if abs(other_rect.right - moving_rect.left) < 10 and moving_speed[0] < 0:
            moving_speed[0] *= -1

    pg.draw.rect(screen, (50, 150, 255), moving_rect)
    pg.draw.rect(screen, (150, 50, 255), other_rect)

if __name__ == '__main__':
    pg.init()

    clock = pg.Clock()
    width, height = 840, 840

    screen = pg.display.set_mode((width, height))

    moving_rect = pg.Rect(300, 350, 100, 100)
    moving_speed = [5, 5]

    other_rect = pg.Rect(300,600, 200, 100)
    other_speed = 2

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        
        screen.fill((30, 30, 30))
        bouncing_rect()
        pg.display.update()
        clock.tick(60)