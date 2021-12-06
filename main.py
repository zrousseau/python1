def array_flip():
    array = [['.', '.', '.', '.', '.', '.'],
             ['.', 'O', 'O', '.', '.', '.'],
             ['O', 'O', 'O', 'O', '.', '.'],
             ['O', 'O', 'O', 'O', 'O', '.'],
             ['.', 'O', 'O', 'O', 'O', 'O'],
             ['O', 'O', 'O', 'O', 'O', '.'],
             ['O', 'O', 'O', 'O', '.', '.'],
             ['.', 'O', 'O', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.']]
    for i in range(6):
        for j in range(9):
            print(array[j][i], end="")
        print()


# Tic Tac Toe Time
import random

def display_board(board):
    print("+-------"*3,"+", sep="")
    print("|       "*4)
    print(f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |")
    print("|       "*4)
    print("+-------" * 3, "+", sep="")
    print("|       " * 4)
    print(f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
    print("|       " * 4)
    print("+-------" * 3, "+", sep="")
    print("|       " * 4)
    print(f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
    print("|       " * 4)
    print("+-------" * 3, "+", sep="")
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            move = int(input("What is your move: "))
        except:
            print("Please enter a number between 1 and 9")
            continue
        if(move > 9 or move <1):
            print("Please enter a number between 1 and 9")
            continue
        for i in range(3):
            for j in range(3):
                if(move == board[i][j]):
                    grid[i][j] = 'O'
                    return board
        print("That is not a free move")
        continue




def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    print("Making list")
    free_squares.clear()
    for i in range(3):
        for j in range(3):
            if(board[i][j] != 'O' and board[i][j] != 'X'):
                free_squares.append(tuple((i,j)))
    return free_squares


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    # horizontals and verticals
    for i in range(3):
        if(board[i][0] == board[i][1] == board[i][2] == sign):
            return True

    for i in range(3):
        if(board[0][i] == board[1][i] == board[2][i] == sign):
            return True

    # diagonals
    if(board[0][0] == board [1][1] == board[2][2] == sign):
        return True

    if (board[0][2] == board[1][1] == board[2][0] == sign):
        return True

    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    # Press the green button in the gutter to run the script.
    while True:
        move = random.randrange(1,10)
        for i in range(3):
            for j in range(3):
                if (move == board[i][j]):
                    grid[i][j] = 'X'
                    return board
        continue


if __name__ == '__main__':
    import random

    # Tic Tac Continued
    grid = [[1, 2, 3, ],
            [4, 'X', 6],
            [7, 8, 9]]
    free_squares = []
    while(True):
        make_list_of_free_fields(grid)
        if (len(free_squares) == 0):
            display_board(grid)
            print("The game is a draw")
            break
        display_board(grid)
        enter_move(grid)
        if(victory_for(grid, 'O')):
            print('You have won!')
            break
        draw_move(grid)
        if(victory_for(grid, 'X')):
            display_board(grid)
            print('The computer has won.')
            break
