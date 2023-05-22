#נחש את המספר
import random

secret_number = random.randint(1, 9)
count_guesses = 0

while True:
    user_guess = int(input("נא להזין מספר בין 1 ל-9: "))
    count_guesses += 1
    if user_guess < secret_number:
        print("המספר שלך נמוך מידי")
    elif user_guess > secret_number:
        print("המספר שלך גבוה מידי")
    else:
        print("כל הכבוד, ניחשת נכון!")
        print("כמות הניחושים שלך היא:", count_guesses)
        break
