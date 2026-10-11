n = int(input("How many resistors? "))
total = 0
for i in range(n):
    R = float(input("Enter resistor value: "))
    total += R
print("Total resistance:", total)