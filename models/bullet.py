import pygame as pg
import math
from models.mob import Mob

class Bullet(Mob):
    def __init__(self, player):
        bullet_img = pg.Surface((5, 10), pg.SRCALPHA)
        bullet_img.fill((255, 0, 0))
        
        self.player = player
        self.offset = 40
        self.angle = player.angle 
        
        angle_rad = math.radians(self.angle)
        
        x = self.player.pos.x + math.sin(angle_rad) * self.offset
        y = self.player.pos.y - math.cos(angle_rad) * self.offset

        self.image = pg.transform.rotate(bullet_img, -self.player.angle)
        self.rect = self.image.get_rect(center=(x, y))
        
        super().__init__(x, y, self.angle, bullet_img)
        self.velocity = pg.Vector2(math.sin(angle_rad), -math.cos(angle_rad)) * 200
        
    def update(self, dt):
         self.pos += self.velocity * dt
    