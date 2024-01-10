number = int(input("Enter a decimal number to convert to binary: "))
binary_representation = bin(number)[2:]  # Convert to binary and remove '0b' prefix
print(f"The binary representation of {number} is: {binary_representation}")

