from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
import sys

input = FileStream(sys.argv[1])

lexer = ExprLexer(input)
tokens = CommonTokenStream(lexer)
parser = ExprParser(tokens)
arbol = parser.archivo_configuracion()

if parser.getNumberOfSyntaxErrors() == 0:
    print("El codigo es correcto")
    print("Arbol sintactico:")
    print(arbol.toStringTree(recog=parser))
else:
    print("El codigo tiene errores de sintaxis")
