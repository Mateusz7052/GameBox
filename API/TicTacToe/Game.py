import Board
import Tile


class Game:
    """
    Controls a game of TicTacToe

    Attributes:
        board (Board): The board with the current game

    Methods:
        check_win (bool): Returns True if the given character has won the game. False otherwise
        check_draw (bool): Returns True if the game is drawn. False otherwise
    """

    def __init__(self):
        self.board = Board(3)

    def check_win(self, char: str) -> bool:
        winning_combinations = [
            # Rows
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # Columns
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            # Diagonals
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]]

        for combo in winning_combinations:
            if self.board[combo[0][0]][combo[0][1]].character == \
               self.board[combo[1][0]][combo[1][1]].character == \
               self.board[combo[2][0]][combo[2][1]].character == char:
                return True
        return False

    def check_draw(self) -> bool:
        # If there is no empty tiles in the board, it is a draw
        for i in range(self.board.board_size):
            for j in range(self.board.board_size):
                if self.board[i][j].character == "":
                    return False
        return True
