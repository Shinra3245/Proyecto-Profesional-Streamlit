from antlr4 import FileStream, CommonTokenStream
from ExprLexer import ExprLexer
from analizador_sintactico import AnalizadorSintactico
from traductor import Traductor

lex = ExprLexer(FileStream("TestHuawei.txt"))
stream = CommonTokenStream(lex)
stream.fill()

an = AnalizadorSintactico()
an.analizar(stream)

if len(an.obtener_errores()) == 0:
    t = Traductor(stream, modo_traduccion="HUAWEI_A_CISCO")
    res = t.traducir(an.arbol)
    print("TRADUCCION EXITOSA:")
    print(res)
else:
    print("ERRORES SINTACTICOS:", an.obtener_errores())
