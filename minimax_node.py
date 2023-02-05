from game import TicTacToe


class MinimaxNode:
    def __init__(self, game: TicTacToe, last_turn_for_bot: bool):
        self.game = game
        self.children = []
        self.score = 0
        self.moves = None
        self.next_turn = not last_turn_for_bot
        self._possible_moves = self._get_possible_moves()

        self.make_all_possible_moves()

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

    def make_all_possible_moves(self):
        #total_moves = 0
        for col, row in self._possible_moves:
            child_score = self.get_next_move_score(col, row)

            self.set_minmax_score((col, row), child_score)
            #self.score += child_score
            #total_moves += 1

        #self.score /= total_moves

    def __repr__(self) -> str:
        return str((self.score, *self.moves))
