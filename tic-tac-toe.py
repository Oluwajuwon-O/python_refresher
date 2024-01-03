
board = [[1,2,3],[4,5,6],[7,8,9]]
a = board[0][0]
b = board[0][1]
c = board[0][2]
d = board[1][0]
e = board[1][1]
f = board[1][2]
g = board[2][0]
h = board[2][1]
i = board[2][2]

# my own solution
def display_board(board):
    print(
    f"""      
    +-------+-------+-------+
    |       |       |       |
    |   {a}   |   {b}   |   {c}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {d}   |   {e}   |   {f}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {g}   |   {h}   |   {i}   |
    |       |       |       |
    +-------+-------+-------+
    """
    )


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.

        