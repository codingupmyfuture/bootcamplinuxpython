from dotenv import dotenv_values

# cargar variables desde el archivo .env en un diccionario
config = dotenv_values(".env")

# acceder a las variables cargadas
print(config['BOOTCAMP_LVL'])
print(config['BOOTCAMP_TOPIC'])
print(config['BOOTCAMP_STUDENTS'])
