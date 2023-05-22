# מספרי פיבונאצי
def fibonacci_sequence(num):
    # בדיקת כניסת נתונים חוקית מהמשתמש
    if num <= 0:
        return "אנא הזן מספר חיובי ושלם."
    elif num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    else:
        # יצירת רשימה להכיל את המספרים ברצף פיבונאצי
        fib_lst = [1, 1]
        for i in range(2, num):
            fib_lst.append(fib_lst[i-1] + fib_lst[i-2])
        return fib_lst

num = int(input("אנא הזן מספר שלם וחיובי של מספרי פיבונאצי להפיק: "))

print(fibonacci_sequence(num))