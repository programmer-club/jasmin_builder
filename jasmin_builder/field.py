class Field:
    type_: str = ''
    name: str = ''

    def __init__(self, type_: str, name):
        self.type_ = type_
        self.name = str(name)

    def __str__(self):
        return f".field private {self.name} {self.type_}"  # TODO: field modifiers
