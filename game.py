"""
Conforms all the things related to the game, with a principal class that represent the game itself.
"""


class TicTacToe:
    """
    Class that represents the game
    """

    def __init__(self, turn=1, moves=0, _board=[0 for _ in range(9)]):
        self.turn = turn
        self.moves = moves
        self._board = _board[:]

    @property
    def board(self):
        return self._board

    def choice_cell(self, col: int, row: int) -> None:
        """
        Choise a cell to fill with the actual mark
        """
        cell = col + 3 * row

        if self._board[cell] != 0:
            raise ValueError('That cell is alredy taked')

        self._board[cell] = self.turn
        self.turn *= -1
        self.moves += 1

    def is_winner(self) -> bool:
        """
        Check if there is a winner, returning True if yes, False otherwise
        """
        if self.moves < 5:
            return False

        lines = self._get_lines()

        for line in lines:
            if abs(sum(line)) == 3:
                return True

        return False

    def _get_lines(self) -> list:
        """
        Return Fal the lines where it can be a winner
        """
        lines = []

        for i, j in enumerate(range(0, 9, 3)):
            lines.append(self._board[j:j + 3])
            lines.append(self._board[i:9:3])

        lines.append([self._board[0], self._board[4], self._board[8]])
        lines.append([self._board[2], self._board[4], self._board[6]])

        return lines

    def __str__(self) -> str:
        _board = ""

        for i in range(9):
            if i % 3 != 0:
                _board += "|"

            match self._board[i]:
                case -1: _board += " X "
                case 1: _board += " O "
                case _: _board += "   "

            if (i + 1) % 3 == 0:
                _board += "\n---|---|---\n"

        return _board

    def __repr__(self) -> str:
        string = "["
        for num in self._board:
            value = " "

            if num == -1:
                value = "X"

            elif num == 1:
                value = "O"

            string += f"{value},"

        string += "]"
        return string

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, TicTacToe) and self._board == __o._board
