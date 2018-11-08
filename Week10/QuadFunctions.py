import Quadratic

keep_going = 'y'

while keep_going == 'y':
    a = int(input("Enter the A value: "))
    b = int(input("Enter the B value: "))
    c = int(input("Enter the C value: "))
    quad = Quadratic.Quadratic(a, b, Quadratic.absolute_value(c))
    try:
        print("X intercepts are {0:.3f} and {0:.3f}".format(quad.get_x_intercepts()[0],quad.get_x_intercepts()[1]))
    except Quadratic.NegativeDiscriminantError:
        print("No x intercepts found!")
    keep_going = input("Try again? y/n ")
