import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge The Obstacle")

BackGround = pygame.image.load("background.jpeg")
sprite_image = pygame.image.load("player.png")

sprite_image = pygame.transform.scale(sprite_image, (50, 70))
start_time = 0

obstacle_image = pygame.image.load("obstacle.png")
obstacle_image = pygame.transform.scale(obstacle_image, (50, 50))

class PlayerImage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_image
        self.rect = self.image.get_rect()
        self.speed = 3
        self.rect.centerx = WIDTH // 2
        self.initial_height = HEIGHT - 150
        self.rect.bottom = self.initial_height

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, all_obstacles, obstacle_image):
        super().__init__()
        self.image = obstacle_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.generate_non_overlapping_position(all_obstacles)
        self.speed = 5
        self.speed_increment = 0.001

    def generate_non_overlapping_position(self, all_obstacles):
        while True:
            x = random.randint(0, WIDTH - self.rect.width)
            y = random.randint(-100, -50)
            self.rect.topleft = (x, y)
            if (
                not any(self.rect.colliderect(obstacle.rect) for obstacle in all_obstacles)
                and not self.rect.colliderect(my_sprite.rect)
            ):
                return x, y

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -50)

        if pygame.sprite.spritecollide(self, all_sprites, False):
            global running
            running = False

        self.speed += self.speed_increment

def generate_random_obstacle_size():
    size = random.randint(50, 70)
    return pygame.transform.scale(obstacle_image, (size, size))

my_sprite = PlayerImage()
all_sprites = pygame.sprite.Group()
all_sprites.add(my_sprite)

obstacles = pygame.sprite.Group()

for _ in range(7):
    obstacle = Obstacle(obstacles, generate_random_obstacle_size())
    obstacles.add(obstacle)

clock = pygame.time.Clock()

running = False

def main_menu():
    global running
    menu_font = pygame.font.Font(None, 72)
    menu_text = menu_font.render("Dodge The Obstacle", True, (255, 255, 255))
    menu_text_rect = menu_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

    play_text = menu_font.render("Press 'Space' to Play", True, (255, 255, 255))
    play_text_rect = play_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    WIN.blit(BackGround, (0, 0))
    WIN.blit(menu_text, menu_text_rect)
    WIN.blit(play_text, play_text_rect)
    pygame.display.update()

    waiting_for_space = True
    while waiting_for_space:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting_for_space = False
                running = True

def main():
    global running, start_time
    play_again = True

    while play_again:
        main_menu()

        start_time = pygame.time.get_ticks()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            Game_Loop()

        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, (255, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        WIN.blit(text, text_rect)
        pygame.display.flip()

        play_again_font = pygame.font.Font(None, 36)
        play_again_text = play_again_font.render("Press 'R' to play again", True, (255, 255, 255))
        play_again_text_rect = play_again_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        WIN.blit(play_again_text, play_again_text_rect)
        pygame.display.flip()

        waiting_for_restart = True
        while waiting_for_restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play_again = False
                    waiting_for_restart = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        play_again = True
                        waiting_for_restart = False
                        my_sprite.rect.centerx = WIDTH // 2
                        my_sprite.rect.bottom = my_sprite.initial_height
                        obstacles.empty()
                        for _ in range(7):
                            obstacle = Obstacle(obstacles, generate_random_obstacle_size())
                            obstacles.add(obstacle)

        pygame.time.delay(500)

    pygame.quit()

def Game_Loop():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if running:
        all_sprites.update()
        obstacles.update()

        WIN.blit(BackGround, (0, 0))
        all_sprites.draw(WIN)
        obstacles.draw(WIN)

        if running:
            collisions = pygame.sprite.spritecollide(my_sprite, obstacles, False)
            if collisions:
                running = False

        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) // 1000
        font = pygame.font.Font(None, 36)
        text = font.render(f"Time: {elapsed_time}", True, (255, 255, 255))
        WIN.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
