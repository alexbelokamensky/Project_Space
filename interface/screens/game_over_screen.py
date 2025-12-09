import pygame as pg
import pygame_gui as pgui
import os

from core.config import WINDOW_WIDTH, WINDOW_HEIGHT, IMAGE_PATH, THEMES_PATH
from interface.screens.base_screen import Screen

class GameOverScreen(Screen):
    def __init__(self, manager):
        self.manager = manager
        self.ui_manager = pgui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT), os.path.join(THEMES_PATH, "game_over_theme.json"))
        
        gameover_image = pg.image.load(os.path.join(IMAGE_PATH, "hud/gameover.png")).convert_alpha()
        self.gameover_image_surface = pg.Surface((420, 270))
        self.gameover_image_surface.blit(pg.transform.scale_by(gameover_image, 0.4))
        
        self.img_gameover = pgui.elements.UIImage(relative_rect=pg.Rect(WINDOW_WIDTH/2 - 210, WINDOW_HEIGHT/2-300, 420, 270),
                                            image_surface=self.gameover_image_surface,
                                            manager=self.ui_manager)
        
        self.lb_score = pgui.elements.UILabel(relative_rect=pg.Rect(WINDOW_WIDTH/2 - 100 , WINDOW_HEIGHT/2-25, 300, 100),
                                                text="Score: 0000", manager=self.ui_manager)
        
        self.menu_button = pgui.elements.UIButton(relative_rect=pg.Rect(WINDOW_WIDTH/2-100, WINDOW_HEIGHT/2+100, 200, 80),
                                                               text="Menu", manager=self.ui_manager)

        background_image = pg.image.load(os.path.join(IMAGE_PATH, "background/background3.jpg")).convert_alpha()
        self.background = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background.blit(pg.transform.scale_by(background_image, 1.6))
    
    def update_score(self, score):
        self.lb_score.set_text("Score: " + str(score))    
    
    def handle_event(self, event):
        self.ui_manager.process_events(event)
        if event.type == pgui.UI_BUTTON_PRESSED:
            if event.ui_element == self.menu_button:
                self.manager.set_screen("menu")

    def update(self, dt):
        self.ui_manager.update(dt)

    def draw(self, surface):
        surface.blit(self.background, (0, 0))
        self.ui_manager.draw_ui(surface)
        