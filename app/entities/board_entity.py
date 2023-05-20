class BoardEntity:
    def __init__(self):
        self.board = [[0 for j in range(8)] for i in range(8)]
    
    def getBoard(self):
        return self.board
    
    def setRoom(self, room):
        x, y = room
        self.board[x][y] = 2
        
    def setBoard(self, board):
        for i, row in enumerate(board):
            for j, room in enumerate(row):
                self.board[i][j] = board[i][j]
                

        
