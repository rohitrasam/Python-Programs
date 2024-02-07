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


# import pygame
# import math

# pygame.init()
# window = pygame.display.set_mode((500, 500))
# clock = pygame.time.Clock()

# class Bullet:
#     def __init__(self, x, y):
#         self.pos = (x, y)
#         mx, my = pygame.mouse.get_pos()
#         self.dir = (mx - x, my - y)
#         length = math.hypot(*self.dir)
        
#         if length == 0.0:
#             self.dir = (0, -1)
#         else:
#             self.dir = (self.dir[0]/length, self.dir[1]/length)
#         angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

#         self.bullet = pygame.Surface((7, 2)).convert_alpha()
#         self.bullet.fill((255, 255, 255))
#         self.bullet = pygame.transform.rotate(self.bullet, angle)
#         self.speed = 2

#     def update(self):  
#         self.pos = (self.pos[0]+self.dir[0]*self.speed, 
#                     self.pos[1]+self.dir[1]*self.speed)

#     def draw(self, surf):
#         bullet_rect = self.bullet.get_rect(center = self.pos)
#         surf.blit(self.bullet, bullet_rect)  

# bullets = []
# pos = (250, 250)
# run = True
# while run:
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             bullets.append(Bullet(*pos))

#     for bullet in bullets[:]:
#         bullet.update()
#         if not window.get_rect().collidepoint(bullet.pos):
#             bullets.remove(bullet)

#     window.fill(0)
#     pygame.draw.circle(window, (0, 255, 0), pos, 10)
#     for bullet in bullets:
#         bullet.draw(window)
#     pygame.display.flip()