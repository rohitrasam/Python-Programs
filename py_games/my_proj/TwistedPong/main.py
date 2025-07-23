import pygame as pg
from sys import exit
from scripts.ball import Ball
from scripts.bot import Bot
from scripts.player import Player
from scripts.utils import debug, load_image
from scripts.button import Button

""" 
1. TODO: Implement UI for main menu:
    - Button class  ✔️ 
    - Load images   ✔️
    - Check for click (later)
    - Some effect on hover or selection (later)
    - Implement update method
        - Title bounce ✔️
2. TODO: Implement timer before game resume ✔️
    - Try to improve
3. TODO: Code VFX
4. TODO: Screen shake
5. TODO: Power ups
6. TODO: Implement Score
7. TODO: Improve image loading code
"""

class Game:

    WIDTH, HEIGHT = 1080, 480
    FPS = 60

    def __init__(self):
        pg.init()
        pg.display.set_caption("Twisted Pong")
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.display = pg.Surface((self.WIDTH // 2, self.HEIGHT // 2))
        self.clock = pg.Clock()
        self.ball = Ball(self, (self.get_display_width() // 2, self.get_display_height() // 2), size=16)
        self.assets = {
                    'ball': load_image("ball/0.png"),
                    'player': load_image("player/0.png"),
                    'board': load_image("board/0.png"),
                    'partition': load_image('board/1.png'),
                    'main': load_image("buttons/main.png"),
                    'cpu': load_image("buttons/cpu.png"),
                    '2P': load_image("buttons/2P.png"),
                    'exit': load_image("buttons/exit.png"),
                    'title': load_image('title.png'),
                    'paused': load_image('buttons/paused.png'),
                    '1': load_image('/counter/0.png'),
                    '2': load_image('/counter/1.png'),
                    '3': load_image('/counter/2.png'),
            }
        pg.display.set_icon(self.assets["ball"])
        self.player = Player(self, [2, self.get_display_height() // 2], [5, 32], "P1")
        self.entities: list[Player, Bot | Player] = [self.player, Bot(self, [self.get_display_width()-7, self.get_display_height() // 2], [5, 32], 3)]
        self.state = "main"
        self.pause = False
        self.dt = 0
        self.select = Button(self, "ball", [self.get_display_width() // 2 - 25, self.get_display_height() // 2], size=[16, 16])
        self.title = Button(self, "title", [self.get_display_width() // 2, 50], size=[116, 29])  
        self.main = Button(self, "main", [self.get_display_width() // 2, 120])
        self.paused = Button(self, 'paused', [self.get_display_width() // 2, self.get_display_height() // 2])
        self.buttons = [
                        Button(self, "2P", [self.get_display_width() // 2, self.get_display_height() // 2 + 30]),
                        Button(self, "cpu", [self.get_display_width() // 2, self.get_display_height() // 2 + 55]), 
                        Button(self, "exit", [self.get_display_width() // 2, self.get_display_height() // 2 + 80])
                        ]
        self.counters = [
                    Button(self, '1', self.paused.pos, size=[10, 17]),
                    Button(self, '2', self.paused.pos, size=[10, 17]),
                    Button(self, '3', self.paused.pos, size=[10, 17])
        ]
        self.selection = 0
        self.timer_event = pg.USEREVENT + 1
        self.counter = 4

    def get_display_width(self):
        return self.display.get_width()

    def get_display_height(self):
        return self.display.get_height()

    def run(self):

        while True:
            self.dt = self.clock.tick(self.FPS) / 1000
            self.display.blit(self.assets['board'], (0, 0))

            if self.state == "main":
                self.menu()
            elif self.state == "game":
                self.game()

            self.screen.blit(pg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pg.display.update()
                      
    def menu(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.quit()
            if event.type == pg.KEYDOWN and event.key == pg.K_w:
                self.selection = (self.selection - 1) % len(self.buttons)
            if event.type == pg.KEYDOWN and event.key == pg.K_s:
                self.selection = (self.selection + 1) % len(self.buttons)
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                if self.buttons[self.selection].text == "2P":
                    self.entities[1] = Player(self, [self.get_display_width()- 7, self.get_display_height() // 2], [5, 32], "P2")
                elif self.buttons[self.selection].text == "exit":
                    self.quit()
                self.state = 'game'
        
        self.select.pos.y = self.buttons[self.selection].pos.y
        self.select.render()
        self.title.render()
        self.main.render()
        for button in self.buttons:
            button.render()
            
        self.title.update(self.dt)

    def game(self):

        debug(f"FPS: {int(self.clock.get_fps())}", self.display)
        self.display.blit(self.assets['partition'], (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            elif (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.pause = not self.pause
                if not self.pause:
                    pg.time.set_timer(self.timer_event, 1000)
                    self.pause = True
            elif event.type == self.timer_event:
                self.counter -= 1
                if self.counter == 0:
                    self.counter = 4
                    pg.time.set_timer(self.timer_event, 0)
                    self.pause = False

        # all render statements      
        self.ball.render()
        for entity in self.entities:
            entity.render()

        # all update statements
        if not self.pause:
            self.ball.update(self.dt)
            for entity in self.entities:
                entity.update(self.dt)
        else:
            if self.counter == 4:
                self.paused.render()
            else:
                self.counters[self.counter-1].render()

    def quit(self):
        pg.quit()
        exit()        

if __name__ == '__main__':
    Game().run()
