# בונה סיסמאות לפי חוזק שירצה המשתמש
import random
import string
def generate_weak_password(): #הגדרת סיסמה חלשה
    return str(random.randint(0,9999))

def generate_medium_password(): #הגדרת סיסמה בינונית
        # בחירת כל התווים האפשריים לסיסמה
        characters = string.ascii_lowercase + string.digits

        # השתמשות בפונקציית choices כדי לבחור 6 תווים באופן רנדומלי מהרשימה של התווים
        password = ''.join(random.choices(characters, k=6))

        return password

def generate_strong_password(): #הגדרת סיסמה חזקה

        # בחירת כל התווים האפשריים לסיסמה
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

        # השתמשות בפונקציית choices כדי לבחור 8 תווים באופן רנדומלי מהרשימה של התווים
    password = ''.join(random.choices(characters, k=8))

    return password

level = input("Enter password strength level (weak/medium/strong): ")
if level == "weak":
    print("Your weak password is:", generate_weak_password())
elif level == "medium":
    print("Your medium password is:", generate_medium_password())
elif level == "strong":
    print("Your strong password is:", generate_strong_password())
else:
    print("Invalid input, please enter weak/medium/strong.")
