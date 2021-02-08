import random

import os

import time


def pause(sec):
    time.sleep(sec)


def clear():  # update console
    os.system('cls')


symbol_val = (
    "did not shot",
    "there is no ship here",
    "you hit the ship",
    "you destroyed the ship"
)

symbol = ("|_|",
          "\033[34m|\033[4m0\033[0m\033[34m|\033[0m",  # missed ("0" with blue color and underline)
          "\033[33m|\033[4m*\033[0m\033[33m|\033[0m",  # hit ("*" with yellow color and underline)
          "\033[31m|\033[4mX\033[0m\033[31m|\033[0m"  # destroyed ("X" with red color and underline)
          )  # parts for the game_area

ships_hangar = [[], [], [], []]  # array for have already created ships
destroy_ships = [[], [], [], []]  # array for destroyed ships

game_area = [[symbol[0]] * 11 for cell in range(11)]  # created area for a game
ship_location = [[0] * 10 for cell2 in range(10)]  # created area with ships
letters_array = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")


def prepare_area():  # area signature
    for i in range(1, 11):
        game_area[0][i] = " " + letters_array[i - 1] + " "
        if i < 10:
            game_area[i][0] = "  " + str(i) + " "
        else:
            game_area[i][0] = " " + str(i) + " "
        game_area[0][0] = "    "


class Ship:
    def __init__(self, size, x_cordinate, y_cordinate, status_ship_cell):
        self.size = size
        self.hp = size
        self.position = []
        self.position.append({"x": x_cordinate, "y": y_cordinate, "status": status_ship_cell})

    def grow(self, curent_possition):
        self.position.append({"x": curent_possition[0], "y": curent_possition[1], "status": self.position[0]["status"]})


def create_ship(size, ship_location, count):  # create and locate ships
    while len(ships_hangar[size - 1]) != count:
        x, y = random.randint(size - 1, (len(ship_location) - size) - 1), random.randint(size - 1, (
                len(ship_location) - size) - 1)
        if ship_location[x][y] == 0:
            if (ship_location[x - 1][y - 1] == 0 and ship_location[x][y - 1] == 0 and ship_location[x + 1][
                y - 1] == 0 and
                    ship_location[x - 1][y] == 0 and ship_location[x][y] == 0 and ship_location[x + 1][y] == 0 and
                    ship_location[x - 1][y + 1] == 0 and ship_location[x][y + 1] == 0 and ship_location[x + 1][
                        y + 1] == 0):
                ship_location[x][y] = size
                if size == 1:
                    ship_1 = Ship(size, x, y, ship_location[x][y])
                    ships_hangar[size - 1].append(ship_1)
                else:  # if size bigger than 1 cell
                    while True:
                        orientation = random.randint(0, 1)
                        if orientation == 1:  # vertical orientation
                            if ship_location[x - 2][y - 1] == 0 and ship_location[x - 2][y] == 0 and \
                                    ship_location[x - 2][y + 1] == 0:
                                ship_location[x - 1][y] = size
                                curent_position_2 = (x - 1, y)
                                if size == 3:
                                    if ship_location[x - 3][y - 1] == 0 and ship_location[x - 3][y] == 0 and \
                                            ship_location[x - 3][y + 1] == 0:
                                        ship_location[x - 2][y] = size
                                        curent_position_3 = (x - 2, y)
                                    elif ship_location[x + 2][y - 1] == 0 and ship_location[x + 2][y] == 0 and \
                                            ship_location[x + 2][y + 1] == 0:
                                        ship_location[x + 1][y] = size
                                        curent_position_3 = (x + 1, y)
                                    else:
                                        continue
                            elif ship_location[x + 2][y - 1] == 0 and ship_location[x + 2][y] == 0 and \
                                    ship_location[x + 2][y + 1] == 0:
                                ship_location[x + 1][y] = size
                                curent_position_2 = (x + 1, y)
                                if size == 3:
                                    if ship_location[x + 3][y - 1] == 0 and ship_location[x + 3][y] == 0 and \
                                            ship_location[x + 3][y + 1] == 0:
                                        ship_location[x + 2][y] = size
                                        curent_position_3 = (x + 2, y)
                                    elif ship_location[x - 2][y - 1] == 0 and ship_location[x - 2][y] == 0 and \
                                            ship_location[x - 2][y + 1] == 0:
                                        ship_location[x - 1][y] = size
                                        curent_position_3 = (x - 1, y)
                                    else:
                                        continue

                            if curent_position_2:
                                if size == 2:
                                    ship_2 = Ship(size, x, y, ship_location[x][y])
                                    ships_hangar[size - 1].append(ship_2)
                                    ship_2.grow(curent_position_2)
                                    break
                                if size == 3:
                                    ship_3 = Ship(size, x, y, ship_location[x][y])
                                    ships_hangar[size - 1].append(ship_3)
                                    ship_3.grow(curent_position_2)
                                    ship_3.grow(curent_position_3)
                                    break
                                if size == 4:
                                    ship_location[x + 1][y] = size
                                    curent_position_3 = (x + 1, y)
                                    ship_location[x - 2][y] = size
                                    curent_position_4 = (x - 2, y)
                                    ship_4 = Ship(size, x, y, ship_location[x][y])
                                    ships_hangar[size - 1].append(ship_4)
                                    ship_4.grow(curent_position_2)
                                    ship_4.grow(curent_position_3)
                                    ship_4.grow(curent_position_4)
                                    break
                            else:
                                continue

                        else:  # if horizontal orientation
                            if ship_location[x - 1][y - 2] == 0 and ship_location[x][y - 2] == 0 and \
                                    ship_location[x + 1][y - 2] == 0:
                                ship_location[x][y - 1] = size
                                curent_position_2 = (x, y - 1)
                                if size == 3:
                                    if ship_location[x - 1][y - 3] == 0 and ship_location[x][y - 3] == symbol[0] and \
                                            ship_location[x + 1][y - 3] == 0:
                                        ship_location[x][y - 2] = size
                                        curent_position_3 = (x, y - 2)
                                    else:
                                        ship_location[x][y + 1] = size
                                        curent_position_3 = (x, y + 1)
                            elif ship_location[x - 1][y + 2] == 0 and ship_location[x][y + 2] == 0 and \
                                    ship_location[x + 1][y + 2] == 0:
                                ship_location[x][y + 1] = size
                                curent_position_2 = (x, y + 1)
                                if size == 3:
                                    if ship_location[x - 1][y + 3] == 0 and ship_location[x][y + 3] == 0 and \
                                            ship_location[x + 1][y + 3] == 0:
                                        ship_location[x][y + 2] = size
                                        curent_position_3 = (x, y + 2)
                                    elif ship_location[x - 1][y - 2] == 0 and ship_location[x][y - 2] == 0 and \
                                            ship_location[x + 1][y - 2] == 0:
                                        ship_location[x][y - 1] = size
                                        curent_position_3 = (x, y - 1)

                            if curent_position_2:
                                if size == 2:
                                    ship_2 = Ship(size, x, y, ship_location[x][y])
                                    ships_hangar[size - 1].append(ship_2)
                                    ship_2.grow(curent_position_2)
                                    break
                                if size == 3:
                                    ship_3 = Ship(size, x, y, ship_location[x][y])
                                    ships_hangar[size - 1].append(ship_3)
                                    ship_3.grow(curent_position_2)
                                    ship_3.grow(curent_position_3)
                                    break
                                if size == 4:
                                    ship_location[x][y + 1] = size
                                    curent_position_3 = (x, y + 1)
                                    ship_location[x][y - 2] = size
                                    curent_position_4 = (x, y - 2)
                                    ship_4 = Ship(size, x, y, ship_location[x][y])
                                    ships_hangar[size - 1].append(ship_4)
                                    ship_4.grow(curent_position_2)
                                    ship_4.grow(curent_position_3)
                                    ship_4.grow(curent_position_4)
                                    break
                            else:
                                continue
            else:
                continue
        else:
            continue


