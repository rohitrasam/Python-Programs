import pygame as pg
import math
from sys import exit
from random import random, randint

VEL = 6
BULLET_VEL = 15
HEIGHT = 720
WIDTH = 1000

vec = pg.math.Vector2

"""Implement inheritance later"""
class Player:
        
        def __init__(self) -> None:
            self.gunshot = pg.mixer.Sound("sfx\shoot.wav")
            self.explosion = pg.mixer.Sound("sfx\explode.wav")

class Sparks:

    def __init__(self, pos) -> None:
        self.pos = vec(pos)
        self.angle = 0.25
        self.speed = BULLET_VEL

    def update(self):

        self.pos.x += math.cos(0.25) * self.speed
        self.pos.y += math.sin(0.25) * self.speed
        self.speed = max(0, self.speed - 0.2)


class Explosion:

    def __init__(self, pos) -> None:
        self.current_frame = 0
        self.surfs = [pg.transform.rotate(pg.image.load(f"imgs\Explosion\CircleSplosionV2_100x100px{i}.png"), -180) for i in range(2, 14)]
        self.surf = self.surfs[0]
        self.rect = self.surf.get_rect(center=pos)

    def update(self):
        self.current_frame += 0.3
        if self.current_frame > len(self.surfs):
            self.current_frame = 11
            explosions.remove(self)
        else:
            self.surf = self.surfs[int(self.current_frame)]
            screen.blit(self.surf, self.rect)
    

class Enemy(Player):

    def __init__(self) -> None:
        super().__init__()
        self.surf = pg.transform.rotate(pg.image.load("imgs/tiny-spaceships/2X/tiny_ship9.png"), 90)
        self.rect = self.surf.get_rect(center=(WIDTH +50, HEIGHT * random()))
        self.pos = vec(self.rect.center)
        self.vel = vec(0, VEL if randint(0, 1) == 1 else -VEL)
        self.start = True
        self.max_hp = 10
        self.hp = self.max_hp
        # self.hp = 2

    def update(self):
        self.health()
        if self.pos.x >= WIDTH - 400:
            self.vel.x = -VEL*0.5
        else:
            self.vel.x = 0
            if self.start:
                self.vel.y = VEL if randint(0, 1) == 1 else -VEL
                self.start = False
        
        if self.hp <= 0:
            explosions.append(Explosion(self.pos))
            self.explosion.play()
            enemies.remove(self)

        if self.pos.y < 0:
            self.vel.y = VEL
        if self.pos.y > HEIGHT:
            self.vel.y = -VEL

        self.pos += self.vel
        self.rect.center = self.pos
    
    def health(self):   
        ratio = self.hp / self.max_hp
        pg.draw.rect(screen, "red", (self.rect.midright[0]+10, self.rect.midleft[1]-36, 5, self.rect.height))
        pg.draw.rect(screen, "green", (self.rect.midright[0]+10, self.rect.midleft[1]-36, 5, self.rect.height*ratio))

    def shoot_bullet(self):
        self.gunshot.play().set_volume(0.1)
        return Bullet((30, 10), self.rect.midleft, "Enemy")


class Shooter(Player):
    def __init__(self) -> None:
        super().__init__()
        self.surf = pg.transform.rotate(pg.image.load("imgs/tiny-spaceships/2X/tiny_ship15.png"), -90)
        self.rect = self.surf.get_rect(center=(50, HEIGHT/2))
        self.pos = vec(self.rect.center)
        self.vel = vec(0, 0)
        self.max_hp = 100
        self.hp = self.max_hp
        # self.hp = 2
    
    def update(self):
        self.health()
        keys = pg.key.get_pressed()

        if keys[pg.K_UP]:
            self.vel.y = -VEL
        if keys[pg.K_DOWN]:
            self.vel.y = VEL
        if keys[pg.K_LEFT] and self.rect.midleft[0] - 30 > 0:
            self.vel.x = -VEL
        if keys[pg.K_RIGHT]:
            self.vel.x = VEL

        if self.hp <= 0:
            explosions.append(Explosion(self.pos))
            self.explosion.play()
            player.remove(self)
            
        self.pos += self.vel
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        
        self.rect.center = self.pos
        self.vel = vec(0, 0)

    def shoot_bullet(self):
        self.gunshot.play().set_volume(0.1)
        return Bullet((30, 10), self.rect.midright, "Player")
    
    def health(self):   
        ratio = self.hp / self.max_hp
        pg.draw.rect(screen, "red", (self.rect.midleft[0]-20, self.rect.midleft[1]-35, 10, self.rect.height))
        pg.draw.rect(screen, "green", (self.rect.midleft[0]-20, self.rect.midleft[1]-35, 10, self.rect.height*ratio))


