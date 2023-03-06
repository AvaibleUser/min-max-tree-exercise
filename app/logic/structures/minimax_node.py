import threading
from game import TicTacToe


class MinimaxNode:
    first_human_moves = {}
    first_bot_moves = {}

    def __init__(self, game: TicTacToe, last_turn_for_bot: bool):
        self.game = game
        self.children = []
        self.score = 0
        self.moves = None
        self.next_turn = not last_turn_for_bot
        self._possible_moves = self._get_possible_moves()

        self._set_values_if_exists()

    def _set_values_if_exists(self):
        if self.game.moves == 0:
            if self.next_turn and MinimaxNode.first_human_moves:
                self.moves = MinimaxNode.first_human_moves["moves"]
                self.children = MinimaxNode.first_human_moves["children"]

            elif not self.next_turn and MinimaxNode.first_bot_moves:
                self.moves = MinimaxNode.first_bot_moves["moves"]
                self.children = MinimaxNode.first_bot_moves["children"]

            else:
                self._make_all_possible_moves_threading()

        else:
            for col, row in self._possible_moves:
                self.make_next_move(col, row)

    def _get_possible_moves(self) -> tuple[tuple[int, int], ...]:
        if self.game.moves == 0:
            return tuple((col, row) for col in range(3) for row in range(3))

        moves = []
        for move in range(9):
            if self.game.board[move] == 0:
                moves.append((move % 3, move // 3))

        return tuple(moves)

    def get_next_move_score(self, col: int, row: int):
        child_node_game = TicTacToe(
            self.game.turn, self.game.moves, self.game.board)

        child_node_game.choice_cell(col, row)

        if child_node_game.is_winner():
            return 100 if self.next_turn else -100

        if child_node_game.moves == 9:
            return -50

        new_node = MinimaxNode(child_node_game, self.next_turn)
        self.children.append(new_node)
        return new_node.score

    def set_minmax_score(self, moves: tuple[int, int], child_score: int):
        if self.moves is None:
            self.moves = moves
            self.score = child_score

        elif self.next_turn and self.score < child_score:
            self.moves = moves
            self.score = child_score

        elif not self.next_turn and self.score > child_score:
            self.moves = moves
            self.score = child_score

    def make_next_move(self, col: int, row: int):
        child_score = self.get_next_move_score(col, row)
        self.set_minmax_score((col, row), child_score)

    def _make_all_possible_moves_threading(self):
        threads = []

        for col, row in self._possible_moves:
            threads.append(threading.Thread(
                target=self.make_next_move, args=(col, row)))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        if self.next_turn:
            MinimaxNode.first_human_moves = {
                "moves": self.moves, "children": self.children}

        else:
            self.first_bot_moves = {
                "moves": self.moves, "children": self.children}

    def __repr__(self) -> str:
        return str((self.score, *self.moves))
