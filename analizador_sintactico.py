# Importamos ErrorListener para capturar errores sintacticos
from antlr4.error.ErrorListener import ErrorListener

# Importamos el parser generado por ANTLR
from ExprParser import ExprParser


# Clase para guardar errores sintacticos
class ErroresSintacticos(ErrorListener):

    # Constructor
    def __init__(self):

        # Lista donde guardaremos los errores
        self.lista = []

    # Metodo que ANTLR ejecuta cuando encuentra error sintactico
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        # Guardamos el error en la lista
        self.lista.append({
            "linea": line,
            "columna": column,
            "mensaje": msg
        })


# Clase para hacer el analisis sintactico
class AnalizadorSintactico:

    # Constructor, recibe el helper que le dara formato al arbol
    def __init__(self, helper):

        # Guardamos el helper que nos inyectan desde app.py
        self.helper = helper

        # Variable para guardar el parser
        self.parser = None

        # Variable para guardar el arbol sintactico
        self.arbol = None

        # Objeto para guardar errores sintacticos
        self.errores = ErroresSintacticos()

    # Metodo para analizar los tokens generados por el analizador lexico
    def analizar(self, tokens):

        # Regresamos el flujo de tokens al inicio, ya que el analizador
        # lexico lo dejo posicionado al final despues de leerlo con fill()
        tokens.seek(0)

        # Creamos el parser
        self.parser = ExprParser(tokens)

        # Quitamos los errores normales de ANTLR
        self.parser.removeErrorListeners()

        # Agregamos nuestro capturador de errores
        self.parser.addErrorListener(self.errores)

        # Ejecutamos la regla inicial de la gramatica y guardamos el arbol
        self.arbol = self.parser.archivo_configuracion()

    # Metodo para obtener errores sintacticos
    def obtener_errores(self):

        # Retornamos la lista de errores
        return self.errores.lista

    # Metodo para obtener el arbol como texto, le pedimos el formato al helper
    def obtener_arbol_texto(self):

        # Le pasamos el arbol y el parser al helper para que arme el texto
        return self.helper.obtener_arbol_texto(self.arbol, self.parser)
