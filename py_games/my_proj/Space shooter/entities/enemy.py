import pygame as pg
from entities.player import Player
from random import randint, random
from scripts.consts import *


vec = pg.math.Vector2

class Enemy(Player):

    def __init__(self, vel, pos, game) -> None:
        super().__init__()
        self.surf = pg.transform.rotate(pg.image.load("Space Shooter/imgs/tiny-spaceships/2X/tiny_ship9.png"), 90)
        self.rect = self.surf.get_rect(center=(pos[0]+50, pos[1] * random()))
        self.pos = vec(self.rect.center)
        self.vel = vec(0, vel if randint(0, 1) == 1 else -vel)
        self.start = True
        self.max_hp = 10
        self.game = game
        # self.hp = self.max_hp
        self.hp = 2

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
        if ratio <= 0.3:
            smoke_particles.append(Smoke(randint(4, 7), self.rect.center))

        pg.draw.rect(screen, "red", (self.rect.midright[0]+10, self.rect.midleft[1]-36, 5, self.rect.height))
        pg.draw.rect(screen, "green", (self.rect.midright[0]+10, self.rect.midleft[1]-36, 5, self.rect.height*ratio))

    def shoot_bullet(self):
        self.gunshot.play().set_volume(0.1)
        return Bullet((30, 10), self.rect.midleft, "Enemy")