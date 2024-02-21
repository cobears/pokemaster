from abc import abstractmethod
from typing import Any

class Game:
    def __init__(self, **kwargs):
        pass

    def play(self) -> Any:
        """ step-by-step through entire game """
        raise NotImplemented
   
    @abstractmethod
    def turn(self) -> Any:
        """ take a turn as the computer """
        raise NotImplemented

    @abstractmethod
    def result(self) -> Any:
        """ determines if the computer or player won """
        raise NotImplemented
    
    @abstractmethod
    def adjustment(self) -> Any:
        """ makes an adjustment (if any) to increase winning odds """
        raise NotImplemented






        

