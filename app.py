import streamlit as st
from archivo import Archivo
from analizador_lexico import AnalizadorLexico
from analizador_sintactico import AnalizadorSintactico
from helper_sintactico import HelperSintactico


class App:

    def __init__(self):
        st.set_page_config(page_title="Analizador Lexico y Sintactico", layout="wide")
        self.analizador = AnalizadorLexico()

        # Creamos el helper y lo inyectamos al analizador sintactico, para que
        # el analizador solo analice y el helper se encargue del formato
        self.helper_sintactico = HelperSintactico()
        self.analizador_sintactico = AnalizadorSintactico(self.helper_sintactico)

    def ejecutar(self):
        st.title("Analizador Lexico y Sintactico con ANTLR y Streamlit")
        st.write("Sube un archivo `.txt` o `.cfg` para ver tokens y errores.")

        archivo_subido = st.file_uploader("Selecciona tu archivo", type=["txt", "cfg"])

        if archivo_subido is None:
            st.info("Primero sube un archivo .txt o .cfg")
            return

        archivo = Archivo(archivo_subido)

        if not archivo.es_extension_valida():
            st.error("El archivo debe ser .txt o .cfg")
            return

        codigo = archivo.leer()
        info = archivo.obtener_info()

        st.subheader("Informacion del archivo")
        st.write("Nombre:", info["nombre"])
        st.write("Extension:", info["extension"])

        st.subheader("Codigo original")
        st.code(codigo, language="text")

        self.analizador.analizar(codigo)

        tokens = self.analizador.obtener_tokens()
        errores = self.analizador.obtener_errores()

        st.subheader("Tokens")

        if len(tokens) == 0:
            st.warning("No se encontraron tokens")
        else:
            st.dataframe(tokens, use_container_width=True)

        self.analizador_sintactico.analizar(self.analizador.tokens)

        st.subheader("Arbol sintactico")

        with st.expander("Ver arbol sintactico"):
            st.code(self.analizador_sintactico.obtener_arbol_texto(), language="text")

        st.subheader("Errores lexicos")

        if len(errores) == 0:
            st.success("No hay errores lexicos")
        else:
            st.dataframe(errores, use_container_width=True)

        errores_sintacticos = self.analizador_sintactico.obtener_errores()

        st.subheader("Errores sintacticos")

        if len(errores_sintacticos) == 0:
            st.success("No hay errores sintacticos")
        else:
            st.dataframe(errores_sintacticos, use_container_width=True)


if __name__ == "__main__":
    app = App()
    app.ejecutar()
