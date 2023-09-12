import pygame
import random
import time
import numpy

pygame.init()

WIDTH, HEIGHT = 600, 600
GRID_SIZE = 4
CELL_SIZE = WIDTH // GRID_SIZE
LINE_HEIGHT = HEIGHT // GRID_SIZE
LINE_WIDTH = 6
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (180, 180, 180)
DARK_GRAY = (90, 90, 90)

REALLY_LIGHT_GRAY = (220, 220, 220)
LESS_LIGHT_GRAY = (160, 160, 160)
LIGHT_ORANGE = (252, 210, 153)
ORANGE = (253, 127, 57)
DARK_ORANGE = (255, 94, 5)
REALLY_DARK_ORANGE = (195, 82, 20)
LIGHT_YELLOW = (239, 253, 95)
YELLOW = (250, 218, 94)
DARK_YELLOW = (252, 209, 42)
REALLY_DARK_YELLOW = (255, 211, 0)
FINAL_YELLOW = (255, 255, 0)

colors = {
    2: REALLY_LIGHT_GRAY,
    4: LESS_LIGHT_GRAY,
    8: LIGHT_ORANGE,
    16: ORANGE,
    32: DARK_ORANGE,
    64: REALLY_DARK_ORANGE,
    128: LIGHT_YELLOW,
    256: YELLOW,
    512: DARK_YELLOW,
    1024: REALLY_DARK_YELLOW,
    2048: FINAL_YELLOW,
    4096: BLACK,
    8192: BLACK,
    16384: BLACK,
    32768: BLACK,
    65536: BLACK
}


def twozerofoureightGame():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.Font(None, 48)
    gameMode = 1
    while True:
        if gameMode == 1:
            startScreen(screen, font)
        winner = gameLoop(screen, font)
        gameMode = endScreen(screen, font, winner)


def startScreen(screen, font):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return
        if keys[pygame.K_s]:
            pygame.quit()
            from main import main
            main()
        if keys[pygame.K_q]:
            pygame.quit()
            quit()

        screen.fill(BLACK)

        screen.blit(font.render("Welcome to 2048 game!", True, WHITE), (10, 80))
        screen.blit(font.render("To start the game, press SPACE", True, WHITE), (10, 120))
        screen.blit(font.render("To go back to game select, press S", True, WHITE), (10, 160))
        screen.blit(font.render("To quit, press Q", True, WHITE), (10, 200))

        pygame.display.flip()


def drawGrid(screen):
    screen.fill(LIGHT_GRAY)
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, DARK_GRAY, (0, i * LINE_HEIGHT), (WIDTH, i * LINE_HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, DARK_GRAY, (i * LINE_HEIGHT, 0), (i * LINE_HEIGHT, WIDTH), LINE_WIDTH)


def drawField(screen, font, row, col, num):
    color = colors[num]
    pygame.draw.rect(screen, color, pygame.Rect(col * CELL_SIZE + 3, row * CELL_SIZE + 3, CELL_SIZE - 6, CELL_SIZE - 6))
    if num > 2048:
        text = font.render(str(num), True, WHITE)
    else:
        text = font.render(str(num), True, BLACK)

    text_rect = text.get_rect(center=pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE).center)
    screen.blit(text, text_rect)


def addRandom(grid):
    num = random.random()
    if num > 0.9:
        x = 4
    else:
        x = 2
    col = random.randint(0, 3)
    row = random.randint(0, 3)
    if grid[row][col] == 0:
        grid[row][col] = x
    else:
        addRandom(grid)


def moveLeft(grid):
    for row in grid:
        done = [0 for _ in range(len(row))]
        y = 0
        for k in range(1, len(row)):
            if y == 1:
                break
            for i in range(len(row) - k):
                if row[i] == row[i + k] != 0:
                    x = 0
                    for j in range(1, k):
                        if row[i + j] != 0:
                            x = 1
                    if x == 0 and done[i] == 0:
                        row[i + k] = 0
                        row[i] *= 2
                        done[i] = 1
                        y = 1

        cur = 1
        temp = 0
        i = 0
        while i < len(row):
            if row[i] != 0 and cur == 0:
                row[i], row[temp] = row[temp], row[i]
                cur = 1
                i = temp
            elif row[i] == 0:
                if cur == 1:
                    temp = i
                    cur = 0
            i = i + 1


def moveRight(grid):
    for row in grid:
        done = [0 for _ in range(len(row))]
        y = 0
        for k in range(1, len(row)):
            if y == 1:
                break
            for i in range(len(row) - k):
                if row[i] == row[i + k] != 0:
                    x = 0
                    for j in range(1, k):
                        if row[i + j] != 0:
                            x = 1
                    if x == 0 and done[i] == 0:
                        row[i + k] *= 2
                        row[i] = 0
                        done[i + k] = 1
                        y = 1

        cur = 1
        temp = 0
        i = len(row) - 1
        while i > -1:
            if row[i] != 0 and cur == 0:
                row[i], row[temp] = row[temp], row[i]
                cur = 1
                i = temp
            elif row[i] == 0:
                if cur == 1:
                    temp = i
                    cur = 0
            i = i - 1


def moveUp(grid):
    grid = numpy.rot90(grid, 1)
    moveLeft(grid)
    grid = numpy.rot90(grid, 3)
    return grid


def moveDown(grid):
    grid = numpy.rot90(grid, 1)
    moveRight(grid)
    grid = numpy.rot90(grid, 3)
    return grid


def gameLoop(screen, font):
    winner = 0
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    addRandom(grid)
    while True:
        drawGrid(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                el = False
                copy = [[grid[j][i] for i in range(len(grid))] for j in range(len(grid))]
                if event.key == pygame.K_UP:
                    grid = moveUp(grid)
                if event.key == pygame.K_DOWN:
                    grid = moveDown(grid)
                if event.key == pygame.K_LEFT:
                    moveLeft(grid)
                if event.key == pygame.K_RIGHT:
                    moveRight(grid)

                for i in range(len(grid)):
                    for j in range(len(grid)):
                        if grid[i][j] != copy[i][j]:
                            el = True
                if el:
                    addRandom(grid)
                else:

                    for i in range(len(grid)):
                        for j in range(len(grid[i])):
                            if grid[i][j] == 0:
                                el = True
                    if not el:
                        return 2

        drawGrid(screen)

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if grid[row][col] != 0:
                    drawField(screen, font, row, col, grid[row][col])

        pygame.display.flip()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2048 and winner == 0:
                    winner = endScreen(screen, font, 1)


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
        if keys[pygame.K_SPACE]:
            return 3
        screen.fill(BLACK)

        if winner == 1:
            screen.blit(font.render("Game over! You won!", True, WHITE), (10, 80))
            screen.blit(font.render("To continue the game, press SPACE", True, WHITE), (10, 240))
        else:
            screen.blit(font.render("Game over! You lost!", True, WHITE), (10, 80))
        screen.blit(font.render("To restart, press R", True, WHITE), (10, 120))
        screen.blit(font.render("To go to menu, press M", True, WHITE), (10, 160))
        screen.blit(font.render("To quit, press Q", True, WHITE), (10, 200))

        pygame.display.flip()
