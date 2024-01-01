
# these are two ways to create the board


# my own solution
def display_board():
    digits = [[1,2,3],[4,5,6],[7,8,9]]
    board = f"""      
    +-------+-------+-------+
    |       |       |       |
    |   {digits[0][0]}   |   {digits[0][1]}   |   {digits[0][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {digits[1][0]}   |   {digits[1][1]}   |   {digits[1][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {digits[2][0]}   |   {digits[2][1]}   |   {digits[2][2]}   |
    |       |       |       |
    +-------+-------+-------+
    """
    print(board)

display_board()


# cisco solution
board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
print("+-------" * 3,"+", sep="")
for row in range(3):
    print("|       " * 3,"|", sep="")
    for col in range(3):
        print("|   " + str(board[row][col]) + "   ", end="")
    print("|")
    print("|       " * 3,"|",sep="")
    print("+-------" * 3,"+",sep="")