
import pygame as pg
import math
from sys import exit
from random import random, randint

pg.init()
VEL = 6
BULLET_VEL = 20
WIDTH, HEIGHT = 1280, 720
vec = pg.math.Vector2

"""Implement inheritance later"""
class Player:
        
        def __init__(self) -> None:
            self.gunshot = pg.mixer.Sound("Space Shooter/sfx/shoot.wav")
            self.explosion = pg.mixer.Sound("Space Shooter/sfx/explode.wav")


class Explosion:

    def __init__(self, pos) -> None:
        self.current_frame = 0
        self.surfs = [pg.transform.scale2x(pg.transform.rotate(pg.image.load(f"Space Shooter/imgs/Explosion/CircleSplosionV2_100x100px{i}.png").convert_alpha(), -180)) for i in range(2, 14)]
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
        self.pos = vec(pos)
        self.vel = vec(6, randint(0, 60) / 10 - 3)
        self.colours = {
                        0:(255, 128, 0), 
                        1:(255, 250, 0), 
                        2:(0, 250, 250), 
                        3:(13, 0, 26),
                        4:(150, 150, 150), 
                        5:(200, 200, 200), 
                        6:(100, 100, 100), 
                        }
        
        self.colour = self.colours[randint(0, 6)]
        self.angle = math.tau*random()
        self.radius = radius
    
    def update(self):
        
        """ Old smoke effect """
        # self.pos[1] += self.vel[1]
        # # self.pos[0] += math.cos(self.angle)
        # self.pos[0] += self.vel[0]
        # self.angle += 0.1

        """ Refactored smoke effect """
        self.pos[0] += math.cos(self.angle)
        self.pos[1] += math.sin(self.angle)
        # self.angle -= 0.1

        self.radius -= 0.1
        if self.radius <= 0:
            smoke_particles.remove(self)
        
        self.draw()

    def draw(self):
        pg.draw.circle(screen, self.colour, self.pos, self.radius)


class Enemy(Player):

    def __init__(self) -> None:
        super().__init__()
        self.surf = pg.image.load("Space Shooter/imgs/tiny-spaceships/2X/tiny_ship9.png").convert_alpha()
        self.surf_copy = self.surf
        self.pos = vec(WIDTH+50, HEIGHT * random())
        self.rect = self.surf_copy.get_rect(center=self.pos)
        self.vel = vec(0, 0)
        self.max_hp = 5
        self.drag = randint(4, 8) / 10
        self.hp = self.max_hp
        self.angle = 0
        self.mask = pg.mask.from_surface(self.surf_copy)
        # self.hp = 2

    def update(self):

        self.angle = get_angle(self.pos, player[0].pos)
        self.surf_copy = pg.transform.rotate(self.surf, self.angle-90)
        self.mask = pg.mask.from_surface(self.surf_copy)
        self.rect = self.surf_copy.get_rect(center=self.pos)
        
        self.health()

        dist = ((self.pos.x - player[0].pos.x)**2 + (self.pos.y - player[0].pos.y)**2)**0.5
        self.vel.x = (player[0].pos.x - self.pos.x) 
        self.vel.y = (player[0].pos.y - self.pos.y) 
        
        if self.hp <= 0:
            explosions.append(Explosion(self.pos))
            self.explosion.play()
            enemies.remove(self)

        self.pos += (self.vel / dist * VEL * self.drag)
        self.rect.center = self.pos
    
    def health(self):   
        ratio = self.hp / self.max_hp
        if ratio <= 0.3:
            for _ in range(3):
                smoke_particles.append(Smoke(randint(4, 7), self.rect.center))

    def shoot_bullet(self):
        self.gunshot.play().set_volume(0.1)
        mx, my = player[0].pos
        return Bullet((30, 10), vec(self.rect.center), "Enemy", self.angle, vec(mx, my))


class Shooter(Player):
    def __init__(self) -> None:
        super().__init__()
        self.pos = vec(50, HEIGHT/2)
        self.surf = pg.image.load("Space Shooter/imgs/tiny-spaceships/2X/tiny_ship15.png").convert_alpha()
        self.surf_copy = self.surf
        self.mask = pg.mask.from_surface(self.surf_copy)
        self.rect = self.surf_copy.get_rect(center=self.pos)
        self.vel = vec(0, 0)
        self.max_hp = 100
        self.hp = self.max_hp
        self.angle = 0

    def update(self):
        
        self.angle = get_angle(self.pos)
        self.surf_copy = pg.transform.rotate(self.surf, self.angle-90)
        self.mask = pg.mask.from_surface(self.surf_copy)
        self.rect = self.surf_copy.get_rect(center=self.pos)

        self.health()
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            # self.vel.x = math.cos(math.pi / 180 *self.angle)*VEL
            # self.vel.y = -math.sin(math.pi / 180 *self.angle)*VEL
            self.vel.y = -VEL
        if keys[pg.K_s]:
            self.vel.y = VEL
        if keys[pg.K_a]:
            self.vel.x = -VEL
        if keys[pg.K_d]:
            self.vel.x = VEL

        if self.hp <= 0:
            explosions.append(Explosion(self.pos))
            self.explosion.play()
            player.remove(self)
        
        """ Correcting the diagonal movement by normalizing it """
        if self.vel.x != 0 and self.vel.y != 0:
            self.pos += self.vel.normalize() * VEL  # == self.pos += self.vel / math.hypot(self.vel.x, self.vel.y) * VEL
        else:
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
        return Bullet((30, 10), vec(self.rect.center), "Player", self.angle, vec(mx, my))
    
    def health(self):   
        ratio = self.hp / self.max_hp
        pg.draw.rect(screen, "red", (25, 25, 300, 10))
        pg.draw.rect(screen, "lightgreen", (25, 25, 300*ratio, 10))


