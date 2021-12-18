from location import *

class Grid:
    __rows = 0
    __columns = 0
    __cells = []

    def __init__(self, Rows, Columns):
        self.__rows = Rows
        self.__columns = Columns
        for _ in range(Rows * Columns):
            self.__cells.append(None)

    def place(self, loc: Location, elm: str) -> None: 
        if not isinstance(loc, Location):
            raise TypeError("Wrong input: Should be Location")

        self.check_location(loc)
        
        self.__cells[self.location_to_index(loc)] = elm

    def check_location(self, loc: Location) -> None:
        if not isinstance(loc, Location):
            raise TypeError("Wrong input: Should be Location")

        if not self.is_on_grid(loc):
            raise IndexError("Row and column indices must be within bounds")

    def is_on_grid(self, loc: Location) -> bool:
        if not isinstance(loc, Location):
            return False
        if loc.get_row() < 0 or loc.get_row() >= self.__rows:
            return False
        
        return loc.get_col() >= 0 and loc.get_col() < self.__columns

    def get(self, loc: Location) -> str:
        self.check_location(loc)

        return self.__cells[self.location_to_index(loc)]

    def location_to_index(self, loc: Location) -> int:
        return loc.get_row() + (loc.get_col() * self.__rows)

    def get_rows(self) -> int:
        return self.__rows

    def get_columns(self) -> int:
        return self.__columns
    
    def __str__(self):
        s = ""
        for c in range(self.__columns * self.__rows):
            cell = self.__cells[c]
            if not cell == None:
                s += str(cell) 
            else:
                s += str(0) 

            if not ((c + 1) % self.__rows) == 0:
                s += " | "
            
            if (c + 1) % self.__rows == 0 and c != 0:
                if not ((c + 1) % self.__columns) == 0:
                    s += "\n"
                    s += (("---" * (self.__rows - 2)) + ("-" * (self.__rows - 1)) + ("--" * 2))
                    s += "\n"
        return "Rows: \t " + str(self.__rows) + "\nColumns: " + str(self.__columns) + "\n\n" + s


if __name__ == "__main__":
    g = Grid(5, 4)

    l = Location(1,2)
    print(l)

    g.place(l, "t")
    print(g.get(l))

    print(g)