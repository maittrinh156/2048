from abc import ABC, abstractclassmethod

class BoardPresenterInterface(ABC):
    @abstractclassmethod
    def showBoard():
        pass
    
    @abstractclassmethod
    def showGameOver():
        pass
    
    @abstractclassmethod
    def showOptions():
        pass
    
    @abstractclassmethod
    def showWin():
        pass