import os
import time


def clear(sec):  # update console
    time.sleep(sec)
    os.system('clear')  # clear console if os Linux / os.system('cls') if os Windows 


COMMAND_WORDS = ["exit", "help"]


class Message(object):  # color for text messages
    @staticmethod
    def red(msg):
        return f"\033[91m {msg} \033[0m"

    @staticmethod
    def green(msg):
        return f"\033[92m {msg} \033[0m"

    @staticmethod
    def yellow(msg):
        return f"\033[93m {msg} \033[0m"

    @staticmethod
    def blue(msg):
        return f"\033[94m {msg} \033[0m"


def check1(number1):  # check first input is number
    if not number1.isdigit():
        return float(number1)
    return int(number1)


def check2():  # check second input is number
    while True:
        number2 = input(Message.blue("2-nd number: "))
        try:
            if not number2.isdigit():
                return float(number2)
            return int(number2)
        except ValueError:
            print(Message.red("Your input is not a correct number!"))
            continue


class Operation(object):
    @staticmethod
    def plus(number1):
        number2 = check2()
        return number1 + number2

    @staticmethod
    def minus(number1):
        number2 = check2()
        return number1 - number2

    @staticmethod
    def times(number1):
        number2 = check2()
        return number1 * number2

    @staticmethod
    def divide(number1):
        while True:
            number2 = check2()
            try:
                results = number1 / number2
                return results
            except ZeroDivisionError:
                print(Message.red("\nCANNOT DIVIDED BY 0!!\n"))
            continue


OPERATIONS_LIST = {
    "+": Operation.plus,
    "-": Operation.minus,
    "*": Operation.times,
    "/": Operation.divide,
}


def run_operation(operation_list, operation, number1):  
    return operation_list[operation](number1)


def help_instruction():  # Instruction 
    print(f'\n{Message.yellow("INSTRUCTION")}:\n',
          f'Input a number and press:\n',
          f'"{Message.green("+")}" if you want to add numbers;\n',
          f'"{Message.green("-")}" if you want to subtract numbers;\n',
          f'"{Message.green("*")}" if you want to multiply numbers;\n',
          f'"{Message.green("/")}" if you want to divide the numbers;\n',
          f'Enter the command "{Message.yellow("help")}", if you want to see Instruction one more time;\n',
          f'And "{Message.yellow("exit")}", if you want to close this program;\n')


def run():
    clear(0.5)
    calc_round = 1
    help_instruction()
    while True:
        print(f"\nStart calculation #{calc_round}\n")
        number1 = input(Message.blue("1-st number: "))
        if number1 not in COMMAND_WORDS:
            try:
                number1 = check1(number1)
            except ValueError:
                print(Message.red("Your input is not a correct"))
                continue
            operation = input(Message.blue("operation: "))
            if operation in OPERATIONS_LIST:
                result = run_operation(OPERATIONS_LIST, operation, number1)
                print(f"\n{Message.blue('Result')}: {Message.green(result)} \n\n")
                calc_round += 1
                clear(2)
            else:
                print(Message.red("Incorrect operation!"))
                continue
        else:
            if number1 == 'exit':
                print("Are you want to close this program? (1 - YES/2 - NO)")
                answer = input(":  ")
                if answer == "1":
                    print(Message.yellow("Calculation is over!"))
                    break
                elif answer == "2":
                    continue
                else:
                    print(Message.red("Incorrect answer!"))
                    clear(1)
                    continue
            elif number1 == "help":
                help_instruction()
                continue
            else:
                print(Message.yellow("Incorrect Input!"))


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        pass
