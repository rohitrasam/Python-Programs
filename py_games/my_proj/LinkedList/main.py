import pygame as pg
from sys import exit
from random import randint


class Node:

    def __init__(self, data, pos, basefont,) -> None:
        self.__size = (150, 40)
        self.basefont = basefont
        self.data = data
        self.surf = pg.Surface(self.__size)
        self.surf.fill((50, 50, 50))
        self.pos = pos
        self.next = None
        self.rect = self.surf.get_rect(center=(self.pos))
        self.data_surf = self.basefont.render(str(self.data), True, (200, 200, 200))
        self.data_rect = self.data_surf.get_rect(center=(self.__size[0]/4, self.__size[1]/2))

    def render(self, screen):
         
        next_surf = self.basefont.render(str(self.next), False, (200, 200, 200))
        next_rect = next_surf.get_rect(center=(self.__size[0]/4*3, self.__size[1]/2))
        self.surf.blit(self.data_surf, self.data_rect)
        self.surf.blit(next_surf, next_rect)
        screen.blit(self.surf, self.rect)
        pg.draw.circle(screen, (255, 0, 0),  self.rect.midright, 4)
        pg.draw.circle(screen, (0, 255, 50), (self.rect.midleft), 4) 
        pg.draw.rect(screen, (255,)*3, (self.rect.topleft[0]+self.__size[0]/2, self.rect.topleft[1], 1, self.__size[1]))


class LinkedList:

    def __init__(self) -> None:
        self.list: list[Node] = []

    def insert(self, value, font, pos=-1,):
        if self.list:
            # newNode = Node(value, (self.list[-1].pos[0] + 150, self.list[-1].pos[1]), font)
            newNode = Node(value, (randint(150, 930), randint(40, 680)), font)
            if pos == -1:
                self.list[-1].next = id(newNode) % len(self.list) + randint(1, len(self.list))
                self.list.append(newNode)
            else:
                newNode.next = self.list[pos].next
                self.list[pos].next = id(newNode) % len(self.list) + randint(1, len(self.list))
                self.list.insert(pos, newNode)
        else:
            # newNode = Node(value, (90, 50), font)
            newNode = Node(value, (randint(150, 930), randint(40, 680)), font)
            self.list.append(newNode)

    
    def render(self, screen):
        for idx in range(len(self.list)-1):
            pg.draw.line(screen, (0, 0, 0), self.list[idx].rect.midright, self.list[idx+1].rect.midleft, 2)

            self.list[idx].render(screen)
        self.list[-1].render(screen)


class App:

    def __init__(self) -> None:
        pg.init()
        self.fps = 60
        self.font = pg.font.Font(None, 30)
        self.size = (1080, 720)
        self.display = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()
        self.list = LinkedList()
        self.activeNode = None
        pg.display.set_caption("Linked List vfx")

    def main(self):

        while True:
            # self.display.fill((255, 255, 255))
            self.display.fill((135, 206, 235))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    for node_num, node in enumerate(self.list.list):
                        if node.rect.collidepoint(pg.mouse.get_pos()):
                            self.activeNode = node_num
                    
                if event.type == pg.MOUSEMOTION and self.activeNode:
                    self.list.list[self.activeNode].rect.centerx += pg.mouse.get_pos()[0] - self.list.list[self.activeNode].rect.centerx
                    self.list.list[self.activeNode].rect.centery += pg.mouse.get_pos()[1] - self.list.list[self.activeNode].rect.centery

                if event.type == pg.MOUSEBUTTONUP:
                    self.activeNode = None
            

            self.list.render(self.display)
            pg.display.update()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    app = App()
    app.list.insert(3, app.font, -1)
    app.list.insert(4, app.font, -1)
    app.list.insert(1, app.font, -1)
    app.list.insert(2, app.font, -1)
    app.list.insert(12, app.font, 2 )
    app.list.insert(11, app.font, 1)
    app.list.insert(22, app.font, -1)
    app.main()