import random

class Rotor:
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, seed):
        self.position = 0
        self.mapping = {}
        self.rotor_number = seed
        random.seed(seed)
        alphabet_list = []
        for letter in Rotor.ALPHABET:
            alphabet_list.append(letter)
        for pair in range(13):
            first_letter = alphabet_list[random.randint(0, len(alphabet_list) - 1)]
            alphabet_list.remove(first_letter)
            second_letter = alphabet_list[random.randint(0, len(alphabet_list) - 1)]
            alphabet_list.remove(second_letter)
            self.mapping[first_letter] = second_letter
            self.mapping[second_letter] = first_letter

    def get_mapped_letter(self, letter):
        return self.mapping.get(letter, letter)

    def _shift_letter(self, letter, shift):
        new_letter = chr(ord(letter) + shift)
        if new_letter > 'Z':
            new_letter = chr(ord(new_letter) - 26)
        return new_letter

    def rotate(self, rotations=1):
        new_rotor = {}
        self.position += rotations
        if self.position > 26:
            self.position -= 26

        for first, second in self.mapping.items():
            new_first = self._shift_letter(first, rotations)
            new_second = self._shift_letter(second, rotations)
            new_rotor[new_first] = new_second
            new_rotor[new_second] = new_first
        self.mapping = new_rotor

    def __str__(self):
        return "Rotor Number: {} - Position: {}".format(self.rotor_number, self.position)


class Enigma:

    def __init__(self,
                 rotor_1_position=1,
                 rotor_2_position=1,
                 rotor_3_position=1):
        self.rotor1 = Rotor(1)
        self.rotor1.rotate(rotor_1_position)

        self.rotor2 = Rotor(2)
        self.rotor2.rotate(rotor_2_position)

        self.rotor3 = Rotor(3)
        self.rotor3.rotate(rotor_3_position)

        self.reflector = Rotor(0)
        self.number_of_letters_encrypted = 0

    def get_encrypted_letter(self, letter):
        self.number_of_letters_encrypted += 1
        letter = self.rotor1.get_mapped_letter(letter)
        letter = self.rotor2.get_mapped_letter(letter)
        letter = self.rotor3.get_mapped_letter(letter)
        letter = self.reflector.get_mapped_letter(letter)
        letter = self.rotor3.get_mapped_letter(letter)
        letter = self.rotor2.get_mapped_letter(letter)
        letter = self.rotor1.get_mapped_letter(letter)

        self.rotor1.rotate()
        if self.number_of_letters_encrypted % 26 == 0:
            self.rotor2.rotate()
        if self.number_of_letters_encrypted % 26*26 == 0:
            self.rotor3.rotate()

        return letter

    def __str__(self):
        return "{} {} {}".format(self.rotor1, self.rotor2, self.rotor3)


starting_positions = input("Enter the starting positions (1 2 3): ").split()
my_machine = Enigma(int(starting_positions[0]),\
                    int(starting_positions[1]),\
                    int(starting_positions[2]))

message = input("Enter a message to encrypt: ")

for letter in message:
    print(my_machine.get_encrypted_letter(letter), end="")
print()
print(my_machine)