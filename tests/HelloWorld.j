.class public HelloWorld
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
	.limit stack 4
	getstatic 'java/lang/System/out' 'Ljava/io/PrintStream;'
	ldc 'Hello, world!'
	invokevirtual 'java/io/PrintStream/println(Ljava/lang/String;)V'
	return 
.end method