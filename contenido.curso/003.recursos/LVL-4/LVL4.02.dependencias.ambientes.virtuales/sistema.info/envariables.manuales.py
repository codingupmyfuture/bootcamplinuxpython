import os

# ruta al archivo .env
env_path = ".env"

# lee el archivo .env y configura las variables de entorno
with open(env_path, "r") as file:
    for line in file:
        key, value = line.strip().split("=")
        os.environ[key] = value

# accede a las variables de entorno configuradas
print(os.environ['BOOTCAMP_LVL'])
print(os.environ['BOOTCAMP_TOPIC'])
print(os.environ['BOOTCAMP_STUDENTS'])