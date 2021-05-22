import random
import os
import time

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

letters_array = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")


class Game(object):
    ships_hangar = [[], [], [], []]  # array for have already created ships
    destroy_ships = [[], [], [], []]  # array for destroyed ships
    game_area = [[symbol[0]] * 11 for cell in range(11)]  # created area for a game
    ship_location = [[0] * 10 for cell2 in range(10)]  # created area with ships

    @classmethod
    def restart(cls):
        cls.ships_hangar = [[], [], [], []]
        cls.ship_location = [[0] * 10 for cell2 in range(10)]
        cls.game_area = [[symbol[0]] * 11 for cell in range(11)]


def pause(sec):
    time.sleep(sec)


def clear():  # update console
    os.system('clear')


def prepare_area():  # area signature
    for i in range(1, 11):
        Game.game_area[0][i] = " " + letters_array[i - 1] + " "
        if i < 10:
            Game.game_area[i][0] = "  " + str(i) + " "
        else:
            Game.game_area[i][0] = " " + str(i) + " "
        Game.game_area[0][0] = "    "


class Ship:
    def __init__(self, size, x_coordinate, y_coordinate, status_ship_cell):
        self.size = size
        self.hp = size
        self.position = []
        self.position.append({"x": x_coordinate, "y": y_coordinate, "status": status_ship_cell})

    def grow(self, current_position):
        self.position.append({"x": current_position[0], "y": current_position[1], "status": self.position[0]["status"]})


def create_ships(size, ship_location, count):
    print(f"Create {size} ships...")

    while len(Game.ships_hangar[size - 1]) != count:
        x = random.randint(1, 8)
        y = random.randint(1, 8)

        if ship_location[x][y] == 0:
            if (ship_location[x - 1][y - 1] == 0 and ship_location[x][y - 1] == 0 and
                    ship_location[x + 1][y - 1] == 0 and ship_location[x - 1][y] == 0 and
                    ship_location[x][y] == 0 and ship_location[x + 1][y] == 0 and
                    ship_location[x - 1][y + 1] == 0 and ship_location[x][y + 1] == 0 and
                    ship_location[x + 1][y + 1] == 0):
                ship_location[x][y] = size
                ship = Ship(size, x, y, ship_location[x][y])
                Game.ships_hangar[size - 1].append(ship)
                if size > 1:  # if size bigger than 1 cell
                    orientation = random.randint(0, 1)
                    if orientation == 1:  # vertical orientation
                        for i in range(2, size + 1):
                            if ship_location[x - 2][y - 1] == 0 and ship_location[x - 2][y] == 0 and \
                                    ship_location[x - 2][y + 1] == 0 and x - 1 >= 0:
                                x -= 1
                                ship_location[x][y] = size
                                current_position = (x, y)
                                ship.grow(current_position)
                            elif ship_location[x + i][y - 1] == 0 and ship_location[x + i][y] == 0 and \
                                    ship_location[x + i][y + 1] == 0 and x + 1 <= 9:
                                ship_location[x + i - 1][y] = size
                                current_position = (x + i - 1, y)
                                ship.grow(current_position)
                            else:
                                raise ValueError(ship_location, Game.ships_hangar)

                    else:  # horizontal orientation
                        for i in range(2, size + 1):
                            if ship_location[x - 1][y - 2] == 0 and ship_location[x][y - 2] == 0 and \
                                    ship_location[x + 1][y - 2] == 0 and y - 1 >= 0:
                                y -= 1
                                ship_location[x][y] = size
                                current_position = (x, y)
                                ship.grow(current_position)
                            elif ship_location[x - 1][y + i] == 0 and ship_location[x][y + i] == 0 and \
                                    ship_location[x + 1][y + i] == 0 and y + 1 <= 9:
                                ship_location[x][y + i - 1] = size
                                current_position = (x, y + i - 1)
                                ship.grow(current_position)
                            else:
                                raise ValueError(ship_location, Game.ships_hangar)
        else:
            continue


