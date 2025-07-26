# main.py
import pygame
from game.dinogame import DinoGame   # adjust if your file is named differently

pygame.init()

game = DinoGame()
game_over = False
running = True

while running and not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    action = 1 if keys[pygame.K_SPACE] else 0

    game_over, score, _ = game.play_step(action)

print("\n" * 5)
print("You achieved a score:", score)
print("\n" * 5)

pygame.quit()