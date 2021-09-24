# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import random
    # print_hi('Zach')

    # ask_name()
    # multiply_number()
    # print_letter_count()
    choice = input("Do you want to do the array flip (a) or coin flip (c)")
    if(choice == "a"):
        array_flip()
    elif(choice == "c"):
        coin_flip()
    else:
        print("Sorry that is not an option...")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
