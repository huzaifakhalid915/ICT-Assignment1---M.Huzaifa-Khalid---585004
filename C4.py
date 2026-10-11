def loaded_divider(vs, r1, r2, rl):
    unloaded = vs * (r2 / (r1 + r2))

    parallel = 1 / ((1 / r2) + (1 / rl))

    loaded = vs * (parallel / (r1 + parallel))
    return unloaded, loaded
 
vs = float(input("Enter the source voltage: "))
r1 = float(input("Enter the resistance of R1: "))
r2 = float(input("Enter the resistance of R2: "))
rl = float(input("Enter the resistance of RL: "))

unloaded, loaded = loaded_divider(vs, r1, r2, rl)

print("Unloaded voltage:", round(unloaded, 2), "V")
print("Loaded voltage:", round(loaded, 2), "V")