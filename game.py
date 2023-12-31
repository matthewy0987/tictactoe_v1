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
        print("ERROR: enter an acceptable integer (0-2)")


def change_board(board: dict, player_1: str, player_with_input: str, user_input: tuple):
    board[user_input] = player_with_input == player_1


def check_winner(board: dict) -> bool:
    """
    Determine if there is a winner

    :param board: dictionary representing the board state
    :precondition: change has been made to board recently
                   board must be a dictionary representing the game board
    :postcondition: correctly determines if there is a winner
                    if there eis a winner returns True otherwise False
    :return: Boolean value representing if there is a winner
    """
    board_list = board.items()
    if column_check(board_list):
        return True
    elif row_check(board_list):
        return True
    elif cross_check_l_r(board_list):
        return True
    elif cross_check_r_l(board_list):
        return True
    else:
        return False


def column_check(items) -> bool:
    current = 0
    while current <= 2:
        current_items = filter(lambda a: a[0][0] == current, items)
        true_count = 0
        false_count = 0
        for item in current_items:
            if item[1] is None:
                continue
            elif item[1]:
                true_count += 1
            else:
                false_count += 1
        if true_count == 3 or false_count == 3:
            return True
        current += 1
    return False


def row_check(items) -> bool:
    current = 0
    while current <= 2:
        current_items = filter(lambda a: a[0][1] == current, items)
        true_count = 0
        false_count = 0
        for item in current_items:
            if item[1] is None:
                continue
            elif item[1]:
                true_count += 1
            else:
                false_count += 1
        if true_count == 3 or false_count == 3:
            return True
        current += 1
    return False


def cross_check_l_r(items) -> bool:
    cross_left_right = set([(0, 0), (1, 1), (2, 2)])
    filtered_l_r = filter(lambda a: a[0] in cross_left_right, items)
    true_count = 0
    false_count = 0
    for item in filtered_l_r:
        if item[1] is None:
            continue
        elif item[1]:
            true_count += 1
        else:
            false_count += 1
    if true_count == 3 or false_count == 3:
        return True
    return False


def cross_check_r_l(items) -> bool:
    cross_right_left = {(0, 2), (1, 1), (2, 0)}
    filtered_r_l = filter(lambda a: a[0] in cross_right_left, items)
    true_count = 0
    false_count = 0
    for item in filtered_r_l:
        if item[1] is None:
            continue
        elif item[1]:
            true_count += 1
        else:
            false_count += 1
    if true_count == 3 or false_count == 3:
        return True
    return False


def check_draw(board: dict) -> bool:
    filtered = [value for value in board.values() if value is None]
    return len(filtered) == 0


def check_rain(board, user_input):
    32


def print_board(board: dict):
    """
    print message displaying game board

    player one is represented using 'X' and player two is represented using 'O' blank paces with '_'

    :param board: dictionary representing current state of board
    :precondition: current board state has not been displayed yet
    :postcondition: message is displayed that correctly displays the board
    """
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


def quit_input() -> bool:
    """
    determine if players want to continue playing

    :precondition: game has completed
    :postcondition: correctly determine if player would like to continue
                    if (N)o than True, player does not want to continue
                    if (Y)es then False, player wants to keep playing
    :return: boolean value representing if player want to continue
    """
    accepted_input = ["y", "n", "Y", "N"]
    while True:
        user_input = input("continue? (Y/N)\n")
        if user_input in accepted_input:
            user_input = user_input.strip()
            return user_input.upper() == "N"
        else:
            print("please enter 'y' or 'n'")


def populate_win_count(count: dict, name_one: str, name_two: str) -> dict:
    """
    add player keys to dictionary

    :param count: dictionary holding the number of an outcome
    :param name_one: string representing plyer one
    :param name_two: string representing player two
    :precondition: dictionary keeping track of wins has not been populated yet
                   count must be a dictionary with key 'draws' already in it
                   name_one must be a string not yet in count
                   name_two must be a string not yet in count
    :postcondition: count dictionary has keys name_one and name_two added with values being integer 0
    :return: dictionary that has had keys added
    """
    count[name_one] = 0
    count[name_two] = 0
    return count


def handle_ending(winner: str, count: dict):
    """
    Perform actions for ending sequence

    ending sequence includes printing messages and changing winner count dictionary

    :param winner: string representing winning player
    :param count: dictionary holding the amount of times a player has won or draw has occurred
    :precondition: game has just been completed
                   winner must be a string representing the winning player
                   count must be a dictionary that has the winner string as a key
    :postcondition: count dictionary values is correctly changed based on outcome of game
    """
    if winner == "draws":
        print("result is a draw")
    else:
        print(f"the winner is {winner}")
    count[winner] += 1
    for key in count.keys():
        if key == "draws":
            print(f"{key}: {count[key]}")
        else:
            print(f"{key}: {count[key]} wins")


def wants_to_swap() -> bool:
    """
    determine if players want to swap who goes first

    :precondition: game has completed
    :postcondition: correctly determine if player would like to swap turns
                    if (N)o than False, player does not want to swap
                    if (Y)es then True, player wants to swap
    :return: boolean value representing if player want to swap
    """
    accepted_input = ["y", "n", "Y", "N"]
    while True:
        user_input = input("want to swap who goes first?(Y/N)\n")
        if user_input in accepted_input:
            user_input = user_input.strip()
            return user_input.upper() == "Y"
        else:
            print("please enter 'y' or 'n'")


def run_ttt():
    """
    drive the game
    """
    want_to_continue = True
    win_count = {"draws": 0}
    player_1 = get_user_name()
    player_2 = get_user_name()
    populate_win_count(win_count, player_1, player_2)
    while want_to_continue:
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
            elif check_draw(board):
                winner = "draws"
            else:
                print(f"{player_2}'s turn")
                player_2_input = player_choice(board)
                change_board(board, player_1, player_2, player_2_input)
                if check_winner(board):
                    winner = player_2
        handle_ending(winner, win_count)
        if quit_input():
            want_to_continue = False
            print("Thanks for Playing")
        elif wants_to_swap():
            placeholder = player_1
            player_1 = player_2
            player_2 = placeholder


def main():
    run_ttt()


if __name__ == "__main__":
    main()