class Bullet:

    ammo = []

    def __init__(self, size, pos, bull_type) -> None:
        self.type = bull_type
        self.size = size
        self.pos = pos

        self.surf = pg.transform.scale(pg.image.load("imgs/projectile.png"), (20, 10))
        # self.surf = pg.Surface(self.size)
        self.vel = vec(0, 0)
        self.rect = self.surf.get_rect(center=self.pos)

    def update(self):
        
        if self.type == "Enemy":
            self.vel.x = -BULLET_VEL
        else:
            self.vel.x = BULLET_VEL

        self.pos += self.vel
        self.rect.center = self.pos

        if self.rect.centerx > WIDTH + 40 or self.rect.centerx < -40:
            Bullet.ammo.remove(self)

        enem_collision_idx = self.rect.collidelist(enemies)
        shooter_coll_idx = self.rect.collidelist(player)
        if enem_collision_idx > -1 and self.type == "Player":
            enemies[enem_collision_idx].hp -= 2
            Bullet.ammo.remove(self)
        
        if shooter_coll_idx > -1 and self.type == "Enemy":
            player[shooter_coll_idx].hp -= 2
            Bullet.ammo.remove(self)
        
        screen.blit(self.surf, self.rect)

""" Render functions"""
def render_bullets():
    for bullet in Bullet.ammo:
        bullet.update()
        
def render_enemies():
    for enemy in enemies:
        enemy.update()
        if randint(1, 61) == 30:
            Bullet.ammo.append(enemy.shoot_bullet())
        screen.blit(enemy.surf, enemy.rect)

def render_explosions():
    for explosion in explosions:
        explosion.update()
    

if __name__ == '__main__':

    pg.init()

    player = [Shooter()]
    enemies = []
    enemies.append(Enemy())
    enemies.append(Enemy())
    enemies.append(Enemy())

    explosions = []

    clock = pg.time.Clock()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Space Jam")

    """ Refactor the part below """
    bg = pg.transform.scale(pg.image.load("imgs\space_background_pack\layers\parallax-space-background.png").convert_alpha(), screen.get_size())
    stars = pg.image.load("imgs\space_background_pack\layers\parallax-space-stars.png").convert_alpha()
    ring = pg.image.load("imgs\space_background_pack\layers\parallax-space-ring-planet.png").convert_alpha()
    far = pg.image.load("imgs\space_background_pack\layers\parallax-space-far-planets.png").convert_alpha()
    big = pg.image.load("imgs\space_background_pack\layers\parallax-space-big-planet.png").convert_alpha()

    stars_height = stars.get_height()
    stars_width = stars.get_width()

    while True:

        # screen.fill((10, 0, 0))
        screen.blit(bg, (0, 0))
        # bg.blit(stars, (0, 0))
        for i in range(10):
            for j in range(5):
                screen.blit(stars, (i*stars_width, j*stars_height))
        
        # scroll -= 5
        # if abs(scroll) > WIDTH:
        #     scroll = 0 
        screen.blit(far, (WIDTH/4, HEIGHT/4))
        screen.blit(ring, (WIDTH/2 + WIDTH/4, HEIGHT/2 + HEIGHT/4))
        screen.blit(big, (WIDTH/4, HEIGHT/2+HEIGHT/4))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_f and player:
                    Bullet.ammo.append(player[0].shoot_bullet())


        # if randint(1, 61) == 30:
        #     Bullet.ammo.append(enemy1.shoot_bullet())
        if player:
            screen.blit(player[0].surf, player[0].rect)
        # screen.blit(enemy1.surf, enemy1.rect)
            player[0].update()
        
        render_enemies()
        render_explosions()
        # enemy1.update()
        render_bullets()

        pg.display.update()
        clock.tick(60)
