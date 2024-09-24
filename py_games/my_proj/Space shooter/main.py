import os
from random import randint, random
import math
from utils.consts import *
from utils.text import Text
from utils.enemy import Enemy
from utils.shooter import Shooter
from utils.bullet import Bullet
from utils.collectibles import HealthPack, MissilePack
from sys import exit

class Game:

    def __init__(self) -> None:
        pg.init()
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        pg.display.set_caption(TITLE)
        self.assets = {
                    "bg": pg.transform.scale(self.load_image("space_background_pack/parallax-space-1.png"), self.display.get_size()),
                    "stars": self.load_image("space_background_pack/parallax-space-2.png"),
                    "rings": self.load_image("space_background_pack/parallax-space-5.png"),
                    "far": self.load_image("space_background_pack/parallax-space-4.png"),
                    "big": self.load_image("space_background_pack/parallax-space-3.png"),
                    "player": self.load_image("tiny-spaceships/2X/tiny_ship15.png"),
                    "enemy": self.load_image("tiny-spaceships/2X/tiny_ship9.png"),
                    "bullet": pg.transform.scale(self.load_image("projectile.png"), (20, 10)),
                    "healthpack": self.load_image("collectibles/health.png"),
                    "missilepack": self.load_image("collectibles/missile.png"),
                }

        self.title = Text(175, [WIDTH/2, HEIGHT/3], TITLE)
        self.hp_text = Text(50, [40, 40], "HP", offset=3, movement=False)
        self.subtitle = Text(75, [WIDTH/2, HEIGHT/1.5], SUBTITLE, offset=3)
        self.player = Shooter(self, (60, HEIGHT/2), self.assets["player"])
        self.enemies = [Enemy(self, self.assets["enemy"]), Enemy(self, self.assets["enemy"]), Enemy(self, self.assets["enemy"])]
        self.sparks = []
        self.smoke = []
        self.stars_width, self.stars_height = self.assets["stars"].get_size()
        self.start = False
        self.scroll = 0
        self.health_pack = HealthPack(self, self.assets["healthpack"])
        self.missle_pack = MissilePack(self, self.assets["missilepack"])
        self.stars_rows = math.ceil(WIDTH / self.stars_width) + 1
        self.stars_cols = math.ceil(HEIGHT / self.stars_height) + 1

    def run(self):
        
        while True:
            fps = self.clock.tick(FPS)
            # print(fps)
            self.display.fill((0, 0, 0))

            # event loop
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    self.quit()
                if event.type == pg.KEYDOWN and not self.start:
                    if event.key == pg.K_SPACE:
                        self.start = not self.start
                if event.type == pg.MOUSEBUTTONDOWN and self.start and pg.mouse.get_pressed()[0] and self.player:
                    Bullet.ammo.append(self.player.shoot())

            if self.start:
                self.main_game()
                self.scroll -= 2
            else:
                self.main_menu()
            
            pg.display.update()

    def main_game(self):
        self.display.blit(self.assets["bg"], (0, 0))

        for row in range(self.stars_rows):
            for col in range(self.stars_cols):
                self.display.blit(self.assets["stars"], (row*self.stars_width+self.scroll, col*self.stars_height))
            
        if abs(self.scroll) > self.stars_width:
            self.scroll = 0

        self.display.blit(self.assets["far"], (WIDTH/4, HEIGHT/4))
        self.display.blit(self.assets["rings"], (WIDTH/2 + WIDTH/4, HEIGHT/2 + HEIGHT/4))
        self.display.blit(self.assets["big"], (WIDTH/4, HEIGHT/2+HEIGHT/4))

        self.hp_text.render(self.display)
        self.health_pack.render()
        self.missle_pack.render()
        if self.smoke:
            self.render_smoke()
        if self.sparks:
            self.render_sparks()
        if Bullet.ammo:
            self.render_bullet()
        if self.enemies:
            self.render_enemies()
        if self.player:
            self.player.render()

    def render_enemies(self):
        for enemy in self.enemies:
            enemy.render()
            if randint(1, 61) == 30:
                Bullet.ammo.append(enemy.shoot())
            
    def render_bullet(self):
        for bullet in Bullet.ammo:
            bullet.render()
    
    def render_sparks(self):
        for spark in self.sparks:
            spark.render()
            if spark.speed <= 0:
                self.sparks.remove(spark)

    def render_smoke(self):
        for smoke in self.smoke:
            smoke.render()
            if smoke.radius <= 0:
                self.smoke.remove(smoke)

    def main_menu(self):
        self.display.blit(self.assets["bg"], (0, 0))
        self.title.render(self.display)
        self.subtitle.render(self.display)

    def load_image(self, path):
        img =  pg.image.load(BASE_PATH + path).convert_alpha()
        # img.set_colorkey((0, 0, 0))
        return img
    
    def load_images(self, path):
        images = []
        for img in os.listdir(BASE_PATH + path):
            images.append(self.load_image(path + "/" + img))
        
        return images

    def quit(self):
        pg.quit()
        exit("Thanks for playing!!")

if __name__ == '__main__':

    game = Game()
    game.run()