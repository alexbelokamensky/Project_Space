import pygame as pg
import pygame_gui as pgui

from core.config import WINDOW_HEIGHT, WINDOW_WIDTH, FPS, PLAYER_MAX_HP
class SurvivalHud:
    def __init__(self, manager):
        self.manager = manager
        self.ui_manager = pgui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.survival_mode_game = pgui.elements.UIButton(relative_rect=pg.Rect(0, 0, 50, 25),
                                                               text="Pause", manager= self.ui_manager)
        self.lb_timer_text = pgui.elements.UILabel(relative_rect=pg.Rect(0, 30, 50, 15), text="time:", manager=self.ui_manager)
        self.lb_timer_time = pgui.elements.UILabel(relative_rect=pg.Rect(25, 30, 50, 15), text="0", manager=self.ui_manager)
        
        self.lb_hp_text = pgui.elements.UILabel(relative_rect=pg.Rect(0, 60, 50, 20), text="hp: ", manager=self.ui_manager)
        self.lb_hp = pgui.elements.UILabel(relative_rect=pg.Rect(25, 60, 50, 20), text=str(PLAYER_MAX_HP), manager=self.ui_manager)
        
        self.start_time = pg.time.get_ticks()
    
    def handle_event(self, event):
        self.ui_manager.process_events(event)
        if event.type == pgui.UI_BUTTON_PRESSED:
            if event.ui_element == self.survival_mode_game:
                self.manager.set_screen("menu")

    def update(self, dt, hp):
        elapsed = (pg.time.get_ticks() - self.start_time) // 1000
        self.lb_timer_time.set_text(str(elapsed))
        
        self.lb_hp.set_text(str(hp))
        self.ui_manager.update(dt)
    
    def draw(self, surface):
        self.ui_manager.draw_ui(surface)