import pygame as pg
import os
from core.config import IMAGE_PATH
from models.mob import Mob

class Explosion(Mob):
    
    original_explosion_image = pg.image.load(os.path.join(IMAGE_PATH, "explosion/explosion.png"))
    explosion_sprite = pg.transform.scale(original_explosion_image, (80, 80))
    
    def __init__(self, asteroid, image=explosion_sprite):
        self.asteroid = asteroid
        super().__init__(asteroid.pos.x, asteroid.pos.y, asteroid.angle, image)
        self.start_time = pg.time.get_ticks()
        
    def update(self, dt):
        if (pg.time.get_ticks() - self.start_time) // 100 == 1:
            self.kill()
        return super().update(dt)