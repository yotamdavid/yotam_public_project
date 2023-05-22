#odd or even
num = int(input("enter a number: "))
if num % 2 == 0:
    print ("your number is even")
else:
    print("your number is odd")
if num % 4 == 0:
    print("your number is also divisble by 4! ")
#שוואה בין שני מספרים מהמתשמש
num = int(input("enter your number: "))
num_1 = int(input("Type the number by which you want to divide the previous number : "))
if (num % num_1 == 0):
    print("Wow the numbers were distributed accurately!")
else:
    print("Unfortunately the numbers were not mutually exclusive")

