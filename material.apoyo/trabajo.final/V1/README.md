<img src="https://i.postimg.cc/cCjTSn8r/ss-cumf.png" alt="reporte" border="0"/>


`# TECDEV: SEC#3, ID#26, README`
# **DESARROLLO TRABAJO FINAL**

El objetivo de este `README` es proporcionar una guía simple sobre el funcionamiento del proyecto que he creado, para que puedan compararlo con sus propios trabajos. Para obtener mas información, mira el siguiente video:
<iframe src="https://drive.google.com/file/d/173U9jP_igF7hPpImIcuiRFovzUrNZ9BW/preview" width="640" height="480" allow="autoplay"></iframe>


## **OBJETIVO & METODOLOGÍA**

### **1. OBJETIVO**

El objetivo del ejercicio era permitirles poner en práctica lo aprendido en el curso a través de un ejercicio que los desafiara a leer y comprender la información de manera repetida. En ocasiones, al abordar la solución de un problema, especialmente al principio, puede resultar abrumador. Sin embargo, lo crucial es mantenerse enfocado y centrado en lo esencial. La segunda expectativa era que pudieran estructurar un proyecto, ya que, desde mi perspectiva, esta es una de las partes más fundamentales.

### **2. METODOLOGÍA**
Cuando abordo la resolución de un problema, mi primer paso suele ser leer, extraer y clasificar información. Esto se lleva a cabo con el objetivo de identificar los datos más relevantes y estructurarlos. En el archivo `documentacion/apuntes/002.problema.pdf `podrán ver como lo clasifique para solucionarlo:



<table>
  <tr style="background-color: yellow;">
    <td>RELLENO (CARRETA)</td>
  </tr>
  <tr style="background-color: blue; color: white;">
    <td>REQUISITOS FUNCIONALES</td>
  </tr>
  <tr style="background-color: green; color: white;">
    <td>INFORMACIÓN IMPORTANTE</td>
  </tr>
  <tr style="background-color: purple; color: white;">
    <td>PARAMETRIZACIÓN</td>
  </tr>
</table>

## **ESTRUCTURA DEL PROYECTO**

`# TECDEV: SEC#3, ID#19, MANEJO DE AMBIENTES VIRTUALES`
### **AMBIENTE VIRTUAL**

En mi caso, seleccioné conda, ya que necesito gestionar varios entornos. Si ya tienen conda instalado, pueden seguir los comandos:

```bash 
# crea ambiente virtual
conda create --name trabajo python=3.10 

# activar el ambiente
conda activate trabajo
```

En caso de tener `conda` o `virtualenv`, pueden activarlo o crearlo en el proyecto e instalar las dependencias utilizando:

```bash
poetry install
```
### **FUNCIONAMIENTO APP**

La aplicación cuenta con parámetros de aplicación utilizando `parseargs`. Estos parámetros modifican el comportamiento de la aplicación. Para ver las opciones, puedes ejecutar:


```bash
# opción #1
python apolo-11.py

# opción #2
python apolo-11.py -h

# opción #3
python apolo-11.py --help

# salida

usage: 
python apolo-11.py [opciones] [opciones]

Herramienta para realizarla generación de mock data y cálculo de
reportes; ejemplo de solución para el trababo final de python lvl4:
--------------------------------------------------------------

    - generador
    - reporteador

options:
  -h, --help            show this help message and exit

[app-opciones]:
  {generador,reporteador}
                        sub-command help
    generador           herramienta para generar archivos aleatorios
    reporteador         herramienta para generar reportes, a partir de losarchivos aleatorios

© todos los derechos reservados 2024.
```

Para llevar a cabo la generación de los archivos, pueden ejecutar el siguiente comando:
```
python apolo-11.py  generador --periodicidad 20
```

Para realizar la generación de reportes, la aplicación soporta dos tipos: usando la librería pandas o utilizando lógica pura de osango. Para utilizar la generación usando pandas, ejecute el siguiente comando:
```
python apolo-11.py  reporteador --metodo pandas
```

Para utilizar la generación usando Python:
```
python apolo-11.py  reporteador --metodo python
```

### **DOCUMENTACIÓN**

Todo el proyecto se encuentra completamente documentado con el objetivo de clarificar puntos, o que puedan aprender nuevas cosas. Principalmente, hay dos etiquetas que serán de mucha ayuda:

* **TECDEV**: encontrarán a qué punto hace referencia en los criterios de evaluación.
* **DOCDEV**: indicará a qué punto hace referencia en el documento.


Podrán encontrar más información detallada revisando el archivo `documentacion/criterios.desarrollados/001.index.documentacion.xlsx`.

### **VALIDACIÓN PROYECTO**

El proyecto incorpora dos prácticas fundamentales para asegurar su calidad: pruebas unitarias y validación del estilo de código (`linting`). Para activar estas validaciones, pueden ejecutar los siguientes comandos:


Usuarios Linux:
```bash
# activar flake8
make lint

# activar pruebas unitarias
make test

# limpiar archivos temporales y datos generados
make clean
```

Usuarios Windows:
```bash
# activar flake8
flake8 nasa
flake8 tests

# activar pruebas unitarias
python -m pytest -v

```

