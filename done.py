import pygame
import random
import sys
import time

pygame.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge The Obstacle")

BackGround = pygame.image.load("DP60WY.jpeg")
sprite_image = pygame.image.load("sprite.png")
obstacle_image = pygame.image.load("meteor.png")

sprite_image = pygame.transform.scale(sprite_image, (50, 70))

class PlayerImage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_image
        self.rect = self.image.get_rect()
        self.speed = 3
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, all_obstacles):
        super().__init__()
        self.width = random.randint(30, 70)
        self.height = random.randint(30, 70)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.generate_non_overlapping_position(all_obstacles)
        self.speed = 5

    def generate_non_overlapping_position(self, all_obstacles):
        while True:
            x = random.randint(0, WIDTH - self.rect.width)
            y = random.randint(-100, -50)
            self.rect.topleft = (x, y)
            if not any(self.rect.colliderect(obstacle.rect) for obstacle in all_obstacles):
                return x, y

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -50)

        if pygame.sprite.spritecollide(self, all_sprites, False):
            global game_over
            game_over = True

def reset_game():
    global game_over
    all_sprites.empty()
    obstacles.empty()
    my_sprite.rect.centerx = WIDTH // 2
    my_sprite.rect.bottom = HEIGHT
    game_over = False

    all_sprites.add(my_sprite)
    for _ in range(10):
        obstacle = Obstacle(obstacles)
        obstacles.add(obstacle) 

my_sprite = PlayerImage()
all_sprites = pygame.sprite.Group()
all_sprites.add(my_sprite)

obstacles = pygame.sprite.Group()
for _ in range(10):
    obstacle = Obstacle(obstacles)
    obstacles.add(obstacle)

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                reset_game()

    if not game_over:  
        all_sprites.update()
        obstacles.update()

    WIN.blit(BackGround, (0, 0))
    all_sprites.draw(WIN)
    obstacles.draw(WIN)

    if not game_over: 
        collisions = pygame.sprite.spritecollide(my_sprite, obstacles, False)
        if collisions:
            game_over = True

    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000
    font = pygame.font.Font(None, 36)
    text = font.render(f"Time: {elapsed_time}", True, (255, 255, 255))
    WIN.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(100)

    if game_over:
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over - Press R to Restart", True, (255, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        WIN.blit(text, text_rect)
        pygame.display.flip()

    if game_over:
        time.sleep(1)

pygame.quit()
