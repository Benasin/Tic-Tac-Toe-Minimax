#!/usr/bin/python
import pygame
from pygame.locals import *
from board import Board
from minmax_bot import Bot

pygame.init()

def create_window(width, height):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Unbeatable Tic Tac Toe")
    return screen

# Each cell of the grid object
class Cell(object):
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    # Color the backgroun
    def color(self, color, screen):
        pygame.draw.rect(screen, (color), (self.x_pos * 200, self.y_pos * 200, 200, 200))
        pygame.draw.rect(screen, (0,0,0), (self.x_pos * 200, self.y_pos * 200, 200, 200), 3)

    # Draw letter O 
    def draw_O(self, screen):
        pygame.draw.circle(screen, (0,0,255), (self.x_pos * 200 + 100, self.y_pos * 200 + 100), 75, 5)

    # Draw letter X 
    def draw_X(self, screen):
        pygame.draw.line(screen, (255,0,0), (self.x_pos * 200 + 30, self.y_pos * 200 + 30), ((self.x_pos + 1) * 200 - 30, (self.y_pos + 1) * 200 - 30), 7)
        pygame.draw.line(screen, (255,0,0), (self.x_pos * 200 + 30, (self.y_pos + 1) * 200 - 30), ((self.x_pos + 1) * 200 - 30, self.y_pos * 200 + 30), 7)

def main():
    width = 600
    height = 600
    screen = create_window(width, height)
    col = 3
    row = 3
    grid = []

    # Add cells to the grid
    for i in range(col):
        container = []
        for j in range(row):
            container.append(Cell(j, i))
        grid.append(container)

    # Paint the grid white
    for i in range(col):
        for j in range(row):
            grid[i][j].color((255,255,255), screen)   

    board = Board()
    bot = Bot()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            # Convert x y mouse coordinates to indexes
            y, x = pygame.mouse.get_pos()
            x_index = round(abs(x) / 200 + 0.5) - 1
            y_index = round(abs(y) / 200 + 0.5) - 1

            if event.type == pygame.MOUSEBUTTONDOWN and not board.check_winner():
                if board.board[x_index][y_index] == '-':
                    # Player's turn
                    board.draw(x_index, y_index, 'O')
                    grid[x_index][y_index].draw_O(screen) 
               
                    # AI's turn
                    if not board.check_winner():
                        bot_x_index, bot_y_index = bot.play(board)
                        grid[bot_x_index][bot_y_index].draw_X(screen)

            elif event.type == pygame.KEYDOWN:
                # Press R to restart the game
                if event.key == pygame.K_r:
                    main()

        pygame.display.update()

if __name__ == '__main__':
    main() 
