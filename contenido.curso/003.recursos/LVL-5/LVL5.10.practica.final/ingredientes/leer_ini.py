import configparser

# crear un objeto ConfigParser
config = configparser.ConfigParser()

# leer el archivo .ini
config.read('archivo_config.ini')

# obtener valores de la sección 1
valor1_seccion1 = config.get('seccion1', 'clave1')
valor2_seccion1 = config.get('seccion1', 'clave2')

# obtener valores de la sección 2
valor3_seccion2 = config.get('seccion2', 'clave3')

# obtener todos:
print(config.items('seccion1'))

# imprimir los valores obtenidos
print(f'valor1 en seccion1: {valor1_seccion1}')
print(f'valor2 en seccion1: {valor2_seccion1}')
print(f'valor3 en seccion2: {valor3_seccion2}')