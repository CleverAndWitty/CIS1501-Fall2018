temp = int(input('Enter the temp in degrees F'))

if temp < 50:
    print("don't forget your jacket!")
else:
    print("put on sunscreen")

print("have a nice walk!")


score = int(input("Enter your score 0-100: "))

# this works, but is ugly
if score > 93:
    print("A")
else:
    if score > 90:
        print("A-")
    else:
        if score > 86:
            print("B+")

# pretty way - chained elif
if score > 93:
    print('A')
elif score > 90:
    print("A-")
elif score > 86:
    print("B+")
elif score > 83:
    print("B")

#long way without nesting
if score > 93:
    print("A")

# same as if 90 < score and score < 94:
if 90 < score < 94:
    print("A-")

if score < 91 and score > 86:
    print("B+")


