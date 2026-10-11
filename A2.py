I = float(input("Enter current in amperes = "))
if I > 0:
    print("Current flows from A to B")
elif I < 0:
    print("Current flows from B to A")
else:
    print("No current flows in the circuit")