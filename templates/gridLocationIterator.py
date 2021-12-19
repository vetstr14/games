from gridDirection import *
from location import *
from grid import *

class GridLocationIterator:
    __rows = 0
    __columns = 0
    __current = Location(0, 0)

    @classmethod
    def grid_iterator(cls, grid):
        if isinstance(grid, Grid):
            s = cls(grid.get_rows(), grid.get_columns())
            iterable = iter(s)
            return iterable

        return None

    @classmethod
    def iterator(cls, rows, columns, current: Location = Location(0,0)):
        s = cls(rows, columns, current)
        iterable = iter(s)
        return iterable

    def __init__(self, rows, columns, current: Location = Location(0,0)):
        self.__rows = rows
        self.__columns = columns
        self.__current = current

    def __iter__(self):
        return self

    def hasNext(self) -> bool:
        return self.__current.get_row() <  self.__rows and self.__current.get_col() < self.__columns

    def __next__(self):
        if not self.hasNext():
            raise StopIteration
        elm = self.__current
        if self.__current.get_col() < self.__columns - 1:
            self.__current = self.__current.get_neighbor(GridDirection.east())
        else:
            self.__current = Location(self.__current.get_row() + 1, 0)
        
        return elm

    def __str__(self):
        return str(self.__current)


if __name__ == "__main__":
    iterator = GridLocationIterator.iterator(2, 2, Location(0,0))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    