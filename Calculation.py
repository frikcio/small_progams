from colorama import init
from colorama import Fore, Back, Style

init()

def my_error():
    print(Fore.RED + "\nWRONG COMAND!\n\n")


def num_error():
    print(Fore.RED + "\nERROR!\n")
    print("Pleace input a number\n\n" + Fore.GREEN)


def check():
    while True:
        num2 = input(Fore.BLUE + "\n2-nd number:  " + Fore.GREEN)
        if num2.isdigit():
            break
        else:
            num_error()
    return num2


def plus(num1):
    num2 = check()
    return float(num1) + float(num2)


def minus(num1):
    num2 = check()
    return float(num1) - float(num2)


def times(num1):
    num2 = check()
    return float(num1) * float(num2)


def divide(num1):
    while True:
        num2 = input(Fore.BLUE + "\n2-nd number:  " + Fore.GREEN)
        if num2.isdigit():
            try:
                result = float(num1) / float(num2)
                break
            except ZeroDivisionError:
                print(Fore.RED + "\nCANNOT DIVIDED BY 0!!\n")
                continue
        else:
            num_error()
            continue
    return float(num1) / float(num2)


operations = {
    "+": plus,
    "-": minus,
    "*": times,
    "/": divide}


def run_operation(num1, operations, operation):
    return operations[operation](num1)


# Instruction block BEGIN
def help():
	print(Fore.MAGENTA + '\n\nINSTRUCTION:\n')
	print(Fore.YELLOW + 'Input a number and press:')
	print(Fore.GREEN + ' "+" ' + Fore.YELLOW + ' if you want add numbers;')
	print(Fore.GREEN + ' "-" ' + Fore.YELLOW + ' if you want subtract numbers;')
	print(Fore.GREEN + ' "*" ' + Fore.YELLOW + ' if you want multiply numbers;')
	print(Fore.GREEN + ' "/" ' + Fore.YELLOW + ' if you want divide the numbers;')
	print('Enter comand ' + Fore.GREEN + ' "help"' + Fore.YELLOW + ', if you want to see Instruction one more time;')
	print('Enter comand ' + Fore.GREEN + ' "exit"' + Fore.YELLOW + ', if you want to close this programm;' + Fore.BLUE)
# Instruction block ENDING

# Calculation module
help()
while True:
    print(Fore.BLUE + "\nStart the calculation\n")
    num1 = input("1-st number:  " + Fore.GREEN)

    # EXIT module
    if num1 == "exit":
        print(Fore.YELLOW + "Are you want to close this programm? " + Fore.BLUE + "(1 - YES/2 - NO)" + Fore.GREEN)
        answer = input(":  ")
        if answer == "1":
            print(Fore.YELLOW + "\n\n calculation is over!")
            break
        elif answer == "2":
            continue
        else:
            my_error()
            continue

    elif num1 == "help":
    	help()
    	continue

    elif num1.isdigit():
        # OPERATION module
        print(Fore.GREEN)
        operation = input(Fore.BLUE + "operation:  " + Fore.GREEN)
        if operation in operations:
            result = run_operation(num1, operations, operation)
            print(Fore.BLUE + "\nResult: " + Fore.GREEN + str(result) + "\n\n")
        else:
            my_error()

    else:
        num_error()
        continue
