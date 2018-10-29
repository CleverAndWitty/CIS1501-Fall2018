import random

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def shift_letter(letter, shift):
    new_letter = chr(ord(letter) + shift)
    if new_letter > 'Z':
        new_letter = chr(ord(new_letter) - 26)
    return new_letter


def encrypt(rotor, letter):
    # return value associated with key of letter, or default of letter
    return rotor.get(letter, letter)


def rotate(rotor, shift=1):
    new_rotor = {}

    for first, second in rotor.items():
        new_first = shift_letter(first, shift)
        new_second = shift_letter(second, shift)
        new_rotor[new_first] = new_second
        new_rotor[new_second] = new_first
    return new_rotor


def make_rotor(seed):
    random.seed(seed)
    rotor = {}
    alphabet_list = []
    for letter in ALPHABET:
        alphabet_list.append(letter)
    for pair in range(13):
        first_letter = alphabet_list[random.randint(0, len(alphabet_list) - 1)]
        alphabet_list.remove(first_letter)
        second_letter = alphabet_list[random.randint(0, len(alphabet_list) - 1)]
        alphabet_list.remove(second_letter)
        rotor[first_letter] = second_letter
        rotor[second_letter] = first_letter
    return rotor


rotors = []

plugboard_pairs = input("Enter 10 pairs for the plugboard ( AB CD EF GH IJ KL MN OP QR ST ): ").split()
plugboard = {}
for pair in plugboard_pairs:
    plugboard[pair[0]] = pair[1]
    plugboard[pair[1]] = pair[0]

rotors.append(plugboard)

rotor_numbers = input("Enter the rotor numbers to insert in the machine( 1 2 3 ): ").split()
for rotor_number in rotor_numbers:
    rotors.append(make_rotor(int(rotor_number)))

rotor_position = input("Enter rotor positions ( 0 0 0 ):").split()
rotors[1] = rotate(rotors[1], int(rotor_position[0]))
rotors[2] = rotate(rotors[2], int(rotor_position[1]))
rotors[3] = rotate(rotors[3], int(rotor_position[2]))

rotors.append(make_rotor(0))

message = input("What should we encrypt?").upper()
#encrypt_or_decrypt = input("(E)ncrypt or (D)ecrypt?")
result = []
for letter in message:
    letter_count = 1
    #if encrypt_or_decrypt == 'E':
    for rotor_index in range(len(rotors)):
        letter = encrypt(rotors[rotor_index], letter)

    for rotor_index in range(3,-1,-1):
        letter = encrypt(rotors[rotor_index], letter)
        if rotor_index == 1:
            rotors[1] = rotate(rotors[1])
        if rotor_index == 2 and letter_count % 26 == 0:
            rotors[2] = rotate(rotors[2])
        if rotor_index == 3 and letter_count % 26**2 == 0:
            rotors[2] = rotate(rotors[3])

    #else:
    #    for rotor_index in range((len(rotors)-1),-1,-1):
    #        letter = encrypt(rotors[rotor_index], letter)
    #        rotors[rotor_index] = rotate(rotors[rotor_index])
    result.append(letter)
    letter_count += 1

print("".join(result))