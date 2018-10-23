import random


def shift_letter(letter, shift):
    new_letter = chr(ord(letter) + shift)
    if new_letter > 'Z':
        new_letter = chr(ord(new_letter) - 26)
    return new_letter


def encrypt(rotor, letter):
    # return value associated with key of letter, or default of letter
    return rotor.get(letter, letter)


def rotate(rotor, shift=1):
    items = rotor.items()
    rotor.clear()
    for first, second in items:
        new_first = shift_letter(first, shift)
        new_second = shift_letter(second, shift)
        rotor[new_first] = new_second
        rotor[new_second] = new_first


rotors = []

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for rotor_number in range(3):
    random.seed(rotor_number)
    rotors.append({})
    alphabet_list = []
    for letter in alphabet:
        alphabet_list.append(letter)
    for pair in range(13):
        first_letter = alphabet_list[random.randint(0,len(alphabet_list)-1)]
        alphabet_list.remove(first_letter)
        second_letter = alphabet_list[random.randint(0, len(alphabet_list) - 1)]
        alphabet_list.remove(second_letter)
        rotors[rotor_number][first_letter] = second_letter
        rotors[rotor_number][second_letter] = first_letter

#for rotor in rotors:
#    print(rotor)

message = input("What should we encrypt?").upper()
result = []
for letter in message:
    for rotor in rotors:
        letter = encrypt(rotor, letter)
        rotate(rotor)
    result.append(letter)

print("".join(result))