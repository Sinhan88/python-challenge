import pygame
import sys

# Initialize Pygame
pygame.init()

running = True
# Load sprite image
sprite_image = pygame.image.load("sprite.png")

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Set the image and rect attributes
        self.image = sprite_image  # Assign the loaded image
        self.rect = self.image.get_rect()  # Get the rectangle of the image

# Create a sprite group
sprite_group = pygame.sprite.Group()

# Create an instance of your sprite and add it to the group
my_sprite = MySprite()
sprite_group.add(my_sprite)

clock = pygame.time.Clock()
# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprite(s)
    sprite_group.update()

    # Drawing code
    BackGround = pygame.image.load("DP60WY.jpeg")
    sprite_group.draw(BackGround)

    WIDTH, HEIGHT = 1000, 800
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("GAME")
    clock.tick(144)

