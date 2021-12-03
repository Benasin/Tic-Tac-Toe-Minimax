#!/usr/bin/python
from minmax_bot import Bot

class Board:
    def __init__(self):
        self.board = [['-','-','-'], 
                      ['-','-','-'],
                      ['-','-','-']]

    # Print the board
    def show(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end = '  ')
            print('\n')

    # Add characters to the board
    def draw(self, x, y, char):
        self.board[x][y] = char
        
    # Check the winner of the game 
    def check_winner(self):
        winner = None
        for i in range(3):
            # Horizontal check
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '-':
                winner = self.board[i][0]
                return winner
        
        for i in range(3):
            # Vertical check
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '-':
                winner = self.board[0][i]
                return winner
        
        # Horizontal check
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '-':
            winner = self.board[0][0]
            return winner

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '-':
            winner = self.board[0][2]
            return winner

        # Check draw
        winner = 'tie'
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    winner = None
                    break
        return winner

# Testing code
if __name__ == '__main__':
    board = Board()
    bot = Bot() 
    player = 1

    while(not board.check_winner()):
        if player:
            x, y = map(int, input("Player 1 position x y >> ").split())
            board.draw(x, y, 'O')
        else:
            print("AI played")
            bot.play(board)

        board.show()
        player ^= 1

    if board.check_winner() == 'tie':
        print("Tied")
    else:
        print("The winner is", board.check_winner())

