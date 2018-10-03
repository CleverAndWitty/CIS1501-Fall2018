def find_x_intercepts(polynomial):
    # FIXME
    return "FIXME"

def print_face(face_char):
    int = 10
    if len(face_char) > 1:
        face_char = face_char[0]
        return face_char
    print('  ', face_char, ' ', face_char)  # Print eyes
    print('    ', face_char)                # Print nose
    print('  ', face_char*5)                # Print mouth
    print(int)

print(int)
character = input("What character should we use to make a face?")
fixed_character = print_face(character)
print_face(character)
print_face(character)
print_face(character)
print(print_face(character))
my_other_function = print_face

my_other_function("b")


def sum(a, b):
    return a + b


print(sum(10, 20))

sum(10, 20, 30)

