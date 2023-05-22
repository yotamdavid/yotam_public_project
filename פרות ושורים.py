#משחק פרות ושורים
import random

def play_game():
    # יצירת מספר אקראי בן 4 ספרות
    number = str(random.randint(1000, 9999))
    print("ברוכים הבאים למשחק פרות ושורים!")
    print("נסו לנחש את המספר בן 4 ספרות שחשבתי.")
    guesses = 0

    while True:
        guess = input("נסו לנחש את המספר: ")
        guesses += 1
        if len(guess) != 4 or not guess.isdigit():
            print("יש להזין מספר בן 4 ספרות!")
            continue
        if guess == number:
            print(f"כל הכבוד, נחשתם את המספר ב-{guesses} ניחושים!")
            break
        else:
            cows = 0
            bulls = 0
            for i in range(4):
                if guess[i] == number[i]:
                    cows += 1
                elif guess[i] in number:
                    bulls += 1
            print(f"{cows} פרות, {bulls} שורים")
    return guesses

play_game()
