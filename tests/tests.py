import unittest
import subprocess
import shlex
import sys

from jasmin_builder.builder import Builder
from jasmin_builder.field import Field
from jasmin_builder.klass import Class
from jasmin_builder.method import *
from jasmin_builder.modifiers import *
from jasmin_builder.types import VOID, Link, Array


def run_jasmin_command(cmd: str = '', pipe: bool = False):
    if pipe:
        return subprocess.Popen(["java", "-jar", "../jasmin-2.4/jasmin.jar"] + shlex.split(cmd),
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        return subprocess.Popen(["java", "-jar", "../jasmin-2.4/jasmin.jar"] + shlex.split(cmd))


class JasminBuilderTests(unittest.TestCase):
    def compile(self, klass: Class = None, quiet=True):
        proc = run_jasmin_command('' if klass is None else klass.name + '.j', True)

        while not (proc.poll(), proc.returncode is not None)[1]:
            pass

        if not quiet:
            sys.stderr.write(proc.stderr.read().decode('utf-8'))
            sys.stdout.write(proc.stdout.read().decode('utf-8'))

        proc.stdout.close()
        proc.stderr.close()

        return proc.returncode

    def testJasminRuns(self):
        self.assertEqual(self.compile(), 255, "Exit code of testing Jasmin")

    def testEmptyMethod(self):
        m = Method("main", [], [MOD_PUBLIC, MOD_STATIC])
        self.assertEqual(str(m), ".method public static main()V\n.end method")

    def testInvalidModifier(self):
        with self.assertRaises(AssertionError):
            m = Method("main", [], ["not-a-modifier"])

    def testBasicInstr(self):
        m = Method("main", [Array(Link("java.lang.String"))], [MOD_PUBLIC, MOD_STATIC], VOID, 4)
        b = Builder(m)
        b.getstatic("java/lang/System/out", Link("java.io.PrintStream"))
        b.ldc("Hello, world!")
        b.invokevirtual("java/io/PrintStream/println(Ljava/lang/String;)V")
        b.return_()

        self.assertEqual(str(m), """.method public static main([Ljava/lang/String;)V
\t.limit stack 4
\tgetstatic "java/lang/System/out" "Ljava/io/PrintStream;"
\tldc "Hello, world!"
\tinvokevirtual "java/io/PrintStream/println(Ljava/lang/String;)V"
\treturn 
.end method""")

    def testClass(self):
        c = Class("HelloWorld", ACC_PUBLIC)
        # c.add_field(Field("str", Link("java.lang.String")))
        m = Method("main", [Array(Link("java.lang.String"))], [MOD_PUBLIC, MOD_STATIC], VOID, 4)
        b = Builder(m)
        b.getstatic("java/lang/System/out", Link("java.io.PrintStream"))
        # b.aload_0()
        b.ldc("Hello, world!")
        # b.putfield("HelloWorld/str", Link("java.lang.String"))
        # b.aload_0()
        # b.getfield("HelloWorld/str", Link("java.lang.String"))
        b.invokevirtual("java/io/PrintStream/println(Ljava/lang/String;)V")
        b.return_()

        c.add_method(m)

        c.to_file()

        self.assertEqual(self.compile(c, False), 0)


if __name__ == '__main__':
    unittest.main()
