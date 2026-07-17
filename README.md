# Proyecto-Profesional-Streamlit

Analizador lexico y sintactico para archivos de configuracion de red de
Cisco IOS y Huawei VRP, hecho con ANTLR y Streamlit.

La aplicacion recibe un archivo `.txt` o `.cfg` con comandos de configuracion, lo analiza y muestra los tokens encontrados, el arbol sintactico y los errores. tiene 3 niveles de revision

1. **Nivel lexico**: checa que las palabras existan y que no haya caracteres raros como @
2. **Nivel sintactico**: checa que las palabras esten en orden y formen comandos validos usando el arbol de ANTLR
3. **Nivel semantico**: revisa errores de logica por ejemplo poner la misma ip a dos interfaces diferentes o usar una vlan que no se declaro antes. ademas tiene validacion de archivo para no aceptar texto basura

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

Los archivos `ExprLexer.py`, `ExprParser.py` y `ExprListener.py` no estan en
el repositorio porque los genera ANTLR a partir de la gramatica `Expr.g4`.
Hay que generarlos despues de clonar el proyecto y cada vez que se modifique
la gramatica.

En Linux y macOS, indicando la ruta del archivo .jar:

```
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 Expr.g4
```

En Windows (PowerShell), con ANTLR configurado en la variable de entorno
CLASSPATH:

```
java -jar $env:CLASSPATH -Dlanguage=Python3 .\Expr.g4
```

No usar la bandera `-no-listener`. Esa bandera evita que ANTLR genere el
archivo `ExprListener.py`, que es la clase base que necesita el analizador
semantico.

## Ejecutar

```
streamlit run app.py
```

## Archivos de prueba

- `TestCisco.txt`: Configuracion de ejemplo de Cisco IOS.
- `TestHuawei.txt`: Configuracion de ejemplo de Huawei VRP.
- `TestCisco_Nivel3.cfg` y `TestHuawei_Nivel3.cfg`: archivos especiales para probar el nivel 3, no tienen errores de sintaxis pero tienen errores semanticos

## Integrantes

- Bolaños Garcia Omar Gadiel
- Monjaras Ortega Andres
- Elguera Tovar Jesus Alejandro
