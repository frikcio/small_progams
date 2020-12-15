import random


def red(text):  # added red color
    return ("\033[31m{}\033[0m".format(text))


def yellow(text):  # added yellow color
    return ("\033[33m{}\033[0m".format(text))


def blue(text):  # added blue color
    return ("\033[34m{}\033[0m".format(text))


def edging(mass1, mass2, x, y):  # added "empty" around position
    for x in range(x-1, x+2):
        for y in range(y-1, y+2):
            print(mass[x][y], end="")
            print()
            if mass1[x][y] == symbol[0] and mass2[x][y] == symbol[0]:
                mass[x][y] = symbol[1]


hor, vert = 0, 0
symbol = ("|_|", "|O|", "|*|", "|X|")
m1 = [[symbol[0]] * 11 for i in range(11)]  # created area for a game
m2 = [[symbol[0]] * 10 for i in range(10)]  # created area with ships
ship_1 = 0
ship_2 = 0
ship_3 = 0
ship_4 = 0
k = 0

while True:

    if ship_4 <= 1:
        hor, vert = random.randint(0, 8), random.randint(0, 8)
        m2[hor][vert] = 4
        if vert <= 6:
            m2[hor][vert + 1] = 4
            m2[hor][vert + 2] = 4
            m2[hor][vert + 3] = 4
        elif vert >= 4:
            m2[hor][vert - 1] = 4
            m2[hor][vert - 2] = 4
            m2[hor][vert - 3] = 4
        ship_4 += 1

    while ship_3 <= 2:
        hor, vert = random.randint(0, 6), random.randint(0, 8)
        if m2[hor][vert] == symbol[0]:
            if m2[hor - 1][vert - 1] == symbol[0] and m2[hor - 2][vert - 1] == symbol[0] and m2[hor][vert - 1] == symbol[0] and \
                    m2[hor - 1][vert] == symbol[0] and m2[hor - 2][vert] == symbol[0] and \
                    m2[hor + 1][
                        vert - 1] == symbol[0] and m2[hor + 2][vert - 1] == symbol[0] and m2[hor - 1][vert + 1] == symbol[0] and \
                    m2[hor - 2][vert + 1] == symbol[0] and m2[hor][vert + 1] == symbol[0] and \
                    m2[hor + 1][
                        vert] == symbol[0] and m2[hor + 2][vert] == symbol[0] and m2[hor + 1][vert + 1] == symbol[0] and \
                    m2[hor + 2][vert + 1] == symbol[0]:
                m2[hor][vert] = 3
                if hor == 0:
                    m2[hor + 1][vert] = 3
                    m2[hor + 2][vert] = 3
                else:
                    m2[hor - 1][vert] = 3
                    m2[hor + 1][vert] = 3
                ship_3 += 1

    while ship_2 <= 2:
        hor, vert = random.randint(0, 8), random.randint(0, 7)
        if m2[hor][vert] == symbol[0]:
            for i in range(3):
                if m2[hor - 1][vert - 1] == symbol[0] and m2[hor][vert - 1] == symbol[0] and m2[hor - 1][vert] == symbol[0] and \
                        m2[hor + 1][
                            vert - 1] == symbol[0] and m2[hor - 1][vert + 1] == symbol[0] and m2[hor - 1][vert + 2] == symbol[0] and \
                        m2[hor][vert + 1] == symbol[0] and m2[hor][vert + 2] == symbol[0] and m2[hor + 1][
                    vert] == symbol[0] and m2[hor + 1][vert + 1] == symbol[0] and m2[hor + 1][vert + 2] == symbol[0]:
                    m2[hor][vert] = 2
                    if vert <= 7:
                        vert += 1
                    elif vert >= 2:
                        vert -= 1
                    m2[hor][vert] = 2
                    ship_2 += 1

    while ship_1 <= 3:
        hor, vert = random.randint(0, 8), random.randint(0, 8)
        if m2[hor][vert] == symbol[0]:
            if m2[hor - 1][vert - 1] == symbol[0] and m2[hor][vert - 1] == symbol[0] and m2[hor - 1][vert] == symbol[0] and \
                    m2[hor + 1][
                        vert - 1] == symbol[0] and m2[hor - 1][vert + 1] == symbol[0] and m2[hor][vert + 1] == symbol[0] and \
                    m2[hor + 1][
                        vert] == symbol[0] and m2[hor + 1][vert + 1] == symbol[0]:
                m2[hor][vert] = 1
                ship_1 += 1
    break
for i in range(1, 11):
    m1[0][i] = " " + str(i) + " "
    m1[i][0] = " " + str(i) + " "
    m1[0][0] = "   "

while True:
    if ship_1 == 0 and ship_2 == 0 and ship_3 == 0 and ship_4 == 0:
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

    hor, vert = int(input("horizontal: ")), int(input("vertical: "))
    if m2[hor - 1][vert - 1] == symbol[0]:
        m1[hor][vert] = symbol[1]
    else:
        if m2[hor - 1][vert - 1] == 1:
            m1[hor][vert] = symbol[3]
            ship_1 -= 1
            edging(m1, m2, hor, vert)

        elif m2[hor - 1][vert - 1] >= 2:
            m1[hor][vert] = symbol[2]

