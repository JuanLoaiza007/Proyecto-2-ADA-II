# Proyecto-2-ADA-II

## Descripción

Este repositorio contiene la implementación del proyecto del curso Análisis de Algoritmos II de la Escuela de Ingeniería de Sistemas y Computación, el proyecto se centra en el Problema de la Ubicación de Instalaciones de Capacidad Acotada (PUICA) que implica la optimización de la ubicación de instalaciones para satisfacer la demanda de los clientes, respetando las restricciones de capacidad y maximizando la utilidad total.

## Tecnologías

Este proyecto es una implementación en python de la solución del problema PUICA utilizando la herramienta MiniZinc, para la implementación se utilizaron las siguientes tecnologías:

- PyQt5: para el desarrollo de la interfaz.

NOTA: Este proyecto incluye archivos .dzn y .mzn pero no integra Minizinc o alguna instalación de esta herramienta.

## Estructura del Repositorio

Este proyecto está organizado en forma de modelo, vista, controlador y cuenta con otras carpetas y archivos adicionales:

- `data/` - Directorio de datos.
  - `test/` - Directorio de datos de prueba para el problema, incluyendo la pila de pruebas.
- `models/` - Directorio de modelos donde se encuentran los archivos .dzn y .mzn que se utilizan para el desarrollo del problema.
  - `PUICAProblem/` - Directorio de modelos del problema PUICA junto al Parser `PUICAProblemParser.py` para la generación de archivos .dzn a partir de las entradas específicadas en el enunciado del proyecto.
  - `tools/` - Directorio de herramientas reusables.
- `views/` - Directorio de vistas donde se encuentran los archivos .ui y .py que se utilizan para la interfaz de usuario.
  - `_bootstylesheet.css` es el archivo de estilos que usa cada vista.
  - `_uitop.py` es el programa usado para convertir de .ui a .py.

## Requisitos

Para que la aplicación funcione correctamente, se requieren lo siguiente:

- Tener instalado Python 3.8 o superior.
- Tener instalado MiniZinc 2.8.0 o superior y accesible desde la terminal (compruebe ejecutando `minizinc --version` en la terminal).

## Instrucciones de Uso

Para ejecutar el proyecto, sigue estos pasos:

1. Clonar el repositorio:

```bash
git clone https://github.com/JuanLoaiza007/Proyecto-2-ADA-II.git
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar el main.py desde la carpeta raíz:

En Windows:

```bash
python main.py
```

En Linux/macOS:

```bash
python3 main.py
```

## Autores

- John Freddy Belalcazar Rojas - 2182464 - john.freddy.belalcazar@correounivalle.edu.co
- Juan David Loaiza Santiago - 2177570 - juan.loaiza.santiago@correounivalle.edu.co
- Juan Sebastian Muñoz Rojas - 2177436 - juan.munoz.rojas@correounivalle.edu.co
- Julian David Rendon Cardona - 2177387 - julian.david.rendon@correounivalle.edu.co

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](https://opensource.org/licenses/MIT).
