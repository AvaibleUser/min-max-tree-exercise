"""Executes and manage the game"""

from game import TicTacToe


def ask_move(game: TicTacToe) -> None:
    """
    Ask the position of the next move
    """
    turn = "O" if game.turn == 1 else "X"
    print(f"Turn of {turn}")

    print("Col: ", end="")
    col = int(input())

    print("Row: ", end="")
    row = int(input())

    if game.moves == 9:
        raise OverflowError("Its a draw")

    if col < 1 or row < 1 or 3 < col or 3 < row:
        msg = "The given values are invalid. Valid values are between 1 and 3 (included)"
        raise IndexError(msg)

    game.choice_cell(col - 1, row - 1)
    print(f"\n{game}")


def main() -> None:
    """
    Runs the all the game until its finished
    """
    game = TicTacToe()
    print(game)

    while not game.is_winner():
        try:
            ask_move(game)

        except (IndexError, ValueError) as error:
            print(error)

        except OverflowError as error:
            print(error)
            break

    print("Winner")


if __name__ == "__main__":
    main()
