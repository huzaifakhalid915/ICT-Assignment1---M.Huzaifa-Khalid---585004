def ohm_current(v, r):
    return v / r
def power_dissipated(i, r):
    return i ** 2 * r

v = 12
r = 6
i = ohm_current(v, r)
p = power_dissipated(i, r)

print("Current: ", i, "A")
print("Power Dissipated: ", p, "W")