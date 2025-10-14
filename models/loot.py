import pygame as pg
import os
import random

from core.config import IMAGE_PATH, WINDOW_WIDTH, WINDOW_HEIGHT
from models.mob import Mob

class Loot(Mob):
    def __init__(self, angle=0, image=None, alfa=255):
        self.loot_type = 0
        self.x = 0
        self.y = 0
        self.generate_image()
        self.generate_position()
        super().__init__(self.x, self.y, angle, self.image, alfa)
        
    def generate_image(self):
        self.loot_type = random.randrange(0, 3)
        original_loot_image = None
        loot_sprite = None
        
        match self.loot_type:
            case 0: 
                original_loot_image =pg.image.load(os.path.join(IMAGE_PATH, "shield/shield.png"))
                loot_sprite = pg.transform.scale(original_loot_image, (35, 35))                
            case 1: 
                original_loot_image =pg.image.load(os.path.join(IMAGE_PATH, "ultimate/bomb.png"))
                loot_sprite = pg.transform.scale(original_loot_image, (35, 35))                
            case 2: 
                original_loot_image =pg.image.load(os.path.join(IMAGE_PATH, "player/player.png"))
                loot_sprite = pg.transform.scale(original_loot_image, (45, 45))                

        self.image = loot_sprite
        self.original_image = loot_sprite
    
    def generate_position(self):
        self.x = random.randrange(0, WINDOW_WIDTH)
        self.y = random.randrange(0, WINDOW_HEIGHT)