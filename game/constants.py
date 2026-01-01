# game/constants.py
import pygame
import os 

# Window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Physics
JUMP_HEIGHT = 18
Y_GRAVITY = 1
COLLISION_THRESHOLD = 35

# Cactus spawning
CACTII_LIMIT = 10
CACTUS_INTERVALS = range(1, 5)
INITIAL_CACTUS_SPEED = 400
SPEED_INCREMENT = 200



# Absolute base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Image paths (now absolute)
DINO_IMG         = os.path.join(BASE_DIR, "images", "Dino.bmp")
DINO_RUNNING_IMG = os.path.join(BASE_DIR, "images", "Dino_running.png")
CACTUS_IMG       = os.path.join(BASE_DIR, "images", "Cactus.png")
