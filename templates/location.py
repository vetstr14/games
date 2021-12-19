from gridDirection import *

class Location:
    __row = 0
    __col = 0
    def __init__(self, Row, Col):
        self.__row = Row
        self.__col = Col

    def get_row(self) -> int:
        return self.__row

    def get_col(self) -> int:
        return self.__col

    def equals(self, loc) -> bool:
        if isinstance(loc, Location):
            return self.__row == loc.get_row() and self.__col == loc.get_col()
        
        return False

    def grid_distance_to(self, loc) -> int:
        return abs(self.__row - loc.get_row()) + abs(self.__col - loc.get_col())

    def get_neighbor(self, dir):
        return dir.get_neighbor(self)

    def get_all_neighbors(self) -> list:
        neighbors = []
        for direction in GridDirection.EIGHT_DIRECTIONS:
            d = GridDirection(direction)
            neighbors.append(self.get_neighbor(d))
        
        return neighbors

    def direction_to(self, loc):
        bestDir = GridDirection.center()
        bestDist = self.grid_distance_to(loc)
        for direction in GridDirection.EIGHT_DIRECTIONS:
            d = GridDirection(direction)
            neighbor = self.get_neighbor(d)
            curDist = neighbor.grid_distance_to(loc)
            if curDist < bestDist:
                bestDist = curDist
                bestDir = d

        return bestDir

    def __str__(self):
        return "(" + str(self.__row) + ", " + str(self.__col) + ")"

if __name__ == "__main__":
    l = Location(0, 1)
    e = GridDirection.east()
    print(l)
    print(l.get_neighbor(e))

    l.get_all_neighbors()

