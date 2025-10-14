import pygame as pg
import os

from core.config import IMAGE_PATH
from models.mob import Mob

class Shield(Mob):
    original_shield_image = pg.image.load(os.path.join(IMAGE_PATH, "shield/shield.png"))
    shield_sprite = pg.transform.scale(original_shield_image, (120, 120))
    
    def __init__(self, player, x=0, y=0, angle=0, image=shield_sprite, alfa=100):
        super().__init__(x, y, angle, image, alfa)
        self.player = player
        self.start_time = pg.time.get_ticks()
    
    def update(self, dt):
        self.pos = self.player.pos
        if (pg.time.get_ticks() - self.start_time) // 1000 == 10:
            self.kill()