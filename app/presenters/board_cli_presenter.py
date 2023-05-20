from interfaces.board_presenter_interface import BoardPresenterInterface
class BoardCLIPresenter(BoardPresenterInterface):
    def showBoard(self, board):
        print(" "+"_"*39+" ")
        for line in board:
            row = "|"
            for x in line:
                if not x:
                    row += "____|"
                else:
                    xString = str(x)
                    row += xString+"_"*(4-len(xString))+"|"
            print(row)
        print()
    
    def showGameOver(self):
        print("Game over!")
        
    def showWin(self):
        print("You win!")
        
    def showOptions(self):
        directions = ["", "left", "right", "up", "down"]
        
        options = ""
        for i in range(1,5):
            options = options + str(i) + ": " + directions[i] + "   "
            
        print(options)
        