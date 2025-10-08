import pygame as pg
import os
import math
from models.mob import Mob
from core.config import WINDOW_HEIGHT, WINDOW_WIDTH, IMAGE_PATH

class Player(Mob):
    
    original_player_image = pg.image.load(os.path.join(IMAGE_PATH, "player/player.png"))
    player_sprite = pg.transform.scale(original_player_image, (75,75))
    image = player_sprite
    
    def __init__(self, x, y, angle=0, image=image):
        super().__init__(x, y, angle, image)
        
    def handle_input(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.angle -= 50*dt
        elif keys[pg.K_d]:
            self.angle += 50*dt
        elif keys[pg.K_w]:
            self.velocity += self.acceleration / 10 * 5
        elif keys[pg.K_s]:
            self.velocity -= self.acceleration / 10
    
    def update(self, dt):
        self.handle_input(dt)
        self.border_controll()
        self.acceleration = pg.Vector2(math.sin(math.radians(self.angle)),-math.cos(math.radians(self.angle)))
        self.velocity += self.acceleration / 10
        self.pos += self.velocity * dt
    
    def border_controll(self):
        if self.pos.x > WINDOW_WIDTH+40:
            self.pos.x = 0-40
        elif self.pos.x < 0-40:
            self.pos.x = WINDOW_WIDTH+40
            
        if self.pos.y > WINDOW_HEIGHT+40:
            self.pos.y = 0-40
        elif self.pos.y < 0-40:
            self.pos.y = WINDOW_HEIGHT+40
    
    