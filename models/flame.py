import pygame as pg
import os
import math
from core.config import IMAGE_PATH

class Flame(pg.sprite.Sprite):
    original_flame0_image = pg.image.load(os.path.join(IMAGE_PATH, "flame/flame0.png"))
    flame0_sprite = pg.transform.scale(original_flame0_image, (0, 0))
    
    original_flame1_image = pg.image.load(os.path.join(IMAGE_PATH, "flame/flame1.png"))
    flame1_sprite = pg.transform.scale(original_flame1_image, (15, 25))

    original_flame2_image = pg.image.load(os.path.join(IMAGE_PATH, "flame/flame2.png"))
    flame2_sprite = pg.transform.scale(original_flame2_image, (20, 35))

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.image = self.flame1_sprite
        self.rect = self.image.get_rect()
        self.offset = 40 
        self.power = 1

    def update(self):
        angle_rad = math.radians(self.player.angle)
        x = self.player.pos.x - math.sin(angle_rad) * self.offset
        y = self.player.pos.y + math.cos(angle_rad) * self.offset
        if self.power == 1:
            self.image = pg.transform.rotate(self.flame1_sprite, -self.player.angle)  
        elif self.power == 2:
            self.image = pg.transform.rotate(self.flame2_sprite, -self.player.angle)
        else:
            self.image = pg.transform.rotate(self.flame0_sprite, -self.player.angle)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)