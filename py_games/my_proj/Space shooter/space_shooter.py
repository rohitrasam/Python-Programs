
import pygame as pg
import math
from sys import exit
from random import random, randint

pg.init()
VEL = 6
BULLET_VEL = 20
WIDTH, HEIGHT = 1280, 720
vec2 = pg.math.Vector2

"""Implement inheritance later"""

class Collectibles:

    def __init__(self) -> None:
        pass    

class HealthPack(Collectibles):

    def __init__(self) -> None:
        super().__init__()
        self.pos = vec2(WIDTH + 50, randint(3, 4) / 10*HEIGHT)
        self.surf = pg.image.load("Space shooter\data\imgs\collectibles\health.png")
        self.rect = self.surf.get_rect(center=(self.pos))
        self.vel = vec2(randint(1, 3), randint(4, 8))
        self.angle = 0

    def update(self):
        self.pos.x -= self.vel.x
        # self.pos.y += math.sin(self.angle)
        self.pos.y += self.vel.y*math.sin(self.angle)
        self.rect.center = self.pos
        self.angle += 0.04
        print(self.vel)

        screen.blit(self.surf, self.rect)
        

class Player:
        
        def __init__(self) -> None:
            self.gunshot = pg.mixer.Sound("Space Shooter/data/sfx/shoot.wav")
            self.explosion = pg.mixer.Sound("Space Shooter/data/sfx/explode.wav")


class Explosion:

    def __init__(self, pos) -> None:
        self.current_frame = 0
        self.surfs = [pg.transform.scale2x(pg.transform.rotate(pg.image.load(f"Space Shooter/data/imgs/Explosion/CircleSplosionV2_100x100px{i}.png").convert_alpha(), -180)) for i in range(2, 14)]
        self.surf = self.surfs[0]
        self.rect = self.surf.get_rect(center=pos)

    def update(self):
        self.current_frame += 0.3
        if self.current_frame > len(self.surfs):
            self.current_frame = 11
            # explosions.remove(self)
        else:
            self.surf = self.surfs[int(self.current_frame)]
            screen.blit(self.surf, self.rect)


class Spark:

    minor = 1
    major = 1

    def __init__(self, pos, angle, colour, speed) -> None:
        self.pos = vec2(pos)
        self.angle = angle
        self.colour = colour
        self.speed = speed

    def draw(self):
        points = [
                    [self.pos[0] + self.major*self.speed*math.cos(self.angle), self.pos[1] + self.minor*self.speed*math.sin(self.angle)],
                    [self.pos[0] + self.major*self.speed*math.cos(self.angle+math.pi/2)*0.3, self.pos[1] + self.minor*self.speed*math.sin(self.angle+math.pi/2)*0.3],
                    [self.pos[0] + self.major*self.speed*math.cos(self.angle+math.pi)*3.5, self.pos[1] + self.minor*self.speed*math.sin(self.angle+math.pi)*3.5],
                    [self.pos[0] + self.major*self.speed*math.cos(self.angle+1.5*math.pi)*0.3, self.pos[1] + self.minor*self.speed*math.sin(self.angle+1.5*math.pi)*0.3],
                   ]
        self.speed -= 0.1
        pg.draw.polygon(screen, self.colour, points)

    def update(self):
        movement = [math.cos(self.angle)*self.speed, math.sin(self.angle)*self.speed]
        self.pos[0] += movement[0]
        self.pos[1] += movement[1]

        if self.speed <= 0:
            sparks.remove(self)

        self.draw()


class Smoke:

    def __init__(self, radius, pos) -> None:
        self.pos = vec2(pos)
        # self.vel = vec2(6, randint(0, 60) / 10 - 3)
        # self.colours = {
                        # 0:(255, 150, 0), 
                        # 1:(200, 100, 0), 
                        # 2:(150, 75, 0), 
                        # 3:(100, 50, 0), 
                        # 4:(150, 150, 150), 
                        # 5:(13, 0, 26),
                        # 7:(250, 250, 250), 
                        # }
        
        self.colour = [255, 150, 0] 
        self.angle = math.radians(randint(0, 360))
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
        self.colour[0] -= 2.35*2
        self.colour[1] -= 1.38*2
        if self.colour[0] <= 0 or self.colour[1] <= 0:
            self.colour[0] = 25
            self.colour[1] = 15
        self.radius -= 0.07
        if self.radius <= 0:
            smoke_particles.remove(self)
        
        self.draw()

    def draw(self):
        pg.draw.circle(screen, self.colour, self.pos, self.radius)


