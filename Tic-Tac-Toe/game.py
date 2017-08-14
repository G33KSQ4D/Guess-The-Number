"""
[1] Create a new tic-tac-toe board

Main Loop:
[2] Display the tic-tac-toe board
[3] Ask for user input
[5] Update the board (If you can, warn them is spot is taken/not available)
[6] Check if the player won

Prototype board:
----------------------
| //\\ | \\// | //\\ |
| \\// | //\\ | \\// |
----------------------
| \\// | //\\ | \\// |
| //\\ | \\// | //\\ |
----------------------
| 7777 | 8888 | 9999 |
| 7777 | 8888 | 9999 |
----------------------

Prototype:
    \\//
    //\\

Prototype:
    //\\
    \\//
"""

import time


def main():
    print("Welcome to Tic-Tac-Toe!\n")

    while True:
        board = create_board()
        symbol = pick_a_symbol()
        game_loop(board, symbol)

        # For when the game restarts
        clear_screen()


def game_loop(board, symbol):
    while True:
        display_board(board)
        spot = user_input(symbol)
        update_board(board, spot, symbol)

        # If anyone won the game
        if check_win_condition(board, symbol):
            # Since the win message is long I'll to a longer wait time
            time.sleep(2)
            break

        symbol = change_symbol(symbol)
        time.sleep(0.75)


def change_symbol(symbol):
    if symbol == "x":
        return "o"
    else:
        return "x"


def get_symbol(symbol):
    symbol_x = [
        [" \\\\// "],
        [" //\\\\ "]
    ]
    symbol_o = [
        [" //\\\\ "],
        [" \\\\// "]
    ]

    if symbol == "x":
        return symbol_x
    else:
        return symbol_o


def pick_a_symbol():
    while True:
        symbol = input("Do you want to be X or O: ")[0].lower()

        if symbol == "x":
            return "x"
        elif symbol == "o":
            return "o"


def create_board():
    """
    ANOTHER VERSION OF THE BOARD:
    IDEA: MAKE THE USER CHOOSE WHICH BOARD THEY WANT
    ["----------------------"],
    ["|", [" 1111 "], "|", [" 2222 "], "|", [" 3333 "], "|"],
    ["|", [" 1111 "], "|", [" 2222 "], "|", [" 3333 "], "|"],
    ["----------------------"],
    ["|", [" 4444 "], "|", [" 5555 "], "|", [" 6666 "], "|"],
    ["|", [" 4444 "], "|", [" 5555 "], "|", [" 6666 "], "|"],
    ["----------------------"],
    ["|", [" 7777 "], "|", [" 8888 "], "|", [" 9999 "], "|"],
    ["|", [" 7777 "], "|", [" 8888 "], "|", [" 9999 "], "|"],
    ["----------------------"]
    """

    board = [

        [" "],
        [" ", [" 1111 "], "|", [" 2222 "], "|", [" 3333 "], " "],
        [" ", [" 1111 "], "|", [" 2222 "], "|", [" 3333 "], " "],
        ["----------------------"],
        [" ", [" 4444 "], "|", [" 5555 "], "|", [" 6666 "], " "],
        [" ", [" 4444 "], "|", [" 5555 "], "|", [" 6666 "], " "],
        ["----------------------"],
        [" ", [" 7777 "], "|", [" 8888 "], "|", [" 9999 "], " "],
        [" ", [" 7777 "], "|", [" 8888 "], "|", [" 9999 "], " "],
        [" "]
    ]

    return board


def display_board(board):
    clear_screen()

    temp_string = ""

    for row in board:
        for col in row:
            if type(col) != list:
                temp_string += "".join(col)
            else:
                for content in col:
                    temp_string += content
        print(temp_string)
        temp_string = ""


def user_input(player):
    while True:
        # Abs in case they enter negative number
        move = str(input("Player '{0}'s turn: ".format(player.upper())))

        if type(move) == str and move.isdigit():
            move = int(move)

        if type(move) == int and move >= 1 and move <= 9:
            break

    return move


