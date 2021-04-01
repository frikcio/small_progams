from colorama import init
from colorama import Fore

init()


def my_error():
    print(Fore.RED + "\nWRONG COMMAND!\n\n")


def num_error():
    print(Fore.RED + "\nERROR!\n")
    print("Please input a number\n\n" + Fore.GREEN)


def check():
    while True:
        number2 = input(Fore.BLUE + "\n2-nd number:  " + Fore.GREEN)
        if number2.isdigit():
            return number2
        else:
            num_error()
    

def plus(number1):
    number2 = check()
    return float(number1) + float(number2)


def minus(number1):
    number2 = check()
    return float(number1) - float(number2)


def times(number1):
    number2 = check()
    return float(number1) * float(number2)


def divide(number1):
    while True:
        number2 = input(Fore.BLUE + "\n2-nd number:  " + Fore.GREEN)
        if number2.isdigit():
            try:
                results = float(number1) / float(number2)
                return results
            except ZeroDivisionError:
                print(Fore.RED + "\nCANNOT DIVIDED BY 0!!\n")
                continue
        else:
            num_error()
            continue


operations_list = {
    "+": plus,
    "-": minus,
    "*": times,
    "/": divide}


def run_operation(number1, operations_list, operation):
    return operations_list[operation](number1)


# Instruction block BEGIN
def help_instruction():
    print(Fore.MAGENTA + '\n\nINSTRUCTION:\n',
          Fore.YELLOW + 'Input a number and press:\n',
          Fore.GREEN + ' "+" ' + Fore.YELLOW + ' if you want add numbers;\n',
          Fore.GREEN + ' "-" ' + Fore.YELLOW + ' if you want subtract numbers;\n',
          Fore.GREEN + ' "*" ' + Fore.YELLOW + ' if you want multiply numbers;\n',
          Fore.GREEN + ' "/" ' + Fore.YELLOW + ' if you want divide the numbers;\n',
          'Enter command ' + Fore.GREEN + ' "help"' + Fore.YELLOW + ', if you want to see Instruction one more time;\n',
          'And ' + Fore.GREEN + ' "exit"' + Fore.YELLOW + ', if you want to close this program;\n' + Fore.BLUE)
# Instruction block ENDING


help_instruction()  # Calculation module
while True:
    print(Fore.BLUE + "\nStart the calculation\n")
    number1 = input("1-st number:  " + Fore.GREEN)

    # EXIT module
    if number1 == "exit":
        print(Fore.YELLOW + "Are you want to close this program? " + Fore.BLUE + "(1 - YES/2 - NO)" + Fore.GREEN)
        answer = input(":  ")
        if answer == "1":
            print(Fore.YELLOW + "\n\n calculation is over!")
            break
        elif answer == "2":
            continue
        else:
            my_error()
            continue

    elif number1 == "help":
        help_instruction()
        continue

    elif number1.isdigit():
        # OPERATION module
        print(Fore.GREEN)
        operation = input(Fore.BLUE + "operation:  " + Fore.GREEN)
        if operation in operations_list:
            result = run_operation(number1, operations_list, operation)
            print(Fore.BLUE + "\nResult: " + Fore.GREEN + str(result) + "\n\n")
        else:
            my_error()

    else:
        num_error()
        continue
