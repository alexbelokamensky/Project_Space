import pygame
import pygame_gui
import os

from core.config import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, FPS, IMAGE_PATH
from interface.screens.main_menu_screen import MainMenuScreen
from interface.screens.survival_mode_screen import SurvivalModeScreen
from controllers.screen_controller import ScreenController

pygame.init()

pygame.display.set_caption(WINDOW_TITLE)
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

screenController = ScreenController()
screenController.add_screen("menu", MainMenuScreen(screenController))
screenController.add_screen("survival", SurvivalModeScreen(screenController))
screenController.set_screen("menu")

clock = pygame.time.Clock()
is_running = True

while is_running:
    dt = clock.tick(FPS)/200.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
                
        screenController.handle_event(event)
    
    screenController.update(dt)
    screenController.draw(window_surface)

    pygame.display.update()