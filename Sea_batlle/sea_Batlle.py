import random

hor, vert = 0, 0
grap = ("|X|", "|O|", "|*|")
m1 = [["|_|"] * 11 for i in range(11)]
m2 = [["|_|"] * 10 for i in range(10)]
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
        if m2[hor][vert] == "|_|":
            if m2[hor - 1][vert - 1] == "|_|" and m2[hor - 2][vert - 1] == "|_|" and m2[hor][vert - 1] == "|_|" and \
                    m2[hor - 1][vert] == "|_|" and m2[hor - 2][vert] == "|_|" and \
                    m2[hor + 1][
                        vert - 1] == "|_|" and m2[hor + 2][vert - 1] == "|_|" and m2[hor - 1][vert + 1] == "|_|" and \
                    m2[hor - 2][vert + 1] == "|_|" and m2[hor][vert + 1] == "|_|" and \
                    m2[hor + 1][
                        vert] == "|_|" and m2[hor + 2][vert] == "|_|" and m2[hor + 1][vert + 1] == "|_|" and \
                    m2[hor + 2][vert + 1] == "|_|":
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
        if m2[hor][vert] == "|_|":
            for i in range(3):
                if m2[hor - 1][vert - 1] == "|_|" and m2[hor][vert - 1] == "|_|" and m2[hor - 1][vert] == "|_|" and \
                        m2[hor + 1][
                            vert - 1] == "|_|" and m2[hor - 1][vert + 1] == "|_|" and m2[hor - 1][vert + 2] == "|_|" and \
                        m2[hor][vert + 1] == "|_|" and m2[hor][vert + 2] == "|_|" and m2[hor + 1][
                    vert] == "|_|" and m2[hor + 1][vert + 1] == "|_|" and m2[hor + 1][vert + 2] == "|_|":
                    m2[hor][vert] = 2
                    if vert <= 7:
                        vert += 1
                    elif vert >= 2:
                        vert -= 1
                    m2[hor][vert] = 2
                    ship_2 += 1

    while ship_1 <= 3:
        hor, vert = random.randint(0, 8), random.randint(0, 8)
        if m2[hor][vert] == "|_|":
            if m2[hor - 1][vert - 1] == "|_|" and m2[hor][vert - 1] == "|_|" and m2[hor - 1][vert] == "|_|" and \
                    m2[hor + 1][
                        vert - 1] == "|_|" and m2[hor - 1][vert + 1] == "|_|" and m2[hor][vert + 1] == "|_|" and \
                    m2[hor + 1][
                        vert] == "|_|" and m2[hor + 1][vert + 1] == "|_|":
                m2[hor][vert] = 1
                ship_1 += 1
    break
for i in range(1, 11):
    m1[0][i] = " " + str(i) + " "
    m1[i][0] = " " + str(i) + " "
r = 0
while r != 100:
    r += 1
    for i in m1:
        print(i)
    print()
    hor, vert = int(input("first: ")), int(input("second: "))
    if m2[hor - 1][vert - 1] == "|_|":
        m1[hor][vert] = grap[1]
    else:
        if m2[hor - 1][vert - 1] == 1:
            m1[hor][vert] = grap[0]
        elif m2[hor - 1][vert - 1] >= 2:
            m1[hor][vert] = grap[2]