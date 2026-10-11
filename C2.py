def parallel_resistance(resistors):
    total = 0
    for r in resistors:
        total += 1 / r
    return 1/total

resistors = [6, 12, 18]
result = parallel_resistance(resistors)
print("Total Parallel Resistance: ", result)