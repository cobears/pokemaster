import yaml
import os

from abc import abstractmethod
from typing import Any
from itertools import permutations
from random import shuffle

from pokemaster.utils.api import PokeBaseApi
from pokemaster.type import Type

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


class TypeGame(Game):
    def __init__(self, **kwargs):
        super().__init__()
        # create the types that will be iterated over
        self.all_types: list = PokeBaseApi.get_all_types()
        self.types: list = [Type(t) for t in self.all_types]

        # create all permutations of attackers and defenders
        self.games: list = list(permutations(self.types, 2))
        shuffle(self.games)

        # create basic score-keeping
        self.rounds: int = len(self.games)
        self.current_round: int = 1
        self.score = 0
        with open(os.path.join(os.path.dirname(__file__), "./scoring/type.yaml"), "r") as f:
            self.scoring = yaml.safe_load(f)

        print(20*"-"+"\nWelcome to the Type Effectiveness Game!\n"+20*"-"+"\n")

    def play(self):
        for _ in range(self.rounds):
            self.turn()
            self.current_round += 1

    def turn(self):
        # use the first index to create a game, where a game is a tuple of (attacker, defender)
        game, *_ = self.games
        attacker, defender = game
        
        print(20*"-"+f"\nRound {self.current_round}\n"+20*"-")
        print(f"Attacker: {attacker.name}")
        print(f"Defender: {defender.name}")
        print("\nWhat is the effectivness to this match-up?")
        ans = input("Answer: ")

        while isinstance(ans, str):
            try:
                ans = float(ans)
                assert ans in [0, 0.5, 1, 2]
            except:
                print("\nAnswer must be 0, 0.5, 1, or 2 - Please try again...")
                ans = input("New Answer: ")

        self.result(ans, attacker, defender)
        print(f"Score after Round {self.current_round}: {self.score}")

        # delete the game we just played
        self.games.remove(game)

    def result(self, ans: float, attacker: Type, defender: Type) -> None:
        """result determines if the answer provided by the user is correct and updates
        the score

        Args:
            ans (float): answer of effectiveness score by user1
            attacker (Type): Type object for the attacker
            defender (Type): Type object for the defender
        """
        solution, *_ = [key for key in self.scoring.keys() if defender.name in attacker.damage_relations[key]]
        
        if ans == self.scoring[solution]:
            print(f"Correct! Effectiveness is {self.scoring[solution]}x!")
            self.score += 10
        else:
            print(f"Incorrect! Effectiveness is {self.scoring[solution]}x! Dumbass.")



        

