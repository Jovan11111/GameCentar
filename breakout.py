import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LEVEL = 1
BALL_SPEED = 0.1
PADDLE_SPEED = 0.2
BRICK_WIDTH = 60
BRICK_HEIGHT = 20
NUM_BRICKS_X = 9
NUM_BRICKS_Y = 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)


def breakoutGame():
    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Breakout")

    font = pygame.font.Font(None, 48)
    gameMode = 1
    while True:
        if gameMode == 1:
            startScreen(screen, font)
        winner = gameLoop(screen)
        gameMode = endScreen(winner, screen, font)


def startScreen(screen, font):
    j = d = t = e = m = h = False
    global BALL_SPEED
    global PADDLE_SPEED
    global LEVEL
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
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

        if keys[pygame.K_e]:
            e = True
            m = h = False
            BALL_SPEED = 0.1

        if keys[pygame.K_m]:
            m = True
            e = h = False
            BALL_SPEED = 0.25

        if keys[pygame.K_h]:
            h = True
            m = e = False
            BALL_SPEED = 0.4
            PADDLE_SPEED = 0.3

        if keys[pygame.K_SPACE]:
            if (j or d or t) and (e or m or h):
                return

        if keys[pygame.K_q]:
            pygame.quit()
            quit()

        if keys[pygame.K_s]:
            pygame.quit()
            from main import main
            main()

        screen.fill(BLACK)

        screen.blit(font.render("Welcome to Breakout game!", True, WHITE), (10, 80))
        if j:
            screen.blit(font.render("For level 1, select 1", True, GREEN), (10, 120))
        else:
            screen.blit(font.render("For level 1, select 1", True, WHITE), (10, 120))
        if d:
            screen.blit(font.render("For level 2, select 2", True, GREEN), (10, 160))
        else:
            screen.blit(font.render("For level 2, select 2", True, WHITE), (10, 160))
        if t:
            screen.blit(font.render("For level 3, select 3", True, GREEN), (10, 200))
        else:
            screen.blit(font.render("For level 3, select 3", True, WHITE), (10, 200))
        if e:
            screen.blit(font.render("For easy mode, press E", True, RED), (10, 240))
        else:
            screen.blit(font.render("For easy mode, press E", True, WHITE), (10, 240))
        if m:
            screen.blit(font.render("For medium mode, press M", True, RED), (10, 280))
        else:
            screen.blit(font.render("For medium mode, press M", True, WHITE), (10, 280))
        if h:
            screen.blit(font.render("For hard mode, press H", True, RED), (10, 320))
        else:
            screen.blit(font.render("For hard mode, press H", True, WHITE), (10, 320))

        screen.blit(font.render("To start the game, press SPACE", True, WHITE), (10, 360))
        screen.blit(font.render("To go back to game select, press S", True, WHITE), (10, 400))
        screen.blit(font.render("To quit, press Q", True, WHITE), (10, 440))

        pygame.display.flip()


def endScreen(winner, screen, font):
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
            screen.blit(font.render("Game over! You lost!", True, WHITE), (10, 80))
        if winner == 2:
            screen.blit(font.render("Game over! You won!", True, WHITE), (10, 80))
        screen.blit(font.render("To restart the same settings, press R", True, WHITE), (10, 120))
        screen.blit(font.render("To go to menu, press M", True, WHITE), (10, 160))
        screen.blit(font.render("To quit, press Q", True, WHITE), (10, 200))

        pygame.display.flip()


def gameLoop(screen):
    # Bricks
    bricks = []
    brick_colors = []
    if LEVEL == 1:
        brick_colors = [GREEN] * NUM_BRICKS_X * NUM_BRICKS_Y
    elif LEVEL == 2:
        brick_colors1 = [YELLOW] * NUM_BRICKS_X * 4
        brick_colors2 = [GREEN] * NUM_BRICKS_X * 4
        brick_colors.extend(brick_colors1)
        brick_colors.extend(brick_colors2)
    else:
        brick_colors1 = [RED] * NUM_BRICKS_X * 3
        brick_colors2 = [YELLOW] * NUM_BRICKS_X * 3
        brick_colors3 = [GREEN] * NUM_BRICKS_X * 2
        brick_colors.extend(brick_colors1)
        brick_colors.extend(brick_colors2)
        brick_colors.extend(brick_colors3)

    for i in range(NUM_BRICKS_Y):
        for j in range(NUM_BRICKS_X):
            brick_x = j * (BRICK_WIDTH + 7)
            brick_y = i * (BRICK_HEIGHT + 7)
            bricks.append(pygame.Rect(brick_x + 2, brick_y + 4, BRICK_WIDTH, BRICK_HEIGHT))

    # Ball
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_dx = random.choice((BALL_SPEED, -BALL_SPEED))
    ball_dy = -BALL_SPEED
    ball_radius = 10

    # Paddle
    paddle_width = 100
    paddle_height = 10
    paddle_x = (WIDTH - paddle_width) // 2
    paddle_y = HEIGHT - 20

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Move the paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle_x + paddle_width < WIDTH:
            paddle_x += PADDLE_SPEED

        # Move the ball
        ball_x += ball_dx
        ball_y += ball_dy

        # Ball collisions with walls
        if ball_x < ball_radius or ball_x > WIDTH - ball_radius:
            ball_dx = -ball_dx
        if ball_y < ball_radius:
            ball_dy = -ball_dy

        # Ball collisions with paddle
        if (
                ball_y + ball_radius > paddle_y
                and paddle_x <= ball_x <= paddle_x + paddle_width
        ):
            ball_dy = -ball_dy
            ball_dx *= random.uniform(0.8, 1.2)

        # Ball collisions with bricks
        for i, brick in enumerate(bricks):
            if brick.colliderect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius):
                if brick_colors[i] == YELLOW:
                    brick_colors[i] = GREEN
                elif brick_colors[i] == RED:
                    brick_colors[i] = YELLOW
                else:
                    brick_colors[i] = WHITE
                if ball_x >= brick.x + BRICK_WIDTH or ball_x <= brick.x:
                    ball_dx = -ball_dx
                else:
                    ball_dy = -ball_dy
                if brick_colors[i] == WHITE:
                    bricks[i] = pygame.Rect(0, 0, 0, 0)  # Remove the brick

        if checkWinner(bricks):
            return 2
        # Check if the ball missed the paddle
        if ball_y > HEIGHT:
            return 1

        # Clear the screen
        screen.fill(BLACK)

        # Draw the bricks
        for i, brick in enumerate(bricks):
            pygame.draw.rect(screen, brick_colors[i], brick)

        # Draw the paddle
        pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))

        # Draw the ball
        pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

        # Update the display
        pygame.display.flip()


def checkWinner(bricks):
    for brick in bricks:
        if brick != pygame.Rect(0, 0, 0, 0):
            return False
    return True
