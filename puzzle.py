"""

"""


def check_rows(board: list):
    """
    Checks rows

    >>> check_rows(["     9 5 "," 6  83  *"])
    True
    """
    for line in board:
        line = line.replace('*', '')
        line = line.replace(' ', '')
        if len(set(line)) != len(line):
            return False
    return True


def check_columns(board: list):
    """
    Checks columns

    >>> check_columns(["***1 ****", "** 13****"])
    False
    """
    inverse_board = []
    for index in range(9):
        temp = ""
        for line in board:
            temp += line[index]
        inverse_board.append(temp)
    return check_rows(inverse_board)


def check_colour(board: list):
    """
    Checks colour

    >>> check_colour(["**** ****","***1 ****","**  3****","* 4 1****","     9 5 "," 6  83  *",\
"3   1  **","  8  2***","  2  ****"])
    True
    """
    for index in range(9):
        temp = []
        for line in range(9-index):
            if board[line][index] != '*' and board[line][index] != ' ':
                temp.append(board[line][index])
        for number in board[8-index][index+1:]:
            if number != '*' and number != ' ':
                temp.append(number)
        if len(set(temp)) != len(temp):
            return False
    return True


def validate_board(board: list):
    """
    Checks rules of the game
    """
    return check_rows(board) and check_columns(board) and check_colour(board)
