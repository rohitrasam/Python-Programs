from sys import exit
import math
import pygame as pg



""" 1st Method using pygame's functions """
# class Player:

#     def __init__(self, pos) -> None:
        
#         self.surf = pg.image.load("Space shooter/data/imgs/tiny-spaceships/2X/tiny_ship15.png")
#         self.surf_copy = self.surf
#         self.pos = pos
#         self.rect = self.surf_copy.get_rect(center=pos)
#         self.display = pg.display.get_surface()
#         self.angle = 0

#     def move(self, vel):
#         dir = pg.Vector2(vel, 0).rotate(-self.angle)
#         self.pos += dir
#         self.rect.center = self.pos

#     def update(self):
#         mx, my = pg.mouse.get_pos()
#         dx = mx - self.pos[0]
#         dy = self.pos[1] - my
#         self.angle = math.atan2(dy, dx) * 180 / math.pi
#         self.surf_copy = pg.transform.rotate(self.surf, self.angle-90)
#         self.rect = self.surf_copy.get_rect(center=self.pos)

#         keys = pg.key.get_pressed()
#         if keys[pg.K_w]:
#             self.move(5)
#         if keys[pg.K_s]:
#             self.move(-5)


""" 2nd Method using cos and sin """
# class Player:

#     def __init__(self, pos) -> None:
        
#         self.surf = pg.image.load("Space shooter/data/imgs/tiny-spaceships/2X/tiny_ship15.png")
#         self.surf_copy = self.surf
#         self.pos = pos
#         self.rect = self.surf_copy.get_rect(center=pos)
#         self.display = pg.display.get_surface()
#         self.angle = 0
#         self.speed = 6
#         self.vel = pg.Vector2()

#     def move(self, speed):
#         self.vel.x = speed * math.cos(math.radians(self.angle))
#         self.vel.y = -speed * math.sin(math.radians(self.angle))
#         self.pos += self.vel
#         self.rect.center = self.pos

#     def update(self):
#         mx, my = pg.mouse.get_pos()
#         dx = mx - self.pos[0]
#         dy = self.pos[1] - my
#         self.angle = math.atan2(dy, dx) * 180 / math.pi
#         self.surf_copy = pg.transform.rotate(self.surf, self.angle - 90)
#         self.rect = self.surf_copy.get_rect(center=self.pos)

#         keys = pg.key.get_pressed()
#         if keys[pg.K_w]:
#             self.move(self.speed)
#         if keys[pg.K_s]:
#             self.move(-self.speed)


""" 3rd Method using distances and direction """
class Player:

    def __init__(self, pos) -> None:
        
        self.surf = pg.image.load("Space shooter/data/imgs/tiny-spaceships/2X/tiny_ship15.png")
        self.surf_copy = self.surf
        self.pos = pos
        self.rect = self.surf_copy.get_rect(center=pos)
        self.display = pg.display.get_surface()
        self.angle = 0
        self.speed = 6
        self.vel = pg.Vector2()
        # self.dist = -1

    def move(self, dx, dy, speed):
        self.vel.x = (dx / self.dist) * speed
        self.vel.y = -(dy / self.dist) * speed

        self.pos += self.vel


    def update(self):
        mx, my = pg.mouse.get_pos()
        dx = mx - self.pos[0]
        dy = self.pos[1] - my
        self.angle = math.atan2(dy, dx) * 180 / math.pi
        self.surf_copy = pg.transform.rotate(self.surf, self.angle - 90)
        self.rect = self.surf_copy.get_rect(center=self.pos)
        self.dist = math.hypot(dx, dy)

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.move(dx, dy, self.speed)
        if keys[pg.K_s]:
            self.move(dx, dy, -self.speed)


    def render(self):
        self.display.blit(self.surf_copy, self.rect)
        

if __name__ == '__main__':

    pg.init()

    screen = pg.display.set_mode([800]*2)
    clock = pg.time.Clock()
    run = True
    bas_font = pg.font.Font(None, 30)
    x = y = 400

    ship = Player((x, y))

    while run:
        
        fps = clock.tick(60)/1000
        text_render = bas_font.render(f"FPS: {str(round(1/fps))}", True, (0, 127, 250))
        screen.fill("white")
        screen.blit(text_render, (0, 0))
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        
        ship.update()
        ship.render()

        
        # if keys[pg.K_a]:
        #     x -= 5
        # if keys[pg.K_d]:
        #     x += 5
        
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