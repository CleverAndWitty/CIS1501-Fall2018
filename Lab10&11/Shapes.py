import CustomExceptions

class RightAngleTriangle:

    def __init__(self):
        self._length_a = 0
        self._length_b = 0
        self._length_c = 0


    def get_area(self):
        if self._length_a == 0 or self._length_b == 0 or self._length_c == 0:
            raise CustomExceptions.LengthNotDefined("Side lengths may not be 0")
        return self._length_a * self._length_b * .5