class InvalidNumberOfSideLengths(Exception):

    def __init__(self, value=""):
        self.value = value


class Polygon:

    def __init__(self, number_of_sides, side_lengths):
        if number_of_sides != len(side_lengths):
            raise InvalidNumberOfSideLengths("Expecting {} lengths".format(number_of_sides))
        self.number_of_sides = number_of_sides
        self.side_lengths = side_lengths

    def get_perimeter(self):
        return 0

    def get_area(self):
        return