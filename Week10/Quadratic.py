# x = (-b +- sqrt(b**2 - ( 4ac )))/2a

def absolute_value(value):
    if value < 0:
        return value * -1
    return value

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


if __name__ == '__main__':
    print("Hi, I'm the quadratic module!")