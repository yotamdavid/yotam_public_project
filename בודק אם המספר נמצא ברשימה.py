#בודק אם מספר נמצא ברשימה
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False

# לדוגמה:
my_list = [1, 3, 5, 7, 9]
num = 4

if binary_search(my_list, num):
    print(f"{num} נמצא ברשימה")
else:
    print(f"{num} לא נמצא ברשימה")