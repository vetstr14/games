from gridDirection import *
from location import *
from gridLocationIterator import *
from player import *

class Grid:
    __list = []
    __rows = 0
    __columns = 0
    __cells = []

    @classmethod
    def initialiser(cls, Rows, Columns, initialiser):
        i = cls(Rows, Columns)
        i.fill(initialiser)
        return i

    @classmethod
    def initialiser_elm(cls, Rows, Columns, init_Elm):
        i = cls(Rows, Columns)
        i.fill_with_elm(init_Elm)
        return i

    def __init__(self, Rows, Columns):
        self.__rows = Rows
        self.__columns = Columns
        for _ in range(Rows * Columns):
            self.__cells.append(None)

    def place(self, loc: Location, elm: Player) -> None: 
        self.check_location(loc)
        
        self.__cells[self.location_to_index(loc)] = elm

    def check_location(self, loc: Location) -> None:
        if not isinstance(loc, Location):
            raise TypeError("Wrong input: Should be Location")

        if not self.is_on_grid(loc):
            raise IndexError("Row and column indices must be within bounds")

    def is_on_grid(self, loc: Location) -> bool:
        if not isinstance(loc, Location) or loc == None:
            return False
        if loc.get_row() < 0 or loc.get_row() >= self.__rows:
            return False
        
        return loc.get_col() >= 0 and loc.get_col() < self.__columns

    def get(self, loc: Location):
        self.check_location(loc)

        return self.__cells[self.location_to_index(loc)]

    def location_to_index(self, loc: Location) -> int:
        return loc.get_col() + (loc.get_row() * self.__columns)

    def get_rows(self) -> int:
        return self.__rows

    def get_columns(self) -> int:
        return self.__columns

    def get_cells(self) -> list:
        return self.__cells

    def locations(self):
        return GridLocationIterator.iterator(self.get_rows(), self.get_columns())

    def copy(self):
        newGrid = Grid(self.get_rows(), self.get_columns())
        self.fill_copy(newGrid)
        return newGrid

    def fill_copy(self, copy):
        for loc in self.locations():
            copy.place(loc, self.get(loc))

    def fill(self, initialiser):
        if initialiser == None:
            raise Exception("NullPointerException")

        for loc in self.locations():
            try:
                self.place(loc, initialiser[self.location_to_index(loc)][1])
            except IndexError:
                None
    
    def fill_with_elm(self, elm: str):
        for loc in self.locations():
            self.place(loc, elm)

    def get_or_default(self, loc: Location, defaultResult):
        r = self.get(loc)
        if r != None:
            return r
        return defaultResult

    def iterator(self):
        return iter(self.__cells)

    def can_go(self, loc_from: Location, dir: GridDirection) -> bool:
        return self.is_on_grid(loc_from.get_neighbor(dir))

    def contains(self, obj: object):
        return obj in self.__cells

    def location_of(self, obj: object):
        for loc in self.locations():
            p = self.get(loc)
            if isinstance(p, Player):
                if p.equals(obj):
                    return loc
        
        raise Exception("Can not find element")

    def clear(self):
        for loc in self.locations():
            self.place(loc, None)

    
    def __str__(self):
        s = ""
        for c in range(self.__columns * self.__rows):
            cell = self.__cells[c]
            if not cell == None:
                s += str(cell) 
            else:
                s += str(0) 

            if not ((c + 1) % self.__columns) == 0:
                s += " | "
            
            if (c + 1) % self.__columns == 0 and c != 0:
                if not ((c + 1) % self.__rows) == 0:
                    s += "\n"
                    s += (("---" * (self.__columns - 2)) + ("-" * (self.__columns - 1)) + ("--" * 2))
                    s += "\n"
        return "Rows: \t " + str(self.__rows) + "\nColumns: " + str(self.__columns) + "\n\n" + s


if __name__ == "__main__":
    g = Grid(4, 5)
    p = Player("p")
    g.place(Location(0, 0), p)

    print(g)
    print(g.contains(p))