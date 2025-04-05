import time
import pygame
import random


class DinoGame:

    def __init__(self):
        self.score = 0
        self.running = True
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.reset()

    class Cactus(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load('Cactus.png').convert()
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * 1, self.image.get_height() * 1))
            self.image.set_colorkey((0, 0, 0))  # Set black as transparent
            self.pos = pygame.Vector2(x, y)
            self.scored = False

    def reset(self):
        self.jumping = False
        self.Jump_Height = 18
        self.Y_velocity = self.Jump_Height
        self.Y_gravity = 1
        self.cactii_limit = 5
        self.cactii_list = []
        self.cactus_time = time.time()
        self.cactus_intervals = range(1, 30, 2)
        self.cactus_speed = 400
        self.score = 0
        self.level_time = time.time()
        self.load_sprites()
        self.place_sprites()
        self.frame_iteration = 0

    def load_sprites(self):
        print("Loading sprites!!")
        self.player = pygame.image.load('Dino.bmp').convert()
        self.player_runnning = pygame.image.load('Dino_Running.png').convert()
        new_size = (self.player.get_width() * 1, self.player.get_height() * 1)  # 2x bigger
        self.player = pygame.transform.scale(self.player, new_size)
        self.player_runnning = pygame.transform.scale(self.player_runnning, new_size)
        self.player.set_colorkey((0, 0, 0))
        self.player_runnning.set_colorkey((0, 0, 0))
        self.cactus = pygame.image.load('Cactus.png').convert()
        self.cactus = pygame.transform.scale(self.cactus, new_size)
        self.cactus.set_colorkey((0, 0, 0))
        self.font = pygame.font.Font(None, 36)
    
    def place_sprites(self):
        # Adjust player position to be within the visible screen area
        self.player_pos = pygame.Vector2(-self.screen.get_width() * 5/6,self.screen.get_height() - self.player.get_height() + 2)
        # Adjust cactus position to ensure it starts on-screen
        self.cactus_pos = pygame.Vector2(self.screen.get_width(), self.screen.get_height() * 2 / 3 + 40)
    
    def play_step(self, action):
        self.frame_iteration += 1

        # Collect user input 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # Render the game (Issue with rendering the charactyers)
        self.render()



        # Move the player
        self.move(action)

        # Check if game over and update cactii
        reward = 0
        game_over = False
        # Cactus
        dt = self.clock.tick(60) / 1000
        for i in self.cactii_list:
            # Collision Detection
            if i.pos.distance_to(self.player_pos) < 44:
                print("Collision Detected!")
                game_over = True
                return game_over, self.score
            elif i.pos.x - self.player_pos.x < 0 and not i.scored:
                self.score += 1
                i.scored = True
                print(f"Score: {self.score}")
                print(f"Time = {time.time() - self.level_time}")
            # Removing out of border cactus
            elif i.pos.x < -self.screen.get_width():
                self.cactii_list.remove(i)
            # Moving cactii
            else:
                i.pos.x -= self.cactus_speed * dt
        
        # Spawning new cactii
        if len(self.cactii_list) < self.cactii_limit and time.time() - self.cactus_time > random.choice(self.cactus_intervals):
            self.cactii_list.append(self.Cactus(self.cactus_pos.x, self.cactus_pos.y))
            self.cactus_time = time.time()
    

        # Increasing difficulty
        if time.time() - self.level_time % 10 == 0:
            self.cactus_speed += 400
            print(f"New Speed: {self.cactus_speed}")
            self.level_time = time.time()
        
        pygame.display.flip()
    
    def render(self):
        # Background
        self.screen.fill("black") 
        pygame.draw.rect(self.screen, "gray", (0, self.screen.get_height() - 50, self.screen.get_width(), 50))
        text = self.font.render(f"Score: {self.score}", True, (255,255,255))
        self.screen.blit(text, (0, 0))
        
        # Render player at the correct position
        if self.jumping:
            print("This is being rendered")
            self.screen.blit(self.player_runnning, self.player_pos)
        else:
            print("This is being rendered")
            self.screen.blit(self.player, self.player_pos)
            print(f"The player is present at {self.player_pos}")
        
        # Render cactii at their correct positions
        for cactus in self.cactii_list:
            self.screen.blit(self.cactus, cactus.pos)

    def move(self, action):
        if action == 1:
            self.jumping = True
        
        # Update player position
        if self.jumping:
            self.player_pos.y -= self.Y_velocity
            self.Y_velocity -= self.Y_gravity
            if self.Y_velocity < -self.Jump_Height:
                self.jumping = False
                self.Y_velocity = self.Jump_Height



if __name__ == "__main__":
    pygame.init()
    game = DinoGame()
    while game.running:
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            game.play_step(1)
        else:
            game.play_step(0)
        if not game.running:
            break
    pygame.quit()