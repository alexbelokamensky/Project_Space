import pygame as pg
import os

from models.player import Player
from models.asteroid import Asteroid
from models.bullet import Bullet
from models.explosion import Explosion
from models.shield import Shield
from models.loot import Loot

from interface.screens.base_screen import Screen
from interface.hud.survival_hud import SurvivalHud

from core.config import WINDOW_WIDTH, WINDOW_HEIGHT, IMAGE_PATH, FPS

class SurvivalModeScreen(Screen):
    def __init__(self, screen_manager):
        self.autofire_flag = False
        
        self.frame_counter = 0
        
        self.screen_manager = screen_manager
        
        #background
        background_image = pg.image.load(os.path.join(IMAGE_PATH, "background/background1.jpg")).convert_alpha()
        self.background = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background.blit(pg.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT)))
        
        #hud
        self.survival_hud = SurvivalHud(screen_manager)
        
        #player initialization
        self.player = Player(WINDOW_WIDTH/2-100, WINDOW_HEIGHT/2-75)
        
        #asteroids
        self.asteroids = pg.sprite.Group()
        
        #bullets
        self.bullets = pg.sprite.Group()
        
        #explosions
        self.explosions = pg.sprite.Group()
        
        #shields
        self.shields = pg.sprite.Group()
        
        #loot
        self.loots = pg.sprite.Group()
        
    def handle_event(self, event):
        self.survival_hud.handle_event(event)
        
        if self.survival_hud.restart_flag:
            self.reset_game()
            
        if event.type == pg.KEYDOWN:
            #pause game
            if event.unicode == '\x1b':
                self.screen_manager.set_screen("menu")
                
            #delete all astoroids
            if event.key == 1073742049:
                if self.player.ult > 0:
                    for asteroid in self.asteroids:
                        explosion = Explosion(asteroid)
                        self.explosions.add(explosion)
                        asteroid.kill()
                    self.player.ult -= 1
                
            #shoot
            if event.unicode == ' ':
               self.shoot(3)
            
            #shield
            if event.unicode == 'q':
                if self.player.shields > 0:
                    shield = Shield(self.player)
                    self.shields.add(shield)
                    self.player.shields -= 1

            #autofire enable/disable
            if event.unicode == "t":
                self.autofire_flag = not self.autofire_flag
        

    def update(self, dt):
        #update interface
        self.survival_hud.update(dt, self.player.hp, self.player.shields, self.player.ult)
        
        self.player.update(dt)
        
        #shield moovement and collison
        for shield in self.shields:
            if pg.sprite.spritecollide(shield, self.asteroids, False):     
                if pg.sprite.spritecollide(shield, self.asteroids, False, pg.sprite.collide_mask):       
                    collidet_asteroid = pg.sprite.spritecollide(shield, self.asteroids, False, pg.sprite.collide_mask)[0]
                    explosion = Explosion(collidet_asteroid)
                    self.explosions.add(explosion)
                    collidet_asteroid.kill()
                    
            shield.update(dt)
            
        #asteroid generation
        self.frame_counter += 1
        if self.frame_counter % (FPS/4) == 0:
            asteroid = Asteroid()
            self.asteroids.add(asteroid)
        
        #loot generation
        if self.frame_counter % (FPS*10) == 0:
            loot = Loot()
            self.loots.add(loot)
        
        if self.autofire_flag:
            if self.frame_counter % (FPS/6) == 0:
               self.shoot(3) 
            
        #loot collision
        if pg.sprite.spritecollide(self.player, self.loots, False):     
            if pg.sprite.spritecollide(self.player, self.loots, False, pg.sprite.collide_mask):
                #loot effects
                collidet_loot = pg.sprite.spritecollide(self.player, self.loots, False, pg.sprite.collide_mask)[0]
                if collidet_loot.loot_type == 0:
                    self.player.shields += 1
                if collidet_loot.loot_type == 1:
                    self.player.ult += 1
                if collidet_loot.loot_type == 2:
                    self.player.hp += 1
                collidet_loot.kill()
        
        #asteroid moovement
        for asteroid in self.asteroids:
            asteroid.update(dt)    
        
        #asteroid collision
        if pg.sprite.spritecollide(self.player, self.asteroids, False):     
            if pg.sprite.spritecollide(self.player, self.asteroids, False, pg.sprite.collide_mask):
                
                collidet_asteroid = pg.sprite.spritecollide(self.player, self.asteroids, False, pg.sprite.collide_mask)[0]
                explosion = Explosion(collidet_asteroid)
                self.explosions.add(explosion)
                collidet_asteroid.kill()
                
                self.player.hp -= 1
                
                #player die
                if self.player.hp == 0:
                    self.reset_game()
                    self.screen_manager.set_screen("menu")
        
       #bullet moovement and collision
        for bullet in self.bullets:
            bullet.update(dt)
            if pg.sprite.spritecollide(bullet, self.asteroids, False):
                if pg.sprite.spritecollide(bullet, self.asteroids, False, pg.sprite.collide_mask):
                    collidet_asteroid =pg.sprite.spritecollide(bullet, self.asteroids, False, pg.sprite.collide_mask)[0]
                    explosion = Explosion(collidet_asteroid)
                    self.explosions.add(explosion)
                    collidet_asteroid.kill()
                    bullet.kill()
                    
        #explosion update
        for explosion in self.explosions:
            explosion.update(dt)
        
    def draw(self, surface):
        surface.blit(self.background, (0, 0))
        
        self.survival_hud.draw(surface)
        
        self.player.draw(surface)
        
        for shield in self.shields:
            shield.draw(surface)
        
        for asteroid in self.asteroids:
            asteroid.draw(surface)
        
        for bullet in self.bullets:
            bullet.draw(surface)
        
        for explosion in self.explosions:
            explosion.draw(surface)
            
        for loot in self.loots:
            loot.draw(surface)
    
    
    def reset_game(self):
        self.player = Player(WINDOW_WIDTH/2-100, WINDOW_HEIGHT/2-75)
        self.asteroids = pg.sprite.Group()
        self.explosions = pg.sprite.Group()
        self.loots = pg.sprite.Group()
        self.shields = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.survival_hud = SurvivalHud(self.screen_manager)
    
    def shoot(self, num_bullets):
        angle_between_bullets = 15
        init_angle = self.player.angle - int(num_bullets / 2) * angle_between_bullets
        for x in range(num_bullets):
            angle = init_angle + x * angle_between_bullets
            bullet = Bullet(self.player, angle)
            self.bullets.add(bullet)
        