import os

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Project Space"
FPS = 120

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
RES_PATH = os.path.join(BASE_PATH, "resources")
IMAGE_PATH = os.path.join(RES_PATH, "images")
SOUND_PATH = os.path.join(RES_PATH, "sounds")
LEVEL_PATH = os.path.join(RES_PATH, "levels")

PLAYER_MAX_HP = 5