def update_board(board, spot, symbol):
    # Will get me the ASCII symbol
    symbol_sign = get_symbol(symbol)

    # Checks if a given spot is available
    if spot == 1 and board[1][1] == [" 1111 "]:
        board[1][1] = symbol_sign[0][0]
        board[2][1] = symbol_sign[1][0]
    elif spot == 2 and board[1][3] == [" 2222 "]:
        board[1][3] = symbol_sign[0][0]
        board[2][3] = symbol_sign[1][0]
    elif spot == 3 and board[1][5] == [" 3333 "]:
        board[1][5] = symbol_sign[0][0]
        board[2][5] = symbol_sign[1][0]

    elif spot == 4 and board[4][1] == [" 4444 "]:
        board[4][1] = symbol_sign[0][0]
        board[5][1] = symbol_sign[1][0]
    elif spot == 5 and board[4][3] == [" 5555 "]:
        board[4][3] = symbol_sign[0][0]
        board[5][3] = symbol_sign[1][0]
    elif spot == 6 and board[4][5] == [" 6666 "]:
        board[4][5] = symbol_sign[0][0]
        board[5][5] = symbol_sign[1][0]

    elif spot == 7 and board[7][1] == [" 7777 "]:
        board[7][1] = symbol_sign[0][0]
        board[8][1] = symbol_sign[1][0]
    elif spot == 8 and board[7][3] == [" 8888 "]:
        board[7][3] = symbol_sign[0][0]
        board[8][3] = symbol_sign[1][0]
    elif spot == 9 and board[7][5] == [" 9999 "]:
        board[7][5] = symbol_sign[0][0]
        board[8][5] = symbol_sign[1][0]
    else:
        print("Spot not available. Lost your turn. --FIX--")


def check_win_condition(board, player):
    # Checks if any players won

    # Hard to explain, but best I can say is, each of the 9 spots
    # On the board start with //\\ and \\//. The symbol O start with //\\
    # And X starts with \\//. That's the best I can do

    if player == "x":
        symbol = " \\\\// "
    else:
        symbol = " //\\\\ "

    # Checking horizontal rows
    if board[1][1] == symbol and board[1][3] == symbol and board[1][5] == symbol:
        print("Player {0} has won with pattern: {1}".format(player, "1-2-3"))
        return True
    if board[4][1] == symbol and board[4][3] == symbol and board[4][5] == symbol:
        print("Player {0} has won with pattern: {1}".format(player, "4-5-6"))
        return True
    if board[7][1] == symbol and board[7][3] == symbol and board[7][5] == symbol:
        print("Player {0} has won with pattern: {1}".format(player, "7-8-9"))
        return True

    # Checking vertical columns
    if board[1][1] == symbol and board[4][1] == symbol and board[7][1] == symbol:
        print("Player {0} has won with pattern: {1}".format(player, "1-4-7"))
        return True
    if board[1][3] == symbol and board[4][3] == symbol and board[7][3] == symbol:
        print("Player {0} has won with pattern: {1}".format(player, "2-5-8"))
        return True
    if board[1][5] == symbol and board[4][5] == symbol and board[7][5] == symbol:
        print("Player {0} has won with pattern: {1}".format(player, "3-6-9"))
        return True

    # Checking diagonal patterns
    # Top-left to bottom-right
    if board[1][1] == symbol and board[4][3] == symbol and board[7][5] == symbol:
        print("Player {0} has won with pattern: {1}".format(player, "1-3-5"))
        return True
    # Bottom-left to top-right
    if board[7][1] == symbol and board[4][3] == symbol and board[1][5] == symbol:
        print("Player {0} has won with pattern: {1}".format(player, "4-5-6"))
        return True

    # Check if a draw was made


def clear_screen():
    print('\n'*50)


if __name__ == "__main__":
    main()
