# import pygame as pg, sys
# from random import randint


# class Crosshair():

#     def __init__(self) -> None:
#         super().__init__()
#         self.surf = pg.Surface((5, 5))
#         self.surf.fill((250, 0, 0))
#         self.rect = self.surf.get_rect(center=(WIDTH/2, HEIGHT/2))
#         self.gunshot = pg.mixer.Sound("D:\Python Programs\py_games\gameTut\data\sfx\shoot.wav")

#     def shoot(self):
#         self.gunshot.play()
#         for target in target_group:
#             if self.rect.colliderect(target):
#                 target_group.remove(target)
    
#     def move(self):
#         self.rect.center = pg.mouse.get_pos()

# class Target():
    
#     def __init__(self, pos) -> None:
#         super().__init__()
#         self.surf = pg.Surface((30, 30))
#         self.surf.fill((100, 100, 100))
#         self.rect = self.surf.get_rect(center=pos)
#         self.vel =[randint(1, 5), randint(1, 5)]
        
#     def move(self):
#         self.rect.centerx += self.vel[0]
#         self.rect.centery += self.vel[1]
#         if self.rect.midright[0] >= WIDTH or self.rect.midleft[0] <=0:
#             self.vel[0] = -self.vel[0]
#         if self.rect.midbottom[1] >= HEIGHT or self.rect.midtop[1] <= 0:
#             self.vel[1] = -self.vel[1]
    
# def render():
#     for tar in target_group:
#         tar.move()
#         screen.blit(tar.surf, tar.rect)
            

# WIDTH = 1000
# HEIGHT = 720
# BG = ()

# pg.init()

# pg.mouse.set_visible(False)
# clock = pg.time.Clock()
# screen = pg.display.set_mode((WIDTH, HEIGHT))
# bg = pg.image.load("py_games\gameTut\data\images\\background.png")

# crosshair = Crosshair()


# target_group = [Target((randint(0, WIDTH), randint(0, HEIGHT)))]
# for target in range(1, 41):
#     pos = randint(0, WIDTH), randint(0, HEIGHT)
#     new_target = Target(pos)
#     target_group.append(new_target)


# while True:
#     for event in pg.event.get():

#         if event.type == pg.QUIT:
#             pg.quit()
#             sys.exit()
            
#         if event.type == pg.MOUSEBUTTONDOWN:
#             crosshair.shoot()

#     screen.blit(pg.transform.scale(bg, screen.get_size()), (0, 0))
#     render()

#     screen.blit(crosshair.surf, crosshair.rect)
#     crosshair.move()

#     pg.display.flip()
#     clock.tick(60)


# import os


# for file in os.listdir("./Space shooter"):
#     print(file)


# names = ['John', 'Paul', 'George', 'Ringo']

# for name in names[:]:
#     if name not in ['John', 'Paul']:
#         names.remove(name)

# print(names)
