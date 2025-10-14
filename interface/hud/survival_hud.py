import pygame as pg
import os
import pygame_gui as pgui

from core.config import WINDOW_HEIGHT, WINDOW_WIDTH, THEMES_PATH, IMAGE_PATH
class SurvivalHud:
    
    def __init__(self, manager):
        self.manager = manager
        self.ui_manager = pgui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT), os.path.join(THEMES_PATH, "survival_hud_theme.json"))
        
        self.survival_mode_game = pgui.elements.UIButton(relative_rect=pg.Rect(WINDOW_WIDTH-55, 5, 50, 25),
                                                               text="Pause", manager= self.ui_manager)
        
        self.lb_timer_text = pgui.elements.UILabel(relative_rect=pg.Rect(5, 5, 100, 30),
                                                   text="time:", manager=self.ui_manager)
        
        #hp
        self.pnl_hp_parent = pgui.elements.UIPanel(relative_rect=pg.Rect(125, 5, 60, 30),
                                                   manager=self.ui_manager,
                                                   visible=0)
        self.img_hp = pgui.elements.UIImage(relative_rect=pg.Rect(125, 5, 30, 30),
                                            image_surface=pg.image.load(os.path.join(IMAGE_PATH, "player/player.png")),
                                            parent_element=self.pnl_hp_parent,
                                            manager=self.ui_manager)
        self.lb_hp_text = pgui.elements.UILabel(relative_rect=pg.Rect(155, 5, 25, 30),
                                                text="", parent_element=self.pnl_hp_parent, manager=self.ui_manager)
        
        #shield
        self.pnl_shield_parent = pgui.elements.UIPanel(relative_rect=pg.Rect(185, 5, 60, 30),
                                                   manager=self.ui_manager,
                                                   visible=0)
        self.img_shield = pgui.elements.UIImage(relative_rect=pg.Rect(187, 7, 25, 25),
                                            image_surface=pg.image.load(os.path.join(IMAGE_PATH, "shield/shield.png")),
                                            parent_element=self.pnl_hp_parent,
                                            manager=self.ui_manager)
        self.lb_shield_text = pgui.elements.UILabel(relative_rect=pg.Rect(215, 5, 25, 30),
                                                text="", parent_element=self.pnl_hp_parent, manager=self.ui_manager)
        

        self.pnl_ultimate_parent = pgui.elements.UIPanel(relative_rect=pg.Rect(245, 5, 60, 30),
                                                   manager=self.ui_manager,
                                                   visible=0)
        self.img_ultimate = pgui.elements.UIImage(relative_rect=pg.Rect(247, 7, 25, 25),
                                            image_surface=pg.image.load(os.path.join(IMAGE_PATH, "ultimate/bomb.png")),
                                            parent_element=self.pnl_hp_parent,
                                            manager=self.ui_manager)
        self.lb_ultimate_text = pgui.elements.UILabel(relative_rect=pg.Rect(275, 5, 25, 30),
                                                text="", parent_element=self.pnl_hp_parent, manager=self.ui_manager)
        
        self.start_time = pg.time.get_ticks()
    
    def handle_event(self, event):
        self.ui_manager.process_events(event)
        if event.type == pgui.UI_BUTTON_PRESSED:
            if event.ui_element == self.survival_mode_game:
                self.manager.set_screen("menu")

    def update(self, dt, hp, sh, ult):
        elapsed = (pg.time.get_ticks() - self.start_time) // 1000
        self.lb_timer_text.set_text("time: " + str(elapsed) + "s")
        
        self.lb_hp_text.set_text(str(hp))
        self.lb_shield_text.set_text(str(sh))
        self.lb_ultimate_text.set_text(str(ult))
        
        self.ui_manager.update(dt)
    
    def draw(self, surface):
        self.ui_manager.draw_ui(surface)