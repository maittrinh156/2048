import random

class BoardInteractor:
    def __init__(self, boardEntity, boardPresenter):
        self.boardEntity = boardEntity
        self.boardPresenter = boardPresenter
        
    def convertCollumnsToRows(self, board):
        return [[row[collumnIndex] for row in board] for collumnIndex in range(len(board))]
    
    def swipeUpOrLeft(self, board):
        N = len(board)
        
        for line in board:
            scan1, scan2, write = 0, 1, 0
            
            while scan1 < N and scan2 < N:
                if line[scan1] == 0:
                    scan1 += 1
                    continue
                if line[scan2] == 0 or scan1 == scan2:
                    scan2 += 1
                    continue
                if line[scan1] == line[scan2]:
                    line[scan1], line[scan2], line[write] = 0, 0, line[scan1] * 2
                    scan1, scan2 = scan2 + 1, scan2 + 2
                    write += 1
                else:
                    line[scan1], line[write] = 0, line[scan1]
                    scan1 += 1
                    write += 1
            if scan1 < N:
                line[scan1], line[write] = 0, line[scan1]
        
        return board
    
    def swipeDownOrRight(self, board):
        N = len(board)
        
        for line in board:
            scan1, scan2, write = N-1, N-2, N-1
            
            while scan1 > -1 and scan2 > -1:
                if line[scan1] == 0:
                    scan1 -= 1
                    continue
                if line[scan2] == 0 or scan1 == scan2:
                    scan2 -= 1
                    continue
                if line[scan1] == line[scan2]:
                    line[scan1], line[scan2], line[write] = 0, 0, line[scan1] * 2
                    scan1, scan2 = scan2 - 1, scan2 - 2
                    write -= 1
                else:
                    line[scan1], line[write] = 0, line[scan1]
                    scan1 -= 1
                    write -= 1
            if scan1 > -1:
                line[scan1], line[write] = 0, line[scan1]
        
        return board
                           
    def swipe(self, direction):
        board = self.boardEntity.getBoard()
        
        if direction == 1:
            board = self.swipeUpOrLeft(board)
        elif direction == 2:
            board = self.swipeDownOrRight(board)
        elif direction == 3:
            board = self.convertCollumnsToRows(board)
            board = self.swipeUpOrLeft(board)
            board = self.convertCollumnsToRows(board)
        else:
            board = self.convertCollumnsToRows(board)
            board = self.swipeDownOrRight(board)
            board = self.convertCollumnsToRows(board)
            
        self.boardEntity.setBoard(board)           
            
    def getRandomEmptyRoom(self):
        board = self.boardEntity.getBoard()
        emptyRooms = []
        for i, row in enumerate(board):
            for j, room in enumerate(row):
                if room == 0:
                    emptyRooms.append((i,j))
        return random.choice(emptyRooms)                    
            
    def openNewRoom(self):
        randomRoom = self.getRandomEmptyRoom()
        self.boardEntity.setRoom(room=randomRoom)
        
    def checkWin(self):
        board = self.boardEntity.getBoard()
        rooms = [room for x in board for room in x]
        if 2048 in set(rooms):
            return True
        return False
        
    def isGameOver(self):
        if self.checkWin():
            return True
        board = self.boardEntity.getBoard()
        rooms = [room for x in board for room in x]
        if rooms.count(0) == 0:
            return True
        return False
        
    def playPerTurn(self, direction):
        self.swipe(direction=direction)
        self.openNewRoom()
        
        board = self.boardEntity.getBoard()
        self.boardPresenter.showBoard(board=board)
        
        if self.checkWin():
            self.boardPresenter.showWin()
        elif self.isGameOver():
            self.boardPresenter.showGameOver()
        else:
            self.boardPresenter.showOptions()
            
    def createNewBoard(self):
        self.openNewRoom()
        self.openNewRoom()
        
        board = self.boardEntity.getBoard()
        self.boardPresenter.showBoard(board=board)
        
        self.boardPresenter.showOptions()

        
        
        
        
        

        
