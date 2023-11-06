import pygame
import random
import sys
import time

pygame.init()                                                       # Initialize Pygame

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))                      # Set windows display
pygame.display.set_caption("Dodge The Obstacle")


BackGround = pygame.image.load("background.jpeg")                   # Load the image

clock = pygame.time.Clock()                                         # Create a Pygame clock object
start_time = pygame.time.get_ticks()                                # Get the start time (milliseconds)

# Game loop
running = True
while running:
    # Force quit windows
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