def check_status():  # check and update status of ships
    for index_p, part in enumerate(ships_hangar):
        for index_s, ship in enumerate(part):
            for index_c, cell in enumerate(ship.position):
                if ship.position[index_c]["status"] == "X":
                    ship_location[ship.position[index_c]["x"]][ship.position[index_c]["y"]] = ship.position[index_c][
                        "status"]
                    game_area[ship.position[index_c]["x"] + 1][ship.position[index_c]["y"] + 1] = symbol[3]
                    current = part[index_s]
                    part.pop(index_s)
                    destroy_ships[index_p].append(current)
                    break

                if ship.position[index_c]["status"] == "*":
                    ship_location[ship.position[index_c]["x"]][ship.position[index_c]["y"]] = ship.position[index_c]["status"]
                    game_area[ship.position[index_c]["x"] + 1][ship.position[index_c]["y"] + 1] = symbol[2]

                    if (ship.position[0]["status"] == "*" and
                            ship.position[1]["status"] == "*" and
                            ship.position[-2]["status"] == "*" and
                            ship.position[-1]["status"] == "*"):

                        ship.position[0]["status"] = "X"
                        ship.position[1]["status"] = "X"
                        ship.position[-2]["status"] = "X"
                        ship.position[-1]["status"] = "X"
                        ship_location[ship.position[0]["x"]][ship.position[0]["y"]] = ship.position[0]["status"]
                        game_area[ship.position[0]["x"] + 1][ship.position[0]["y"] + 1] = symbol[3]
                        edging(ship_location, game_area, ship.position[0]["x"] + 1, ship.position[0]["y"] + 1)

                        ship_location[ship.position[1]["x"]][ship.position[1]["y"]] = ship.position[1]["status"]
                        game_area[ship.position[1]["x"] + 1][ship.position[1]["y"] + 1] = symbol[3]
                        edging(ship_location, game_area, ship.position[1]["x"] + 1, ship.position[1]["y"] + 1)

                        ship_location[ship.position[-2]["x"]][ship.position[-2]["y"]] = ship.position[-2]["status"]
                        game_area[ship.position[-2]["x"] + 1][ship.position[-2]["y"] + 1] = symbol[3]
                        edging(ship_location, game_area, ship.position[-2]["x"] + 1, ship.position[-2]["y"] + 1)

                        ship_location[ship.position[-1]["x"]][ship.position[-1]["y"]] = ship.position[-1]["status"]
                        game_area[ship.position[-1]["x"] + 1][ship.position[-1]["y"] + 1] = symbol[3]
                        edging(ship_location, game_area, ship.position[-2]["x"] + 1, ship.position[-2]["y"] + 1)

                        current = part[index_s]
                        part.pop(index_s)
                        destroy_ships[index_p].append(current)
                        break


