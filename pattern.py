# The code to output an arrow pattern using if statement and while loop
rows = int(input("Enter the number of rows: "))

for r in range(rows):
    for c in range(1, r + 1):
        print("*", end="")
    print()

for r in range(rows - 1, 1, -1):
    for c in range(1, r + 1):
        print("*", end="")
    print()