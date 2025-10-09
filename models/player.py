import pygame as pg
import os
import math
from models.mob import Mob
from models.flame import Flame
from core.config import WINDOW_HEIGHT, WINDOW_WIDTH, IMAGE_PATH, PLAYER_MAX_HP

class Player(Mob):
    
    original_player_image = pg.image.load(os.path.join(IMAGE_PATH, "player/player.png"))
    player_sprite = pg.transform.scale(original_player_image, (80,80))
    image = player_sprite
    
    def __init__(self, x, y, angle=0, image=image):
        super().__init__(x, y, angle, image)
        self.flame = Flame(self)
        self.hp = PLAYER_MAX_HP
        
    def handle_input(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.angle -= 50*dt
        elif keys[pg.K_d]:
            self.angle += 50*dt
        elif keys[pg.K_w]:
            self.velocity += self.acceleration / 10 * 5
            self.flame.power = 2
        elif keys[pg.K_s]:
            self.velocity -= self.acceleration / 10
            self.flame.power = 0
    
    def update(self, dt):
        self.flame.power = 1 #standart flame power
        self.handle_input(dt)
        self.border_controll()
        self.acceleration = pg.Vector2(math.sin(math.radians(self.angle)),-math.cos(math.radians(self.angle)))
        self.velocity += self.acceleration / 10
        self.pos += self.velocity * dt
        
        self.flame.update()
        
    def draw(self, surface):
        self.flame.draw(surface)
        surface.blit(self.image, self.rect.topleft)
        return super().draw(surface)
    
    def border_controll(self):
        if self.pos.x > WINDOW_WIDTH+40:
            self.pos.x = 0-40
        elif self.pos.x < 0-40:
            self.pos.x = WINDOW_WIDTH+40
            
        if self.pos.y > WINDOW_HEIGHT+40:
            self.pos.y = 0-40
        elif self.pos.y < 0-40:
            self.pos.y = WINDOW_HEIGHT+40
    
    