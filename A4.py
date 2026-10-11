A = int(input("Enter A: "))
B = int(input("Enter B: "))

if A not in [0, 1] or B not in [0, 1]:
    print("Bits must be 0 or 1")
else:
    print("AND =", A & B)
    print("OR =", A | B)
    print("XOR =", A ^ B)
