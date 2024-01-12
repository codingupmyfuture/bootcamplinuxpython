<img src="https://i.postimg.cc/cCjTSn8r/ss-cumf.png" alt="reporte" border="0"/>


# **ESTANDAR DE CALIDAD EN UN PROYECTO**

La calidad de un proyecto de software se refiere a la medida en que el software satisface los requisitos y expectativas establecidos. La calidad no es un atributo único, sino un conjunto de características que se pueden evaluar en diferentes dimensiones. 
## **REQUISITOS FUNCIONALES**

Describen las acciones específicas que el sistema debe realizar y cómo debe comportarse en determinadas situaciones. Estos requisitos definen lo que el sistema debe hacer.

## **REQUISITOS NO FUNCIONALES**

Los requisitos no funcionales se refieren a las cualidades o características del sistema que no están relacionadas directamente con funciones específicas. Estos requisitos abordan aspectos como el rendimiento, la seguridad, la usabilidad y otros atributos del sistema. Eje:

**Rendimiento**: El sistema debe ser capaz de manejar 1000 transacciones por segundo.
**Seguridad**: El acceso al sistema debe requerir autenticación de dos factores.
**Usabilidad**: El tiempo de aprendizaje para utilizar la interfaz del usuario no debe superar los 30 minutos para un usuario novato.
**Disponibilidad**: El sistema debe estar disponible el 99.9% del tiempo de operación.

## **PRUEBAS Y ASEGURAMIENTO DE LA CALIDAD**

Este término abarca diversas prácticas y actividades que tienen como objetivo garantizar que el software cumpla con los estándares de calidad establecidos.



1. **Pruebas Unitarias:** Verificar individualmente que unidades específicas de código funcionen correctamente.
  
2. **Pruebas de Integración:** Asegurarse de que los diferentes módulos o componentes del sistema funcionen adecuadamente cuando se integran.

3. **Pruebas de Sistema:** Evaluar el sistema como un todo para garantizar que todas las partes funcionen correctamente juntas.

4. **Validación de Buenas Prácticas:** Asegurarse de que el desarrollo siga estándares y prácticas recomendadas.

5. **Revisión de Código:** Examinar el código fuente para identificar posibles problemas y garantizar la consistencia y calidad del código.

6. **Pruebas de Rendimiento:** Evaluar el rendimiento del sistema bajo diferentes condiciones para garantizar que cumpla con los requisitos de rendimiento.






### **ACTIVIDADES ELEMENTALES**

En un proyecto hecho en Python, dos de las herramientas esenciales para este propósito son Flake8 y Pytest.

#### **FLAKE8**

Flake8 es una herramienta de linting para Python que combina varias verificaciones estáticas para identificar posibles errores y violaciones de estilo en el código fuente. Al integrar Flake8 en el proceso de desarrollo, se asegura que el código siga las mejores prácticas y estándares de codificación establecidos, lo que contribuye a un código más limpio, legible y garantiza la adherencia a convenciones de estilo como [PEP8](https://peps.python.org/pep-0008/).

```python
# antes
diccionario = {"a":1,"b":2}

diccionario["nueva_clave"]="nuevo_valor"
resultado=5+3
```


```python
# después
diccionario = {
    "a": 1,
    "b": 2,
}

diccionario["nueva_clave"] = "nuevo_valor"
resultado = 5 + 3
```


#### **PYTEST**

Pytest es un framework de pruebas unitarias que simplifica la creación y ejecución de pruebas en proyectos Python. Permite diseñar pruebas de manera clara y concisa, facilitando la identificación de posibles fallos y garantizando que cada componente del software funcione como se espera. Además de las pruebas unitarias, Pytest también admite la realización de pruebas de integración y funcionales.

#### **PYTEST COVERAGE**

`pytest-cov` es un complemento de Pytest que se utiliza para medir la cobertura de código durante la ejecución de las pruebas. La cobertura de código es una métrica que indica qué porcentaje del código fuente está siendo ejecutado por las pruebas automatizadas. Cuanto mayor sea la cobertura, más confianza se puede tener en que las pruebas están evaluando adecuadamente todas las partes del código.


```bash!
collected 31 items                                                                                                

tests/common/test_common_reader.py::test_get_blob_client PASSED                                             [  3%]
tests/common/test_common_reader.py::test_get_blob_exist PASSED                                              [  6%]
tests/common/test_common_reader.py::test_load_json PASSED                                       .....

---------- coverage: platform darwin, python 3.9.13-final-0 ----------
Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
roadquality/__init__.py                0      0   100%
roadquality/common/__init__.py         0      0   100%
roadquality/common/__loader__.py      24      0   100%
roadquality/common/common.py          90      4    96%   118, 235, 237, 302
roadquality/common/constants.py       18      2    89%   23, 28
roadquality/common/exceptions.py      51      1    98%   58
roadquality/common/geojsonio.py       60      2    97%   62, 86
roadquality/common/secrets.py         23      1    96%   36
roadquality/common/utilities.py       79      9    89%   62-63, 147-149, 166-167, 188-189
----------------------------------------------------------------
TOTAL                                345     19    94%
```


## **TIPS TRABAJO FINAL**

Para el trabajo final se espera que todos los temas vistos en esta sección sean incluidos.
