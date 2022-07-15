#Collatz sequence

def collatz_sequence(num):
    print("Your number is:", num)
    while num != 1:
        cnum = num%2
        if cnum == 0:
            num //= 2
            print(num)
        else:
            num = (3*num + 1)
            print(num)

try:
    n = abs(int(input("Enter your number")))

except:
    print("Invalid input")

collatz_sequence(n)