from statistics import mean as MEAN
import sys


def singular(string):
    if(string.endswith('s')):
       return string[:-1]
    else:
        return string

def titleTime(string):
    string = string.title()
    string = string.center(20, "=")
    return string

def findMean():
    print("The mean is", MEAN([1, 2, 3, 4, 5, 6, 7]))


def ask_name():
    # ask user for name
    name = input("what is your name\n>")
    # print user's name
    print(f"Hello {name}")


def multiply_number():
    # ask the user for a number
    num = float(input("Enter a number\n>"))
    # multiply number by itself
    print(f' {num} times {num} is {num*num}')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_letter_count():
    # ask the user for a word
    word = input("Please enter a word\n")
    # print the letter count
    print("The length of the word is", len(word))


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


def coin_flip():
    number = int(input("Pick a number 0 or 1"))
    one_or_two = [0,1]
    if(random.choice(one_or_two) == number):
        print("You win!")
    else:
        print("You lose...")

# a
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
                    # grid[i][j] = 'O'
                    return board
        print("That is not a free move")
        continue




def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    print("Making list")
    # free_squares.clear()
    # for i in range(3):
        # for j in range(3):
            # if(board[i][j] != 'O' and board[i][j] != 'X'):
                    # free_squares.append(tuple((i,j)))
    # return free_squares


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
                # if (move == board[i][j]):
                    # grid[i][j] = 'X'
                    return board
        continue


if __name__ == '__main__':
    import random
    # print_hi('Zach')

    # ask_name()
    # multiply_number()
    # print_letter_count()
    # choice = input("Do you want to do the array flip (a) or coin flip (c)")
    # if(choice == "a"):
    #   array_flip()
    # elif(choice == "c"):
    #    coin_flip()
    # else:
    #    print("Sorry that is not an option...")
    # Tic Tac Continued
    # grid = [[1, 2, 3, ],
    #        [4, 'X', 6],
    #        [7, 8, 9]]
    # free_squares = []
    # while(True):
    #    make_list_of_free_fields(grid)
    #    if (len(free_squares) == 0):
    #        display_board(grid)
    #        print("The game is a draw")
    #        break
    #    display_board(grid)
    #    enter_move(grid)
    #    if(victory_for(grid, 'O')):
    #       print('You have won!')
    #        break
    #    draw_move(grid)
    #    if(victory_for(grid, 'X')):
    #        display_board(grid)
    #        print('The computer has won.')
    #        break
    # findMean()
    print(str(sys.argv))
    print(singular(sys.argv[1]))
    print(titleTime(" ".join(sys.argv[1:])))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
