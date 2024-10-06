from Tile import Tile
from typing import List


class Board:
    """
    Represents a Tic-Tac-Toe board.

    The Board is initialized with a specified size and consists of a grid of tiles.
    Each tile can be empty or contain a character representing a move by either player.

    Attributes:
        board_size (int): The size of the board (number of rows and columns).
        total_tiles (float): The total number of tiles on the board.
        tiles (List[List[Tile]]): A 2D list containing Tile objects representing the board.

    Methods:
        __str__(): Returns a string representation of the board for display.
        __repr__(): Returns the same string representation as __str__().
        add_tile(Tile, int, int): Adds the tile to the tiles 2D list at specified position.
            Returns True if tile was added. Returns False if position was already taken.
    """

    def __init__(self, board_size: int):
        self.board_size = board_size
        self.total_tiles: float = board_size * board_size
        self.tiles: List[List[Tile]] = []

        for _ in range(self.board_size):
            rows = []

            for _ in range(self.board_size):
                rows.append(Tile())

            self.tiles.append(rows)

    def __str__(self):
        return "\n".join(
            ["".join([str(tile) for tile in tile_row]) for tile_row in self.tiles]
        )

    def __repr__(self):
        return self.__str__()

    def add_tile(self, tile: Tile, row: int, col: int) -> bool:
        if self.tiles[row][col].character == "":
            self.tiles[row][col] = tile
            return True
        else:
            return False
