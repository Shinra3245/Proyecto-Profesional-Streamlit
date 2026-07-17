# Proyecto-Profesional-Streamlit

Analizador lexico y sintactico para archivos de configuracion de red de
Cisco IOS y Huawei VRP, hecho con ANTLR y Streamlit.

La aplicacion recibe un archivo `.txt` o `.cfg` con comandos de
configuracion, lo analiza y muestra los tokens encontrados, el arbol
sintactico y los errores lexicos y sintacticos.

## Requisitos

- Python 3
- Java (lo necesita ANTLR para generar el analizador)
- ANTLR 4.13.2 (archivo `antlr-4.13.2-complete.jar`)

## Instalacion

Crear el entorno virtual e instalar las dependencias:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En Windows el entorno virtual se activa con:

```
.venv\Scripts\activate
```

## Generar el analizador

Los archivos `ExprLexer.py` y `ExprParser.py` no estan en el repositorio
porque los genera ANTLR a partir de la gramatica `Expr.g4`. Hay que
generarlos despues de clonar el proyecto y cada vez que se modifique la
gramatica:

```
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 Expr.g4
```

## Ejecutar

```
streamlit run app.py
```

## Archivos de prueba

- `TestCisco.txt`: configuracion de ejemplo de Cisco IOS
- `TestHuawei.txt`: configuracion de ejemplo de Huawei VRP

## Integrantes

- Bolaños Garcia Omar Gadiel
- Monjaras Ortega Andres
- Elguera Tovar Jesus Alejandro
