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

Crear el entorno virtual e instalar las dependencias.

En Linux y macOS:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En Windows (PowerShell):

```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Generar el analizador

Los archivos `ExprLexer.py`, `ExprParser.py`, `ExprListener.py` y
`ExprVisitor.py` no estan en el repositorio porque los genera ANTLR a partir
de la gramatica `Expr.g4`. Hay que generarlos despues de clonar el proyecto y
cada vez que se modifique la gramatica.

En Linux y macOS, indicando la ruta del archivo .jar:

```
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor Expr.g4
```

En Windows (PowerShell), con ANTLR configurado en la variable de entorno
CLASSPATH:

```
java -jar $env:CLASSPATH -Dlanguage=Python3 -visitor .\Expr.g4
```

La bandera `-visitor` es obligatoria: sin ella ANTLR no genera el archivo
`ExprVisitor.py`, que es la clase base que necesita el analizador semantico, y
la aplicacion no arranca. Tampoco usar la bandera `-no-listener`.

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
