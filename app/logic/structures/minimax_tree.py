from game import TicTacToe
from minimax_node import MinimaxNode


class MinimaxTree:
    def __init__(self, game: TicTacToe, bot_turn: bool):
        self.root = MinimaxNode(game, bot_turn)
        self.recent_moves = (None, None)
        self.bot_turn = bot_turn

    def make_move_in_game(self, game: TicTacToe):
        if not self.bot_turn:
            raise ValueError("Its not the ai turn.")

        game.choice_cell(*self.root.moves)

    def update_game(self, actual_game: TicTacToe):
        self.bot_turn = not self.bot_turn

        for node in self.root.children:
            if node.game == actual_game:
                self.root = node
                break
