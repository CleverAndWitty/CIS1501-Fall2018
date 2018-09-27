print('Welcome to our coffee shop')

# set this to something that will make the loop run
menu_number_picked = 1

receipt = {}

while menu_number_picked != 0:
    print("What do you want buy?")
    print("1 - Coffee - $1.50")
    print("2 - Expensive Coffee - $6.50")
    print("3 - Latte - $3.50")
    print("0 - Complete Order")

    answer = input()

    # python short circuits the expression, if not answer.isdigit() is true
    #   then the int() never converts
    while not answer.isdigit() or int(answer) < 0 or int(answer) > 3:
        print("Invalid choice, please enter 0, 1, 2 or 3")
        answer = input()

    menu_number_picked = int(answer)

    if menu_number_picked == 1:
        if 'Coffee' in receipt:
            receipt["Coffee"] += 1.50
        else:
            receipt["Coffee"] = 1.50
    elif menu_number_picked == 2:
        if "Expensive Coffee" in receipt:
            receipt["Expensive Coffee"] += 6.5
        else:
            receipt["Expensive Coffee"] = 6.5
    elif menu_number_picked == 3:
        if "Latte" in receipt:
            receipt["Latte"] += 3.5
        else:
            receipt["Latte"] = 3.5

total = 0

print("Receipt:")
# looping through a dictionary gives only the KEY
for item in receipt:
    print(item, "$%.2f" % receipt[item])
    total += receipt[item]

# %.2f gives a 2 decimal point floating point number
print("Total: $%.2f" % total)
