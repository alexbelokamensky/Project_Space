import pygame as pg
import pygame_gui as pgui
import os
import sys

from core.config import WINDOW_WIDTH, WINDOW_HEIGHT, IMAGE_PATH
from interface.screens.base_screen import Screen

class MainMenuScreen(Screen):
    def __init__(self, manager):
        self.manager = manager
        self.ui_manager = pgui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.start_survival_mode_game = pgui.elements.UIButton(relative_rect=pg.Rect(WINDOW_WIDTH/2-100, WINDOW_HEIGHT/2-140, 200, 80),
                                                               text="Survival Mode", manager=self.ui_manager)
        
        self.start_parking_mode_game = pgui.elements.UIButton(relative_rect=pg.Rect(WINDOW_WIDTH/2-100, WINDOW_HEIGHT/2-40, 200, 80),
                                                               text="Parking Mode", manager=self.ui_manager)

        self.exit_game = pgui.elements.UIButton(relative_rect=pg.Rect(WINDOW_WIDTH/2-100, WINDOW_HEIGHT/2+60, 200, 80),
                                                               text="Exit", manager=self.ui_manager)
        
        background_image = pg.image.load(os.path.join(IMAGE_PATH, "background/background3.jpg")).convert_alpha()
        self.background = pg.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.background.blit(pg.transform.scale_by(background_image, 1.6))
        
    def handle_event(self, event):
        self.ui_manager.process_events(event)
        if event.type == pgui.UI_BUTTON_PRESSED:
            if event.ui_element == self.start_survival_mode_game:
                self.manager.set_screen("survival")
            if event.ui_element == self.exit_game:
                sys.exit()

    def update(self, dt):
        self.ui_manager.update(dt)

    def draw(self, surface):
        surface.blit(self.background, (0, 0))
        self.ui_manager.draw_ui(surface)
        