class Tile:
    """
    Represents a single tile on a Tic-Tac-Toe board.

    A Tile can hold one of three states:
    - "X": representing a move by player X
    - "O": representing a move by player O
    - "": representing an empty tile

    Attributes:
        character (str): The character representing the state of the tile, either "X", "O", or an empty string.

    Methods:
        __str__(): Returns a string representation of the tile for display.
        __repr__(): Returns the same string representation as __str__().
    """

    def __init__(self, character: str = "") -> None:
        self.character = character.upper()

    def __str__(self):
        if self.character == "X":
            return "|X|"
        elif self.character == "O":
            return "|O|"
        else:
            return "| |"

    def __repr__(self):
        return self.__str__()