class Enemy(Player):

    def __init__(self) -> None:
        super().__init__()
        self.surf = pg.image.load("Space Shooter/data/imgs/tiny-spaceships/2X/tiny_ship9.png").convert_alpha()
        self.surf_copy = self.surf
        self.pos = vec2(WIDTH+randint(25, 50), HEIGHT * random())
        self.rect = self.surf_copy.get_rect(center=self.pos)
        self.vel = vec2(0, 0)
        self.max_hp = 5
        self.drag = randint(3, 5) / 10
        self.hp = self.max_hp
        self.angle = 0
        self.mask = pg.mask.from_surface(self.surf_copy)
        # self.hp = 2

    def update(self):

        self.angle = get_angle(self.pos, players[0].pos)
        self.surf_copy = pg.transform.rotate(self.surf, self.angle-90)
        self.mask = pg.mask.from_surface(self.surf_copy)
        self.rect = self.surf_copy.get_rect(center=self.pos)
        
        self.health()

        dist = ((self.pos.x - players[0].pos.x)**2 + (self.pos.y - players[0].pos.y)**2)**0.5
        self.vel.x = (players[0].pos.x - self.pos.x) 
        self.vel.y = (players[0].pos.y - self.pos.y) 
        
        if self.hp <= 0:
            # explosions.append(Explosion(self.pos))
            self.explosion.play()
            enemies.remove(self)

        """ Normalizing enemies' movement """
        self.pos += (self.vel / dist ) * VEL * (self.drag / 1.2)  # == self.pos += (self.vel.normalize() * VEL * (self.drag / 1.2))
        self.rect.center = self.pos
    
    def health(self):   
        ratio = self.hp / self.max_hp
        if ratio <= 0.3:
            for _ in range(8):
                smoke_particles.append(Smoke(randint(4, 7), self.rect.center))

    def shoot_bullet(self):
        self.gunshot.play().set_volume(0.1)
        mx, my = players[0].pos
        return Bullet((30, 10), vec2(self.rect.center), "Enemy", self.angle, vec2(mx, my))


class Shooter(Player):
    def __init__(self) -> None:
        super().__init__()
        self.pos = vec2(50, HEIGHT/2)
        self.surf = pg.image.load("Space Shooter/data/imgs/tiny-spaceships/2X/tiny_ship15.png").convert_alpha()
        self.surf_copy = self.surf
        self.mask = pg.mask.from_surface(self.surf_copy)
        self.rect = self.surf_copy.get_rect(center=self.pos)
        self.vel = vec2(0, 0)
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
            # move in the direction of the move
            # self.vel.x = math.cos(math.pi / 180 *self.angle)*VEL
            # self.vel.y = -math.sin(math.pi / 180 *self.angle)*VEL 
            self.vel.y = -VEL
        if keys[pg.K_s]:
            self.vel.y = VEL
        if keys[pg.K_a] and self.rect.left >= 0:
            self.vel.x = -VEL
        if keys[pg.K_d]:
            self.vel.x = VEL

        if self.hp <= 0:
            # explosions.append(Explosion(self.pos))
            self.explosion.play()
            players.remove(self)
        
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
        self.vel = vec2(0, 0)

    def shoot_bullet(self):
        self.gunshot.play().set_volume(0.1)
        
        mx, my = pg.mouse.get_pos()
        return Bullet((30, 10), vec2(self.rect.center), "Player", self.angle, vec2(mx, my))
    
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
        self.surf = pg.transform.scale(pg.image.load("Space Shooter/data/imgs/projectile.png").convert_alpha(), (20, 10))
        self.surf_copy = pg.transform.rotate(self.surf, self.angle)
        self.mask = pg.mask.from_surface(self.surf_copy)
        self.dist = ((self.dest.x-self.pos.x)**2 + (self.dest.y-self.pos.y)**2)**0.5
        self.dir = vec2(self.dest.x - self.pos.x, self.dest.y - self.pos.y)
        self.vel = vec2(0, 0)
        self.rect = self.surf.get_rect(center=self.pos)

    def update(self):

        if self.dist > 0:   
            self.vel.x = (self.dir.x / self.dist) * BULLET_VEL
            self.vel.y = (self.dir.y / self.dist) * BULLET_VEL
        
        # self.surf_copy = pg.transform.rotate(self.surf, self.angle)
        # self.mask = pg.mask.from_surface(self.surf_copy)
        self.pos += self.vel
        self.rect.center = self.pos

        if self.rect.centerx > WIDTH + 40 or self.rect.centerx < -40 or self.rect.centery < -40 or self.rect.centery > HEIGHT + 40:
            Bullet.ammo.remove(self)

        """ Collision detection"""
        enem_collision_idx = self.rect.collidelist(enemies)
        shooter_coll_idx = self.rect.collidelist(players)

        if enem_collision_idx > -1 and self.type == "Player":
            enemy = enemies[enem_collision_idx]
            offset = enemy.rect.left - self.rect.left, enemy.rect.top - self.rect.top
            """ Pixel perfect collision """
            if self.mask.overlap(enemy.mask, offset):
                for _ in range(10):
                    sparks.append(Spark(self.rect.midright, random()*math.pi*2, (255,)*3, randint(4, 6)))
                enemy.hp -= 1
                Bullet.ammo.remove(self)
        
        if shooter_coll_idx > -1 and self.type == "Enemy":
            offset = players[0].rect.left - self.rect.left, players[0].rect.top - self.rect.top
            """ Pixel perfect collision """
            if self.mask.overlap(players[0].mask, offset):
                for _ in range(15):
                    sparks.append(Spark(self.rect.midright, random()*math.pi*2, (255,)*3, randint(4, 6)))
                players[shooter_coll_idx].hp -= 1
                Bullet.ammo.remove(self)
        
        screen.blit(self.surf_copy, self.rect)


