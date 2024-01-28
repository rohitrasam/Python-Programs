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
            self.gunshot = pg.mixer.Sound("Space Shooter/sfx/shoot.wav")
            self.explosion = pg.mixer.Sound("Space Shooter/sfx/explode.wav")


class Explosion:

    def __init__(self, pos) -> None:
        self.current_frame = 0
        self.surfs = [pg.transform.rotate(pg.image.load(f"Space Shooter/imgs/Explosion/CircleSplosionV2_100x100px{i}.png"), -180) for i in range(2, 14)]
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


class Smoke:

    def __init__(self, radius, pos) -> None:
        self.pos = list(pos)
        self.vel = [6, randint(0, 60) / 10 - 3]
        self.colours = {
                        # 0:(255, 128, 0), 
                        # 1:(255, 250, 0), 
                        # 2:(150, 150, 150), 
                        # 3:(13, 0, 26)
                        0:(150, 150, 150), 
                        1:(200, 200, 200), 
                        2:(100, 100, 100), 
                        # 3:(13, 0, 26)
                        }
        # self.angle = 2*math.pi*random()
        self.radius = radius
    
    def update(self):

        # angle = 2*math.pi*random()
        self.pos[0] += self.vel[0]
        # self.pos[1] += math.cos(self.angle)*self.radius
        self.pos[1] += self.vel[1]

        self.radius -= 0.1
        if self.radius <= 0:
            smoke_particles.remove(self)
        
        self.draw()

    def draw(self):
        pg.draw.circle(screen, self.colours[randint(0, 2)], self.pos, self.radius)


class Enemy(Player):

    def __init__(self) -> None:
        super().__init__()
        self.surf = pg.image.load("Space Shooter/imgs/tiny-spaceships/2X/tiny_ship9.png")
        self.surf_copy = self.surf
        self.pos = vec(WIDTH-500, HEIGHT * random())
        self.rect = self.surf_copy.get_rect(center=self.pos)
        self.vel = vec(0, VEL if randint(0, 1) == 1 else -VEL)
        self.start = True
        self.max_hp = 10
        self.hp = self.max_hp
        # self.hp = 2

    def update(self):

        dx = player[0].pos.x - self.pos.x
        dy = self.pos.y - player[0].pos.y
        angle = math.atan2(dy, dx) * 180 / math.pi
        self.surf_copy = pg.transform.rotate(self.surf, angle-90)
        self.rect = self.surf_copy.get_rect(center=self.pos)
        
        self.health()
        

        dist = ((self.pos.x - player[0].pos.x)**2 + (self.pos.y - player[0].pos.y)**2)**0.5
        self.vel.x = (player[0].pos.x - self.pos.x) / dist * VEL * 0.5
        self.vel.y = (player[0].pos.y - self.pos.y) / dist * VEL * 0.5
        
        if self.hp <= 0:
            explosions.append(Explosion(self.pos))
            self.explosion.play()
            enemies.remove(self)

        self.pos += self.vel
        self.rect.center = self.pos

    # def update(self):
    #     self.health()
    #     if self.pos.x >= WIDTH - 400:
    #         self.vel.x = -VEL*0.5
    #     else:
    #         self.vel.x = 0
    #         if self.start:
    #             self.vel.y = VEL if randint(0, 1) == 1 else -VEL
    #             self.start = False
        
    #     if self.hp <= 0:
    #         explosions.append(Explosion(self.pos))
    #         self.explosion.play()
    #         enemies.remove(self)

    #     if self.pos.y < 0:
    #         self.vel.y = VEL
    #     if self.pos.y > HEIGHT:
    #         self.vel.y = -VEL

    #     self.pos += self.vel
    #     self.rect.center = self.pos
    
    def health(self):   
        ratio = self.hp / self.max_hp
        if ratio <= 0.3:
            smoke_particles.append(Smoke(randint(4, 7), self.rect.center))

        pg.draw.rect(screen, "red", (self.rect.midright[0]+10, self.rect.midleft[1]-36, 5, self.rect.height))
        pg.draw.rect(screen, "green", (self.rect.midright[0]+10, self.rect.midleft[1]-36, 5, self.rect.height*ratio))

    def shoot_bullet(self):
        self.gunshot.play().set_volume(0.1)
        return Bullet((30, 10), self.rect.midleft, "Enemy")


