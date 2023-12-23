"""
matthew Yoon
"""


def make_board() -> dict:
    """
    Create playboard for tic-tac-toe

    :precondition: game is starting and there is no clean board available
    :postcondition: creates dictionary with the correct amount of key value pairs representing a tile on the board
                    each key will be a tuple with the first value representing the x coordinate and the second the y
    :return: dictionary with tuple keys and None as values

    >>> make_board()
    {(0, 0): None, (0, 1): None, (0, 2): None, (1, 0): None, (1, 1): None, (1, 2): None, (2, 0): None, (2, 1): None, (2, 2): None}
    """
    return {(x, y): None for x in range(3) for y in range(3)}


def get_user_name() -> str:
    """

    :precondition: there is no name accosciated with player
    :postcondition: removes excess white space around input
    :return: string representing a player name
    """
    player_name = input("enter player name: \n")
    return player_name.strip()


def player_choice(board: dict) -> tuple:
    """
    :precondition:
    :postcondition:
    :return:
    """
    while True:
        column = get_player_xy()
        row = get_player_xy()
        user_coordinate = (column, row)
        if board[user_coordinate] is None:
            return user_coordinate
        else:
            print("invalid coordinate")


def get_player_xy() -> int:
    """

    :return:
    """
    accepted_input = range(3)
    while True:
        user_input = input("enter an integer for coordinate between 0-2:\n")
        user_input = user_input.strip()
        try:
            user_input = int(user_input)
        except ValueError:
            print("type an integer\n")
        else:
            if user_input in accepted_input:
                return user_input


def change_board(board: dict, player_1: str, player_with_input: str, user_input: tuple):
    board[user_input] = player_with_input == player_1


def check_winner(board: dict) -> bool:
    # match board:
    #     case (0,_):
    pass


def print_board(board: dict):
    for row in range(3):
        row_to_print = ""
        for column in range(3):
            if board[(column, row)] is None:
                row_to_print += "_"
            elif board[(column, row)]:
                row_to_print += "X"
            else:
                row_to_print += "O"
        print(row_to_print)
    return


def run_ttt():
    player_1 = get_user_name()
    player_2 = get_user_name()
    board = make_board()
    winner = None
    while winner is None:
        print_board(board)
        print(f"{player_1}'s turn")
        player_1_input = player_choice(board)
        change_board(board, player_1, player_1, player_1_input)
        print_board(board)
        if check_winner(board):
            winner = player_1
        else:
            print(f"{player_2}'s turn")
            player_2_input = player_choice(board)
            change_board(board, player_1, player_2, player_2_input)
            if check_winner(board):
                winner = player_2
    print(f"the winner is {winner}")


def main():
    run_ttt()


if __name__ == "__main__":
    main()
