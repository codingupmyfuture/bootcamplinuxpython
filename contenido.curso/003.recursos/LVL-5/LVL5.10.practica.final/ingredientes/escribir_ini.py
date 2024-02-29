import configparser

# crear un objeto ConfigParser
config = configparser.ConfigParser()

# crear un archivo de configuración
config['seccion1'] = {'clave1': 'valor1', 'clave2': 'valor2'}
config['seccion2'] = {'clave3': 'Valor3'}

# Escribir al archivo
with open('archivo_config.ini', 'w') as configfile:
    config.write(configfile)

print("demo finalizado!!")