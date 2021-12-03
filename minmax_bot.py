class Bot:
    
    def play(self, board):
        x, y = self.bestMove(board)
        board.draw(x, y, 'X')
        return x, y
        
    # Pick the next best move and return x,y coordinates
    def bestMove(self, board):
        highScore = -9999 
        best_x = 0
        best_y = 0

        for i in range(3):
            for j in range(3):
                if board.board[i][j] == '-':
                    board.draw(i, j, 'X')
                    score = self.minimax(board, -9999, 9999, False)          
                    board.draw(i, j, '-')
                    if(score > highScore):
                        highScore = score
                        best_x = i
                        best_y = j

        return best_x, best_y

    # Recursive minimax algorithm with alpha beta pruning
    def minimax(self, board, alpha, beta, isBotTurn):
        winner = board.check_winner()
        if winner == 'O':
            return -1
        elif winner == 'X':
            return 1
        elif winner == 'tie':
            return 0
        
        # Maximizing turn
        if isBotTurn:
            highScore = -9999
            for i in range(3):
                for j in range(3):
                    if board.board[i][j] == '-':
                        board.draw(i, j, 'X')
                        score = self.minimax(board, alpha, beta, False)          
                        board.draw(i, j, '-')
                        highScore = max(highScore, score)
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break
            return highScore

        # Minimizing turn
        if not isBotTurn:
            lowScore = 9999
            for i in range(3):
                for j in range(3):
                    if board.board[i][j] == '-':
                        board.draw(i, j, 'O')
                        score = self.minimax(board, alpha, beta, True)          
                        board.draw(i, j, '-')
                        lowScore = min(lowScore, score)
                        beta = min(beta, score)
                        if beta <= alpha:
                            break
            return lowScore
