# game/cactus.py
import pygame
from .constants import CACTUS_IMG

class Cactus(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float):
        super().__init__()
        from .utils import load_image
        self.image = load_image(CACTUS_IMG)
        self.pos = pygame.Vector2(x, y)
        self.scored = False
        