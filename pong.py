import pygame
import random
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def pongGame():
    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong Game")

    # Fonts
    font1 = pygame.font.Font(None, 36)
    font2 = pygame.font.Font(None, 48)

    # When the gameMode is 1, program goes to menu screen
    gameMode = 1

    # game can be play infinitely
    while True:
        if gameMode == 1:
            startScreen(screen, font2)
        winner = gameLoop(screen, font1)
        gameMode = endScreen(winner, font2, screen)


def startScreen(screen, font):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # checking if any keys were pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return
        if keys[pygame.K_q]:
            pygame.quit()
            quit()
        if keys[pygame.K_f]:
            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            global WIDTH
            global HEIGHT
            WIDTH, HEIGHT = screen.get_size()
        if keys[pygame.K_ESCAPE]:
            WIDTH, HEIGHT = 800, 600
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
        if keys[pygame.K_q]:
            pygame.quit()
            quit()

        if keys[pygame.K_s]:
            pygame.quit()
            from main import main
            main()
        # clearing the screen
        screen.fill(BLACK)

        # Writing on the screen what is supposed to be written
        screen.blit(font.render("Welcome to pong game!", True, WHITE), (10, 80))
        screen.blit(font.render("Left paddle is player1, it moves with W/S", True, WHITE), (10, 120))
        screen.blit(font.render("Right paddle is player2, it moves with UP/DOWN", True, WHITE), (10, 160))
        screen.blit(font.render("Press space to start the game", True, WHITE), (10, 200))
        screen.blit(font.render("To go fullscreen, press F", True, WHITE), (10, 240))
        screen.blit(font.render("To exit fullscreen, at any time, press ESC", True, WHITE), (10, 280))
        screen.blit(font.render("To go to game selection, press S", True, WHITE), (10, 320))
        screen.blit(font.render("To quit, press Q", True, WHITE), (10, 360))
        # Update the display
        pygame.display.flip()

        # Set the framerate
        pygame.time.Clock().tick(60)


def endScreen(winner, font, screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Checking if any keys were pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            return 2
        if keys[pygame.K_q]:
            pygame.quit()
            quit()
        if keys[pygame.K_m]:
            return 1
        if keys[pygame.K_ESCAPE]:
            global WIDTH
            global HEIGHT
            WIDTH, HEIGHT = 800, 600
            screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # Clearing the screen
        screen.fill(BLACK)

        # Writing on the screen what is supposed to be written
        if winner == 1:
            screen.blit(font.render("Player 1 Won!", True, WHITE), (10, 80))
        else:
            screen.blit(font.render("Player 2 Won!", True, WHITE), (10, 80))

        screen.blit(font.render("To restart press R", True, WHITE), (10, 120))
        screen.blit(font.render("To quit press Q", True, WHITE), (10, 160))
        screen.blit(font.render("To go back to menu, press M", True, WHITE), (10, 200))

        # Updating the display
        pygame.display.flip()

        # Setting the framerate
        pygame.time.Clock().tick(60)


def gameLoop(screen, font):
    # global variables are changed, they need to be declared
    global WIDTH
    global HEIGHT

    # Initialising all the varibales used in the game loop
    ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
    player1 = pygame.Rect(50, HEIGHT // 2 - 60, 10, 120)  # paddle on the left, moves with WS
    player2 = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 60, 10, 120)  # paddle on the right, moves with UP/DOWN
    ball_dx = random.choice((1, -1))  # movement of the ball in x coordinate
    ball_dy = random.choice((1, -1))  # movement of the ball in y coordinate
    player1_score = 0
    player2_score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Move the paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1.top > 0:
            player1.y -= PADDLE_SPEED
        if keys[pygame.K_s] and player1.bottom < HEIGHT:
            player1.y += PADDLE_SPEED
        if keys[pygame.K_UP] and player2.top > 0:
            player2.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
            player2.y += PADDLE_SPEED
        if keys[pygame.K_ESCAPE]:
            WIDTH, HEIGHT = 800, 600
            ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
            player1 = pygame.Rect(50, HEIGHT // 2 - 60, 10, 120)  # paddle on the left, moves with WS
            player2 = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 60, 10, 120)  # paddle on the right, moves with UP/DOWN
            screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # Move the ball
        ball.x += ball_dx * BALL_SPEED
        ball.y += ball_dy * BALL_SPEED

        # Ball / wall collisions
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_dy *= -1

        # Ball / paddle collision
        if ball.colliderect(player1) or ball.colliderect(player2):
            if ball_dx > 5 or ball_dx < -5:
                ball_dx *= -0.95
            else:
                ball_dx *= -1.05
            ball_dy *= random.choice((1, -1))

        # Update the score
        if ball.left <= 0:
            player2_score += 1
            if player2_score == 10:
                return 2
            ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
            ball_dx = random.choice((1, -1))
        if ball.right >= WIDTH:
            player1_score += 1
            if player1_score == 10:
                return 1
            ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
            ball_dx = random.choice((1, -1))

        # Clear the screen
        screen.fill(BLACK)

        # Draw paddles and ball
        pygame.draw.rect(screen, WHITE, player1)
        pygame.draw.rect(screen, WHITE, player2)
        pygame.draw.ellipse(screen, WHITE, ball)

        # Draw the score
        player1_text = font.render(str(player1_score), True, WHITE)
        player2_text = font.render(str(player2_score), True, WHITE)
        screen.blit(player1_text, (WIDTH // 4, 50))
        screen.blit(player2_text, (3 * WIDTH // 4 - 36, 50))

        # Update the display
        pygame.display.flip()

        # Set the frame rate
        pygame.time.Clock().tick(60)