class Bullet:

    ammo = []

    def __init__(self, size, pos, bull_type, angle, dest) -> None:
        self.type = bull_type
        self.size = size
        self.pos = pos
        self.angle = angle
        self.dest = dest
        self.surf = pg.transform.scale(pg.image.load("Space Shooter/imgs/projectile.png").convert_alpha(), (20, 10))
        self.surf_copy = self.surf
        self.mask = pg.mask.from_surface(self.surf_copy)
        self.dist = ((self.dest.x-self.pos.x)**2 + (self.dest.y-self.pos.y)**2)**0.5
        self.dir = vec(self.dest.x - self.pos.x, self.dest.y - self.pos.y)
        self.vel = vec(0, 0)
        self.rect = self.surf.get_rect(center=self.pos)
        # self.surf = pg.Surface(self.size)

    def update(self):

        if self.dist > 0:   
            self.vel.x = self.dir.x * BULLET_VEL / self.dist
            self.vel.y = self.dir.y * BULLET_VEL / self.dist
        
        self.surf_copy = pg.transform.rotate(self.surf, self.angle)
        self.mask = pg.mask.from_surface(self.surf_copy)
        self.pos += self.vel
        self.rect.center = self.pos

        if self.rect.centerx > WIDTH + 40 or self.rect.centerx < -40:
            Bullet.ammo.remove(self)

        """ Collision detection"""
        enem_collision_idx = self.rect.collidelist(enemies)
        shooter_coll_idx = self.rect.collidelist(player)
        if enem_collision_idx > -1 and self.type == "Player":
            enemy = enemies[enem_collision_idx]
            offset = enemy.rect.left - self.rect.left, enemy.rect.top - self.rect.top
            """ Pixel perfect collision """
            if self.mask.overlap(enemy.mask, offset):
                enemies[enem_collision_idx].hp -= 1
                Bullet.ammo.remove(self)
        
        if shooter_coll_idx > -1 and self.type == "Enemy":
            offset = player[0].rect.left - self.rect.left, player[0].rect.top - self.rect.top
            """ Pixel perfect collision """
            if self.mask.overlap(player[0].mask, offset):
                player[shooter_coll_idx].hp -= 1
                Bullet.ammo.remove(self)
        
        screen.blit(self.surf_copy, self.rect)


def get_angle(pos, dest_pos=None):
    
    """ Returns the angle of object it is pointing towards in degrees. """

    mx, my = pg.mouse.get_pos() if not dest_pos else dest_pos
    dy = pos.y - my
    dx = mx - pos.x
    angle = math.atan2(dy, dx)
    return angle * 180 / math.pi

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

    # pg.init()

    clock = pg.time.Clock()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Space Jam")



    player = [Shooter()]
    enemies = []
    smoke_particles = []
    enemies.append(Enemy())
    # enemies.append(Enemy())
    # enemies.append(Enemy())
    # enemies.append(Enemy())

    # bas_font = pg.font.Font(None, 30)
    explosions = []


    """ Refactor the part below """
    bg = pg.transform.scale(pg.image.load("Space Shooter/imgs/space_background_pack/parallax-space-1.png").convert_alpha(), screen.get_size())
    stars = pg.image.load("Space Shooter/imgs/space_background_pack/parallax-space-2.png").convert_alpha()
    ring = pg.image.load("Space Shooter/imgs/space_background_pack/parallax-space-5.png").convert_alpha()
    far = pg.image.load("Space Shooter/imgs/space_background_pack/parallax-space-3.png").convert_alpha()
    big = pg.image.load("Space Shooter/imgs/space_background_pack/parallax-space-4.png").convert_alpha()

    stars_width, stars_height = stars.get_size()
    start = False
    scroll = 0

    stars_w_no = math.ceil(WIDTH / stars_width)+1
    stars_h_no = math.ceil(HEIGHT / stars_height)+1

    """ Main loop """
    while True:

        fps = clock.tick(60)/1000
        screen.blit(bg, (0, 0))
        for i in range(stars_w_no):
            for j in range(stars_h_no):
                screen.blit(stars, (i*stars_width+scroll, j*stars_height))
        
        if abs(scroll) > stars_width:
            scroll = 0 
        screen.blit(far, (WIDTH/4, HEIGHT/4))
        screen.blit(ring, (WIDTH/2 + WIDTH/4, HEIGHT/2 + HEIGHT/4))
        screen.blit(big, (WIDTH/4, HEIGHT/2+HEIGHT/4))

        for event in pg.event.get():

            # if event.type == pg.QUIT:  
        
            if start and event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[0] and player:
                Bullet.ammo.append(player[0].shoot_bullet())
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    start = not start
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()
        if start:
            if player:
 
                screen.blit(player[0].surf_copy, player[0].rect)
                player[0].update()
                # text_surf = bas_font.render("HP: ", True, (0, 127, 250))
                # screen.blit(text_surf, (40, 20))
            
            scroll -= 2
            if smoke_particles:
                render_smoke()
            render_enemies()
            render_explosions()
            render_bullets()

        pg.display.update()
