import random
import threading
from game import TicTacToe
from minimax_node import MinimaxNode


class MinimaxTree:
    def __init__(self, bot_turn: bool):
        self.root = None
        self.recent_moves = (None, None)
        self.bot_turn = bot_turn

    def assign_root(self, game: TicTacToe, bot_turn: bool):
        self.root = MinimaxNode(game, bot_turn)

    @staticmethod
    def get_random_moves(game: TicTacToe):
        moves = []
        for i in range(9):
            if game.board[i] == 0:
                moves.append(i)

        move = random.randint(0, len(moves) - 1)

        return (move % 3, move // 3)

    def init_nodes_creation(self, game):
        nodes_thread = threading.Thread(
            target=self.assign_root, args=(game, self.bot_turn))
        nodes_thread.start()
        nodes_thread.join()

    def make_move_in_game(self, game: TicTacToe):
        if not self.bot_turn:
            raise ValueError("Its not the ai turn.")

        #if self.root is None or self.root.moves is None:
        #    self.recent_moves = MinimaxTree.get_random_moves(game)

        else:
            self.recent_moves = self.root.moves

        game.choice_cell(*self.recent_moves)

    def update_game(self, actual_game: TicTacToe):
        #if actual_game.moves == 3:
        #    self.init_nodes_creation(actual_game)

        self.bot_turn = not self.bot_turn

        #if actual_game.moves < 4:
        #    return

        for node in self.root.children:
            if node.game == actual_game:
                self.root = node
                break
