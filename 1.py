import pygame
import random
import sys
import time

pygame.init()                                                       # Initialize Pygame

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))                      # Set windows display
pygame.display.set_caption("Dodge The Obstacle")


BackGround = pygame.image.load("background.jpeg")                       # Load the image
sprite_image = pygame.image.load("player.png")

sprite_image = pygame.transform.scale(sprite_image, (50, 70))       # Sprite scale setting

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
        if keys[pygame.K_a] and self.rect.left > 0:                 # Left key and boundary
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < WIDTH:            # Right key and boundary
            self.rect.x += self.speed

my_sprite = PlayerImage()                                           # Create an instance of your custom sprite
all_sprites = pygame.sprite.Group()
all_sprites.add(my_sprite)                                          # Add the sprite to the group

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
    all_sprites.update()

    # Draw sprite or other object
    WIN.blit(BackGround, (0, 0))
    all_sprites.draw(WIN)

    # Time code (Elapsed time)
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000               # Convert to seconds
    font = pygame.font.Font(None, 36)
    text = font.render(f"Time: {elapsed_time}", True, (255, 255, 255))
    WIN.blit(text, (10, 10))

    pygame.display.flip()

    # Limit the frame rate to 60 frames per second (FPS)
    clock.tick(144)

pygame.quit()                                                        # Quit pygame
#