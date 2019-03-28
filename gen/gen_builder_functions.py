var_number_fns = """    ret <var-num>
    aload <var-num>
    astore <var-num>
    dload <var-num>
    dstore <var-num>
    fload <var-num>
    fstore <var-num>
    iload <var-num>
    istore <var-num>
    lload <var-num>
    lstore <var-num>
""".split('<var-num>')

var_number_fns = [i.strip() for i in var_number_fns if i.strip()]

for i in var_number_fns:
    print(f"""
    def {i}(self, variable_number: int, label=''):
        self.insert_instruction(Instruction("{i}", variable_number), label)
    """[1:])

nilads = "aaload aastore aconst_null aload_0 aload_1 aload_2 aload_3 areturn arraylength astore_0 astore_1 astore_2 astore_3 athrow baload bastore breakpoint caload castore d2f d2i d2l dadd daload dastore dcmpg dcmpl dconst_0 dconst_1 ddiv dload_0 dload_1 dload_2 dload_3 dmul dneg drem dreturn dstore_0 dstore_1 dstore_2 dstore_3 dsub dup dup2 dup2_x1 dup2_x2 dup_x1 dup_x2 f2d f2i f2l fadd faload fastore fcmpg fcmpl fconst_0 fconst_1 fconst_2 fdiv fload_0 fload_1 fload_2 fload_3 fmul fneg frem freturn fstore_0 fstore_1 fstore_2 fstore_3 fsub i2d i2f i2l iadd iaload iand iastore iconst_0 iconst_1 iconst_2 iconst_3 iconst_4 iconst_5 iconst_m1 idiv iload_0 iload_1 iload_2 iload_3 imul ineg int2byte int2char int2short ior irem ireturn ishl ishr istore_0 istore_1 istore_2 istore_3 isub iushr ixor l2d l2f l2i ladd laload land lastore lcmp lconst_0 lconst_1 ldiv lload_0 lload_1 lload_2 lload_3 lmul lneg lor lrem lreturn lshl lshr lstore_0 lstore_1 lstore_2 lstore_3 lsub lushr lxor monitorenter monitorexit nop pop pop2 return saload sastore swap".split()
for i in nilads:
    print(f"""
    def {i}(self, label=''):
        self.insert_instruction(Instruction("{i}"), label)
    """[1:])

print("""
    def bipush(self, value: int, label=''):
        self.insert_instruction(Instruction("bipush", value), label)

    def sipush(self, value: int, label=''):
        self.insert_instruction(Instruction("sipush", value), label)
    
    def iinc(self, variable_number: int, value: int, label=''):
        self.insert_instruction(Instruction("{i}", variable_number, value), label)
""")

branches = """    goto  <label>
    goto_w  <label>
    if_acmpeq  <label>
    if_acmpne  <label>
    if_icmpeq  <label>
    if_icmpge  <label>
    if_icmpgt  <label>
    if_icmple  <label>
    if_icmplt  <label>
    if_icmpne  <label>
    ifeq  <label>
    ifge  <label>
    ifgt  <label>
    ifle  <label>
    iflt  <label>
    ifne  <label>
    ifnonnull  <label>
    ifnull  <label>
    jsr  <label>
    jsr_w  <label>""".split("<label>")

branches = [b.strip() for b in branches if b.strip()]

for i in branches:
    print(f"""
    def {i}(self, to_br: str, label=''):
        self.insert_instruction(Instruction("{i}", to_br), label)
    """[1:])

class_instr = """    anewarray  <class>
    checkcast  <class>
    instanceof <class>
    new        <class>""".split("<class>")

class_instr = [c.strip() for c in class_instr if c.strip()]

for i in class_instr:
    print(f"""
    def {i}(self, cls: str, label=''):
        self.insert_instruction(Instruction("{i}", cls), label)
    """[1:])

method_inv = """    invokenonvirtual  <method-spec>
    invokestatic      <method-spec>
    invokevirtual     <method-spec>""".split("<method-spec>")

method_inv = [c.strip() for c in method_inv if c.strip()]

for i in method_inv:
    print(f"""
    def {i}(self, method: str, label=''):
        self.insert_instruction(Instruction("{i}", method), label)
    """[1:])

print("""
    def invokeinterface(self, method: str, args: int, label=''):
        self.insert_instruction(Instruction("invokeinterface", method, args), label)
""")

field_manip = "getfield getstatic putfield putstatic".split()

for i in field_manip:
    print(f"""
    def {i}(self, field: str, type_: str, label=''):
        self.insert_instruction(Instruction("{i}", field, type_), label)
    """[1:])

print("""
    def newarray(self, type_: str, label=''):
        self.insert_instruction(Instruction("newarray", type_), label)

    def multianewarray(self, type_: str, dimensions: int, label=''):
        self.insert_instruction(Instruction("multianewarray", type_, dimensions), label)
""")

loads = """     ldc  <constant>
     ldc_w  <constant>
""".split("<constant>")

loads = [c.strip() for c in loads if c.strip()]

for i in loads:
    print(f"""
    def {i}(self, constant, label=''):
        self.insert_instruction(Instruction("{i}", constant), label)
    """[1:])
