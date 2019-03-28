from typing import List

from jasmin_builder.field import Field
from jasmin_builder.method import Method
from jasmin_builder.modifiers import *


class Class:
    methods: List[Method] = []
    fields: List[Field] = ''
    super: str = ''
    modifiers: int = 0  # Bitfield from modifiers.py
    name: str = ''

    def __init__(self, name: str, modifiers: int = 0, superclass="java/lang/Object", methods: List[Method] = None,
                 fields: List[Field] = None):
        self.name = name
        self.super = superclass
        self.methods = methods if methods else []
        self.fields = fields if fields else []
        self.modifiers |= modifiers

    def add_method(self, meth: Method):
        self.methods.append(meth)

    def add_field(self, field):
        self.fields.append(field)

    def format_mods(self):
        mods = []

        # ACC_PUBLIC = 0x0001
        # ACC_FINAL = 0x0010
        # ACC_SUPER = 0x0020
        # ACC_INTERFACE = 0x0200
        # ACC_ABSTRACT = 0x0400
        # ACC_SYNTHETIC = 0x1000
        # ACC_ANNOTATION = 0x2000
        # ACC_ENUM = 0x4000
        # ACC_MODULE = 0x8000

        if self.modifiers & ACC_PUBLIC:
            mods.append("public")
        if self.modifiers & ACC_FINAL:
            mods.append("final")
        if self.modifiers & ACC_SUPER:
            mods.append("super")  # TODO: this is wrong
        if self.modifiers & ACC_INTERFACE:
            mods.append("interface")  # TODO: this is too probably
        if self.modifiers & ACC_ABSTRACT:
            mods.append("abstract")
        if self.modifiers & ACC_SYNTHETIC:
            mods.append("synthetic")
        if self.modifiers & ACC_ANNOTATION:
            mods.append("annotation")
        if self.modifiers & ACC_ENUM:
            mods.append("enum")
        if self.modifiers & ACC_MODULE:
            mods.append("module")

        return " ".join(mods)

    def format_fields(self):
        return "\n".join(map(str, self.fields))

    def format_methods(self):
        return "\n\n".join(map(str, self.methods))

    def __str__(self):
        return f"""
.class {self.format_mods()} {self.name}
.super {self.super}
{self.format_fields()}
{self.format_methods()}
"""[1:-1]

    def to_file(self):
        with open(self.name + '.j', 'w') as f:
            f.write(str(self))
