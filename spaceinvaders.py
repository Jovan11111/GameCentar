import pygame
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5
ENEMY_SPEED = 0.2
BULLET_SPEED = 10
LEVEL = 1
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)


def spaceinvadersGame():
    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders Game")

    font = pygame.font.Font(None, 48)
    gameMode = 1
    while True:
        if gameMode == 1:
            startScreen(screen, font)
        winner = gameLoop(screen)
        gameMode = endScreen(screen, font, winner)


def startScreen(screen, font):
    global LEVEL
    j = d = t = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return
        if keys[pygame.K_q]:
            pygame.quit()
            quit()
        if keys[pygame.K_1]:
            j = True
            d = t = False
            LEVEL = 1
        if keys[pygame.K_2]:
            d = True
            j = t = False
            LEVEL = 2
        if keys[pygame.K_3]:
            t = True
            j = d = False
            LEVEL = 3
        if keys[pygame.K_s]:
            pygame.quit()
            from main import main
            main()

        screen.fill(BLACK)

        screen.blit(font.render("Welcome to space invaders game!", True, WHITE), (10, 80))
        if j:
            screen.blit(font.render("To select level 1, press 1", True, YELLOW), (10, 120))
        else:
            screen.blit(font.render("To select level 1, press 1", True, WHITE), (10, 120))
        if d:
            screen.blit(font.render("To select level 2, press 2", True, ORANGE), (10, 160))
        else:
            screen.blit(font.render("To select level 2, press 2", True, WHITE), (10, 160))
        if t:
            screen.blit(font.render("To select level 3, press 3", True, RED), (10, 200))
        else:
            screen.blit(font.render("To select level 3, press 3", True, WHITE), (10, 200))

        screen.blit(font.render("To start, press SPACE", True, WHITE), (10, 240))
        screen.blit(font.render("To go back to game select, press S", True, WHITE), (10, 280))
        screen.blit(font.render("To quit, press Q", True, WHITE), (10, 320))

        pygame.display.flip()


def endScreen(screen, font, winner):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            return 2
        if keys[pygame.K_m]:
            return 1
        if keys[pygame.K_q]:
            pygame.quit()
            quit()

        screen.fill(BLACK)

        if winner == 1:
            screen.blit(font.render("Game over! You won!", True, WHITE), (10, 80))
        else:
            screen.blit(font.render("Game over! You lost!", True, WHITE), (10, 80))
        screen.blit(font.render("To restart, press R", True, WHITE), (10, 120))
        screen.blit(font.render("To go to menu, press M", True, WHITE), (10, 160))
        screen.blit(font.render("To quit, press Q", True, WHITE), (10, 200))

        pygame.display.flip()


def gameLoop(screen):
    # Player
    player_width = 50
    player_height = 50
    player_x = (WIDTH - player_width) // 2
    player_y = HEIGHT - player_height - 20

    # Enemies
    enemy_width = 60
    enemy_height = 40
    enemies = []
    enemy_colors = []

    # Bullets
    bullet_width = 10
    bullet_height = 20
    bullets = []

    # Create enemies
    for i in range(10):
        for j in range(6):
            x = i * (enemy_width + 18)
            y = j * (enemy_height + 10)
            enemies.append([x + 20, y])
            if LEVEL == 1:
                enemy_colors.append(YELLOW)
            elif LEVEL == 2:
                if j > 2:
                    enemy_colors.append(YELLOW)
                else:
                    enemy_colors.append(ORANGE)
            else:
                if j > 3:
                    enemy_colors.append(YELLOW)
                elif j > 1:
                    enemy_colors.append(ORANGE)
                else:
                    enemy_colors.append(RED)
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet_x = player_x + player_width // 2 - bullet_width // 2
                    bullet_y = player_y
                    bullets.append([bullet_x, bullet_y])

        # Move the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player_x + player_width < WIDTH:
            player_x += PLAYER_SPEED

        # Move bullets
        for bullet in bullets:
            bullet[1] -= BULLET_SPEED

        # Check for bullet-enemy collisions
        for bullet in bullets:
            for i, enemy in enumerate(enemies):
                if (
                        enemy[0] - 10 <= bullet[0] <= enemy[0] + enemy_width
                        and enemy[1] <= bullet[1] <= enemy[1] + enemy_height
                ):
                    if enemy_colors[i] == YELLOW:
                        bullets.remove(bullet)
                        enemies.remove(enemy)
                        del enemy_colors[i]
                    elif enemy_colors[i] == ORANGE:
                        bullets.remove(bullet)
                        enemy_colors[i] = YELLOW
                    else:
                        bullets.remove(bullet)
                        enemy_colors[i] = ORANGE

        # Update the screen
        screen.fill(BLACK)

        # Draw player
        pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

        # Draw enemies
        for i, enemy in enumerate(enemies):
            pygame.draw.rect(screen, enemy_colors[i], (enemy[0], enemy[1], enemy_width, enemy_height))

        for enemy in enemies:
            enemy[1] += ENEMY_SPEED

        # Draw bullets
        for bullet in bullets:
            pygame.draw.rect(screen, BLUE, (bullet[0], bullet[1], bullet_width, bullet_height))

        pygame.display.update()

        if len(enemies) == 0:
            time.sleep(1)
            return 1

        pygame.time.Clock().tick(60)