Nota: las pruebas unitarias cuentan con un 90% de coverage
```
PASSED                                                     [ 10%]
tests/comunes/decoradores.py::test_tiempo_ejecucion_sin_reporte PASSED                                                 [ 15%]
tests/comunes/excepciones.py::test_excepcion_personalizada PASSED                                                      [ 20%]
tests/comunes/inicializador.py::test_obtener_instancias_configuracion PASSED                                           [ 25%]
tests/comunes/parametros.py::test_argumentos_generador PASSED                                                          [ 30%]
tests/comunes/parametros.py::test_argumentos_reporte_pandas PASSED                                                     [ 35%]
tests/comunes/parametros.py::test_argumentos_reporte_python PASSED                                                     [ 40%]
tests/comunes/parametros.py::test_sin_argumentos PASSED                                                                [ 45%]
tests/comunes/utilitarios_funcionalidades.py::test_configurar_logger PASSED                                            [ 50%]
tests/comunes/utilitarios_funcionalidades.py::test_escribir_yaml PASSED                                                [ 55%]
tests/comunes/utilitarios_funcionalidades.py::test_leer_yaml PASSED                                                    [ 60%]
tests/comunes/utilitarios_funcionalidades.py::test_obtener_encabezado PASSED                                           [ 65%]
tests/comunes/utilitarios_funcionalidades.py::test_numeros_positivos PASSED                                            [ 70%]
tests/comunes/utilitarios_struct.py::test_struct PASSED                                                                [ 75%]
tests/modelamiento/enumeradores.py::test_enum_valores PASSED                                                           [ 80%]
tests/modelamiento/enumeradores.py::test_enum_nombres PASSED                                                           [ 85%]
tests/modelamiento/modelo.py::test_pydantic PASSED                                                                     [ 90%]
tests/negocio/generador_reporte.py::test_generar_archivos_pandas PASSED                                                [ 95%]
tests/negocio/generador_reporte.py::test_generar_archivos_python PASSED                                                [100%]

--------- coverage: platform darwin, python 3.10.13-final-0 ----------
Name                                              Stmts   Miss  Cover   Missing
-------------------------------------------------------------------------------
nasa/__init__.py                                      0      0   100%
nasa/comunes/constantes.py                           34      0   100%
nasa/comunes/decoradores.py                          41      1    98%   88
nasa/comunes/excepcion.py                            15      0   100%
nasa/comunes/inicializador.py                        42      0   100%
nasa/comunes/parametros.py                           16      2    88%   79-80
nasa/comunes/utilitarios.py                          60      2    97%   78, 131
nasa/modelamiento/abstraccion/operaciones_os.py      20      6    70%   24, 33, 44, 55, 73, 85
nasa/modelamiento/abstraccion/reportes.py            34     10    71%   26, 40, 52, 67, 82, 97, 114, 129, 144, 150
nasa/modelamiento/enumeradores/reportes.py            7      0   100%
nasa/modelamiento/herencia/acciones_os.py            34     16    53%   70-86, 98-110
nasa/modelamiento/modelo/archivos.py                  7      0   100%
nasa/modelamiento/propiedades/instancias.py          61      0   100%
nasa/negocio/generardor.py                           36     22    39%   41-112, 120
nasa/negocio/reportes.py                            227      0   100%
-------------------------------------------------------------------------------
TOTAL                                               634     59    91%
Coverage HTML written to dir htmlcov

Required test coverage of 60% reached. Total coverage: 90.69%

==================================================== 20 passed in 30.97s =====================================================
```

### **ESTRUCTURA DE CARPETAS**

El proyecto cuenta con la siguiente estructura:


```bash 
# TECDEV: SEC#3, ID#25, DISTRIBUCIÓN ADECUADA O CON ORDEN
.
├── documentacion        # doc estudiantes
│   ├── apuntes          # pdf con apuntes
│   └── diagramas        # diagramas elementales
├── nasa                 # carpeta principal código
│   ├── comunes          # librerías comunes
│   ├── config           # carpeta de conf
│   │   ├── archivos     # archivos de conf
│   │   ├── deltas       # manejo de deltas
│   │   └── logotipos    # logotipos de app
│   ├── modelamiento     # guía temas
│   │   ├── abstraccion  # ejem. Abstracción
│   │   ├── enumeradores # ejem. Enumeradores
│   │   ├── herencia     # ejem. Herencia
│   │   ├── modelo       # ejem. Pydantic
│   │   └── propiedades  # ejem. Properties
│   └── negocio          # Lógica de negocio (reportes y archivos)
├── recursos             # carpeta datos generados
│   ├── archivos         
│   │   ├── backup       # carpeta respaldo
│   │   ├── devises      # carpeta dispositivos
│   │   └── reports      # carpeta reportes
│   ├── auditoria        # carpeta auditoria (decorador)
│   └── logs             # logs de aplicación
└── tests                # carpeta de pruebas
    ├── comunes          # test para comunes
    ├── modelamiento     # test para modelamiento
    ├── nasa             # configuración temporal
    │   └── config
    │       ├── archivos
    │       ├── deltas
    │       └── logotipos
    └── negocio          # test lógica de negocio
```