import pygame
import random
import sys
import time

pygame.font.init()
pygame.init()

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))      # Win display
pygame.display.set_caption("Dodge The Obstacle")

screen = pygame.image.load("DP60WY.jpeg")           # Load image
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

sprite_group = pygame.sprite.Group()        #Create a group
my_sprite = PlayerImage()

all_sprite = pygame.sprite.Group()          # Create an instance of your sprite
all_sprite.add(my_sprite)                   # Add the sprite to the group

running = True
player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
# Game loop
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    all_sprite.update()
    pygame.display.update()

    # Game Draw
    all_sprite.draw(screen)

    




if __name__ == "__main__":
    main()