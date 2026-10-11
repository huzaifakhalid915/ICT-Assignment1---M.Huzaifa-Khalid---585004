V = float(input("Enter voltage in volts = "))
R = float(input("Enter resistance in ohms = "))

if R <= 0:
    print("Invalid Resistance")
else:
    I = V/R
    print("Current =", I, "A")

    if I > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")