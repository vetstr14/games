from location import *

class GridDirection:
    @classmethod
    def east(cls): return cls((1,0))
    @classmethod
    def north(cls): return cls((0, -1))
    @classmethod
    def west(cls): return cls((-1, 0))
    @classmethod
    def south(cls): return cls((0, 1))
    @classmethod
    def northeast(cls): return cls((1, -1))
    @classmethod
    def northwest(cls): return cls((-1, -1))
    @classmethod
    def southwest(cls): return cls((-1, 1))
    @classmethod
    def southeast(cls): return cls((1, 1))
    @classmethod
    def center(cls): return cls((0, 0))

    FOUR_DIRECTIONS = list(((1,0), (0, -1), (-1, 0), (0, 1)))
    EIGHT_DIRECTIONS = list(((1,0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)))
    NINE_DIRECTIONS = list(((1,0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (0, 0)))

    __dx = 0
    __dy = 0

    def __init__(self, direction: tuple):
        self.__dx = direction[0]
        self.__dy = direction[1]

    def get_neighbor(self, loc): 
        return Location(loc.get_row() + self.__dy, loc.get_col() + self.__dx)

    def __str__(self):
        return "x = " + str(self.__dx) + "\ty = " + str(self.__dy)

if __name__ == "__main__":
    print(GridDirection.east())
    east = GridDirection.east()
    g = GridDirection(GridDirection.EIGHT_DIRECTIONS[0])
    print(g)
    print(g.FOUR_DIRECTIONS)
    