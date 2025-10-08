import pygame as pg
import math
from models.mob import Mob

class Bullet(Mob):
    def update(self, dt):
        self.acceleration = pg.Vector2(math.sin(math.radians(self.angle)),-math.cos(math.radians(self.angle)))
        self.velocity += self.acceleration
        self.pos += self.velocity * dt
    