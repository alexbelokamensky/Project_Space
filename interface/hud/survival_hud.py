import pygame as pg
import os
import pygame_gui as pgui

from core.config import WINDOW_HEIGHT, WINDOW_WIDTH, FPS, PLAYER_MAX_HP, THEMES_PATH
class SurvivalHud:
    
    def __init__(self, manager):
        self.manager = manager
        self.ui_manager = pgui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT), os.path.join(THEMES_PATH, "survival_hud_theme.json"))
        
        self.survival_mode_game = pgui.elements.UIButton(relative_rect=pg.Rect(WINDOW_WIDTH-55, 5, 50, 25),
                                                               text="Pause", manager= self.ui_manager)
        
        self.lb_timer_text = pgui.elements.UILabel(relative_rect=pg.Rect(5, 5, 100, 30),
                                                   text="time:", manager=self.ui_manager)
        
        self.lb_hp_text = pgui.elements.UILabel(relative_rect=pg.Rect(125, 5, 50, 50),
                                                text="hp: ", manager=self.ui_manager)
        
        self.start_time = pg.time.get_ticks()
    
    def handle_event(self, event):
        self.ui_manager.process_events(event)
        if event.type == pgui.UI_BUTTON_PRESSED:
            if event.ui_element == self.survival_mode_game:
                self.manager.set_screen("menu")

    def update(self, dt, hp):
        elapsed = (pg.time.get_ticks() - self.start_time) // 1000
        self.lb_timer_text.set_text("time: " + str(elapsed) + "s")
        
        self.lb_hp_text.set_text("hp: " + str(hp))
        self.ui_manager.update(dt)
    
    def draw(self, surface):
        self.ui_manager.draw_ui(surface)