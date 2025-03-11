import pygame

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Shooter")

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

player_x = 350
player_y = 500
player_width = 50
player_height = 40

enemy_x = 400
enemy_y = 100
enemy_radius = 25

bullet_x = player_x + player_width // 2
bullet_y = player_y
bullet_width = 10
bullet_height = 20
bullet_speed = 10
bullet_active = False

game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not bullet_active and not game_over:
                bullet_active = True
                bullet_x = player_x + player_width // 2
                bullet_y = player_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0 and not game_over:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < width - player_width and not game_over:
        player_x += 5

    if bullet_active:
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_active = False

    #Collision Detection
    if bullet_active:
        distance = ((bullet_x + bullet_width//2 - enemy_x)**2 + (bullet_y + bullet_height//2 - enemy_y)**2)**0.5
        if distance < enemy_radius + bullet_width//2:
            game_over = True
            bullet_active = False


    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))
    pygame.draw.circle(screen, red, (enemy_x, enemy_y), enemy_radius)
    if bullet_active:
        pygame.draw.rect(screen, green, (bullet_x, bullet_y, bullet_width, bullet_height))

    #Display Game Over message
    if game_over:
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over!", True, red)
        text_rect = text.get_rect(center=(width//2, height//2))
        screen.blit(text, text_rect)

    pygame.display.update()

pygame.quit()
