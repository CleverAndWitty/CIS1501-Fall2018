base = int(input("What size triangle do you want?"))

# int 0 is false
# if not base % 2:
# this makes sure we have an odd base
if base % 2 == 0:
    base += 1

rows = (base + 1) // 2

for row_number in range(1, rows+1):
    print(" " * (rows - row_number), end="")
    print("*" * ((row_number * 2) - 1))

print()
print()


spaces = (base + 1) // 2 - 1
stars = 1

while stars <= base:
    print(" " * spaces, end="")
    print("*" * stars)
    spaces -= 1
    stars += 2

