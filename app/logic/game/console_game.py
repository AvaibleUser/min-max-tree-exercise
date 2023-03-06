"""Executes and manage the game"""

from . import TicTacToe
from . import MinimaxTree


def ask_to_human_move(game: TicTacToe) -> None:
    """
    Ask the position of the next move, throws an error everytime that don't make the move
    """
    print("Col: ", end="")
    col = int(input())

    print("Row: ", end="")
    row = int(input())

    if col < 1 or row < 1 or 3 < col or 3 < row:
        msg = "The given values are invalid. Valid values are between 1 and 3 (included)"
        raise IndexError(msg)

    game.choice_cell(col - 1, row - 1)


def main() -> None:
    """
    Runs the all the game until its finished
    """
    human_turn = True
    game = TicTacToe()
    tree = MinimaxTree(game, not human_turn)

    print(game)

    while not game.is_winner() and game.moves < 9:
        turn = "O" if game.turn == 1 else "X"
        print(f"Turn of {turn}")

        try:
            if human_turn:
                ask_to_human_move(game)
                tree.update_game(game)
                human_turn = False

            else:
                tree.make_move_in_game(game)
                tree.update_game(game)

                print("\nThe ai move was")
                print(f"col: {tree.root.moves[0] + 1}")
                print(f"row: {tree.root.moves[1] + 1}")

                human_turn = True

        except (IndexError, ValueError) as error:
            print(error)

        except OverflowError as error:
            print(error)
            break

        finally:
            print(f"\n{game}")

    if game.is_winner():
        print(f"The winner is... the {'human' if not human_turn else 'ai'}")

    else:
        print("Its a draw")


if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        pass
