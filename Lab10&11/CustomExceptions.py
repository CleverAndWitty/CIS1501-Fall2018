class InvalidHypotenuseLength(Exception):

    def __init__(self, message):
        self.message = message


class LengthNotDefined(Exception):

    def __init__(self, message):
        self.message = message
        