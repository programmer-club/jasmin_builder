import unittest
import subprocess
import shlex

from jasmin_builder.builder import Builder
from jasmin_builder.method import *
from jasmin_builder.types import VOID, Link, Array


def run_jasmin_command(cmd: str = '', pipe: bool = False):
    if pipe:
        return subprocess.Popen(["java", "-jar", "../jasmin-2.4/jasmin.jar"] + shlex.split(cmd),
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        return subprocess.Popen(["java", "-jar", "../jasmin-2.4/jasmin.jar"] + shlex.split(cmd))


class JasminBuilderTests(unittest.TestCase):
    def testJasminRuns(self):
        proc = run_jasmin_command('', True)

        while not (proc.poll(), proc.returncode is not None)[1]:
            pass

        # print('\n'.join(map(lambda x: x.decode('utf-8'), proc.communicate())))

        proc.stdout.close()
        proc.stderr.close()

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
\tgetstatic 'java/lang/System/out' 'Ljava/io/PrintStream;'
\tldc 'Hello, world!'
\tinvokevirtual 'java/io/PrintStream/println(Ljava/lang/String;)V'
\treturn 
.end method""")


if __name__ == '__main__':
    unittest.main()
