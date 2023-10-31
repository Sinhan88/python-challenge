import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))      # Win display
pygame.display.set_caption("Dodge The Obstacle")

BackGround = pygame.image.load("DP60WY.jpeg")       # Load image

class PlayerImage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_image          # Assign the loaded image
        self.rect = self.image.get_rect()  # Get the rectangle of the image