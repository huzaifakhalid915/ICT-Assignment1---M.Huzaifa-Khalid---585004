R1 = float(input("Enter first resistor: "))
R2 = float(input("Enter second resistor: "))
R3 = float(input("Enter third resistor: "))

if R1 < R2 and R1 < R3:
    small = R1
elif R2 < R1 and R2 < R3:
    small = R2
else:
    small = R3

if R1 > R2 and R1 > R3:
    large = R1
elif R2 > R1 and R2 > R3:
    large = R2
else:
    large = R3

print("Smallest =", small)
print("Largest =", large)