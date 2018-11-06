# x = (-b +- sqrt(b**2 - ( 4ac )))/2a

class NegativeDiscriminantError(Exception):

    def __init__(self, value):
        self.value = value


class Quadratic:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_x_intercepts(self):
        discriminant = self.b**2 - (4 * self.a * self.c)
        if discriminant < 0:
            raise NegativeDiscriminantError("There are no roots if the discrim... is negative")
        x1 = ( -1 * self.b + (self.b**2 - (4 * self.a * self.c))**.5 ) \
             / (2 * self.a)
        x2 = ( -1 * self.b - (self.b**2 - (4 * self.a * self.c))**.5 ) \
             / (2 * self.a)
        return (x1, x2)


keep_going = 'y'

while keep_going == 'y':
    a = int(input("Enter the A value: "))
    b = int(input("Enter the B value: "))
    c = int(input("Enter the C value: "))
    quad = Quadratic(a, b, c)
    try:
        print("X intercepts are {0:.3f} and {0:.3f}".format(quad.get_x_intercepts()[0],quad.get_x_intercepts()[1]))
    except NegativeDiscriminantError:
        print("No x intercepts found!")
    keep_going = input("Try again? y/n ")