def edging(mass1, mass2, x, y):  # added "empty" around destroyed ship
    for horizontal in range(x - 1, x + 2):
        for vertical in range(y - 1, y + 2):
            if mass1[horizontal - 1][vertical - 1] == 0 and mass2[horizontal][vertical] == symbol[0]:
                mass2[horizontal][vertical] = symbol[1]


def attacks_result(horizontal, vertical):
    if ship_location[horizontal - 1][vertical - 1] == 0:
        game_area[horizontal][vertical] = symbol[1]
    else:
        if ship_location[horizontal - 1][vertical - 1] == "*" or ship_location[horizontal - 1][vertical - 1] == "X":
            pass
        elif ship_location[horizontal - 1][vertical - 1] == 1:
            for index_s, ships in enumerate(ships_hangar[0]):
                for cell in ships_hangar[0][index_s].position:
                    if horizontal - 1 == cell["x"] and vertical - 1 == cell["y"]:
                        cell["status"] = "X"
                        edging(ship_location, game_area, horizontal, vertical)

        elif ship_location[horizontal - 1][vertical - 1] >= 2:
            for index_p, part in enumerate(ships_hangar):
                for index_s, ship in enumerate(part):
                    for index_c, cell in enumerate(ship.position):
                        if horizontal - 1 == cell["x"] and vertical - 1 == cell["y"]:
                            cell["status"] = "*"
            if ship_location[horizontal - 1][vertical - 1] == 2:
                pass
            elif ship_location[horizontal - 1][vertical - 1] == 3:
                pass
            elif ship_location[horizontal - 1][vertical - 1] == 4:
                pass


def graphic():
    clear()

    array_print = [
        (len(ships_hangar[1 - 1])),
        (len(ships_hangar[2 - 1])),
        (len(ships_hangar[3 - 1])),
        (len(ships_hangar[4 - 1])),
        0
    ]

    for line in range(0, len(game_area)):
        for cell in game_area[line]:
            print(cell, end="")

        if line >= 1 and line <= 4:
            print("\t\t\t{}- {}".format(symbol[array_print[4]], symbol_val[array_print[4]]), end="")
            array_print[4] += 1
            if line == 4:
                array_print[4] = 0

        elif line >= 7 and line <= 10:
            if array_print[array_print[4]] > 0:
                print("\t\t\t{}-deck ship left: {}".format(array_print[4] + 1, array_print[array_print[4]]), end="")
            else:
                print("\t\t\t{}-deck ship: all destroyed".format(array_print[4] + 1), end="")
            array_print[4] += 1
        print()


def person_input():
    while True:
        letter = input("letter: ")
        if letter.upper() in letters_array:
            vertical = letters_array.index(letter.upper()) + 1
            while True:
                horizontal = input("horizontal: ")
                if horizontal.isnumeric():
                    horizontal = int(horizontal)
                    if horizontal <= 10:
                        attacks_result(horizontal, vertical)
                        check_status()
                        break
                    else:
                        print("Please input number from 1 to 10")
                else:
                    print("Something wrong. \nPlease input number from 1 to 10")
                    continue
            break
        else:
            print("Your letter is out of range")


def start():
    create_ship(4, ship_location, 1)
    create_ship(3, ship_location, 2)
    create_ship(2, ship_location, 3)
    create_ship(1, ship_location, 4)
    prepare_area()


def run():
    start()
    moves = 0
    while True:
        graphic()
        person_input()
        moves += 1
        start_time = time.time()
        if len(ships_hangar[0]) == 0 and len(ships_hangar[1]) == 0 and len(ships_hangar[2]) == 0 and len(
                ships_hangar[3]) == 0:
            print("You did it!!!")
            print(f"You coped for {moves} moves")
            all_spend_time = time.time() - start_time
            minute = int(all_spend_time // 60)
            second = str(all_spend_time - minute * 60)
            print(f"And you spend {minute} minutes and {second[0:3]} seconds")
            break


run()
