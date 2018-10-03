import random

number_of_dice = int(input("How many dice do you want to roll?" ))
number_of_rolls = int(input("How many times should we roll them?" ))

sums = {}
for total in range(number_of_dice, number_of_dice*6 + 1):
    sums[total] = 0

for roll in range(number_of_rolls):
    total = 0
    for die in range(number_of_dice):
        total += random.randint(1, 6)
    sums[total] += 1

# order isn't guaranteed in dictionaries, so if we had to sort we could use:
# for total in sorted(list(sums.keys())):
for total in sums:
    print("%2d: %s" % (total, "*" * sums[total]))
