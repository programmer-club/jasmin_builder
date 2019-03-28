class Instruction:
    args = []
    name = ''
    label = ''

    def __init__(self, name, *args):
        self.name = name
        self.args = args

    @staticmethod
    def modded_repr(arg):
        if isinstance(arg, str):
            return '"' + repr(arg)[1:-1] + '"'
        else:
            return repr(arg)

    def __str__(self):
        return (f"{self.label}: " if self.label else "") + f"\t{self.name} {' '.join([Instruction.modded_repr(i) for i in self.args])}\n"
