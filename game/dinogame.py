# game/dino_game.py
import time
import random
import pygame
from .constants import *
from .cactus import Cactus
from .utils import load_image

class DinoGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Dino Game")
        self.clock = pygame.time.Clock()
        self.reset()

        print("\n" * 4)
        print("[DEBUG] Initialized Game")
        print("\n" * 4)

    # ---------- Sprite setup ----------
    def _load_sprites(self):
        print("[DEBUG] Loading and Resizing Sprites")
        self.player_img = load_image(DINO_IMG)
        self.player_running_img = load_image(DINO_RUNNING_IMG)
        self.cactus_img = load_image(CACTUS_IMG)
        self.font = pygame.font.Font(None, 36)

    def _place_sprites(self):
        print("[DEBUG] Placing sprites")
        self.player_pos = pygame.Vector2(-SCREEN_WIDTH * 5 / 6,
                                         SCREEN_HEIGHT - self.player_img.get_height() + 2)
        self.cactus_spawn = pygame.Vector2(SCREEN_WIDTH,
                                           SCREEN_HEIGHT * 2 / 3 + 40)

    # ---------- Reset ----------
    def reset(self):
        self.jumping = False
        self.y_velocity = JUMP_HEIGHT
        self.cactii_list = []
        self.cactus_timer = time.time()
        self.score = 0
        self.level_timer = time.time()
        self.cactus_speed = INITIAL_CACTUS_SPEED
        self.frame_iteration = 0
        self._load_sprites()
        self._place_sprites()

    # ---------- Render ----------
    def render(self):
        self.screen.fill("black")
        pygame.draw.rect(self.screen, "gray",
                         (0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50))
        score_surf = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_surf, (0, 0))

        player_img = self.player_running_img if self.jumping else self.player_img
        self.screen.blit(player_img, self.player_pos)

        for cactus in self.cactii_list:
            self.screen.blit(self.cactus_img, cactus.pos)

    # ---------- Move player ----------
    def move(self, action: int):
        print("[DEBUG] Action:", action)
        if action == 1 and not self.jumping:
            self.jumping = True

        if self.jumping:
            self.player_pos.y -= self.y_velocity
            self.y_velocity -= Y_GRAVITY
            if self.y_velocity < -JUMP_HEIGHT:
                self.jumping = False
                self.y_velocity = JUMP_HEIGHT

    # ---------- Step ----------
    def play_step(self, action: int):
        self.frame_iteration += 1
        dt = self.clock.tick(FPS) / 1000.0

        self.render()
        self.move(action)

        game_over = False

        # Spawn cactii
        if (len(self.cactii_list) < CACTII_LIMIT and
                time.time() - self.cactus_timer > random.choice(CACTUS_INTERVALS)):
            self.cactii_list.append(Cactus(self.cactus_spawn.x, self.cactus_spawn.y))
            self.cactus_timer = time.time()

        for cactus in self.cactii_list[:]:
            # Collision
            if cactus.pos.distance_to(self.player_pos) < COLLISION_THRESHOLD:
                print("[DEBUG] Collision Detected!")
                game_over = True
                break

            # Score
            if cactus.pos.x < self.player_pos.x and not cactus.scored:
                self.score += 1
                cactus.scored = True
                print(f"Score: {self.score}")

            # Remove off-screen
            if cactus.pos.x < -SCREEN_WIDTH:
                self.cactii_list.remove(cactus)
            else:
                cactus.pos.x -= self.cactus_speed * dt

        # Increase difficulty every 10 seconds
        if int(time.time() - self.level_timer) % 10 == 0 and int(time.time() - self.level_timer) > 0:
            self.cactus_speed += SPEED_INCREMENT
            print(f"[DEBUG] New speed: {self.cactus_speed}")
            self.level_timer = time.time()

        pygame.display.flip()
        print("[DEBUG] Cactii on field:", len(self.cactii_list))

        cactus_pos = self.cactii_list[0].pos if self.cactii_list else pygame.Vector2(0, 0)
        return game_over, self.score, cactus_pos