# pattern_drawing.py

# Ask the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop using while
while row < size:
    # Inner loop using for to print asterisks in the row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line
    row += 1
