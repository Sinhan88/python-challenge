import pygame
import random                                                       # Import library
import sys
import time

pygame.init()                                                       # Initialize Pygame

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))                      # Set windows display
pygame.display.set_caption("Dodge The Obstacle")


BackGround = pygame.image.load("background.jpeg")                       # Load the image
sprite_image = pygame.image.load("player.png")

sprite_image = pygame.transform.scale(sprite_image, (50, 70))       # Sprite scale setting
best_time = float('inf')

class PlayerImage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_image                                   # Assign the loaded image
        self.rect = self.image.get_rect()                           # Get the rectangle of the image
        self.speed = 3                                              # Movement speed
        self.rect.centerx = WIDTH // 2                              # Start at the horizontal center of the screen
        self.rect.bottom = HEIGHT                                   # Start at the bottom of the screen                     

    def update(self):
        keys = pygame.key.get_pressed()    
        # Left key and boundary
        if keys[pygame.K_a] and self.rect.left > 0:                 
            self.rect.x -= self.speed
        # Right key and boundary
        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, all_obstacles):
        super().__init__()
        self.width = random.randint(30, 70)                         # Generate random width for the obstacle
        self.height = random.randint(30, 70)                        # Generate random height for the obstacle
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 255, 255))                            # Obstacle color
        self.rect = self.image.get_rect()                           # Rect form 
        self.rect.x, self.rect.y = self.generate_non_overlapping_position(all_obstacles)
        self.speed = 5                                              # Set the initial speed of the obstacle

    def generate_non_overlapping_position(self, all_obstacles):
        while True:
            x = random.randint(0, WIDTH - self.rect.width)
            y = random.randint(-100, -50)
            self.rect.topleft = (x, y)
            if not any(self.rect.colliderect(obstacle.rect) for obstacle in all_obstacles):
                return x, y

    def update(self):
        self.rect.y += self.speed
        # If the obstacle goes off the screen, reset its position
        if self.rect.top > HEIGHT:                                  
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -50)

        # Check for collision with the player
        if pygame.sprite.spritecollide(self, all_sprites, False):
            global running                                          # Set the game over flag
            running = False                                         

my_sprite = PlayerImage()                                           # Create an instance of your custom sprite
all_sprites = pygame.sprite.Group()
all_sprites.add(my_sprite)                                          # Add the sprite to the group

obstacles = pygame.sprite.Group()                                   # Create a group for obstacles
# Add some initial obstacles to the group
for _ in range(7):                                                  # Add a number of obstacles that can be appear on 1 wave 
    obstacle = Obstacle(obstacles)
    obstacles.add(obstacle)

clock = pygame.time.Clock()                                         # Create a Pygame clock object
start_time = pygame.time.get_ticks()                                # Get the start time (milliseconds)

# Game loop
running = True
while running:
    # Force quit windows
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update or perform any game logic
    if running:
        all_sprites.update()                                         # Sprite update
        obstacles.update()                                           # Obstacles update

    # Draw object so it can be seen on the screen
    WIN.blit(BackGround, (0, 0))
    all_sprites.draw(WIN)                                            # Sprite draw
    obstacles.draw(WIN)                                              # Obstacles draw

    # Check for collisions
    if running:
        collisions = pygame.sprite.spritecollide(my_sprite, obstacles, False)
        if collisions:                                               # Set the game over flag
            running = False  

    # Time code (Elapsed time)
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000               # Convert to seconds
    font = pygame.font.Font(None, 36)
    text = font.render(f"Time: {elapsed_time}", True, (255, 255, 255))
    WIN.blit(text, (10, 10))

    # Check for record to be break
    if elapsed_time < best_time:
        best_time = elapsed_time

    # Display the best time on the screen
    best_time_text = font.render(f"Best Time: {best_time}", True, (255, 255, 255))
    WIN.blit(best_time_text, (10, 50))  

    pygame.display.flip()
    clock.tick(100)                                                  # Limit the frame rate to 100 frames per second (FPS)
                                         
# Game over message
font = pygame.font.Font(None, 72)
text = font.render("Game Over", True, (255, 0, 0))                   # Red "Game Over" text
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))          # Center the text
WIN.blit(text, text_rect)
pygame.display.flip()

time.sleep(1)                                                        # Wait for a few seconds before quitting

pygame.quit()                                                        # Quit pygame
#