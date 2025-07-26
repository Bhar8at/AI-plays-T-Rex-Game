# game/utils.py
import pygame

def load_image(path, scale_factor=1, colorkey=(0, 0, 0)):
    img = pygame.image.load(path).convert()
    w, h = img.get_width() * scale_factor, img.get_height() * scale_factor
    img = pygame.transform.scale(img, (int(w), int(h)))
    img.set_colorkey(colorkey)
    return img