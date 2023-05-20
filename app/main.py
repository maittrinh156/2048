import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.entities.board_entity import BoardEntity
from app.presenters.board_cli_presenter import BoardCLIPresenter
from app.interactors.board_interactor import BoardInteractor
from app.controllers.board_controller import BoardController

def main():
    boardPresenter = BoardCLIPresenter()
    boardEntity = BoardEntity()
    boardInterfactor = BoardInteractor(boardEntity=boardEntity, boardPresenter = boardPresenter)
    boardController = BoardController(boardInteractor=boardInterfactor)
    
    boardController.handleGamePlaying()    
    
    
if __name__ == "__main__":
    main()


