import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while len(alphabet) > 0:

    index = random.randint(0, len(alphabet)-1)
    random_letter = alphabet[index, index+1]
    alphabet = alphabet.replace(random_letter, "")
    print(random_letter)


long_names = "Eric|Talia|Muhammed||Patrick"

names_list = long_names.split("|")
names_list.remove("")

long_names_with_spaces = "Eric   Talia     Muhammed   Patrick"

names_list_with_spaces = long_names_with_spaces.split()

print(names_list_with_spaces)

words = "here are some words"

# https://stackoverflow.com/questions/766141/reverse-a-string-in-python
print(words[::-1])