def check_status():  # check and update status of ships
    for index_p, part in enumerate(Game.ships_hangar):
        for index_s, ship in enumerate(part):
            for index_c, cell in enumerate(ship.position):
                if ship.position[index_c]["status"] == "X":
                    Game.ship_location[ship.position[index_c]["x"]][ship.position[index_c]["y"]] = \
                        ship.position[index_c][
                            "status"]
                    Game.game_area[ship.position[index_c]["x"] + 1][ship.position[index_c]["y"] + 1] = symbol[3]
                    current = part[index_s]
                    part.pop(index_s)
                    Game.destroy_ships[index_p].append(current)
                    break

                if ship.position[index_c]["status"] == "*":
                    Game.ship_location[ship.position[index_c]["x"]][ship.position[index_c]["y"]] = "*"
                    Game.game_area[ship.position[index_c]["x"] + 1][ship.position[index_c]["y"] + 1] = symbol[2]

                    if (ship.position[0]["status"] == "*" and ship.position[1]["status"] == "*" and
                            ship.position[-2]["status"] == "*" and ship.position[-1]["status"] == "*"):
                        for i in range(1, -3, -1):
                            ship.position[i]["status"] = "X"
                            Game.ship_location[ship.position[i]["x"]][ship.position[i]["y"]] = ship.position[0][
                                "status"]
                            Game.game_area[ship.position[i]["x"] + 1][ship.position[i]["y"] + 1] = symbol[3]
                            edging(ship, Game.ship_location, Game.game_area)

                        current = part[index_s]
                        part.pop(index_s)
                        Game.destroy_ships[index_p].append(current)
                        break


def edging(ship, mass1, mass2):  # added "empty" around destroyed ship
    for index_c, cell in enumerate(ship.position):
        x = cell['x'] + 1
        y = cell['y'] + 1
        for horizontal in range(x - 1, x + 2):
            for vertical in range(y - 1, y + 2):
                if mass1[horizontal - 1][vertical - 1] == 0 and mass2[horizontal][vertical] == symbol[0]:
                    mass2[horizontal][vertical] = symbol[1]


def attacks_result(horizontal, vertical):
    if Game.ship_location[horizontal - 1][vertical - 1] == 0:
        Game.game_area[horizontal][vertical] = symbol[1]
    else:
        if Game.ship_location[horizontal - 1][vertical - 1] == "*" or \
                Game.ship_location[horizontal - 1][vertical - 1] == "X":
            pass
        elif Game.ship_location[horizontal - 1][vertical - 1] == 1:
            for index_s, ships in enumerate(Game.ships_hangar[0]):
                for cell in Game.ships_hangar[0][index_s].position:
                    if horizontal - 1 == cell["x"] and vertical - 1 == cell["y"]:
                        cell["status"] = "X"
                        edging(ships, Game.ship_location, Game.game_area)

        elif Game.ship_location[horizontal - 1][vertical - 1] >= 2:
            for index_p, part in enumerate(Game.ships_hangar):
                for index_s, ship in enumerate(part):
                    for index_c, cell in enumerate(ship.position):
                        if horizontal - 1 == cell["x"] and vertical - 1 == cell["y"]:
                            cell["status"] = "*"
            if Game.ship_location[horizontal - 1][vertical - 1] == 2:
                pass
            elif Game.ship_location[horizontal - 1][vertical - 1] == 3:
                pass
            elif Game.ship_location[horizontal - 1][vertical - 1] == 4:
                pass


def graphic():
    clear()
    
    array_print = [
        (len(Game.ships_hangar[1 - 1])),
        (len(Game.ships_hangar[2 - 1])),
        (len(Game.ships_hangar[3 - 1])),
        (len(Game.ships_hangar[4 - 1])),
        0
    ]

    for line in range(0, len(Game.game_area)):
        for cell in Game.game_area[line]:
            print(cell, end="")

        if 1 <= line <= 4:
            print("\t\t\t{}- {}".format(symbol[array_print[4]], symbol_val[array_print[4]]), end="")
            array_print[4] += 1
            if line == 4:
                array_print[4] = 0

        elif 7 <= line <= 10:
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
    while True:
        try:
            create_ships(4, Game.ship_location, 1)
            create_ships(3, Game.ship_location, 2)
            create_ships(2, Game.ship_location, 3)
            create_ships(1, Game.ship_location, 4)
            break
        except ValueError:
            print("Fail to dislocate ships")
            Game.restart()
            continue
        except IndexError:
            print("Index out of range")
            Game.restart()
            continue
    prepare_area()


def run():
    start()
    moves = 0
    while True:
        graphic()
        person_input()
        moves += 1
        start_time = time.time()
        if len(Game.ships_hangar[0]) == 0 and len(Game.ships_hangar[1]) == 0 and len(Game.ships_hangar[2]) == 0 and len(
                Game.ships_hangar[3]) == 0:
            print("You did it!!!")
            print(f"You coped for {moves} moves")
            all_spend_time = time.time() - start_time
            minute = int(all_spend_time // 60)
            second = str(all_spend_time - minute * 60)
            print(f"And you spend {minute} minutes and {second[0:3]} seconds")
            break


run()
