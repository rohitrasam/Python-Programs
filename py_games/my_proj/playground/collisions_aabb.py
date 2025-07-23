import pygame as pg
from sys import exit

""" AABB Collision """
def collision_test(rect: pg.Rect, tiles: list[pg.Rect]) -> list[pg.Rect]:

    collisions = []
    for tile in tiles:
        if rect.colliderect(tile):
            collisions.append(tile)
    
    return collisions

def move(rect: pg.Rect, movement, tiles: list[pg.Rect]) -> pg.Rect:
    rect.x += movement[0]
    collisions: list[pg.Rect] = collision_test(rect, tiles)
    for tile in collisions:
        if movement[0] > 0:
            rect.right = tile.left
        if movement[0] < 0:
            rect.left = tile.right

    rect.y += movement[1]
    collisions: list[pg.Rect] = collision_test(rect, tiles)
    for tile in collisions:
        if movement[1] > 0:
            rect.bottom = tile.top
        if movement[1] < 0:
            rect.top = tile.bottom
    return rect


if __name__ == '__main__':

    clock = pg.time.Clock()
    display = pg.display.set_mode((500, 500))
    pg.display.set_caption("AABB Collision")

    player = pg.Rect(100, 100, 50, 80)
    tiles = [pg.Rect(200, 350, 50, 50), pg.Rect(260, 300, 50, 50)]

    while True:

        display.fill((0, 0, 0))

        vel = [0, 0]
        pg.draw.rect(display, (255, 255, 255), player)
        
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            vel[1] = -5
        if keys[pg.K_s]:
            vel[1] = 5
        if keys[pg.K_d]:
            vel[0] = 5
        if keys[pg.K_a]:
            vel[0] = -5
            
        player = move(player, vel, tiles)

        for tile in tiles:
            pg.draw.rect(display, (255, 50, 10), tile)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()


        pg.display.update()
        clock.tick(60)