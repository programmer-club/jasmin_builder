from jasmin_builder.instruction import Instruction
from jasmin_builder.method import Method


class Builder:
    def __init__(self, method: Method):
        self.method = method

    def insert_instruction(self, instr, label=""):
        self.method.insert_instructon(instr, label)

    # TODO: switch instructions

    def ret(self, variable_number: int, label=''):
        self.insert_instruction(Instruction("ret", variable_number), label)

    def aload(self, variable_number: int, label=''):
        self.insert_instruction(Instruction("aload", variable_number), label)

    def astore(self, variable_number: int, label=''):
        self.insert_instruction(Instruction("astore", variable_number), label)

    def dload(self, variable_number: int, label=''):
        self.insert_instruction(Instruction("dload", variable_number), label)

    def dstore(self, variable_number: int, label=''):
        self.insert_instruction(Instruction("dstore", variable_number), label)

    def fload(self, variable_number: int, label=''):
        self.insert_instruction(Instruction("fload", variable_number), label)

    def fstore(self, variable_number: int, label=''):
        self.insert_instruction(Instruction("fstore", variable_number), label)

    def iload(self, variable_number: int, label=''):
        self.insert_instruction(Instruction("iload", variable_number), label)

    def istore(self, variable_number: int, label=''):
        self.insert_instruction(Instruction("istore", variable_number), label)

    def lload(self, variable_number: int, label=''):
        self.insert_instruction(Instruction("lload", variable_number), label)

    def lstore(self, variable_number: int, label=''):
        self.insert_instruction(Instruction("lstore", variable_number), label)

    def aaload(self, label=''):
        self.insert_instruction(Instruction("aaload"), label)

    def aastore(self, label=''):
        self.insert_instruction(Instruction("aastore"), label)

    def aconst_null(self, label=''):
        self.insert_instruction(Instruction("aconst_null"), label)

    def aload_0(self, label=''):
        self.insert_instruction(Instruction("aload_0"), label)

    def aload_1(self, label=''):
        self.insert_instruction(Instruction("aload_1"), label)

    def aload_2(self, label=''):
        self.insert_instruction(Instruction("aload_2"), label)

    def aload_3(self, label=''):
        self.insert_instruction(Instruction("aload_3"), label)

    def areturn(self, label=''):
        self.insert_instruction(Instruction("areturn"), label)

    def arraylength(self, label=''):
        self.insert_instruction(Instruction("arraylength"), label)

    def astore_0(self, label=''):
        self.insert_instruction(Instruction("astore_0"), label)

    def astore_1(self, label=''):
        self.insert_instruction(Instruction("astore_1"), label)

    def astore_2(self, label=''):
        self.insert_instruction(Instruction("astore_2"), label)

    def astore_3(self, label=''):
        self.insert_instruction(Instruction("astore_3"), label)

    def athrow(self, label=''):
        self.insert_instruction(Instruction("athrow"), label)

    def baload(self, label=''):
        self.insert_instruction(Instruction("baload"), label)

    def bastore(self, label=''):
        self.insert_instruction(Instruction("bastore"), label)

    def breakpoint(self, label=''):
        self.insert_instruction(Instruction("breakpoint"), label)

    def caload(self, label=''):
        self.insert_instruction(Instruction("caload"), label)

    def castore(self, label=''):
        self.insert_instruction(Instruction("castore"), label)

    def d2f(self, label=''):
        self.insert_instruction(Instruction("d2f"), label)

    def d2i(self, label=''):
        self.insert_instruction(Instruction("d2i"), label)

    def d2l(self, label=''):
        self.insert_instruction(Instruction("d2l"), label)

    def dadd(self, label=''):
        self.insert_instruction(Instruction("dadd"), label)

    def daload(self, label=''):
        self.insert_instruction(Instruction("daload"), label)

    def dastore(self, label=''):
        self.insert_instruction(Instruction("dastore"), label)

    def dcmpg(self, label=''):
        self.insert_instruction(Instruction("dcmpg"), label)

    def dcmpl(self, label=''):
        self.insert_instruction(Instruction("dcmpl"), label)

    def dconst_0(self, label=''):
        self.insert_instruction(Instruction("dconst_0"), label)

    def dconst_1(self, label=''):
        self.insert_instruction(Instruction("dconst_1"), label)

    def ddiv(self, label=''):
        self.insert_instruction(Instruction("ddiv"), label)

    def dload_0(self, label=''):
        self.insert_instruction(Instruction("dload_0"), label)

    def dload_1(self, label=''):
        self.insert_instruction(Instruction("dload_1"), label)

    def dload_2(self, label=''):
        self.insert_instruction(Instruction("dload_2"), label)

    def dload_3(self, label=''):
        self.insert_instruction(Instruction("dload_3"), label)

    def dmul(self, label=''):
        self.insert_instruction(Instruction("dmul"), label)

    def dneg(self, label=''):
        self.insert_instruction(Instruction("dneg"), label)

    def drem(self, label=''):
        self.insert_instruction(Instruction("drem"), label)

    def dreturn(self, label=''):
        self.insert_instruction(Instruction("dreturn"), label)

    def dstore_0(self, label=''):
        self.insert_instruction(Instruction("dstore_0"), label)

    def dstore_1(self, label=''):
        self.insert_instruction(Instruction("dstore_1"), label)

    def dstore_2(self, label=''):
        self.insert_instruction(Instruction("dstore_2"), label)

    def dstore_3(self, label=''):
        self.insert_instruction(Instruction("dstore_3"), label)

    def dsub(self, label=''):
        self.insert_instruction(Instruction("dsub"), label)

    def dup(self, label=''):
        self.insert_instruction(Instruction("dup"), label)

    def dup2(self, label=''):
        self.insert_instruction(Instruction("dup2"), label)

    def dup2_x1(self, label=''):
        self.insert_instruction(Instruction("dup2_x1"), label)

    def dup2_x2(self, label=''):
        self.insert_instruction(Instruction("dup2_x2"), label)

    def dup_x1(self, label=''):
        self.insert_instruction(Instruction("dup_x1"), label)

    def dup_x2(self, label=''):
        self.insert_instruction(Instruction("dup_x2"), label)

    def f2d(self, label=''):
        self.insert_instruction(Instruction("f2d"), label)

    def f2i(self, label=''):
        self.insert_instruction(Instruction("f2i"), label)

    def f2l(self, label=''):
        self.insert_instruction(Instruction("f2l"), label)

    def fadd(self, label=''):
        self.insert_instruction(Instruction("fadd"), label)

    def faload(self, label=''):
        self.insert_instruction(Instruction("faload"), label)

    def fastore(self, label=''):
        self.insert_instruction(Instruction("fastore"), label)

    def fcmpg(self, label=''):
        self.insert_instruction(Instruction("fcmpg"), label)

    def fcmpl(self, label=''):
        self.insert_instruction(Instruction("fcmpl"), label)

    def fconst_0(self, label=''):
        self.insert_instruction(Instruction("fconst_0"), label)

    def fconst_1(self, label=''):
        self.insert_instruction(Instruction("fconst_1"), label)

    def fconst_2(self, label=''):
        self.insert_instruction(Instruction("fconst_2"), label)

    def fdiv(self, label=''):
        self.insert_instruction(Instruction("fdiv"), label)

    def fload_0(self, label=''):
        self.insert_instruction(Instruction("fload_0"), label)

    def fload_1(self, label=''):
        self.insert_instruction(Instruction("fload_1"), label)

    def fload_2(self, label=''):
        self.insert_instruction(Instruction("fload_2"), label)

    def fload_3(self, label=''):
        self.insert_instruction(Instruction("fload_3"), label)

    def fmul(self, label=''):
        self.insert_instruction(Instruction("fmul"), label)

    def fneg(self, label=''):
        self.insert_instruction(Instruction("fneg"), label)

    def frem(self, label=''):
        self.insert_instruction(Instruction("frem"), label)

    def freturn(self, label=''):
        self.insert_instruction(Instruction("freturn"), label)

    def fstore_0(self, label=''):
        self.insert_instruction(Instruction("fstore_0"), label)

    def fstore_1(self, label=''):
        self.insert_instruction(Instruction("fstore_1"), label)

    def fstore_2(self, label=''):
        self.insert_instruction(Instruction("fstore_2"), label)

    def fstore_3(self, label=''):
        self.insert_instruction(Instruction("fstore_3"), label)

    def fsub(self, label=''):
        self.insert_instruction(Instruction("fsub"), label)

    def i2d(self, label=''):
        self.insert_instruction(Instruction("i2d"), label)

    def i2f(self, label=''):
        self.insert_instruction(Instruction("i2f"), label)

    def i2l(self, label=''):
        self.insert_instruction(Instruction("i2l"), label)

    def iadd(self, label=''):
        self.insert_instruction(Instruction("iadd"), label)

    def iaload(self, label=''):
        self.insert_instruction(Instruction("iaload"), label)

    def iand(self, label=''):
        self.insert_instruction(Instruction("iand"), label)

    def iastore(self, label=''):
        self.insert_instruction(Instruction("iastore"), label)

    def iconst_0(self, label=''):
        self.insert_instruction(Instruction("iconst_0"), label)

    def iconst_1(self, label=''):
        self.insert_instruction(Instruction("iconst_1"), label)

    def iconst_2(self, label=''):
        self.insert_instruction(Instruction("iconst_2"), label)

    def iconst_3(self, label=''):
        self.insert_instruction(Instruction("iconst_3"), label)

    def iconst_4(self, label=''):
        self.insert_instruction(Instruction("iconst_4"), label)

    def iconst_5(self, label=''):
        self.insert_instruction(Instruction("iconst_5"), label)

    def iconst_m1(self, label=''):
        self.insert_instruction(Instruction("iconst_m1"), label)

    def idiv(self, label=''):
        self.insert_instruction(Instruction("idiv"), label)

    def iload_0(self, label=''):
        self.insert_instruction(Instruction("iload_0"), label)

    def iload_1(self, label=''):
        self.insert_instruction(Instruction("iload_1"), label)

    def iload_2(self, label=''):
        self.insert_instruction(Instruction("iload_2"), label)

    def iload_3(self, label=''):
        self.insert_instruction(Instruction("iload_3"), label)

    def imul(self, label=''):
        self.insert_instruction(Instruction("imul"), label)

    def ineg(self, label=''):
        self.insert_instruction(Instruction("ineg"), label)

    def int2byte(self, label=''):
        self.insert_instruction(Instruction("int2byte"), label)

    def int2char(self, label=''):
        self.insert_instruction(Instruction("int2char"), label)

    def int2short(self, label=''):
        self.insert_instruction(Instruction("int2short"), label)

    def ior(self, label=''):
        self.insert_instruction(Instruction("ior"), label)

    def irem(self, label=''):
        self.insert_instruction(Instruction("irem"), label)

    def ireturn(self, label=''):
        self.insert_instruction(Instruction("ireturn"), label)

    def ishl(self, label=''):
        self.insert_instruction(Instruction("ishl"), label)

    def ishr(self, label=''):
        self.insert_instruction(Instruction("ishr"), label)

    def istore_0(self, label=''):
        self.insert_instruction(Instruction("istore_0"), label)

    def istore_1(self, label=''):
        self.insert_instruction(Instruction("istore_1"), label)

    def istore_2(self, label=''):
        self.insert_instruction(Instruction("istore_2"), label)

    def istore_3(self, label=''):
        self.insert_instruction(Instruction("istore_3"), label)

    def isub(self, label=''):
        self.insert_instruction(Instruction("isub"), label)

    def iushr(self, label=''):
        self.insert_instruction(Instruction("iushr"), label)

    def ixor(self, label=''):
        self.insert_instruction(Instruction("ixor"), label)

    def l2d(self, label=''):
        self.insert_instruction(Instruction("l2d"), label)

    def l2f(self, label=''):
        self.insert_instruction(Instruction("l2f"), label)

    def l2i(self, label=''):
        self.insert_instruction(Instruction("l2i"), label)

    def ladd(self, label=''):
        self.insert_instruction(Instruction("ladd"), label)

    def laload(self, label=''):
        self.insert_instruction(Instruction("laload"), label)

    def land(self, label=''):
        self.insert_instruction(Instruction("land"), label)

    def lastore(self, label=''):
        self.insert_instruction(Instruction("lastore"), label)

    def lcmp(self, label=''):
        self.insert_instruction(Instruction("lcmp"), label)

    def lconst_0(self, label=''):
        self.insert_instruction(Instruction("lconst_0"), label)

    def lconst_1(self, label=''):
        self.insert_instruction(Instruction("lconst_1"), label)

    def ldiv(self, label=''):
        self.insert_instruction(Instruction("ldiv"), label)

    def lload_0(self, label=''):
        self.insert_instruction(Instruction("lload_0"), label)

    def lload_1(self, label=''):
        self.insert_instruction(Instruction("lload_1"), label)

    def lload_2(self, label=''):
        self.insert_instruction(Instruction("lload_2"), label)

    def lload_3(self, label=''):
        self.insert_instruction(Instruction("lload_3"), label)

    def lmul(self, label=''):
        self.insert_instruction(Instruction("lmul"), label)

    def lneg(self, label=''):
        self.insert_instruction(Instruction("lneg"), label)

    def lor(self, label=''):
        self.insert_instruction(Instruction("lor"), label)

    def lrem(self, label=''):
        self.insert_instruction(Instruction("lrem"), label)

    def lreturn(self, label=''):
        self.insert_instruction(Instruction("lreturn"), label)

    def lshl(self, label=''):
        self.insert_instruction(Instruction("lshl"), label)

    def lshr(self, label=''):
        self.insert_instruction(Instruction("lshr"), label)

    def lstore_0(self, label=''):
        self.insert_instruction(Instruction("lstore_0"), label)

    def lstore_1(self, label=''):
        self.insert_instruction(Instruction("lstore_1"), label)

    def lstore_2(self, label=''):
        self.insert_instruction(Instruction("lstore_2"), label)

    def lstore_3(self, label=''):
        self.insert_instruction(Instruction("lstore_3"), label)

    def lsub(self, label=''):
        self.insert_instruction(Instruction("lsub"), label)

    def lushr(self, label=''):
        self.insert_instruction(Instruction("lushr"), label)

    def lxor(self, label=''):
        self.insert_instruction(Instruction("lxor"), label)

    def monitorenter(self, label=''):
        self.insert_instruction(Instruction("monitorenter"), label)

    def monitorexit(self, label=''):
        self.insert_instruction(Instruction("monitorexit"), label)

    def nop(self, label=''):
        self.insert_instruction(Instruction("nop"), label)

    def pop(self, label=''):
        self.insert_instruction(Instruction("pop"), label)

    def pop2(self, label=''):
        self.insert_instruction(Instruction("pop2"), label)

    def return_(self, label=''):
        self.insert_instruction(Instruction("return"), label)

    def saload(self, label=''):
        self.insert_instruction(Instruction("saload"), label)

    def sastore(self, label=''):
        self.insert_instruction(Instruction("sastore"), label)

    def swap(self, label=''):
        self.insert_instruction(Instruction("swap"), label)

    def bipush(self, value: int, label=''):
        self.insert_instruction(Instruction("bipush", value), label)

    def sipush(self, value: int, label=''):
        self.insert_instruction(Instruction("sipush", value), label)

    def iinc(self, variable_number: int, value: int, label=''):
        self.insert_instruction(Instruction("{i}", variable_number, value), label)

    def goto(self, to_br: str, label=''):
        self.insert_instruction(Instruction("goto", to_br), label)

    def goto_w(self, to_br: str, label=''):
        self.insert_instruction(Instruction("goto_w", to_br), label)

    def if_acmpeq(self, to_br: str, label=''):
        self.insert_instruction(Instruction("if_acmpeq", to_br), label)

    def if_acmpne(self, to_br: str, label=''):
        self.insert_instruction(Instruction("if_acmpne", to_br), label)

    def if_icmpeq(self, to_br: str, label=''):
        self.insert_instruction(Instruction("if_icmpeq", to_br), label)

    def if_icmpge(self, to_br: str, label=''):
        self.insert_instruction(Instruction("if_icmpge", to_br), label)

    def if_icmpgt(self, to_br: str, label=''):
        self.insert_instruction(Instruction("if_icmpgt", to_br), label)

    def if_icmple(self, to_br: str, label=''):
        self.insert_instruction(Instruction("if_icmple", to_br), label)

    def if_icmplt(self, to_br: str, label=''):
        self.insert_instruction(Instruction("if_icmplt", to_br), label)

    def if_icmpne(self, to_br: str, label=''):
        self.insert_instruction(Instruction("if_icmpne", to_br), label)

    def ifeq(self, to_br: str, label=''):
        self.insert_instruction(Instruction("ifeq", to_br), label)

    def ifge(self, to_br: str, label=''):
        self.insert_instruction(Instruction("ifge", to_br), label)

    def ifgt(self, to_br: str, label=''):
        self.insert_instruction(Instruction("ifgt", to_br), label)

    def ifle(self, to_br: str, label=''):
        self.insert_instruction(Instruction("ifle", to_br), label)

    def iflt(self, to_br: str, label=''):
        self.insert_instruction(Instruction("iflt", to_br), label)

    def ifne(self, to_br: str, label=''):
        self.insert_instruction(Instruction("ifne", to_br), label)

    def ifnonnull(self, to_br: str, label=''):
        self.insert_instruction(Instruction("ifnonnull", to_br), label)

    def ifnull(self, to_br: str, label=''):
        self.insert_instruction(Instruction("ifnull", to_br), label)

    def jsr(self, to_br: str, label=''):
        self.insert_instruction(Instruction("jsr", to_br), label)

    def jsr_w(self, to_br: str, label=''):
        self.insert_instruction(Instruction("jsr_w", to_br), label)

    def anewarray(self, cls: str, label=''):
        self.insert_instruction(Instruction("anewarray", cls), label)

    def checkcast(self, cls: str, label=''):
        self.insert_instruction(Instruction("checkcast", cls), label)

    def instanceof(self, cls: str, label=''):
        self.insert_instruction(Instruction("instanceof", cls), label)

    def new(self, cls: str, label=''):
        self.insert_instruction(Instruction("new", cls), label)

    def invokenonvirtual(self, method: str, label=''):
        self.insert_instruction(Instruction("invokenonvirtual", method), label)

    def invokestatic(self, method: str, label=''):
        self.insert_instruction(Instruction("invokestatic", method), label)

    def invokevirtual(self, method: str, label=''):
        self.insert_instruction(Instruction("invokevirtual", method), label)

    def invokeinterface(self, method: str, args: int, label=''):
        self.insert_instruction(Instruction("invokeinterface", method, args), label)

    def getfield(self, field: str, type_, label=''):
        self.insert_instruction(Instruction("getfield", field, str(type_)), label)

    def getstatic(self, field: str, type_, label=''):
        self.insert_instruction(Instruction("getstatic", field, str(type_)), label)

    def putfield(self, field: str, type_, label=''):
        self.insert_instruction(Instruction("putfield", field, str(type_)), label)

    def putstatic(self, field: str, type_, label=''):
        self.insert_instruction(Instruction("putstatic", field, str(type_)), label)

    def newarray(self, type_, label=''):
        self.insert_instruction(Instruction("newarray", str(type_)), label)

    def multianewarray(self, type_, dimensions: int, label=''):
        self.insert_instruction(Instruction("multianewarray", str(type_), dimensions), label)

    def ldc(self, constant, label=''):
        self.insert_instruction(Instruction("ldc", constant), label)

    def ldc_w(self, constant, label=''):
        self.insert_instruction(Instruction("ldc_w", constant), label)