class Shooter(Player):
    def __init__(self) -> None:
        super().__init__()
        self.surf = pg.image.load("Space Shooter/imgs/tiny-spaceships/2X/tiny_ship15.png")
        self.surf_copy = self.surf
        self.pos = vec(50, HEIGHT/2)
        self.rect = self.surf_copy.get_rect(center=self.pos)
        self.vel = vec(0, 0)
        self.max_hp = 100
        self.hp = self.max_hp
        self.countdown = 0
        # self.hp = 2
    
    def update(self):
        mx, my = pg.mouse.get_pos()

        dx = mx - self.pos.x
        dy = self.pos.y - my
        angle = math.atan2(dy, dx) * 180/math.pi
        self.surf_copy = pg.transform.rotate(self.surf, angle-90)
        self.rect = self.surf_copy.get_rect(center=self.pos)

        
        self.health()
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.vel.y = -VEL
        if keys[pg.K_s]:
            self.vel.y = VEL
        if keys[pg.K_a] and self.rect.midleft[0] - 30 > 0:
            self.vel.x = -VEL
        if keys[pg.K_d]:
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
        mx, my = pg.mouse.get_pos()

        dx = mx - self.pos.x
        dy = self.pos.y - my
        angle = math.atan2(dy, dx) * 180/math.pi
        return Bullet((30, 10), vec(self.rect.center), "Player", angle)
    
    def health(self):   
        ratio = self.hp / self.max_hp
        pg.draw.rect(screen, "red", (80, 10, 300, 30))
        pg.draw.rect(screen, "lightblue", (80, 10, 300*ratio, 30))


class Bullet:

    ammo = []

    def __init__(self, size, pos, bull_type, angle) -> None:
        self.type = bull_type
        self.size = size
        self.pos = pos
        self.angle = angle
        self.dest = vec(pg.mouse.get_pos())
        self.surf = pg.transform.scale(pg.image.load("Space Shooter/imgs/projectile.png"), (20, 10))
        self.surf_copy = self.surf
        # self.surf = pg.Surface(self.size)
        self.vel = vec(0, 0)
        self.rect = self.surf.get_rect(center=self.pos)

    def update(self):
        
        if self.type == "Enemy":
            self.vel.x = -BULLET_VEL
        else:
            dist = ((self.dest.x-self.pos.x)**2 + (self.dest.y-self.pos.y)**2)**0.5
            self.vel.x = (self.dest.x - self.pos.x) * BULLET_VEL / dist
            self.vel.y = (self.dest.y - self.pos.y) * BULLET_VEL / dist

        self.surf_copy = pg.transform.rotate(self.surf, self.angle)

        self.pos += self.vel
        self.rect.center = self.pos

        if self.rect.centerx > WIDTH + 40 or self.rect.centerx < -40:
            Bullet.ammo.remove(self)

        enem_collision_idx = self.rect.collidelist(enemies)
        shooter_coll_idx = self.rect.collidelist(player)
        if enem_collision_idx > -1 and self.type == "Player":
            enemies[enem_collision_idx].hp -= 1
            Bullet.ammo.remove(self)
        
        if shooter_coll_idx > -1 and self.type == "Enemy":
            player[shooter_coll_idx].hp -= 2
            Bullet.ammo.remove(self)
        
        screen.blit(self.surf_copy, self.rect)


""" Render functions """
def render_bullets():
    for bullet in Bullet.ammo:
        bullet.update()
        
def render_enemies():
    for enemy in enemies:
        enemy.update()
        if randint(1, 61) == 30:
            Bullet.ammo.append(enemy.shoot_bullet())
        screen.blit(enemy.surf_copy, enemy.rect)

def render_explosions():
    for explosion in explosions:
        explosion.update()

def render_smoke():
    for smoke in smoke_particles:
        smoke.update()
    

if __name__ == '__main__':

    pg.init()

    player = [Shooter()]
    enemies = []
    smoke_particles = []
    enemies.append(Enemy())
    # enemies.append(Enemy())
    # enemies.append(Enemy())
    bas_font = pg.font.Font(None, 50)
    explosions = []

    clock = pg.time.Clock()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Space Jam")

    """ Refactor the part below """
    bg = pg.transform.scale(pg.image.load("Space Shooter/imgs/space_background_pack/parallax-space-1.png").convert_alpha(), screen.get_size())
    stars = pg.image.load("Space Shooter/imgs/space_background_pack/parallax-space-2.png").convert_alpha()
    ring = pg.image.load("Space Shooter/imgs/space_background_pack/parallax-space-5.png").convert_alpha()
    far = pg.image.load("Space Shooter/imgs/space_background_pack/parallax-space-3.png").convert_alpha()
    big = pg.image.load("Space Shooter/imgs/space_background_pack/parallax-space-4.png").convert_alpha()

    stars_height = stars.get_height()
    stars_width = stars.get_width()
    start = False
    scroll = 0


    """ Main loop """
    while True:

        fps = clock.tick(60)/1000
        screen.blit(bg, (0, 0))
        for i in range(6):
            for j in range(5):
                screen.blit(stars, (i*stars_width+scroll, j*stars_height))
        
        scroll -= 2
        if abs(scroll) > stars_width:
            scroll = 0 
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
                if event.key == pg.K_SPACE:
                    start = not start
        if start:
            if player:
                # pg.draw.rect(screen, "red", player[0].rect)
                screen.blit(player[0].surf_copy, player[0].rect)
                player[0].update()
                text_surf = bas_font.render("HP: ", True, (0, 127, 0))
                screen.blit(text_surf, (10, 10))
            
            if smoke_particles:
                render_smoke()
            render_enemies()
            render_explosions()
            # enemy1.update()
            render_bullets()

        pg.display.update()
