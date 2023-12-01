import os

print(f"nombre del sistema operativo : {os.name}")
print(f"separador de ruta            : {os.sep}") # *
print(f"raiz de os                   : {os.path.abspath(os.sep)}")
data = os.uname()
print(f"información sistema          : {os.uname()}")
print(f"información máquina          : {data.machine}")
print(f"información kernel           : {data.version}")
print(f"variables de entorno         : {os.environ}")
print(f"accediendo a una variable específica  : {os.getenv('USER')}")

# definiendo variable propia
os.environ['BOOTCAMP_LVL'] = '4'
print(f"accediendo a una variable propia          : {os.getenv('BOOTCAMP_LVL')}")


# concatenando rutas
ruta: str = os.path.join("a","b","c") # *
print(f"rutas concatenadas #1        : {ruta}")

ruta_2: str = f"{os.sep}".join("a,b,c".split(","))
print(f"rutas concatenadas #2        : {ruta_2}")

