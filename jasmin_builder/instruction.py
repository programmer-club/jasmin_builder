class Instruction:
    args = []
    name = ''
    label = ''

    def __init__(self, name, *args):
        self.name = name
        self.args = args

    def __str__(self):
        return (f"{self.label}: " if self.label else "") + f"\t{self.name} {' '.join([repr(i) for i in self.args])}\n"
