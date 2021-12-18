
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

    def __str__(self):
        return "(" + str(self.__row) + ", " + str(self.__col) + ")"

