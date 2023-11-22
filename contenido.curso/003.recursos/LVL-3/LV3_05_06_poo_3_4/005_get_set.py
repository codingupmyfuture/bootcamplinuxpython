from decoradores_clases.decoradores import MalaPractica, BuenaPractica


print("imprimiendo tipo Java - NO recomendado".center(50, "*"))
malaPractica: MalaPractica = MalaPractica()

# setter
malaPractica.set_nombre("bootcamp")
# getter
valor: str = malaPractica.get_nombre()
print(f"el valor que tiene la variable privada es: {valor}")

print("imprimiendo tipo python -  recomendado".center(50, "*"))
buenaPractica: BuenaPractica = BuenaPractica()

# setter
buenaPractica.nombre = "Python lvl3"

# getter
valor: str = buenaPractica.nombre
print(f"el valor que tiene la variable privada es: {valor}")
print(f"el valor que tiene la variable privada es: {buenaPractica.nombre}")

# 1 < 2