readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
count = 0
total = 0
highest = readings[0]
lowest = readings[0]

for i in readings:
    if i > 3.2:
        count = count + 1

    if i > highest:
        highest = i

    if i < lowest:
        lowest = i

    total = total + i

average = total / len(readings)

print("Above 3.2 V =", count)
print("Highest =", highest)
print("Lowest =", lowest)
print("Average =", average)