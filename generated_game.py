import pygame
import random


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

player_width = 50
player_height = 40
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

bullet_width = 10
bullet_height = 20
bullet_speed = 7
bullets = []

enemy_radius = 25
enemy_speed = 2
num_enemies = 5
enemies = [{"x": random.randint(50, WIDTH - 50), "y": random.randint(50, 300)} for _ in range(num_enemies)]

score = 0
font = pygame.font.Font(None, 36)
game_over = False

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bullets.append({"x": player_x + player_width // 2 - bullet_width // 2, "y": player_y})
            if event.key == pygame.K_r and game_over:
                game_over = False
                score = 0
                player_x = WIDTH // 2 - player_width // 2
                bullets.clear()
                enemies = [{"x": random.randint(50, WIDTH - 50), "y": random.randint(50, 300)} for _ in range(num_enemies)]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0 and not game_over:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width and not game_over:
        player_x += player_speed

    for bullet in bullets:
        bullet["y"] -= bullet_speed
    bullets = [bullet for bullet in bullets if bullet["y"] > 0]  

    for enemy in enemies:
        enemy["y"] += enemy_speed
        if enemy["y"] > HEIGHT:
            enemy["y"] = random.randint(-100, -40)
            enemy["x"] = random.randint(50, WIDTH - 50)

    for bullet in bullets:
        for enemy in enemies:
            distance = ((bullet["x"] + bullet_width // 2 - enemy["x"]) ** 2 + (bullet["y"] - enemy["y"]) ** 2) ** 0.5
            if distance < enemy_radius + bullet_width // 2:
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 10
                break

    for enemy in enemies:
        if enemy["y"] + enemy_radius >= player_y:
            game_over = True

    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    for bullet in bullets:
        pygame.draw.rect(screen, GREEN, (bullet["x"], bullet["y"], bullet_width, bullet_height))

    for enemy in enemies:
        pygame.draw.circle(screen, RED, (enemy["x"], enemy["y"]), enemy_radius)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    if game_over:
        game_over_text = pygame.font.Font(None, 72).render("Game Over!", True, RED)
        restart_text = font.render("Press 'R' to Restart", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
        screen.blit(restart_text, (WIDTH // 2 - 100, HEIGHT // 2 + 20))

    pygame.display.update()
    pygame.time.delay(30)  

pygame.quit()
