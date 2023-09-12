import pygame
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
GRID_SIZE = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRID_CELL_SIZE = WIDTH // GRID_SIZE
LINE_HEIGHT = HEIGHT // GRID_SIZE
CIRCLE_RADIUS = 60
CROSS_SIZE = 60


def draw_grid(screen):
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, i * LINE_HEIGHT), (WIDTH, i * LINE_HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, WHITE, (i * LINE_HEIGHT, 0), (i * LINE_HEIGHT, HEIGHT), LINE_WIDTH)


def draw_board(board, screen):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 'X':
                x_pos = col * GRID_CELL_SIZE + GRID_CELL_SIZE // 2
                y_pos = row * GRID_CELL_SIZE + GRID_CELL_SIZE // 2
                pygame.draw.line(screen, BLUE, (x_pos - CROSS_SIZE, y_pos - CROSS_SIZE),
                                 (x_pos + CROSS_SIZE, y_pos + CROSS_SIZE), LINE_WIDTH)
                pygame.draw.line(screen, BLUE, (x_pos - CROSS_SIZE, y_pos + CROSS_SIZE),
                                 (x_pos + CROSS_SIZE, y_pos - CROSS_SIZE), LINE_WIDTH)
            elif board[row][col] == 'O':
                x_pos = col * GRID_CELL_SIZE + GRID_CELL_SIZE // 2
                y_pos = row * GRID_CELL_SIZE + GRID_CELL_SIZE // 2
                pygame.draw.circle(screen, RED, (x_pos, y_pos), CIRCLE_RADIUS, LINE_WIDTH)


def check_winner(board, screen):
    # Check rows, columns, and diagonals for a win
    for row in range(GRID_SIZE):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            winner = board[row][0]
            return winner
    for col in range(GRID_SIZE):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            winner = board[0][col]
            return winner
    if GRID_SIZE == 3:
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            winner = board[0][0]
            return winner
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            winner = board[0][2]
            return winner

    if GRID_SIZE == 4:
        if board[0][0] == board[1][1] == board[2][2] == board[3][3] != ' ':
            winner = board[0][0]
            return winner
        if board[0][3] == board[1][2] == board[2][1] == board[3][0] != ' ':
            winner = board[0][3]
            return winner
    return 'N'


def check_draw(board, screen):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    if check_winner(board, screen) != 'N':
        return False
    return True


def tictactoeGame():
    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic-Tac-Toe")
    # Fonts
    font = pygame.font.Font(None, 48)
    gameMode = 1
    while True:
        if gameMode == 1:
            startScreen(screen, font)
        winner = gameLoop(screen)
        gameMode = endScreen(winner, screen, font)


def startScreen(screen, font):
    three = four = False
    global GRID_SIZE
    global GRID_CELL_SIZE
    global LINE_HEIGHT
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_3]:
            three = True
            four = False

        if keys[pygame.K_4]:
            three = False
            four = True
            GRID_SIZE = 4
            GRID_CELL_SIZE = WIDTH // GRID_SIZE
            LINE_HEIGHT = HEIGHT // GRID_SIZE
        if keys[pygame.K_SPACE]:
            return

        if keys[pygame.K_q]:
            pygame.quit()
            quit()

        if keys[pygame.K_s]:
            pygame.quit()
            from main import main
            main()

        screen.fill(BLACK)

        screen.blit(font.render("Welcome to TikTacToe!", True, WHITE), (10, 80))
        if three:
            screen.blit(font.render("To play 3x3 game, select 3", True, RED), (10, 120))
        else:
            screen.blit(font.render("To play 3x3 game, select 3", True, WHITE), (10, 120))
        if four:
            screen.blit(font.render("To play 4x4 game, select 4", True, RED), (10, 160))
        else:
            screen.blit(font.render("To play 4x4 game, select 4", True, WHITE), (10, 160))
        screen.blit(font.render("To start, press space", True, WHITE), (10, 200))
        screen.blit(font.render("To go back to game select, press S", True, WHITE), (10, 240))
        screen.blit(font.render("To quit, press q", True, WHITE), (10, 280))

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

        if winner == 'D':
            screen.blit(font.render("Game over, it's a draw!", True, WHITE), (10, 80))
        elif winner == 'X':
            screen.blit(font.render("Game over, X won!", True, WHITE), (10, 80))
        elif winner == 'O':
            screen.blit(font.render("Game over, O won!", True, WHITE), (10, 80))

        screen.blit(font.render("To restart, press R", True, WHITE), (10, 120))
        screen.blit(font.render("To go to menu, press M", True, WHITE), (10, 160))
        screen.blit(font.render("To quit, press Q", True, WHITE), (10, 200))

        pygame.display.flip()


def gameLoop(screen):
    board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    current_player = 'X'
    winner = 'N'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = x // GRID_CELL_SIZE
                row = y // GRID_CELL_SIZE
                if board[row][col] == ' ':
                    board[row][col] = current_player
                    if current_player == 'X':
                        current_player = 'O'
                    else:
                        current_player = 'X'
                    winner = check_winner(board, screen)
                    if check_draw(board, screen):
                        winner = 'D'

        screen.fill(BLACK)
        draw_grid(screen)
        draw_board(board, screen)

        if winner != 'N':
            pygame.display.flip()
            time.sleep(1)
            return winner

        pygame.display.flip()
