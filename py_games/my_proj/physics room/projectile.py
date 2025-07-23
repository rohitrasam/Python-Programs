from random import randint
import pygame as pg
from sys import exit
import math

SIZE = (1080, 720)
FPS = 60
Vec2 = pg.Vector2
ACC = 0.5
GRAV = 50
SPEED = 250
FRIC = -0.11

class Entity:

    def __init__(self, pos: list[float], size: list[float], colour: list[int], speed: float, accl: float, theta=0.0) -> None:
        self.pos = Vec2(pos)
        self.size = size
        self.surf = pg.Surface(self.size)
        self.colour = colour
        self.surf.fill(self.colour)
        self.rect = self.surf.get_rect(midbottom=self.pos)
        self._speed = speed
        self.accl = accl
        self._theta = theta
        self.vel = Vec2(0, 0)
        self.acc = Vec2(0, GRAV)
        self.rest = False

    @property
    def speed(self):
        return self._speed

    @property
    def theta(self):
        return self._theta
    
    @speed.setter
    def speed(self, speed: float):
        self._speed = speed

    @theta.setter
    def theta(self, theta: float):
        self._theta = theta
        self.vel.y = -self.speed*math.sin(self._theta)

    def update(self, dt: float):        
        if self.pos.x > SIZE[0]:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = SIZE[0]

        # setting the x component of velocity
        self.vel.x = self.speed*math.cos(self.theta)

        # checking if the entity hits the ground and if it's in resting state or not
        if self.pos.y > SIZE[1] and not self.rest:
            # decreasing the speed of the entity by 30% each time it hits the ground
            self.speed -= self.speed * 0.3
            self.vel.y = -self.speed * math.sin(self.theta)

        # adding acceleration to velocity for each frame
        self.vel += self.acc * dt

        # checking if the speed is < 0.5 to eliminate the infinite bouce effect
        if self.speed < 0.5:
            # if speed < 0.5, setting the vel to 0 and set rest to True
            self.rest = True
            self.vel.y = 0
            self.speed = 0
        else:
            self.rest = False

        # updating the current position of the entity
        self.pos += self.vel * dt
        self.rect.midbottom = self.pos

    def draw(self, screen: pg.Surface):
        screen.blit(self.surf, self.rect)


def color() -> int:
    return randint(0, 255)

def range(entity: Entity) -> float:
    return entity.speed**2 * math.sin(2*entity.theta) / GRAV

def max_height(entity: Entity) -> float:
    return entity.vel.y**2 / (2*GRAV)


if __name__ == '__main__':

    pg.init()
    display = pg.display.set_mode(SIZE)
    pg.display.set_caption("Projectile")
    clock = pg.time.Clock()
    running = True
    entity1 = Entity([50, SIZE[1]-1], [20, 20], (150, 0, 255), SPEED, ACC)
    # entity2 = Entity([50, SIZE[1]-1], [20, 20], (0, 255, 150), vel, acc, math.pi/4)
    # entity3 = Entity([50, SIZE[1]-1], [20, 20], (0, 150, 255), vel, acc, math.pi/6)

    base_font = pg.font.Font(None, 30)
    start = False

    while running:

        mx, my = pg.mouse.get_pos()
        angle = math.atan2(-(my-entity1.pos.y), mx-entity1.pos.x)
        display.fill((0, 0, 0))
        dt = 1 / clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                running = False
                pg.quit()
                exit("Exited without issues")
            if event.type == pg.KEYDOWN and event.key == pg.K_w:
                SPEED += 1
            if event.type == pg.KEYDOWN and event.key == pg.K_s:
                SPEED -= 1
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                start = not start
                entity1.theta = angle
                entity1.speed = SPEED


        if start:
            entity1.update(dt)
            # entity2.update(dt)
            # entity3.update(dt)
            text_surf = base_font.render(f"Launch angle: {round(entity1.theta * 180 / math.pi)} degs\nSpeed: {round(entity1.speed)} units", True, (255, 255, 255))
        else:
            text_surf = base_font.render(f"Launch angle: {round(angle *180 / math.pi)} degs\nSpeed: {SPEED} units", True, (255, 255, 255))

        
        display.blit(text_surf, (0, 0))
        entity1.draw(display)
        # entity2.draw(display)
        # entity3.draw(display)

        pg.display.update()
