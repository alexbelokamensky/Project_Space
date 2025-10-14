import pygame as pg
import os
import random

from models.mob import Mob
from core.config import WINDOW_HEIGHT, WINDOW_WIDTH, IMAGE_PATH

class Asteroid(Mob):

    def __init__(self,):
        self.rotation_speed = random.randrange(10, 40)
        self.generate_image()
        super().__init__(0, 0, 0, image=self.image)
        self.generate_direction()
        self.update_graphics()
    
    def generate_direction(self):
        match random.randrange(0, 4):
            case 0: 
                self.pos = pg.Vector2(0-self.rect.width/2+1, random.randrange(0, WINDOW_HEIGHT))
                self.acceleration = pg.Vector2(random.uniform(0, 1), random.uniform(-1, 1))
            case 1: 
                self.pos = pg.Vector2(WINDOW_WIDTH+self.rect.width/2-1, random.randrange(0, WINDOW_HEIGHT))
                self.acceleration = pg.Vector2(random.uniform(-1, 0), random.uniform(-1, 1))
            case 2: 
                self.pos = pg.Vector2(random.randrange(0, WINDOW_WIDTH), 0-self.rect.height/2+1)
                self.acceleration = pg.Vector2(random.uniform(-1, 1), random.uniform(0, 1))
            case 3: 
                self.pos = pg.Vector2(random.randrange(0, WINDOW_WIDTH), WINDOW_HEIGHT+self.rect.height/2-1)
                self.acceleration = pg.Vector2(random.uniform(-1, 1), random.uniform(-1, 0))

    def generate_image(self):
        original_asteroid_image = None
        asteroid_sprite = None
        
        match random.randrange(0, 5):
            case 0: 
                original_asteroid_image =pg.image.load(os.path.join(IMAGE_PATH, "asteroid/asteroid1.png"))
            case 1: 
                original_asteroid_image =pg.image.load(os.path.join(IMAGE_PATH, "asteroid/asteroid2.png"))
            case 2: 
                original_asteroid_image =pg.image.load(os.path.join(IMAGE_PATH, "asteroid/asteroid3.png"))
            case 3: 
                original_asteroid_image =pg.image.load(os.path.join(IMAGE_PATH, "asteroid/asteroid4.png"))
            case 4: 
                original_asteroid_image =pg.image.load(os.path.join(IMAGE_PATH, "asteroid/asteroid5.png"))

        asteroid_sprite = pg.transform.scale(original_asteroid_image, (random.randrange(40, 60), random.randrange(40, 60)))                
        self.image = asteroid_sprite
        self.original_image = asteroid_sprite

    def update(self, dt):
        self.angle += self.rotation_speed*dt
        self.velocity += self.acceleration / 10
        self.pos += self.velocity * dt
        self.clear()
    
    def clear(self):
        if self.rect.left > WINDOW_WIDTH or self.rect.right < 0 or self.rect.top > WINDOW_HEIGHT or self.rect.bottom < 0:
            self.kill()