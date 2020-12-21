import random

ship_1 = 0
ship_2 = 0
ship_3 = 0
ship_4 = 0
symbol = ("|_|", "|O|", "|*|", "|X|")

ship_archive = {
    1: ship_1,
    2: ship_2,
    3: ship_3,
    4: ship_4
}


def ship_possition(size, mass2, count):
    while ship_archive[size] != count:
        orientation = random.randint(0, 1)
        x, y = random.randint(size - 1, (len(mass2) - size) - 1), random.randint(size - 1, (len(mass2) - size) - 1)
        if mass2[x][y] == symbol[0]:
            if mass2[x - 1][y - 1] == symbol[0] and mass2[x][y - 1] == symbol[0] and mass2[x + 1][y - 1] == \
                    symbol[0] and mass2[x - 1][y] == symbol[0] and mass2[x][y] == symbol[0] and \
                    mass2[x + 1][y] == symbol[0] and mass2[x - 1][y + 1] == symbol[0] and mass2[x][y + 1] == \
                    symbol[0] and mass2[x + 1][y + 1] == symbol[0]:
                mass2[x][y] = size
                if size == 1:
                    ship_archive[size] += 1
                else:
                    while True:
                        if orientation == 1:
                            if mass2[x - 2][y - 1] == symbol[0] and mass2[x - 2][y] == symbol[0] and mass2[x - 2][y + 1] == symbol[0]:
                                mass2[x - 1][y] = size
                                if size == 3:
                                    if mass2[x - 3][y - 1] == symbol[0] and mass2[x - 3][y] == symbol[0] and mass2[x - 3][y + 1] == symbol[0]:
                                        mass2[x - 2][y] = size
                                    else:
                                        mass2[x + 1][y] = size
                            elif mass2[x + 2][y - 1] == symbol[0] and mass2[x + 2][y] == symbol[0] and mass2[x + 2][
                                y + 1] == symbol[0]:
                                mass2[x + 1][y] = size
                                if size == 3:
                                    if mass2[x + 3][y - 1] == symbol[0] and mass2[x + 3][y] == symbol[0] and mass2[x + 3][y + 1] == symbol[0]:
                                        mass2[x + 2][y] = size
                            if size == 2:
                                break
                            if size==3:
                                break
                            if size == 4:
                                mass2[x + 1][y] = size
                                mass2[x - 2][y] = size
                                break
                            else:
                                continue

                        else:
                            if mass2[x - 1][y - 2] == symbol[0] and mass2[x][y - 2] == symbol[0] and mass2[x + 1][y - 2] == symbol[0]:
                                mass2[x][y - 1] = size
                                if size == 3:
                                    if mass2[x - 1][y - 3] == symbol[0] and mass2[x][y - 3] == symbol[0] and mass2[x + 1][y - 3] == symbol[0]:
                                        mass2[x][y - 2] = size
                                    else:
                                        mass2[x][y + 1] = size
                            elif mass2[x - 1][y + 2] == symbol[0] and mass2[x][y + 2] == symbol[0] and mass2[x + 1][y + 2] == symbol[0]:
                                mass2[x][y + 1] = size
                                if size == 3:
                                    if mass2[x - 1][y + 3] == symbol[0] and mass2[x][y + 3] == symbol[0] and mass2[x + 3][y + 3] == symbol[0]:
                                        mass2[x][y + 2] = size
                            if size == 2:
                                break

                            if size == 3:
                                break
                            if size == 4:
                                mass2[x][y + 1] = size
                                mass2[x][y - 2] = size
                                break
                            else:
                                continue
                    ship_archive[size] += 1
            else:
                continue
        else:
            continue


def red(text):  # added red color
    return ("\033[31m{}\033[0m".format(text))


def yellow(text):  # added yellow color
    return ("\033[33m{}\033[0m".format(text))


def blue(text):  # added blue color
    return ("\033[34m{}\033[0m".format(text))


def edging(mass1, mass2, x, y):  # added "empty" around position
    for horizontal in range(x - 1, x + 2):
        for vertical in range(y - 1, y + 2):
            if mass2[horizontal - 1][vertical - 1] == symbol[0] and mass1[horizontal][vertical] == symbol[0]:
                mass1[horizontal][vertical] = symbol[1]


m1 = [[symbol[0]] * 11 for cell in range(11)]  # created area for a game
m2 = [[symbol[0]] * 10 for cell2 in range(10)]  # created area with ships

roUnd = 0

ship_possition(4, m2, 1)

ship_possition(3, m2, 2)

ship_possition(2, m2, 3)

ship_possition(1, m2, 4)

for i in range(1, 11):
    m1[0][i] = " " + str(i) + " "
    m1[i][0] = " " + str(i) + " "
    m1[0][0] = "   "

while True:
    
    if ship_archive[1] == 0 and ship_archive[2] == 0 and ship_archive[3] == 0 and ship_archive[4] == 0:
        print("You did it!!!")
        break

    for j in range(0, len(m1)):

        for i in m1[j]:
            if i == symbol[3]:
                print(red(i), end="")
            elif i == symbol[2]:
                print(yellow(i), end="")
            elif i == symbol[1]:
                print(blue(i), end="")
            else:
                print(i, end="")
        print()
    print("ship_4: " + str(ship_archive[4]))
    print("ship_3: " + str(ship_archive[3]))
    print("ship_2: " + str(ship_archive[2]))
    print("ship_1: " + str(ship_archive[1]))
    horizontal, vertical = int(input("horizontal: ")), int(input("vertical: "))
    if m2[horizontal - 1][vertical - 1] == symbol[0]:
        m1[horizontal][vertical] = symbol[1]
    else:
        if m2[horizontal - 1][vertical - 1] == 1:
            m2[horizontal - 1][vertical - 1] = symbol[3]
            m1[horizontal][vertical] = symbol[3]
            ship_archive[1] -= 1
            edging(m1, m2, horizontal, vertical)

        elif m2[horizontal - 1][vertical - 1] >= 2:
            m2[horizontal - 1][vertical - 1] = symbol[2]
            m1[horizontal][vertical] = symbol[2]
            if m2[horizontal - 1][vertical - 1] == 2:

                edging(m1, m2, horizontal, vertical)
            elif m2[horizontal - 1][vertical - 1] == 3:
                pass
            elif m2[horizontal - 1][vertical - 1] == 4:
                pass