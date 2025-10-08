import pygame as pg
import pygame_gui as pgui
import time
import os
from models.player import Player
from models.asteroid import Asteroid
from models.bullet import Bullet

from core.config import WINDOW_WIDTH, WINDOW_HEIGHT, IMAGE_PATH
from interface.screens.base_screen import Screen

class SurvivalModeScreen(Screen):
    def __init__(self, manager):
        self.frame_counter = 0
        self.dead_frame = 0
        self.frames_before_dead = 0
        
        self.manager = manager
        self.ui_manager = pgui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))
        
        #background
        background_image = pg.image.load(os.path.join(IMAGE_PATH, "background/background1.jpg")).convert_alpha()
        self.background = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background.blit(pg.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT)))
        
        #buttons
        self.survival_mode_game = pgui.elements.UIButton(relative_rect=pg.Rect(0, 0, 50, 25),
                                                               text="Pause", manager= self.ui_manager)
        
        #player initialization
        self.player = Player(WINDOW_WIDTH/2-100, WINDOW_HEIGHT/2-75)
        
        #asteroids
        self.asteroids = pg.sprite.Group()
        
        #bullets
        self.bullets = pg.sprite.Group()
        
        
    def handle_event(self, event):
        self.ui_manager.process_events(event)
        if event.type == pgui.UI_BUTTON_PRESSED:
            if event.ui_element == self.survival_mode_game:
                self.manager.set_screen("menu")
        if event.type == pg.KEYDOWN:
            if event.unicode == '\x1b':
                self.manager.set_screen("menu")
            if event.key == 1073742049:
                self.asteroids = pg.sprite.Group()
            if event.unicode == ' ':
                bullet = Bullet(self.player)
                self.bullets.add(bullet)

    def update(self, dt):
        self.ui_manager.update(dt)
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
                self.manager.set_screen("menu")
        
        for bullet in self.bullets:
            bullet.update(dt)
            for asteroid in self.asteroids:
                if bullet.collision_verification(asteroid):
                    asteroid.kill()
                    bullet.kill()
        
    def draw(self, surface):
        surface.blit(self.background, (0, 0))
        self.ui_manager.draw_ui(surface)
        self.player.draw(surface)
        
        for asteroid in self.asteroids:
            asteroid.draw(surface)
        
        for bullet in self.bullets:
            bullet.draw(surface)
    
