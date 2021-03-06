from typing import List

from jasmin_builder.instruction import Instruction

# ACC_PUBLIC	0x0001	Declared public; may be accessed from outside its package.
# ACC_PRIVATE	0x0002
# Declared private; accessible only within the defining class and other classes belonging to the same nest (§5.4.4).
#
# ACC_PROTECTED	0x0004	Declared protected; may be accessed within subclasses.
# ACC_STATIC	0x0008	Declared static.
# ACC_FINAL	0x0010	Declared final; must not be overridden (§5.4.5).
# ACC_SYNCHRONIZED	0x0020	Declared synchronized; invocation is wrapped by a monitor use.
# ACC_BRIDGE	0x0040	A bridge method, generated by the compiler.
# ACC_VARARGS	0x0080	Declared with variable number of arguments.
# ACC_NATIVE	0x0100	Declared native; implemented in a language other than the Java programming language.
# ACC_ABSTRACT	0x0400	Declared abstract; no implementation is provided.
# ACC_STRICT	0x0800	Declared strictfp; floating-point mode is FP-strict.
# ACC_SYNTHETIC	0x1000	Declared synthetic; not present in the source code.
MOD_PUBLIC = "public"
MOD_PRIVATE = "private"
MOD_PROTECTED = "protected"
MOD_STATIC = "static"
MOD_FINAL = "final"
MOD_SYNCHRONIZED = "synchronized"
MOD_BRIDGE = "bridge"
MOD_VARARGS = "varargs"
MOD_NATIVE = "native"
MOD_ABSTRACT = "abstract"
MOD_STRICTFP = "strictfp"
MOD_SYNTHETIC = "synthetic"

MODIFIER_LIST = [MOD_PUBLIC, MOD_PRIVATE, MOD_PROTECTED, MOD_STATIC, MOD_FINAL, MOD_SYNCHRONIZED, MOD_BRIDGE,
                 MOD_VARARGS, MOD_NATIVE, MOD_ABSTRACT, MOD_STRICTFP, MOD_SYNTHETIC]


class Method:
    instructions = []  # type: List[Instruction]
    name = ''
    modifiers = []  # type: List[str]
    args = []
    stack_limit = -1
    locals_limit = -1
    cls = None
    ret = ''

    def __init__(self, name: str, args: List, modifiers: List[str], return_: str = "V", stack_limit: int = -1,
                 locals_limit: int = -1):
        self.name = name
        self.args = args
        self.modifiers = modifiers
        for i in self.modifiers:
            assert i in MODIFIER_LIST, "Invalid modifier: " + i
        self.stack_limit = stack_limit
        self.locals_limit = locals_limit
        self.instructions = []
        self.ret = return_

    def add_modifier(self, mod: str):
        assert mod in MODIFIER_LIST, "Invalid modifier: " + mod
        self.modifiers.append(mod)

    def insert_instructon(self, instr, label=""):
        instr.label = label
        self.instructions.append(instr)

    def format_args(self):
        return "".join(map(str, self.args))

    def __str__(self):
        return f".method {' '.join(self.modifiers)} {self.name}({self.format_args()}){self.ret}\n" + \
               (f"\t.limit stack {self.stack_limit}\n" if self.stack_limit != -1 else '') + \
               (f"\t.limit locals {self.locals_limit}\n" if self.locals_limit != -1 else '') + \
               "".join([str(instr) for instr in self.instructions]) + \
               ".end method"
