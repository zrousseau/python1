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