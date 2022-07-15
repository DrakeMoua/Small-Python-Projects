#zigzag program

import time
from math import pi, sin

run = True

while run == True:
    try:
        t = float(input("Enter a time in seconds"))
        w = int(input("Enter the width of the animation"))
        break
    except:
        print("Invalid input")

ttime = time.time() + t

animation = "********"
space = " "
count = 0

while time.time() < ttime:
    for i in range(w):
        print(space*count + animation)
        count += 1

    for i in range(w):
        count -= 1
        print(space*count + animation)