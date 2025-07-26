# game/cactus.py
import pygame

class Cactus(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float):
        super().__init__()
        from .utils import load_image
        self.image = load_image("images/Cactus.png")
        self.pos = pygame.Vector2(x, y)
        self.scored = False
        