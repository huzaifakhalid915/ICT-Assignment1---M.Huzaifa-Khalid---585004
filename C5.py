def star_to_delta(ra, rb, rc):
    total = ra * rb + rb * rc + rc * ra

    r1 = total/ra
    r2 = total/rb
    r3 = total/rc

    return round(r1, 2), round(r2, 2), round(r3, 2)

ra = float(input("Enter ra: "))
rb = float(input("Enter rb: "))
rc = float(input("Enter rc: "))

r1, r2, r3 = star_to_delta(ra, rb, rc)

print("Delta resistance 1:", r1, "ohms")
print("Delta resistance 2:", r2, "ohms")
print("Delta resistance 3:", r3, "ohms")