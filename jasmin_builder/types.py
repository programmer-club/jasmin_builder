class Array:
    def __init__(self, internal):
        self.internal = internal

    def __str__(self):
        return '[' + str(self.internal)


class Link:
    def __init__(self, internal):
        self.internal = internal

    def __str__(self):
        return 'L' + str(self.internal).replace('.', '/') + ';'


BYTE = 'B'
CHAR = 'C'
DOUBLE = 'D'
FLOAT = 'F'
INT = 'I'
LONG = 'J'
SHORT = 'S'
BOOLEAN = 'Z'
VOID = 'V'
