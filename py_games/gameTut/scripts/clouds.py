import random
import pygame as pg

class Cloud:

    def __init__(self, pos: list[int], img: pg.Surface, speed: float, depth: float) -> None:
        self.pos = pg.Vector2(pos)
        self.img = img
        self.speed = speed
        self.depth = depth
        
    def update(self):
        self.pos.x += self.speed

    def render(self, surf: pg.Surface, offset=(0, 0)):
        render_pos = (self.pos.x - offset[0] * self.depth, self.pos.y - offset[1] * self.depth)
        
        # % is used to loop around
        surf.blit(self.img, (render_pos[0] % (surf.get_width() + self.img.get_width()) - self.img.get_width(), render_pos[1] % (surf.get_height() + self.img.get_height()) - self.img.get_height()))


class Clouds:

    def __init__(self, cloud_images: list[Cloud], count=16) -> None:
        self.clouds = [
                Cloud(
                        (random.random() * 99999,)*2, 
                        random.choice(cloud_images), 
                        random.random() * 0.05 + 0.05, 
                        random.random() * 0.6 + 0.2
                    )
                for _ in range(count)
            ]
        self.clouds.sort(key=lambda x: x.depth)
    
    def update(self):
        for cloud in self.clouds:
            cloud.update()
    
    def render(self, surf: pg.Surface, offset=(0, 0)):
        for cloud in self.clouds:
            cloud.render(surf, offset)
        