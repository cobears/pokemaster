from abc import abstractmethod
from typing import Any
from random import shuffle

from pokemaster.utils.api import PokeBaseApi
from pokemaster.data.database import Type

class Game:
    def __init__(self, **kwargs):
        pass
    
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


class TypeGame(Game):
    def __init__(self, **kwargs):
        super().__init__()
        # create the types that will be iterated over
        self.all_types: list = PokeBaseApi.get_all_types()
        self.types: list = [Type(t) for t in self.all_types]

        # create a random set attackers and defenders
        self.attacker: list = shuffle(self.types)
        self.defender: list = shuffle(self.types)
        self.counter: int = 0 # counter determines where to move in the list

    # def turn(self):
        

