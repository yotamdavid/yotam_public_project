# divisors
num = int(input("הכנס מספר: "))
factors = []

# לחשב את כל המחלקים של המספר:
for i in range(1, num+1):
    if num % i == 0:
        factors.append(i)

# להדפיס את המחלקים:
print("המחלקים של", num, "הם:")
for factor in factors:
    print(factor)