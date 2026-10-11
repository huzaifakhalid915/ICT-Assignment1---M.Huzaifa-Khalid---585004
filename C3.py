def decimal_to_binary(n):
    binary = ""

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary

n = int(input("Enter a decimal number: "))
print("Binary: ", decimal_to_binary(n))
