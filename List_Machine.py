#List listing program

on = True
thelist = []

def listreader(l):
    listlength = len(l)
    for i in range(listlength):
        print(i, "index is:", l[i])

while on == True:
    inp = input("Enter something to your list. Keep it blank to end your list")
    if inp == "":
        break
    else:
        thelist.append(inp)

listreader(thelist)