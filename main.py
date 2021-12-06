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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('Zach')

    ask_name()
    multiply_number()
    print_letter_count()

