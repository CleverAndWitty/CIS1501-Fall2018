import random

print("welcome to my awesome guessing game!")
highest_number = int(input("What is the largest number you want to guess? ") )
number_to_guess = random.randint(1, highest_number)
print("Alright, the computer picked a random number between 1 and %d"
      % highest_number )
guess = int(input("Guess a number!"))
keep_guessing = True

if guess == number_to_guess:
    print("You win!")
    keep_guessing = False
elif guess < number_to_guess:
    print("Too low!")
else:
    print("Too high!")

if keep_guessing:
    print("Didn't guess it yet?")



items_for_sale = {
    "coffee": 1.5,
    "expensive coffee": 6.5,
    "latte": 5
}
total_purchase = 0

purchase = input("Welcome to my coffee shop, what do you want to buy?").lower()

if purchase in items_for_sale:
    print("enjoy your %s" % purchase)
    total_purchase += items_for_sale[purchase]
else:
    print("We don't sell that")



