# main.py
import pygame
from game.dinogame import DinoGame   # adjust if your file is named differently

pygame.init()

game = DinoGame()
running = True

while running:

    keys = pygame.key.get_pressed()
    action = 1 if keys[pygame.K_SPACE] else 0
    running = False if keys[pygame.K_q] else True

    if game.game_over:
        # game.reset()
        # game.game_over = False
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.game_over, _, _, _, score = game.step(action)

print("\n" * 5)
print("You achieved a score:", score)
print("\n" * 5)

pygame.quit()