def shift(letter, distance = 1):
    new_letter = chr(ord(letter) + distance)
    if new_letter > 'Z':
        new_letter = chr(ord(new_letter) - 26)
    return new_letter


def rotate(rotor):
    new_rotor = {}
    for key, value in rotor.items():
        key = shift(key)
        value = shift(value)
        new_rotor[key] = value
        new_rotor[value] = key
    return new_rotor


def encrypt(rotor, letter):
    if 'A' <= letter <= 'Z':
        return rotor[letter]
    return letter


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

rotor = {}

for n in range(13):
    rotor[alphabet[0]] = alphabet[1]
    rotor[alphabet[1]] = alphabet[0]
    alphabet = alphabet.replace(alphabet[:2],"")

word = input("Enter something to encrypt").upper()

result = []

for letter in word:
    result.append(encrypt(rotor, letter))
    rotor = rotate(rotor)

print("".join(result))
