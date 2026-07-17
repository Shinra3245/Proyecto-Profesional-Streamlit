# Importamos TerminalNode para diferenciar hojas (tokens) de reglas
from antlr4.tree.Tree import TerminalNode


# Clase auxiliar del analizador sintactico. Se encarga de convertir el arbol
# que genera ANTLR en texto con conectores para poder mostrarlo en pantalla.
# Se separa del analizador porque el analizador solo debe encargarse de
# analizar, no de darle formato al resultado.
class HelperSintactico:

    # Metodo para obtener el arbol sintactico como texto con conectores
    def obtener_arbol_texto(self, arbol, parser):

        # La raiz se escribe sola, sin prefijo ni conector
        texto = self._etiqueta_nodo(arbol, parser) + "\n"

        # Armamos la lista de hijos de la raiz
        hijos = [arbol.getChild(i) for i in range(arbol.getChildCount())]

        # Recorremos los hijos de la raiz, cada uno empieza sin prefijo
        for i, hijo in enumerate(hijos):

            # Agregamos el texto del hijo, indicando si es el ultimo
            texto += self._nodo_a_texto(hijo, parser, "", i == len(hijos) - 1)

        # Retornamos el texto acumulado
        return texto

    # Metodo recursivo que arma el texto de un nodo y sus hijos usando
    # conectores estilo comando "tree" (├──, └──, │)
    def _nodo_a_texto(self, nodo, parser, prefijo, es_ultimo):

        # Elegimos el conector segun si el nodo es el ultimo de su nivel
        conector = "└── " if es_ultimo else "├── "

        # Escribimos la linea del nodo actual con su conector
        texto = prefijo + conector + self._etiqueta_nodo(nodo, parser) + "\n"

        # El prefijo de los hijos depende de si el nodo actual fue el ultimo
        prefijo_hijos = prefijo + ("    " if es_ultimo else "│   ")

        # Armamos la lista de hijos del nodo actual
        hijos = [nodo.getChild(i) for i in range(nodo.getChildCount())]

        # Recorremos cada hijo del nodo actual
        for i, hijo in enumerate(hijos):

            # Agregamos el texto del hijo, indicando si es el ultimo
            texto += self._nodo_a_texto(hijo, parser, prefijo_hijos, i == len(hijos) - 1)

        # Retornamos el texto acumulado
        return texto

    # Metodo para obtener la etiqueta de un nodo (token o regla)
    def _etiqueta_nodo(self, nodo, parser):

        # Si el nodo es una hoja, mostramos el texto literal del token
        if isinstance(nodo, TerminalNode):
            return nodo.getText()

        # Si el nodo es una regla, mostramos su nombre
        return parser.ruleNames[nodo.getRuleIndex()]
