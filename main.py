import pygame
import time
import random



# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

## Agent
# reset
# reward
# play(action) -> state
# game_iteration


# Game Variables
jumping = False
Jump_Height = 18
Y_velocity = Jump_Height
Y_gravity = 1
cactii_limit  = 5
cactii_list = []
cactus_time = time.time()
cactus_intervals = range(1,10,2)
cactus_speed = 400
score = 0
level_time = time.time()
# Cactus

class Cactus(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('Cactus.png').convert()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 1, self.image.get_height() * 1))
        self.image.set_colorkey((0, 0, 0))  # Set black as transparent
        self.pos = pygame.Vector2(x, y)
        self.scored = False


# Loading and Transforming Sprites
player = pygame.image.load('Dino.bmp').convert()
player_runnning = pygame.image.load('Dino_Running.png').convert()
player_pos = pygame.Vector2(-screen.get_width() * 5/6,screen.get_height() - player.get_height() + 2)
new_size = (player.get_width() * 1, player.get_height() * 1)  # 2x bigger
player = pygame.transform.scale(player, new_size)
player_runnning = pygame.transform.scale(player_runnning, new_size)
player.set_colorkey((0, 0, 0))  # Set black as transparent
player_runnning.set_colorkey((0, 0, 0))  # Set black as transparent
cactus = pygame.image.load('Cactus.png').convert()
cactus_pos = pygame.Vector2(100,screen.get_height()*2/3 + 40)
cactus = pygame.transform.scale(cactus, new_size)
cactus.set_colorkey((0, 0, 0))  # Set black as transparent
font = pygame.font.Font(None, 36)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    ## Keyboard input and Rendering
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_SPACE]:
        jumping = True
    # Background
    screen.fill("black") 
    pygame.draw.rect(screen, "gray", (0, screen.get_height() - 50, screen.get_width(), 50))
    text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(text, (0, 0))
    # Player
    if jumping:
        player_pos.y -= Y_velocity
        Y_velocity -= Y_gravity
        if Y_velocity < -Jump_Height:
            jumping = False
            Y_velocity = Jump_Height
        # Player (Walking)
        screen.blit(player_runnning, player_pos)
    else:
        # Player (Standing)
        screen.blit(player, player_pos)
        
    # Cactus
    dt = clock.tick(60) / 1000
    for i in cactii_list:
        # Collision Detection
        if i.pos.distance_to(player_pos) < 44:
            print("Collision Detected!")
            running = False
        elif i.pos.x - player_pos.x < 0 and not i.scored:
            score += 1
            i.scored = True
            print(f"Score: {score}")
            print(f"Time = {time.time() - level_time}")
        # Removing out of border cactus
        elif i.pos.x < -screen.get_width():
            cactii_list.remove(i)
        # Moving cactii
        else:
            screen.blit(cactus, i.pos)
            i.pos.x -= cactus_speed * dt
    
    
    # Spawning new cactii
    if len(cactii_list) < cactii_limit and time.time() - cactus_time > random.choice(cactus_intervals):
        cactii_list.append(Cactus(cactus_pos.x, cactus_pos.y))
        cactus_time = time.time()
    

    # Increasing difficulty
    if time.time() - level_time % 10 == 0:
        cactus_speed += 400
        print(f"New Speed: {cactus_speed}")
        level_time = time.time()



    # flip() the display to put your work on screen
    pygame.display.flip()

    
    

pygame.quit()