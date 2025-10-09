import pygame as pg
import pygame_gui as pgui
import time
import os
from models.player import Player
from models.asteroid import Asteroid
from models.bullet import Bullet

from interface.hud.survival_hud import SurvivalHud

from core.config import WINDOW_WIDTH, WINDOW_HEIGHT, IMAGE_PATH
from interface.screens.base_screen import Screen

class SurvivalModeScreen(Screen):
    def __init__(self, screen_manager):
        self.frame_counter = 0
        self.dead_frame = 0
        self.frames_before_dead = 0
        
        self.screen_manager = screen_manager
        
        #background
        background_image = pg.image.load(os.path.join(IMAGE_PATH, "background/background1.jpg")).convert_alpha()
        self.background = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background.blit(pg.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT)))
        
        self.survival_hud = SurvivalHud(screen_manager)
        
        #player initialization
        self.player = Player(WINDOW_WIDTH/2-100, WINDOW_HEIGHT/2-75)
        
        #asteroids
        self.asteroids = pg.sprite.Group()
        
        #bullets
        self.bullets = pg.sprite.Group()
        
        
    def handle_event(self, event):
        self.survival_hud.handle_event(event)
        if event.type == pg.KEYDOWN:
            if event.unicode == '\x1b':
                self.screen_manager.set_screen("menu")
            if event.key == 1073742049:
                self.asteroids = pg.sprite.Group()
            if event.unicode == ' ':
                bullet = Bullet(self.player)
                self.bullets.add(bullet)

    def update(self, dt):
        self.survival_hud.update(dt)
        self.player.update(dt)
            
        #asteroid generation
        self.frame_counter += 1
        if(self.frame_counter == 30):
            asteroid = Asteroid()
            self.asteroids.add(asteroid)
            self.frame_counter = 0
            
        #asteroin moovement and collision check
        for asteroid in self.asteroids:
            asteroid.update(dt)
            if self.player.collision_verification(asteroid):
                self.player = Player(WINDOW_WIDTH/2-100, WINDOW_HEIGHT/2-75)
                self.asteroids = pg.sprite.Group()
                self.bullets = pg.sprite.Group()
                self.survival_hud = SurvivalHud(self.screen_manager)
                self.screen_manager.set_screen("menu")
        
        for bullet in self.bullets:
            bullet.update(dt)
            for asteroid in self.asteroids:
                if bullet.collision_verification(asteroid):
                    asteroid.kill()
                    bullet.kill()
        
    def draw(self, surface):
        
        surface.blit(self.background, (0, 0))
        self.survival_hud.draw(surface)
        self.player.draw(surface)
        
        for asteroid in self.asteroids:
            asteroid.draw(surface)
        
        for bullet in self.bullets:
            bullet.draw(surface)
    
