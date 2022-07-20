#Conway’s Game of Life Improved
import random
import copy

game = True

state = (" ", "#")
li = []

while game == True:
    try:
        gb = int(input("Enter a single int for the gameboard bigger than 5"))
        if gb < 6:
            print("Choose a larger number")
        else:
            break
    except:
        print("Invalid Input")

for i in range(gb):
    lt = []
    for i in range(gb):
        lt.append(random.choice(state))
    li.append(lt)

for i in range(gb):
    print(li[i])

try:
    gp = int(input("How many iterations of Conways Game do you want?"))

except:
    print("Invalid entry")

for game in range(gp):
    lic = copy.deepcopy(li)
    for row in range(gb):
        for column in range(gb):
            nstate = []
            r = row - 1
            for y in range(3):
                c = column - 1
                for x in range(3):
                    try:
                        if r < 0 or c < 0:
                            c += 1
                        else:
                            nstate.append(lic[r][c])
                            if r == row and c == column:
                                nstate.remove(li[row][column])
                            c += 1
                    except:
                        c += 1
                r += 1
            if li[row][column] == " " and nstate.count("#") == 3:
                #print("Adding to:", row, column)
                li[row][column] = "#"
            elif nstate.count("#") < 2 or nstate.count("#") > 3:
                li[row][column] = " "
    for i in range(6):
        print(li[i])