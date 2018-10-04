def encrypt(string):
    encrypted_string = []

    for index, character in enumerate(string):
        ordinal_value = ord(character)
        ordinal_value += index
        new_character = chr(ordinal_value)
        encrypted_string.append(new_character)

    return "".join(encrypted_string)

word = input("enter a word")

print(encrypt(word))
