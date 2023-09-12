import pygame
from pong import pongGame
from snake import snakeGame
from tictactoe import tictactoeGame
from breakout import breakoutGame
from spaceinvaders import spaceinvadersGame
from minesweeper import minesweeperGame
from twozerofoureight import twozerofoureightGame


def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600

    pong = snake = tic = mine = space = breakout = game2048 = False
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.Font(None, 48)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            pong = True
            snake = tic = mine = space = game2048 = breakout = False
        if keys[pygame.K_2]:
            snake = True
            pong = tic = mine = space = game2048 = breakout = False
        if keys[pygame.K_3]:
            tic = True
            snake = pong = mine = game2048 = space = breakout = False
        if keys[pygame.K_4]:
            mine = True
            snake = game2048 = tic = pong = space = breakout = False
        if keys[pygame.K_5]:
            space = True
            game2048 = snake = tic = mine = pong = breakout = False
        if keys[pygame.K_6]:
            breakout = True
            game2048 = snake = tic = mine = space = pong = False
        if keys[pygame.K_7]:
            game2048 = True
            breakout = snake = tic = mine = space = pong = False
        if keys[pygame.K_KP_ENTER] or keys[pygame.KSCAN_KP_ENTER]:
            if pong:
                pongGame()
            if snake:
                snakeGame()
            if tic:
                tictactoeGame()
            if mine:
                minesweeperGame()
            if space:
                spaceinvadersGame()
            if breakout:
                breakoutGame()
            if game2048:
                twozerofoureightGame()
        if keys[pygame.K_q]:
            pygame.quit()
            quit()

        screen.fill((0, 0, 0))

        screen.blit(font.render("Welcome to game center! Pick a game to play", True, (255, 255, 255)), (10, 80))
        if pong:
            screen.blit(font.render("1. Pong", True, (0, 255, 0)), (10, 120))
        else:
            screen.blit(font.render("1. Pong", True, (255, 255, 255)), (10, 120))
        if snake:
            screen.blit(font.render("2. Snake", True, (0, 255, 0)), (10, 160))
        else:
            screen.blit(font.render("2. Snake", True, (255, 255, 255)), (10, 160))
        if tic:
            screen.blit(font.render("3. Tic-Tac-Toe", True, (0, 255, 0)), (10, 200))
        else:
            screen.blit(font.render("3. Tic-Tac-Toe", True, (255, 255, 255)), (10, 200))
        if mine:
            screen.blit(font.render("4. Minesweeper", True, (0, 255, 0)), (10, 240))
        else:
            screen.blit(font.render("4. Minesweeper", True, (255, 255, 255)), (10, 240))
        if space:
            screen.blit(font.render("5. Space invaders", True, (0, 255, 0)), (10, 280))
        else:
            screen.blit(font.render("5. Space invaders", True, (255, 255, 255)), (10, 280))
        if breakout:
            screen.blit(font.render("6. Breakout", True, (0, 255, 0)), (10, 320))
        else:
            screen.blit(font.render("6. Breakout", True, (255, 255, 255)), (10, 320))
        if game2048:
            screen.blit(font.render("7. 2048", True, (0, 255, 0)), (10, 360))
        else:
            screen.blit(font.render("7. 2048", True, (255, 255, 255)), (10, 360))
        screen.blit(font.render("To start the game, press ENTER", True, (255, 255, 255)), (10, 400))
        screen.blit(font.render("To quit, press Q", True, (255, 255, 255)), (10, 440))

        pygame.display.flip()


main()
