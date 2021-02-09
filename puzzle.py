"""

"""
board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
]
def check_rows(board: str):
    for line in board:
        line = line.replace('*', '')
        line = line.replace(' ', '')
        if len(set(line)) != len(line):
            return False
    return True

print(check_rows(board))
def check_columns(board: str):
    pass


def check_colour(board: str):
    pass


def validate_board(board: str):
    """
    Checks rules of the game
    """
    pass
