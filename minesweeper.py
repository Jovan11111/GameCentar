import pygame
import random
import time

pygame.init()

# Define constants
WIDTH, HEIGHT = 750, 750
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE
LINE_HEIGHT = HEIGHT // GRID_SIZE
LINE_WIDTH = 3
MINES_NUMBER = 10
# Colors
WHITE = (255, 255, 255)
GRAY = (172, 172, 172)
DARK_GRAY = (222, 222, 222)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


def minesweeperGame():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Minesweeper")
    font = pygame.font.Font(None, 36)
    font1 = pygame.font.Font(None, 48)

    gameMode = 1
    while True:
        if gameMode == 1:
            startScreen(screen, font1)
        winner = gameLoop(screen, font)
        gameMode = endScreen(screen, font1, winner)


def startScreen(screen, font):
    j = d = t = False
    global GRID_SIZE
    global MINES_NUMBER
    global CELL_SIZE
    global LINE_HEIGHT
    global WIDTH
    global HEIGHT
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_1]:
            j = True
            d = t = False
            GRID_SIZE = 10
            CELL_SIZE = WIDTH // GRID_SIZE
            LINE_HEIGHT = HEIGHT // GRID_SIZE
            MINES_NUMBER = 10
        if keys[pygame.K_2]:
            d = True
            j = t = False
            GRID_SIZE = 20
            CELL_SIZE = WIDTH // GRID_SIZE
            LINE_HEIGHT = HEIGHT // GRID_SIZE
            MINES_NUMBER = 40
        if keys[pygame.K_3]:
            t = True
            d = j = False
            GRID_SIZE = 30
            CELL_SIZE = WIDTH // GRID_SIZE
            LINE_HEIGHT = HEIGHT // GRID_SIZE
            MINES_NUMBER = 90
        if keys[pygame.K_SPACE]:
            if j or d or t:
                return
        if keys[pygame.K_q]:
            pygame.quit()
            quit()

        if keys[pygame.K_s]:
            pygame.quit()
            from main import main
            main()

        screen.fill(BLACK)

        screen.blit(font.render("Welcome to Minesweeper game! ", True, WHITE), (10, 80))
        screen.blit(font.render("Open fields with lef click", True, WHITE), (10, 120))
        screen.blit(font.render("Put flags with right click", True, WHITE), (10, 160))
        if j:
            screen.blit(font.render("For 10x10 field press 1", True, GREEN), (10, 200))
        else:
            screen.blit(font.render("For 10x10 field press 1", True, WHITE), (10, 200))
        if d:
            screen.blit(font.render("For 20x20 field press 2", True, GREEN), (10, 240))
        else:
            screen.blit(font.render("For 20x20 field press 2", True, WHITE), (10, 240))
        if t:
            screen.blit(font.render("For 30x30 field press 3", True, GREEN), (10, 280))
        else:
            screen.blit(font.render("For 30x30 field press 3", True, WHITE), (10, 280))
        screen.blit(font.render("To start, press SPACE", True, WHITE), (10, 320))
        screen.blit(font.render("To go back to game select, press S", True, WHITE), (10, 360))
        screen.blit(font.render("To quit, press Q", True, WHITE), (10, 400))

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
            screen.blit(font.render("Game over! You lost", True, WHITE), (10, 80))

        screen.blit(font.render("To restart, press R", True, WHITE), (10, 120))
        screen.blit(font.render("To go to menu, press M", True, WHITE), (10, 160))
        screen.blit(font.render("To quit press Q", True, WHITE), (10, 200))

        pygame.display.flip()


def calcBoard(grid):
    mines = []
    while len(mines) < MINES_NUMBER:
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        if (x, y) not in mines:
            mines.append((x, y))
            grid[y][x] = -1

    # Calculate neighboring mine counts
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if grid[y][x] == -1:
                continue
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= x + dx < GRID_SIZE and 0 <= y + dy < GRID_SIZE and grid[y + dy][x + dx] == -1:
                        count += 1
            grid[y][x] = count


def checkWinner(grid, flags):
    cnt = 0
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if flags[i][j] == -2 and grid[i][j] == -1:
                cnt += 1
    if cnt == MINES_NUMBER:
        return True
    else:
        return False


def drawField(col, row, screen, font, grid, flags, drawn):
    pygame.draw.rect(screen, DARK_GRAY,
                     pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    flags[row][col] = -1
    drawn[row][col] = 1
    if grid[row][col] != 0:
        text = font.render(str(grid[row][col]), True, BLACK)
        text_rect = text.get_rect(
            center=pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE).center)
        screen.blit(text, text_rect)
    if grid[row][col] == 0:
        if row + 1 < GRID_SIZE and drawn[row + 1][col] == 0:
            drawField(col, row + 1, screen, font, grid, flags, drawn)
        if col + 1 < GRID_SIZE and drawn[row][col + 1] == 0:
            drawField(col + 1, row, screen, font, grid, flags, drawn)
        if row > 0 and drawn[row - 1][col] == 0:
            drawField(col, row - 1, screen, font, grid, flags, drawn)
        if col > 0 and drawn[row][col - 1] == 0:
            drawField(col - 1, row, screen, font, grid, flags, drawn)
        if col > 0 and row > 0 and drawn[row - 1][col - 1] == 0:
            drawField(col - 1, row - 1, screen, font, grid, flags, drawn)
        if col + 1 < GRID_SIZE and row + 1 < GRID_SIZE and drawn[row + 1][col + 1] == 0:
            drawField(col + 1, row + 1, screen, font, grid, flags, drawn)
        if col > 0 and row + 1 < GRID_SIZE and drawn[row + 1][col - 1] == 0:
            drawField(col - 1, row + 1, screen, font, grid, flags, drawn)
        if col + 1 < GRID_SIZE and row > 0 and drawn[row - 1][col + 1] == 0:
            drawField(col + 1, row - 1, screen, font, grid, flags, drawn)


def gameLoop(screen, font):
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    flags = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    drawn = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    calcBoard(grid)
    screen.fill(GRAY)
    while True:

        # Draw lines that separate cells
        for i in range(1, GRID_SIZE):
            pygame.draw.line(screen, BLACK, (0, i * LINE_HEIGHT), (WIDTH, i * LINE_HEIGHT), LINE_WIDTH)
            pygame.draw.line(screen, BLACK, (i * LINE_HEIGHT, 0), (i * LINE_HEIGHT, HEIGHT), LINE_WIDTH)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                if event.button == 1:
                    if grid[row][col] == -1:
                        pygame.draw.rect(screen, BLACK,
                                         pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        pygame.display.flip()
                        time.sleep(1)
                        return 2
                    else:
                        drawField(col, row, screen, font, grid, flags, drawn)
                elif event.button == 3:
                    if flags[row][col] == -2:
                        flags[row][col] = 0
                        pygame.draw.rect(screen, GRAY,
                                         pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

                    elif flags[row][col] == 0:
                        flags[row][col] = -2
                        pygame.draw.rect(screen, RED,
                                         pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        if checkWinner(grid, flags):
            pygame.display.flip()
            time.sleep(1)
            return 1
        pygame.display.flip()

# def minesweeperGame():
#    print("FDfdfdf")
