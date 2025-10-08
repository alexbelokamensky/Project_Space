import pygame as pg
import os
import random
from models.mob import Mob
from core.config import WINDOW_HEIGHT, WINDOW_WIDTH, IMAGE_PATH

class Asteroid(Mob):

    def __init__(self, x=0, y=0, angle=0, image=None):
        super().__init__(x, y, angle, image)
        self.generate_image()
        self.generate_direction()
    
    def generate_direction(self):
        match random.randrange(0, 3):
            case 0: 
                self.pos = pg.Vector2(0-40, random.randrange(0, WINDOW_HEIGHT))
                self.acceleration = pg.Vector2(random.uniform(0, 1), random.uniform(-1, 1))
            case 1: 
                self.pos = pg.Vector2(WINDOW_WIDTH+40, random.randrange(0, WINDOW_HEIGHT))
                self.acceleration = pg.Vector2(random.uniform(-1, 0), random.uniform(-1, 1))
            case 2: 
                self.pos = pg.Vector2(random.randrange(0, WINDOW_WIDTH), 0-40)
                self.acceleration = pg.Vector2(random.uniform(-1, 1), random.uniform(0, 1))
            case 3: 
                self.pos = pg.Vector2(random.randrange(0, WINDOW_WIDTH), WINDOW_HEIGHT+40)
                self.acceleration = pg.Vector2(random.uniform(-1, 1), random.uniform(-1, 0))

    def generate_image(self):
        original_asteroid_image = None
        asteroid_sprite = None
        
        match random.randrange(0, 3):
            case 0: 
                original_asteroid_image =pg.image.load(os.path.join(IMAGE_PATH, "asteroid/asteroid1.png"))
            case 1: 
                original_asteroid_image =pg.image.load(os.path.join(IMAGE_PATH, "asteroid/asteroid4.png"))
            case 2: 
                original_asteroid_image =pg.image.load(os.path.join(IMAGE_PATH, "asteroid/asteroid5.png"))

        asteroid_sprite = pg.transform.scale(original_asteroid_image, (50, 50))                
        self.image = asteroid_sprite
        self.original_image = asteroid_sprite
        self.update_graphics()

    def update(self, dt):
        self.angle += 20*dt
        self.velocity += self.acceleration / 10
        self.pos += self.velocity * dt
        self.clear()
    
    def clear(self):
        if self.pos.x > WINDOW_WIDTH+50 or self.pos.x < 0-50 or self.pos.y > WINDOW_HEIGHT+50 or self.pos.y < 0-50:
            self.kill()