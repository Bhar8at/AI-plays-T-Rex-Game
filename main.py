from game import DinoGame
import pygame

game = DinoGame()

# Loading sprites
game.reset()

while True:
     ## Keyboard input and Rendering
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_SPACE]:
        game.play_step(1)
    elif keys_pressed[pygame.K_q]:
        pygame.quit()
    else:
        game.play_step(0)
