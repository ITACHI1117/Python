# Nested loops

rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")  # (end="" prevents cursor from moving to the next line in the terminal)
    print()
