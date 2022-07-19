#Conway’s Game of Life
import random
import copy

state = ("#", " ")
li = []


for i in range(6):
    lt = []
    for i in range(6):
        lt.append(random.choice(state))
    li.append(lt)

for i in range(6):
    print(li[i])

try:
    w = int(input("How many iterations of Conways Game do you want?"))

except:
    print("Invalid entry")

for r in range(w):
    lic = copy.deepcopy(li)
    r = 0
    for i in range(6):
        c = 0
        for i in range(6):
            nstate = []
            if c == 0 and r == 0:
                nstate.append(lic[r][c+1])
                nstate.append(lic[r+1][c])
                if nstate.count("#") < 2:
                    li[r][c] = " "

                c += 1
            elif r == 0 and c != 5:
                nstate.append(lic[r][c-1])
                nstate.append(lic[r][c+1])
                nstate.append(lic[r+1][c])
                if nstate.count("#") < 2:
                    li[r][c] = " "

                elif nstate.count("#") >= 3:
                    li[r][c] = "#"

                c += 1
            elif r == 0 and c == 5:
                nstate.append(lic[r][c-1])
                nstate.append(lic[r+1][c])
                if nstate.count("#") < 2:
                    li[r][c] = " "

                c += 1

            elif c == 0 and r != 5:
                nstate.append(lic[r-1][c])
                nstate.append(lic[r][c+1])
                nstate.append(lic[r+1][c])
                if nstate.count("#") < 2:
                    li[r][c] = " "

                elif nstate.count("#") >= 3:
                    li[r][c] = "#"
                    print(r, c, nstate.count("#"))

                c += 1
            elif  0 < c < 5 and 0 < r < 5:
                nstate.append(lic[r][c-1])
                nstate.append(lic[r-1][c])
                nstate.append(lic[r][c+1])
                nstate.append(lic[r+1][c])
                if nstate.count("#") < 2:
                    li[r][c] = " "

                elif nstate.count("#") >= 3:
                    li[r][c] = "#"

                c += 1
            elif c == 5 and r != 5:
                nstate.append(lic[r-1][c])
                nstate.append(lic[r][c-1])
                nstate.append(lic[r+1][c])
                if nstate.count("#") < 2:
                    li[r][c] = " "

                elif nstate.count("#") >= 3:
                    li[r][c] = "#"

                c += 1
            elif c == 0 and r == 5:
                nstate.append(lic[r][c+1])
                nstate.append(lic[r-1][c])
                if nstate.count("#") < 2:
                    li[r][c] = " "

                c += 1
            elif r == 5 and c != 5:
                nstate.append(lic[r][c-1])
                nstate.append(lic[r][c+1])
                nstate.append(lic[r-1][c])
                if nstate.count("#") < 2:
                    li[r][c] = " "

                elif nstate.count("#") >= 3:
                    li[r][c] = "#"

                c += 1
            elif r == 5 and c == 5:
                nstate.append(lic[r][c-1])
                nstate.append(lic[r-1][c])
                if nstate.count("#") < 2:
                    li[r][c] = " "

                c += 1
            else:
                print("you made a mistake somewhere", li[r][c])
                c += 1
        r += 1

    print("")
    for i in range(6):
        print(li[i])