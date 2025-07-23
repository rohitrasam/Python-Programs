import pygame as pg
from sys import exit
from random import randrange

HEIGHT = 720
WIDTH = 1000


class Food:

    def __init__(self) -> None:
        self.surf = pg.Surface((20, 20))
        self.surf.fill((255, 120, 0))
        self.pos = snake.get_random_position()
        self.rect = self.surf.get_rect(center=self.pos)

    def update(self):
        if self.rect.colliderect(snake.rect):
            self.pos = snake.get_random_position()
            self.rect.center = self.pos
            snake.size += 1
            # parts.append(Snake([parts[-1].rect.centerx+100, parts[-1].rect.centery]))

    def draw(self, screen):
        self.update()
        screen.blit(self.surf, self.rect)

class Snake():

    def __init__(self, pos) -> None:

        self.surf = pg.Surface((20, 20))
        self.movement = [False, False, False, False]
        self.surf.fill((0, 255, 200))
        self.pos = self.get_random_position()
        self.rect = self.surf.get_rect(center=self.pos)
        self.vel = 200
        self.size = 1
        self.paths = [self.rect]


    def update(self):
        
        self.pos[0] += (self.movement[1] - self.movement[0]) * self.vel*dt
        self.pos[1] += (self.movement[3] - self.movement[2]) * self.vel*dt
        
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and not self.movement[1]:
            self.movement[0] = True
            self.movement[1] = False
            self.movement[2] = False
            self.movement[3] = False

        if keys[pg.K_RIGHT] and not self.movement[0]:
            self.movement[1] = True
            self.movement[0] = False
            self.movement[2] = False
            self.movement[3] = False

        if keys[pg.K_UP] and not self.movement[3]:
            self.movement[2] = True
            self.movement[0] = False
            self.movement[1] = False
            self.movement[3] = False

        if keys[pg.K_DOWN] and not self.movement[2]:
            self.movement[3] = True
            self.movement[0] = False
            self.movement[1] = False
            self.movement[2] = False
        self.rect.center = self.pos
        snake.paths.append(snake.rect.copy())
        self.paths = self.paths[0:self.size]
        
    def get_random_position(self):
        return [randrange(10, WIDTH - 10, 20),randrange(10, HEIGHT - 10, 20)]

    def draw(self, screen):
        self.update()
        # print(self.rect, self.rect.copy())
        [pg.draw.rect(screen, (0, 255, 200), rect) for rect in self.paths]


def draw_grid():
    for x in range(0, WIDTH, 20):
        pg.draw.line(display, [50]*3, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, 20):
        pg.draw.line(display, [50]*3, (0, y), (WIDTH, y))

if __name__ == '__main__':

    snake = Snake([110, 110])
    food  = Food()

    pg.init()
    display = pg.display.set_mode((WIDTH, HEIGHT))

    clock = pg.time.Clock()

    dt = 0

    running = True
    while running:

        display.fill((0, 0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        snake.draw(display)
        food.draw(display)

        draw_grid()
        pg.display.update()
        dt = clock.tick(10)/1000
        