def get_angle(pos, dest_pos=None):
    
    """ Returns the angle of object it is pointing towards in degrees. """

    mx, my = pg.mouse.get_pos() if not dest_pos else dest_pos
    dy = pos.y - my
    dx = mx - pos.x
    angle = math.atan2(dy, dx)
    return angle * 180 / math.pi

def render_bullets():
    for bullet in Bullet.ammo:
        bullet.update()
        
def render_enemies():
    for enemy in enemies:
        enemy.update()
        if randint(1, 61) == 30:
            Bullet.ammo.append(enemy.shoot_bullet())
        screen.blit(enemy.surf_copy, enemy.rect)

def render_smoke():
    for smoke in smoke_particles:
        smoke.update()

def render_sparks():
    for spark in sparks:
        spark.update()

# def render_explosions():
#     for explosion in explosions:
#         explosion.update()
    

if __name__ == '__main__':

    # pg.init()

    clock = pg.time.Clock()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Space Jam")

    health = HealthPack()
    players = [Shooter()]
    enemies = []
    smoke_particles = []
    sparks = []
    enemies.append(Enemy())
    enemies.append(Enemy())
    enemies.append(Enemy())
    # enemies.append(Enemy())
    # health_p = HealthPack()

    # bas_font = pg.font.Font(None, 30)
    # explosions = []


    """ Refactor the part below """
    bg = pg.transform.scale(pg.image.load("Space Shooter/data/imgs/space_background_pack/parallax-space-1.png").convert_alpha(), screen.get_size())
    stars = pg.image.load("Space Shooter/data/imgs/space_background_pack/parallax-space-2.png").convert_alpha()
    ring = pg.image.load("Space Shooter/data/imgs/space_background_pack/parallax-space-5.png").convert_alpha()
    far = pg.image.load("Space Shooter/data/imgs/space_background_pack/parallax-space-3.png").convert_alpha()
    big = pg.image.load("Space Shooter/data/imgs/space_background_pack/parallax-space-4.png").convert_alpha()

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
        
            if start and event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[0] and players:
                Bullet.ammo.append(players[0].shoot_bullet())
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    start = not start
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    exit()
        if start:
                # text_surf = bas_font.render("HP: ", True, (0, 127, 250))
                # screen.blit(text_surf, (40, 20))
            
            scroll -= 2
            if smoke_particles:
                render_smoke()
            if enemies:
                render_enemies()
            if sparks:
                render_sparks()
            # render_explosions()
            if Bullet.ammo:
                render_bullets()
            if players:
 
                screen.blit(players[0].surf_copy, players[0].rect)
                players[0].update()
            if len(enemies) == 0:
                enemies.append(Enemy())
                enemies.append(Enemy())
                enemies.append(Enemy())
            health.update()


        pg.display.update()
