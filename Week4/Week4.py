nth_fib_term = int(input(
    "What fibbonaci number do you want to count to?"))

current_term = 1
previous = 0
current = 1

while current_term < nth_fib_term:
    next = current + previous
    previous = current
    current = next
    current_term += 1

print("The %d th fibbonaci term is: %d" % ( nth_fib_term, current))


factorial = int(input("Factioral of: "))
original_factorial = factorial
product = 1

while factorial > 1:
    product *= factorial
    factorial -= 1

print("%d factorial is: %d" % (original_factorial, product))



names = [ 'Eric', 'Talia', 'Steven', 'Muhammed', 'Numan', 'Patrick']

index = 0
while index < len(names):
    name = names[index]
    print(name)
    index += 1

for name in names:
    name += " is awesome!"
    print(name)

for index in range(len(names)):
    names[index] += " is awesome!"
    print(names[index])



height = int(input("How big of a triangle should I print?"))

for number_of_stars in range(1, height + 1):
    print("*" * number_of_stars)

number_of_stars = 1
while number_of_stars <= height:
    print("*" * number_of_stars)
    number_of_stars += 1


