import random

print("welcome to my awesome guessing game!")
highest_number = int(input("What is the largest number you want to guess? ") )
number_to_guess = random.randint(1, highest_number)
print("Alright, the computer picked a random number between 1 and %d"
      % highest_number )

keep_guessing = True
number_of_guesses = 1

while keep_guessing and number_of_guesses <= 10:
    guess = int(input("Guess a number!"))
    number_to_guess += 1
    if guess == number_to_guess:
        print("You win!")
        keep_guessing = False
    elif guess < number_to_guess:
        print("Too low!")
    else:
        print("Too high!")

if number_of_guesses > 10:
    print("You ran out of guesses, the number was %d" % number_to_guess)


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



