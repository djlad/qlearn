class tictactoe:
    def __init__(self):
        self.board = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
        self.numActions = 18
        self.turn = 0

    def drawboard(self):
        for row in self.board:
            for col in row:
                print(col, end="")
                print('\t', end="")
            print("\n", end="")

    def validMove(self, row, column, player):
        return self.board[row][column] == 0 and player == self.getTurn()
    
    def updateTurn(self):
        self.turn += 1
        self.turn %= 2
    
    def getTurn(self):
        return self.turn + 1
    
    def playMove(self, row, column, player=1):
        if not self.validMove(row, column, player):
            return False
        if player == 1:
            self.board[row][column] = player
            self.updateTurn()
            return True
        elif player == 2:
            self.board[row][column] = player
            self.updateTurn()
            return True
        return False

    def checkThree(self, row, col, down=0, right=0):
        if down == 0 and right == 0:
            print('error')
            return False

        length = 3
        player = self.board[row][col]
        if player == 0:
            return player
        while True:
            row += down
            col += right
            if row < length and col < length:
                if player == self.board[row][col]:
                    continue
                else:
                    return 0
            else:
                return player

    def detectWin(self):
        win = False
        for coli, col in enumerate(self.board[0]):
            win = self.checkThree(0, coli, down=1)
            if win > 0:
                return win
        
        for rowi, row in enumerate(self.board):
            win = self.checkThree(rowi, 0, right=1)
            if win > 0:
                return win
        
        win = self.checkThree(0, 0, 1, 1)
        if win > 0:
            return win
        win = self.checkThree(2,0,-1,1)
        if win > 0:
            return win
        return win

    def hashState(self):
        state = self.getTurn()
        for row in self.board:
            for piece in row:
                state *= 10
                state += piece
        print(state)
        return state


if __name__ == "__main__":
    t = tictactoe()
    t.drawboard()
            