from location import *
from gridDirection import *

class Player:
    __symbol = ""
    __name = ""

    def __init__(self, symbol, name = None):
        self.__symbol = symbol
        if name == None:
            self.__name = "Player " + symbol
        else:
            self.__name = name

    def get_symbol(self):
        return self.__symbol

    def equals(self, player) -> bool:
        if isinstance(player, Player):
            return self.__symbol == player.get_symbol()
        return False

    def __str__(self):
        return self.__name

    @staticmethod
    def validate_name(name):
        if name == None or name == "":
            raise Exception("Name kan not be blank")
        return name


if __name__ == "__main__":
    p = Player("p")
    s = Player("s", Player.validate_name("Samuel"))
    print(p, "-", s)

    print(s.equals(p))
