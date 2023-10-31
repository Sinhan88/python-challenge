import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))      # Win display
pygame.display.set_caption("Dodge The Obstacle")


BackGround = pygame.image.load("DP60WY.jpeg")       # Load image
sprite_image = pygame.image.load("sprite.png")

class PlayerImage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_image          # Assign the loaded image
        self.rect = self.image.get_rect()  # Get the rectangle of the image
        self.speed = 5                     # Movement speed

    def update(self):                      # Movement key
        keys = pygame.key.get_pressed()    
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

my_sprite = PlayerImage()                  # Create an instance of your custom sprite
all_sprites = pygame.sprite.Group()
all_sprites.add(my_sprite)                 # Add the sprite to the group

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update your sprite or perform any game logic
    all_sprites.update()

    # Draw
    WIN.blit(BackGround, (0, 0))
    all_sprites.draw(WIN)

    pygame.display.flip()

pygame.quit()