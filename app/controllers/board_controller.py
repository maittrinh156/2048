from app.interactors.board_interactor import BoardInteractor

class BoardController:
    def __init__(self, boardInteractor: BoardInteractor):
        self.boardInteractor = boardInteractor
        
    def handleSwiping(self):
        try:
            direction = int(input("Please input the direction: "))
        except ValueError:
            raise Exception("Not a number!")
        
        if direction < 1 or direction > 4:
            raise Exception("Direction must be from 1 to 4!")
            
        return direction
        
    def handleGamePlaying(self):
        self.boardInteractor.createNewBoard()
        
        while not self.boardInteractor.isGameOver():
            try:
                direction = self.handleSwiping()
            except Exception as error:
                print(str(error))
                continue
            self.boardInteractor.playPerTurn(direction)
        
        