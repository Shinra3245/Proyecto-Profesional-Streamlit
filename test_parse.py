import sys
from antlr4 import FileStream, CommonTokenStream
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from analizador_sintactico import AnalizadorSintactico
from archivo import Archivo

with open("TestHuawei.txt", "r") as f:
    codigo = f.read()

lex = ExprLexer(FileStream("TestHuawei.txt"))
stream = CommonTokenStream(lex)
stream.fill()
an = AnalizadorSintactico()
an.analizar(stream)
print(an.obtener_errores())
