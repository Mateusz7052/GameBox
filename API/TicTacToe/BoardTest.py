import unittest
from Tile import Tile
from Board import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        # Create a 3x3 Tic-Tac-Toe board for testing
        self.board = Board(3)

    def test_board_initialization(self):
        # Test if the board is initialized with the correct size
        self.assertEqual(len(self.board.tiles), 3)
        self.assertEqual(len(self.board.tiles[0]), 3)
        self.assertEqual(self.board.total_tiles, 9)

        # Ensure all tiles are empty initially
        for row in self.board.tiles:
            for tile in row:
                self.assertEqual(tile.character, "")

    def test_add_tile_success(self):
        # Add a tile to an empty spot and check if it is added correctly
        tile = Tile("X")
        added = self.board.add_tile(tile, 1, 1)
        self.assertTrue(added)
        self.assertEqual(self.board.tiles[1][1].character, "X")

    def test_add_tile_fail(self):
        # Add a tile to an occupied spot and check that it is not overwritten
        tile_x = Tile("X")
        tile_o = Tile("O")

        self.board.add_tile(tile_x, 0, 0)  # First tile added
        added = self.board.add_tile(tile_o, 0, 0)  # Try to add to the same spot
        self.assertFalse(added)
        self.assertEqual(self.board.tiles[0][0].character, "X")  # Still X


if __name__ == "__main__":
    unittest.main()
