import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge The Obstacle")

BackGround = pygame.image.load("DP60WY.jpeg")
sprite_image = pygame.image.load("sprite.png")

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VELOCITY = 5

PROJECTILE_WIDTH = 10
PROJECTILE_HEIGHT = 20
PROJECTILE_VELOCITY = 3

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, projectiles):
    WIN.blit(BackGround, (0, 0))

    time_text = FONT.render(f"Time : {round(elapsed_time)}s", 1, "WHITE")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "RED", player)

    for projectile in projectiles:
        pygame.draw.rect(WIN, "WHITE", projectile)

    pygame.display.update()

def main(): 
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    projectile_add_increment = 2000
    projectile_count = 0
    projectiles = []
    hit = False

    while run:
        projectile_count += clock.tick(144)
        elapsed_time = time.time()- start_time

        if projectile_count > projectile_add_increment:
            for _ in range(3):
                projectile_x = random.randint(0, WIDTH - PROJECTILE_WIDTH)
                projectile = pygame.Rect(projectile_x, PROJECTILE_HEIGHT, PROJECTILE_WIDTH, PROJECTILE_HEIGHT)
                projectiles.append(projectile)

            projectile_add_increment = max(200, projectile_add_increment - 50)
            projectile_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_d] and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
            player.x += PLAYER_VELOCITY 

        for projectile in projectiles[:]:
            projectile.y += PROJECTILE_VELOCITY
            if projectile.y > HEIGHT:
                projectiles.remove(projectile)
            elif projectile.y + projectile.height >= player.y and projectile.colliderect(player):
                projectiles.remove(projectile)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1, "WHITE")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, projectiles)

    pygame.quit()

if __name__ == "__main__":
    main()


