import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 20
SNAKE_SPEED = 10

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


def snakeGame():
    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake game")

    # Initialize snake and food
    gameMode = 1
    inf = 0
    font = pygame.font.Font(None, 48)
    while True:
        if gameMode == 1:
            inf = startScreen(screen, font, inf)
        score = gameLoop(inf)
        gameMode = endScreen(font, score)


def startScreen(screen, font, inff):
    slow = faster = fast = small = medium = big = inf = False
    global SNAKE_SPEED
    global WIDTH
    global HEIGHT
    global GRID_SIZE
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    if inf:
                        inf = False
                        inff = 0
                    else:
                        inf = True
                        inff = 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            SNAKE_SPEED = 5
            slow = True
            faster = fast = False

        if keys[pygame.K_2]:
            SNAKE_SPEED = 10
            faster = True
            slow = fast = False

        if keys[pygame.K_3]:
            SNAKE_SPEED = 15
            fast = True
            slow = faster = False

        if keys[pygame.K_s]:
            WIDTH = HEIGHT = 250
            small = True
            medium = big = False
        if keys[pygame.K_m]:
            WIDTH = HEIGHT = 500
            medium = True
            small = big = False

        if keys[pygame.K_b]:
            WIDTH = HEIGHT = 750
            big = True
            small = medium = False

        if keys[pygame.K_SPACE]:
            if (small or medium or big) and (slow or fast or faster):
                return inff

        if keys[pygame.K_s]:
            pygame.quit()
            from main import main
            main()
        # Clear the screen
        screen.fill(BLACK)

        screen.blit(font.render("Welcome to snake game", True, WHITE), (10, 80))
        if slow:
            screen.blit(font.render("Press 1 for easy mode", True, GREEN), (10, 120))
        else:
            screen.blit(font.render("Press 1 for easy mode", True, WHITE), (10, 120))
        if faster:
            screen.blit(font.render("Press 2 for medium mode", True, GREEN), (10, 160))
        else:
            screen.blit(font.render("Press 2 for medium mode", True, WHITE), (10, 160))
        if fast:
            screen.blit(font.render("Press 3 for hard mode", True, GREEN), (10, 200))
        else:
            screen.blit(font.render("Press 3 for hard mode", True, WHITE), (10, 200))
        if small:
            screen.blit(font.render("Press s for small grid", True, RED), (10, 240))
        else:
            screen.blit(font.render("Press s for small grid", True, WHITE), (10, 240))
        if medium:
            screen.blit(font.render("Press m for medium grid", True, RED), (10, 280))
        else:
            screen.blit(font.render("Press m for medium grid", True, WHITE), (10, 280))
        if big:
            screen.blit(font.render("Press b for big grid", True, RED), (10, 320))
        else:
            screen.blit(font.render("Press b for big grid", True, WHITE), (10, 320))
        if inf:
            screen.blit(font.render("For infinity mode press i", True, BLUE), (10, 360))
        else:
            screen.blit(font.render("For infinity mode press i", True, WHITE), (10, 360))

        screen.blit(font.render("Press space to start the game", True, WHITE), (10, 400))
        screen.blit(font.render("To go back to game select, press S", True, WHITE), (10, 440))
        screen.blit(font.render("If you font to quit, press q", True, WHITE), (10, 480))

        # Update the display
        pygame.display.flip()

        # Set the framerate
        pygame.time.Clock().tick(60)


def endScreen(font, score):
    global WIDTH
    global HEIGHT
    WIDTH = 800
    HEIGHT = 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

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

        # Clear the screen
        screen.fill(BLACK)

        screen.blit(font.render(f"Game over! Your score is {score}", True, WHITE), (10, 80))
        screen.blit(font.render("To restart, press r", True, WHITE), (10, 120))
        screen.blit(font.render("To go to menu, press m", True, WHITE), (10, 160))
        screen.blit(font.render("To quit, press q", True, WHITE), (10, 200))

        # Update the display
        pygame.display.flip()

        # Set the framerate
        pygame.time.Clock().tick(60)


def gameLoop(inf):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    snake = [(100, 50), (90, 50), (80, 50)]
    snake_direction = (1, 0)
    food = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
            random.randint(0, (HEIGHT - 2 * GRID_SIZE) // GRID_SIZE) * GRID_SIZE + 10)
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1):
                    snake_direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                    snake_direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                    snake_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                    snake_direction = (1, 0)

        # Move the snake
        new_head = (snake[0][0] + snake_direction[0] * GRID_SIZE, snake[0][1] + snake_direction[1] * GRID_SIZE)

        if inf:
            if new_head[0] < 0:
                new_head = (WIDTH, new_head[1])
            elif new_head[0] >= WIDTH:
                new_head = (0, new_head[1])
            if new_head[1] < 0:
                new_head = (new_head[0], HEIGHT - 10)
            elif new_head[1] >= HEIGHT:
                new_head = (new_head[0], 10)
        else:
            if ((new_head[0] < 0 or new_head[0] >= WIDTH or
                 new_head[1] < 0 or new_head[1] >= HEIGHT) and not inf):
                return score

        # Check for collisions with the food
        if new_head == food:
            snake.insert(0, new_head)
            food = (random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
                    random.randint(0, (HEIGHT - 2 * GRID_SIZE) // GRID_SIZE) * GRID_SIZE + 10)
            score += 1
        else:
            snake.insert(0, new_head)
            snake.pop()

        # Check for collisions with walls or itself
        if new_head in snake[1:]:
            return score

        # Clear the screen
        screen.fill(BLACK)

        # Draw the snake
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

        # Draw the food
        pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(SNAKE_SPEED)
